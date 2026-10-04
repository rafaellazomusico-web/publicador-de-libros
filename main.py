import os
import time
from google import genai
from google.genai import errors

def generar():
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    
    # Intentar hasta 5 veces si el servidor de Google está saturado (503)
    for intento in range(1, 6):
        try:
            print(f"Enviando solicitud a gemini-3.8-flash (Intento {intento})...")
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents="Escribe el borrador del siguiente capítulo...",
            )
            print("--- ¡ÉXITO! Contenido generado ---")
            print(response.text)
            return
        except errors.APIError as e:
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                print(f"Servidor saturado (503). Esperando 10 segundos para reintentar...")
                time.sleep(10)
            else:
                raise e
    raise Exception("No se pudo conectar tras 5 intentos por alta demanda.")

if __name__ == "__main__":
    generar()
