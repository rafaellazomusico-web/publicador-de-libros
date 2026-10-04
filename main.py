import os
from google import genai

# Inicializar cliente con la API Key de Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_INSTRUCTION = """
Eres un asistente de redacción académica y técnica especializado en teoría musical contemporánea, 
sistemas microtonales, orquestación y desarrollo de código para música de cámara (Max/MSP, SuperCollider).
Tus respuestas deben seguir el rigor analítico de 'The Chain Theory' y 'Music Code'.
"""

def generar_capitulo():
    directiva = os.getenv("DIRECTIVA_DIARIA", "Redactar la introducción al módulo de orquestación con patrones de ruido rosa.")
    prompt = f"Directiva del autor:\n{directiva}\n\nDesarrolla el contenido técnico, teórico y bloques de código correspondientes."
    
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
        config={
            "system_instruction": SYSTEM_INSTRUCTION,
            "temperature": 0.3,
        }
    )
    return response.text

if __name__ == "__main__":
    borrador = generar_capitulo()
    print("--- BORRADOR GENERADO CON ÉXITO ---")
    print(borrador)
