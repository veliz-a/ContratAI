from groq import Groq

# Cliente inicializado con tu clave de API
client = Groq(api_key="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")

def probar_conexion_modelo():
    prompt_sistema = "Eres un asistente experto en contrataciones públicas del Estado peruano bajo la normativa del OSCE."
    prompt_usuario = "¿Qué requisitos mínimos debe cumplir una MYPE para postular a una licitación pública en el SEACE?"
    
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": prompt_usuario}
        ],
        model="qwen/qwen3.8-27b",
    )
    
    print("--- PRUEBA EXITOSA DE LA HERRAMIENTA (GROQ API) ---")
    print("Modelo utilizado: qwen/qwen3.8-27b")
    print("\nRespuesta generada por el modelo:")
    print(chat_completion.choices[0].message.content)

if __name__ == "__main__":
    probar_conexion_modelo()
