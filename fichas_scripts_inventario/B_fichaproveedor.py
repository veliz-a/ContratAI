"""
B_fichaproveedor.py
Frente B - Inventario de fuentes.
Prueba la API interna del Buscador de Proveedores del Estado (OECE).
Solo se imprimen datos de empresas (RUC 20...). No se imprimen personas naturales.
Uso: python B_fichaproveedor.py > output/B_fichaproveedor.txt
"""
import time
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API = "https://eap.oece.gob.pe/perfilprov-bus/1.0/tarjetas"
HEADERS = {"User-Agent": "Mozilla/5.0 (proyecto academico USIL)",
           "Accept": "application/json"}
RUC_PRUEBA = "20557720708"  # empresa


def pedir(params):
    """GET con verificacion SSL; si falla por certificado, reintenta sin ella y lo avisa."""
    try:
        r = requests.get(API, params=params, headers=HEADERS, timeout=60)
        print("SSL verificado: SI")
    except requests.exceptions.SSLError:
        print("SSL verificado: NO (cadena de certificados incompleta)")
        r = requests.get(API, params=params, headers=HEADERS, timeout=60, verify=False)
    return r


def estructura(obj, prefijo="", nivel=0):
    """Imprime solo nombres de campos y tipos, sin valores."""
    if nivel > 3:
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            print(f"{prefijo}{k}: {type(v).__name__}")
            estructura(v, prefijo + "  ", nivel + 1)
    elif isinstance(obj, list) and obj:
        print(f"{prefijo}[lista de {len(obj)}]")
        estructura(obj[0], prefijo + "  ", nivel + 1)


def solo_empresas(tarjetas):
    return [t for t in tarjetas if str(t.get("numRuc", "")).startswith("20")]


# ---------------------------------------------------------------
print("=== 1) CONSULTA DE UN RUC DE EMPRESA ===")
params = {"searchText": RUC_PRUEBA, "pageSize": 6, "pageNumber": 1, "langTag": "es"}
r = pedir(params)
print("Codigo de estado:", r.status_code)
print("Tipo de contenido:", r.headers.get("Content-Type"))
print("Content-Disposition:", r.headers.get("Content-Disposition"))
print("Tamano (bytes):", len(r.content))
d = r.json()
print("\nEstructura (solo campos):")
estructura(d)
print("\nFecha de corte (dataInfo.updatedTo):", d["dataInfo"]["updatedTo"])
print("Resultados (hitsAll):", d["searchInfo"]["hitsAll"])
for t in solo_empresas(d["tarjetasProvT01"]):
    print("Registro:", t)

# ---------------------------------------------------------------
print("\n=== 2) EFECTO DEL PARAMETRO export=1 ===")
params_exp = dict(params, export=1)
r2 = pedir(params_exp)
print("Mismo contenido con y sin export=1:", r.content == r2.content)
print("Content-Disposition con export=1:", r2.headers.get("Content-Disposition"))

# ---------------------------------------------------------------
print("\n=== 3) BUSQUEDA POR PALABRA Y PAGINACION ('oxigeno') ===")
r3 = pedir({"searchText": "oxigeno", "pageSize": 3, "pageNumber": 1, "langTag": "es"})
d3 = r3.json()
si = d3["searchInfo"]
print("hitsAll:", si["hitsAll"], "| pageTotal:", si["pageTotal"], "| pageSize:", si["pageSize"])
emp = solo_empresas(d3["tarjetasProvT01"])
print("Filas devueltas:", len(d3["tarjetasProvT01"]), "| de empresas:", len(emp))
for t in emp[:2]:
    print("Ejemplo:", t["numRuc"], t["nomRzsProv"], "| habilitado:", t["esHabilitado"],
          "| apto:", t["esAptoContratar"])

# ---------------------------------------------------------------
print("\n=== 4) TOPE DE pageSize ('oxigeno') ===")
for ps in [10, 100, 500, 1000]:
    rr = requests.get(API, params={"searchText": "oxigeno", "pageSize": ps,
                                   "pageNumber": 1, "langTag": "es"},
                      headers=HEADERS, timeout=90)
    try:
        dd = rr.json()
        print(f"pageSize={ps}: estado {rr.status_code}, "
              f"filas={len(dd.get('tarjetasProvT01') or [])}, "
              f"pageTotal={dd['searchInfo']['pageTotal']}")
    except Exception as e:
        print(f"pageSize={ps}: estado {rr.status_code}, error {e}")
    time.sleep(1)
print("No se probaron valores mayores a 1000.")