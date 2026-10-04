import os
import time
import engine  # Importa las funciones matemáticas de tu engine.py
from google import genai

# Inicializar cliente de Gemini usando la SDK oficial
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def cargar_prompt_maestro():
    with open("prompt_maestro.md", "r", encoding="utf-8") as f:
        return f.read()

def generar_siguiente_capitulo():
    prompt_base = cargar_prompt_maestro()
    
    # Calculamos datos usando el engine para alimentar el prompt
    datos_n5 = engine.generar_funciones_tonales(5)
    datos_n7 = engine.generar_funciones_tonales(7)
    datos_n9 = engine.generar_funciones_tonales(9)
    datos_n11 = engine.generar_funciones_tonales(11)
    
    # Definición de la tarea actual con datos calculados
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
    
    print("Enviando petición a Gemini...")
    
    # LÓGICA DE REINTENTOS PARA EVITAR ERRORES 503 POR SATURACIÓN
    intentos = 0
    max_intentos = 3
    response = None
    
    while intentos < max_intentos:
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt_completo,
            )
            break
        except Exception as e:
            intentos += 1
            print(f"Servidor ocupado (intento {intentos}/{max_intentos}). Esperando 10 segundos...")
            time.sleep(10)
            if intentos == max_intentos:
                raise e

    # Guardar la respuesta en archivo Markdown
    nombre_archivo = "capitulo_04_funciones_tonales.md"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(response.text)
        
    print(f"Capítulo generado con éxito: {nombre_archivo}")

if __name__ == "__main__":
    generar_siguiente_capitulo()
