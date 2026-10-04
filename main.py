import os
import time
import engine
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def cargar_prompt_maestro():
    with open("prompt_maestro.md", "r", encoding="utf-8") as f:
        return f.read()

def generar_siguiente_capitulo():
    prompt_base = cargar_prompt_maestro()
    
    # Datos calculados por el motor armónico
    datos_n5 = engine.generar_funciones_tonales(5)
    datos_n7 = engine.generar_funciones_tonales(7)
    datos_n9 = engine.generar_funciones_tonales(9)
    datos_n11 = engine.generar_funciones_tonales(11)
    
    tema_capitulo = f"""
    Redacta el Capítulo 4: 'Formalización Matemática de la Matriz Bi-Eje de Funciones Tonales (F_N)'.
    
    Datos exactos generados por el motor matemático para apoyar la redacción:
    - N=5:  A_N={datos_n5['A_N']}, B_N={datos_n5['B_N']}, Cajita={datos_n5['cajita']}, S_N={datos_n5['S_N']}
    - N=7:  A_N={datos_n7['A_N']}, B_N={datos_n7['B_N']}, Cajita={datos_n7['cajita']}, S_N={datos_n7['S_N']}
    - N=9:  A_N={datos_n9['A_N']}, B_N={datos_n9['B_N']}, Cajita={datos_n9['cajita']}, S_N={datos_n9['S_N']}
    - N=11: A_N={datos_n11['A_N']}, B_N={datos_n11['B_N']}, Cajita={datos_n11['cajita']}, S_N={datos_n11['S_N']}

    REQUERIMIENTOS:
    1. Explica en detalle cómo se desglosa la Cajita Central para N = 5, 7, 9 y 11 notas.
    2. Incluye las tablas de la matriz operativa bi-eje F_N.
    3. Detalla el cálculo exacto del acorde simétrico residual S_N.
    """
    
    prompt_completo = f"{prompt_base}\n\n---\n\nTAREA ACTUAL:\n{tema_capitulo}"
    
    modelo = "gemini-3.8-flash"
    max_intentos = 5
    response = None

    print(f"Iniciando generación con {modelo}...")

    for intento in range(1, max_intentos + 1):
        try:
            print(f"Enviando solicitud (intento {intento}/{max_intentos})...")
            response = client.models.generate_content(
                model=modelo,
                contents=prompt_completo,
            )
            print(f"¡Éxito total! Capítulo generado correctamente.")
            break
        except Exception as e:
            tiempo_espera = intento * 30  # Espera 30s, 60s, 90s, 120s, 150s
            print(f"Servidor ocupado/saturado ({e}). Esperando {tiempo_espera} segundos antes del siguiente intento...")
            time.sleep(tiempo_espera)

    if not response:
        raise RuntimeError("El servidor de Gemini siguió ocupado tras múltiples reintentos con pausas prolongadas.")

    nombre_archivo = "capitulo_04_funciones_tonales.md"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(response.text)
        
    print(f"Capítulo guardado con éxito en: {nombre_archivo}")

if __name__ == "__main__":
    generar_siguiente_capitulo()
