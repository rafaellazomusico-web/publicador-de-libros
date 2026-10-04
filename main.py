import os
import time
import engine
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def cargar_prompt_maestro():
    with open("prompt_maestro.md", "r", encoding="utf-8") as f:
        return f.read()

def generar_capitulo_uno():
    prompt_base = cargar_prompt_maestro()
    
    # Inyectamos datos exactos del engine para N=5, 7, 9 y 11 como demostración
    datos_n5 = engine.generar_funciones_tonales(5)
    datos_n7 = engine.generar_funciones_tonales(7)
    
    tema_capitulo = f"""
    Redacta el Capítulo 1: 'La Cajita Central y los Fundamentos del Acorde Transformante'.
    
    Datos de referencia calculados por el motor matemático:
    - Para N=5: Cajita Central = {datos_n5['cajita']}, P_m = {datos_n5['cajita'][2]}, A_N = {datos_n5['A_N']}
    - Para N=7: Cajita Central = {datos_n7['cajita']}, P_m = {datos_n7['cajita'][2]}, A_N = {datos_n7['A_N']}

    REQUERIMIENTOS DEL CAPÍTULO 1:
    1. Introduce la génesis de The Chain Theory y la necesidad de formalizar sistemas microtonales equitemperados N-ET.
    2. Define matemáticamente la Cajita Central C_N = (P_m - 1, 0, P_m, 1) y el paso de tónica menor P_m = floor(N/2).
    3. Explica cómo la simetría de la Cajita Central da origen al Acorde Transformante T_N y la primera distribución de intervalos.
    4. Muestra un ejemplo práctico paso a paso usando N = 5 y N = 7.
    """
    
    prompt_completo = f"{prompt_base}\n\n---\n\nTAREA ACTUAL:\n{tema_capitulo}"
    
    modelo = "gemini-3.8-flash"
    max_intentos = 5
    response = None

    print(f"Iniciando generación del Capítulo 1 con {modelo}...")

    for intento in range(1, max_intentos + 1):
        try:
            print(f"Enviando solicitud (intento {intento}/{max_intentos})...")
            response = client.models.generate_content(
                model=modelo,
                contents=prompt_completo,
            )
            print("¡Éxito! Capítulo 1 generado correctamente.")
            break
        except Exception as e:
            tiempo_espera = intento * 30
            print(f"Servidor ocupado ({e}). Esperando {tiempo_espera} segundos...")
            time.sleep(tiempo_espera)

    if not response:
        raise RuntimeError("El servidor de Gemini siguió ocupado tras múltiples reintentos.")

    nombre_archivo = "capitulo_01_introduccion_cajita_central.md"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(response.text)
        
    print(f"Capítulo guardado con éxito en: {nombre_archivo}")

if __name__ == "__main__":
    generar_capitulo_uno()
