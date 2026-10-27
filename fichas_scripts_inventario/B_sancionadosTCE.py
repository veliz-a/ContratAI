"""
B_sancionadosTCE.py
Frente B - Inventario de fuentes.
1) Lee la tabla publica de sancionados del RNP/TCE (HTML) y mide que entrega.
2) Cruza las empresas sancionadas (RUC 20) con la API del OECE por RUC.
NO resuelve ni evade el captcha. NO imprime personas naturales (RUC 10): solo conteos.
Uso: python B_sancionadosTCE.py > output/B_sancionadosTCE.txt
"""
import io
import re
import time
import requests
import urllib3
import pandas as pd

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

TCE = "https://www.rnp.gob.pe/consultasenlinea/inhabilitados/busqueda_vnv.asp"
API = "https://eap.oece.gob.pe/perfilprov-bus/1.0/tarjetas"
HEADERS = {"User-Agent": "Mozilla/5.0 (proyecto academico USIL)"}

# ---------------------------------------------------------------
print("=== 1) ACCESO A LA PAGINA DE SANCIONADOS ===")
try:
    r = requests.get(TCE, params={"action": "enviar", "valor": ""},
                     headers=HEADERS, timeout=60)
    print("SSL verificado: SI")
except requests.exceptions.SSLError:
    print("SSL verificado: NO (se usa verify=False solo para lectura de datos publicos)")
    r = requests.get(TCE, params={"action": "enviar", "valor": ""},
                     headers=HEADERS, timeout=60, verify=False)

html = r.content.decode("latin-1", errors="replace")
print("Codigo de estado:", r.status_code)
print("Tipo de contenido:", r.headers.get("Content-Type"))
print("Last-Modified:", r.headers.get("Last-Modified"))
print("Tamano (bytes):", len(r.content))
print("Menciona captcha:", "captcha" in html.lower())
print("Pide codigo de imagen:", "ingrese el c" in html.lower())

# ---------------------------------------------------------------
print("\n=== 2) TABLAS EN EL HTML (sin resolver captcha) ===")
tablas = pd.read_html(io.StringIO(html))
print("Tablas encontradas:", len(tablas))
for i, t in enumerate(tablas):
    print(f"Tabla {i}: {t.shape[0]} filas x {t.shape[1]} columnas")
    print("  Columnas:", [str(c) for c in t.columns])

df = max(tablas, key=lambda t: t.shape[0])
ruc = df["RUC"].astype(str).str.extract(r"(\d{11})")[0]
es_emp = ruc.str.startswith("20", na=False)
es_per = ruc.str.startswith("10", na=False)

print("\nFilas con RUC:", int(ruc.notna().sum()))
print("Filas de empresas (20...):", int(es_emp.sum()))
print("Filas de personas naturales (10...):", int(es_per.sum()), "(solo conteo, no se muestran)")
rucs = sorted(set(ruc[es_emp].dropna()))
print("RUC unicos de empresas:", len(rucs))

fechas = pd.to_datetime(df["Desde"], format="%d/%m/%Y", errors="coerce")
print("Sancion mas reciente (Desde):", fechas.max().date())
print("Sancion mas antigua (Desde):", fechas.min().date())
print("Estados presentes:", sorted(df["Estado"].dropna().astype(str).unique().tolist()))

print("\nEjemplo (3 empresas):")
cols = ["Razón Social", "RUC", "Resolución", "Periodo de Inhabilitación", "Desde", "Estado"]
print(df[es_emp][cols].head(3).to_string(index=False))

# ---------------------------------------------------------------
print("\n=== 3) CRUCE TCE -> API OECE (por RUC, solo empresas) ===")
filas = []
for q in rucs:
    rr = requests.get(API, params={"searchText": q, "pageSize": 6,
                                   "pageNumber": 1, "langTag": "es"},
                      headers={**HEADERS, "Accept": "application/json"}, timeout=60)
    try:
        tarjetas = rr.json().get("tarjetasProvT01") or []
        corte = rr.json()["dataInfo"]["updatedTo"]
    except Exception:
        tarjetas, corte = [], None
    m = [x for x in tarjetas if x.get("numRuc") == q]
    if m:
        filas.append({"ruc": q, "en_oece": True, "habilitado": m[0]["esHabilitado"],
                      "apto": m[0]["esAptoContratar"]})
    else:
        filas.append({"ruc": q, "en_oece": False, "habilitado": None, "apto": None})
    time.sleep(1)

res = pd.DataFrame(filas)
print("Fecha de corte de la API OECE (updatedTo):", corte)
print("Empresas sancionadas consultadas:", len(res))
print("Encontradas en la API del OECE:", int(res["en_oece"].sum()), "de", len(res))
print("\nCombinaciones (en_oece / habilitado / apto):")
print(res.groupby(["en_oece", "habilitado", "apto"], dropna=False).size().to_string())
print("\nEjemplo (5 empresas):")
print(res.head(5).to_string(index=False))