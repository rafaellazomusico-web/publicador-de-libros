import os
import time
import engine
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def cargar_prompt_maestro():
    with open("prompt_maestro.md", "r", encoding="utf-8") as f:
        return f.read()

def generar_capitulo_dos():
    prompt_base = cargar_prompt_maestro()
    
    # Inyectamos datos del engine para N=9 y N=11 para avanzar en la escala
    datos_n9 = engine.generar_funciones_tonales(9)
    datos_n11 = engine.generar_funciones_tonales(11)
    
    tema_capitulo = f"""
    Redacta el Capítulo 2: 'Mapeo Acústico, Ordenamiento Escalar y Expansión de N-ET'.
    
    Datos de referencia calculados por el motor matemático:
    - Para N=9: Cajita Central = {datos_n9['cajita']}, P_m = {datos_n9['cajita'][2]}, A_N = {datos_n9['A_N']}
    - Para N=11: Cajita Central = {datos_n11['cajita']}, P_m = {datos_n11['cajita'][2]}, A_N = {datos_n11['A_N']}

    REQUERIMIENTOS DEL CAPÍTULO 2:
    1. Profundiza en el mapeo acústico e intervalos microtonales generados a partir de la Cajita Central.
    2. Explica el ordenamiento escalar de los grados de paso y la simetría de la cadena tonal en sistemas mayores N-ET.
    3. Desarrolla paso a paso la aplicación práctica y análisis estructural para N = 9 y N = 11.
    4. Conecta las propiedades del Acorde Transformante T_N con la conducción de voces y modulaciones microtonales.
    """
    
    prompt_completo = f"{prompt_base}\n\n---\n\nTAREA ACTUAL:\n{tema_capitulo}"
    
    modelo = "gemini-3.8-flash"
    max_intentos = 5
    response = None

    print(f"Iniciando generación del Capítulo 2 con {modelo}...")

    for intento in range(1, max_intentos + 1):
        try:
            print(f"Enviando solicitud (intento {intento}/{max_intentos})...")
            response = client.models.generate_content(
                model=modelo,
                contents=prompt_completo,
            )
            print("¡Éxito! Capítulo 2 generado correctamente.")
            break
        except Exception as e:
            tiempo_espera = intento * 30
            print(f"Servidor ocupado ({e}). Esperando {tiempo_espera} segundos...")
            time.sleep(tiempo_espera)

    if not response:
        raise RuntimeError("El servidor de Gemini siguió ocupado tras múltiples reintentos.")

    nombre_archivo = "capitulo_02_mapeo_acustico_ordenamiento.md"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(response.text)
        
    print(f"Capítulo guardado con éxito en: {nombre_archivo}")

if __name__ == "__main__":
    generar_capitulo_dos()
