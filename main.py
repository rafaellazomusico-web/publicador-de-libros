import os
import engine  # Importa tu archivo engine.py
from google import genai

# Inicializar cliente de Gemini
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def cargar_prompt_maestro():
    with open("prompt_maestro.md", "r", encoding="utf-8") as f:
        return f.read()

def generar_siguiente_capitulo():
    prompt_base = cargar_prompt_maestro()
    
    # Ejemplo de tema para el capítulo actual (puedes parametrizarlo o leerlo de una lista de temas)
    tema_capitulo = """
    Redacta el Capítulo 4: 'Formalización Matemática de la Matriz Bi-Eje de Funciones Tonales (F_N)'.
    Explica en detalle cómo se desglosa la Cajita Central para N = 5, 7, 9 y 11 notas.
    Incluye las tablas de la matriz operativa y el cálculo del acorde simétrico residual S_N.
    """
    
    prompt_completo = f"{prompt_base}\n\n---\n\nTAREA ACTUAL:\n{tema_capitulo}"
    
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt_completo,
    )
    
    # Guardar en archivo Markdown
    nombre_archivo = "capitulo_04_funciones_tonales.md"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(response.text)
        
    print(f"Capítulo generado con éxito: {nombre_archivo}")

if __name__ == "__main__":
    generar_siguiente_capitulo()
