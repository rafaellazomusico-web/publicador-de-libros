import math

def calcular_acorde_transformante(N):
    """
    Calcula la secuencia de índices del Acorde Transformante T_N.
    """
    A_N = (N + 3) // 4
    B_N = (N - 3) // 4
   
    indices = []
    for j in range(N):
        if j % 2 == 0:
            t_j = A_N + (j // 2)
        else:
            t_j = -B_N + ((j - 1) // 2)
        indices.append(t_j)
   
    indices.append(A_N)
    return indices

def generar_datos_escala(p, N):
    """
    Genera los datos numéricos de la escala microtonal S_{p,N}.
    """
    B_N = (N - 3) // 4
    limite_inferior = -B_N
    limite_superior = N - 1 - B_N
   
    indices_acorde = calcular_acorde_transformante(N)
    log2_p = math.log2(p)
    acorde_cents = [round((1200 * idx * log2_p) % 1200, 4) for idx in indices_acorde]
       
    return {
        "N": N,
        "primo": p,
        "limite_inferior": limite_inferior,
        "limite_superior": limite_superior,
        "indices_acorde": indices_acorde,
        "acorde_cents": acorde_cents
    }

def generar_24_pitch_set(p, f_base=440.0):
    """
    Genera la partición en 24 Pitch Set (Set 1 y Set 2 de 12 notas cada uno).
    Garantiza el formato .scl estándar para Pianoteq (omite tónica 0.0 implícita y cierra en 1200.0).
    """
    indices_set1 = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    indices_set2 = [-5, -4, -3, 0, 10, 11, 12, 13, 14, 15, 16, 17]
    log2_p = math.log2(p)
    
    def procesar_set(indices):
        datos = []
        for idx in indices:
            cents_calc = (1200 * idx * log2_p) % 1200
            cents_round = round(cents_calc, 4)
            
            # CORRECCIÓN DE OCTAVADO:
            # Si el cálculo da 0.0 pero el índice NO es el 0 inicial (Tónica C), 
            # corresponde al cierre de octava (1200.0 cents).
            if cents_round == 0.0 and idx != 0:
                cents_round = 1200.0
                
            freq = f_base * (2 ** (cents_round / 1200))
            datos.append({"ciclo": idx, "cents": cents_round, "freq": round(freq, 2)})
            
        # Ordenamos por cents de menor a mayor
        datos_ordenados = sorted(datos, key=lambda x: x["cents"])
        
        # Filtramos la tónica implícita (0.0 cents) para que la exportación a .scl 
        # arranque en el primer microtono y termine exactamente con el 1200.0
        resultado_scl = [item for item in datos_ordenados if item["cents"] > 0.0001]
        
        # Si la lista no tiene el 1200.0 al final, lo añadimos de cierre de octava
        if not any(abs(item["cents"] - 1200.0) < 0.001 for item in resultado_scl):
            freq_octava = f_base * 2.0
            resultado_scl.append({"ciclo": 0, "cents": 1200.0, "freq": round(freq_octava, 2)})
            
        return resultado_scl
        
    return {
        "set1": procesar_set(indices_set1),
        "set2": procesar_set(indices_set2)
    }

def generar_funciones_tonales(N):
    """
    Genera la estructura matemática de las Funciones Tonales F_N,
    la Cajita Central y el cálculo exacto del Simétrico S_N (Generalizado N>=5).
    """
    if N % 2 == 0 or N < 5:
        raise ValueError("N debe ser un número entero impar mayor o igual a 5.")
       
    A_N = (N + 3) // 4
    B_N = (N - 3) // 4
   
    # 1. Secuencia simétrica raw del Acorde Transformante T_N
    seq = []
    for j in range(N):
        if j % 2 == 0:
            val = A_N + (j // 2)
        else:
            val = -B_N + ((j - 1) // 2)
        seq.append(val)
    seq.append(A_N)
   
    # 2. Desglose exacto de Hilos Generativos
    mayores_raw = [seq[j] for j in range(0, N, 2)]
    menores_raw = [seq[j] for j in range(1, N, 2)]
   
    # 3. Mapeo estructural de la Cajita Central
    cajita = [A_N, -B_N, A_N + 1, -B_N + 1]
   
    # 4. CÁLCULO GENERALIZADO DE S_N PARA CUALQUIER N IMPAR
    if N % 4 == 1:
        S_N = (3 * N + 1) // 4
    else:  # N % 4 == 3
        S_N = (3 * N + 3) // 4

    return {
        "N": N,
        "A_N": A_N,
        "B_N": B_N,
        "S_N": S_N,
        "secuencia_raw": seq,
        "cajita": cajita,
        "mayores_raw": mayores_raw,
        "menores_raw": menores_raw
    }

# Alias de compatibilidad
generar_escala_armonica = generar_datos_escala
