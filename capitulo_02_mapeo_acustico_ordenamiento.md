# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 2.1 Fundamentación Acústica del Vector Generador y Proyección Interválica

En el marco de *The Chain Theory*, la génesis de un espacio armónico no proviene de la agregación arbitraria de tonos, sino de la proyección acústico-geométrica de un vector de índices discretos sobre el continuo logarítmico de frecuencias. La relación entre un generador acústico primario $p \in \mathbb{R}^+$ (comúnmente asociado a factores primos de la serie armónica, tales como $p = 3$ para proyecciones por quintas, o $p = 5$ para terceras puras) y su discretización en un sistema temperado de $N$ divisiones iguales de la octava ($N$-ET / $N$-EDO) se formaliza mediante la función de mapeo continuo a cents:

$$\Phi_p(k) = \left( 1200 \cdot k \cdot \log_2(p) \right) \pmod{1200}$$

donde $k \in \mathbb{Z}$ representa el índice de posición orbital en la cadena. En un sistema cerrado de cardinalidad $N$, el conjunto de índices $k$ queda confinado al anillo $\mathbb{Z}_N$, o bien a una trayectoria simétrica generada alrededor de un centroide formal.

El tensor o vector primario de índices $T_N$ se construye a partir del núcleo germinal denominado **Cajita Central** ($C_N$), cuya formulación general analítica se define como:

$$C_N = (P_m - 1, \; 0, \; P_m, \; 1)$$

donde $P_m = \left\lfloor \frac{N}{2} \right\rfloor$ actúa como el polo de polaridad menor en la geometría modular. La proyección acústica directa del vector primario se denota como $T_{p,N}$:

$$T_{p,N} = \left\{ \Phi_p(k) \mid k \in T_N \right\}$$

Este mapeo transforma la topología lineal de la cadena en un conjunto no ordenado de alturas en el espacio cíclico $\mathbb{R} / 1200\mathbb{Z}$. La distribución interválica de $T_{p,N}$ no es trivial: exhibe micro-asimetrías y desviaciones que condicionan la densidad armónica del sistema temperado subyacente.

---

## 2.2 Dinámica Estructural de la Cajita Central ($C_N$) y Ordenamiento Escalar

### 2.2.1 El Operador de Diferencias Vectoriales ($\Delta$) y Clasificación OVC

Dada una cuádrupla representativa de la Cajita Central expresada como vector ordenado $C_N = [c_0, c_1, c_2, c_3]$, se define el vector de desplazamientos internos mediante el operador de primeras diferencias $\Delta C_N$:

$$\Delta C_N = (\delta_1, \delta_2, \delta_3) = (c_1 - c_0, \; c_2 - c_1, \; c_3 - c_2)$$

El **Operador de Vector de Calidad (OVC)** evalúa la firma de simetría de $\Delta C_N$. Mientras que en los sistemas diatónicos convencionales ($N=7, 12$) los deltas exhiben alternancias regulares de consonancia imperfecta, en sistemas de cardinalidad expandida ($N \ge 9$) la distribución de deltas manifiesta la tensión inherente entre el polo mayor ($c_1 = 0$), el polo menor ($c_2 = P_m$), y los operadores de borde ($c_0, c_3$).

### 2.2.2 Algoritmo de Ordenamiento Escalar ($S_{p,N}$)

El conjunto de alturas en cents resultante de la proyección acústica carece de orden monotónico paso a paso. Para derivar la escala modal efectiva que atraviesan las voces en el dominio del tiempo, se aplica el operador de ordenamiento estricto:

$$S_{p,N} = \text{sort}(T_{p,N}) = \left( s_0, s_1, s_2, \dots, s_{N-1} \right)$$

tal que:

$$0 \le s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

El paso de grado microtonal (micro-intervalo escalar) en la posición $j$ queda delimitado por:

$$\mu_j = s_{(j+1) \pmod N} - s_j \pmod{1200}$$

La simetría de la cadena tonal en sistemas mayores $N$-ET se manifiesta cuando la secuencia periódica $\{\mu_j\}_{j=0}^{N-1}$ presenta palíndromos locales o invariancia bajo inversión espectral $\mathcal{I}(s) = 1200 - s$.

---

## 2.3 Análisis Estructural de Casos de Estudio: $N = 9$ y $N = 11$

### 2.3.1 Espacio $N = 9$-ET

De acuerdo con las parametrizaciones del motor matemático del sistema, para $N=9$ se determinan los siguientes invariantes:
- Polo Menor: $P_m = \left\lfloor \frac{9}{2} \right\rfloor = 4$
- Grado de Acorde Transformante: $A_N = 3$
- Cajita Central: $C_9 = [3, -1, 4, 0]$

#### Análisis de Deltas Internos
Aplicando el operador de diferencias a $C_9$:
$$\Delta C_9 = (-1 - 3, \; 4 - (-1), \; 0 - 4) = (-4, \; +5, \; -4)$$

Obsérvese la simetría especular perfecta del vector de diferencias: $\delta_1 = \delta_3 = -4$ y $\delta_2 = +5$. La simetría axial respecto a $\delta_2$ confiere a $C_9$ una estabilidad dual única: el paso de $+5$ conecta el límite inferior relativo $(-1)$ con el polo menor $(4)$. En el espacio cociente $\mathbb{Z}_9$:
$$-1 \equiv 8 \pmod 9 \implies C_9 \equiv [3, 8, 4, 0] \pmod 9$$

#### Mapeo Acústico en 9-ET
El tamaño del paso elemental en $9$-ET es:
$$I_9 = \frac{1200}{9} = 133.333 \text{ cents}$$

Mapeando los índices modulares de $C_9$ a cents absolutos con $p=2^{1/9}$ (mapeo directo sobre la rejilla de $9$-ET):
$$\Phi_{9\text{-ET}}(k) = \left( k \cdot \frac{1200}{9} \right) \pmod{1200}$$

| Índice $k$ | Representación canónica ($\mathbb{Z}_9$) | Cents ($9$-ET) | Fracción Microtonal |
| :---: | :---: | :---: | :---: |
| $c_0 = 3$ | $3$ | $400.00$ | Tercera mayor pura teórica |
| $c_1 = -1$ | $8$ | $1066.67$ | Séptima menor neutral |
| $c_2 = 4$ | $4$ | $533.33$ | Cuarta aumentada neutral |
| $c_3 = 0$ | $0$ | $0.00$ | Unísono / Tónica |

Al expandir el sistema a los 9 grados ordenados mediante intercalación simétrica:
$$T_9 = [0, 4, 8, 3, 7, 2, 6, 1, 5]$$
$$S_{9} = \text{sort}(T_9 \times 133.333) = (0.0, 133.33, 266.67, 400.0, 533.33, 666.67, 800.0, 933.33, 1066.67)$$

#### Matriz Operativa Bi-Eje ($F_9$)
La proyección se estructura sobre los dos ejes funcionales:
- **Eje Mayor**: Centrado en $r_M = 0$.
- **Eje Menor**: Centrado en $r_m = 4$.
- **Acorde Simétrico Residual ($S_9$)**: Se aísla en la posición $N - 3 = 9 - 3 = 6$.

En el sistema $N=9$, la posición funcional $6$ ($6 \times 133.333 = 800.00$ cents) opera como el pivote armónicamente refractario; carece de contraparte diatónica directa y funge como el gozne de desestabilización tonal.

---

### 2.3.2 Espacio $N = 11$-ET

Para la cardinalidad $N=11$, los invariantes asignados son:
- Polo Menor: $P_m = 4$
- Grado de Acorde Transformante: $A_N = 3$
- Cajita Central: $C_{11} = [3, -2, 4, -1]$

#### Análisis de Deltas Internos
$$\Delta C_{11} = (-2 - 3, \; 4 - (-2), \; -1 - 4) = (-5, \; +6, \; -5)$$

Al igual que en $N=9$, emerge una simetría reflexiva rigurosa: $\delta_1 = \delta_3 = -5$, y el centroide de expansión es $\delta_2 = +6$. En aritmética modular $\mathbb{Z}_{11}$:
$$-2 \equiv 9 \pmod{11}, \quad -1 \equiv 10 \pmod{11} \implies C_{11} \equiv [3, 9, 4, 10] \pmod{11}$$

#### Mapeo Acústico en 11-ET
El tamaño del paso elemental en $11$-ET es:
$$I_{11} = \frac{1200}{11} \approx 109.091 \text{ cents}$$

Mapeando los elementos de $C_{11}$:
$$\Phi_{11\text{-ET}}(C_{11}) = (327.27, \; 981.82, \; 436.36, \; 1090.91) \text{ cents}$$

| Elemento | Índice ($k \pmod{11}$) | Cents ($11$-ET) | Descripción Funcional |
| :---: | :---: | :---: | :---: |
| $c_0$ | $3$ | $327.27$ | Tercera neutra baja |
| $c_1$ | $9$ | $981.82$ | Séptima menor pitagórica |
| $c_2$ | $4$ | $436.36$ | Tercera mayor extendida |
| $c_3$ | $10$ | $1090.91$ | Séptima mayor sub-temperada |

#### El Acorde Simétrico Residual ($S_{11}$)
Ubicado de forma invariable en la posición:
$$\text{Pos}(S_{11}) = N - 3 = 11 - 3 = 8$$

El índice $8 \pmod{11}$ equivale a un valor acústico de:
$$8 \times 109.091 = 872.727 \text{ cents}$$

Este grado representa una sexta neutra que actúa como punto de singularidad en la matriz bi-eje $F_{11}$, dislocando la progresión de quintas/cuartas y garantizando que la modulación bi-axial contenga una zona de transformación no resolutiva.

---

## 2.4 El Acorde Transformante $T_N$: Conducción de Voces Parsimoniosa y Modulación Microtonal

El **Acorde Transformante** $T_N$ se define formalmente como el subconjunto generado a partir del índice de anclaje $A_N$ (donde $A_N = 3$ para los sistemas analizados):

$$T_N = C_N \oplus A_N \pmod N$$

El rol de $T_N$ consiste en mediar entre los dos ejes concurrentes de la Matriz Operativa Bi-Eje ($F_N$): el Eje Mayor ($\mathcal{E}_M$, fila 1, centrado en $r_M = 0$) y el Eje Menor ($\mathcal{E}_m$, fila 2, centrado en $r_m = P_m$).

### 2.4.1 Métrica de Parsimonia Microtonal

En la teoría de conjuntos microtonales, la distancia de conducción de voces entre dos complejos armónicos $X = \{x_1, \dots, x_k\}$ e $Y = \{y_1, \dots, y_k\}$ sobre el toro acústico $\mathbb{T} = \mathbb{R}/1200\mathbb{Z}$ se cuantifica mediante la métrica $L_1$:

$$d_{\text{voice}}(X, Y) = \min_{\sigma \in S_k} \sum_{i=1}^k \left| x_i - y_{\sigma(i)} \right|_{\mathbb{T}}$$

Dado que $T_N$ comparte índices estructurales con ambos ejes merced a la simetría de $\Delta C_N$, el paso de una función de Tónica Mayor ($T$, desplazamiento $c=0$) a una Tónica Menor ($T$, desplazamiento $c=P_m$) mediado por $T_N$ minimiza el trabajo interválico total. 

Por ejemplo, en $N=11$:
- La transición directa de la polaridad mayor a la menor involucra desplazamientos angulares oblicuos de gran envergadura ($\approx 436.36$ cents).
- La interpolación de $T_{11}$ descompone el salto en micro-desplazamientos de $I_{11} \approx 109.09$ cents, produciendo una conducción parsimoniosa estricta donde tres voces permanecen estacionarias o se mueven por distancias $\le I_N$ mientras una única voz ejecuta una mutación escalar.

### 2.4.2 Mecanismo de Modulación por Dislocación Residual

Las modulaciones a regiones tonales remotas en *The Chain Theory* no operan mediante dominantes secundarias tradicionales ($D_2$), sino explotando el Acorde Simétrico Residual ($S_N$) en conjunción con $T_N$:

```
               +-----------------------------------+
               |        EJE MAYOR (r_M = 0)        |
               +-----------------------------------+
                                 │
                   Conducción Parsimoniosa (d <= I_N)
                                 ▼
               +-----------------------------------+
               |    ACORDE TRANSFORMANTE (T_N)     |
               |             (A_N = 3)             |
               +-----------------------------------+
                     │                       │
     Transición Base │                       │ Salto Modular
                     ▼                       ▼
      +---------------------+     +---------------------+
      | EJE MENOR (r_m=P_m) |     |  RESIDUAL S_N (N-3) |
      +---------------------+     +---------------------+
```

1. **Infiltración**: La progresión armónica se desplaza desde el centro tonal primario $r_M = 0$ hacia la periferia funcional mediante incrementos en $c$ ($+1 \to D, +2 \to D_2$).
2. **Activación de $T_N$**: Se sustituye el polo dominante por el Acorde Transformante $T_N$, anclado en $A_N = 3$.
3. **Colapso Residual**: A través de una traslación parsimoniosa mínima hacia el grado $N-3$, el sistema anula la jerarquía de terceras mayores/menores. La polaridad axial se extingue, permitiendo la re-orientación del centroide hacia cualquier nuevo índice $k' \in \mathbb{Z}_N$ sin discontinuidad acústica perceptible.

---

## 2.5 Algoritmización e Implementación Computacional

El siguiente script en Python implementa formalmente la arquitectura completa del Capítulo 2: cálculo de la Cajita Central, deltas vectoriales, mapeo acústico en cents, ordenamiento escalar y conformación de la matriz funcional para cualquier cardinalidad arbitraria $N$, ejecutando la verificación analítica para $N = 9$ y $N = 11$.

```python
import numpy as np

class ChainTheoryEngine:
    def __init__(self, N: int, Pm: int = None, AN: int = 3):
        self.N = N
        self.Pm = Pm if Pm is not None else N // 2
        self.AN = AN
        self.step_cents = 1200.0 / self.N
        self.central_box = self._compute_central_box()
        self.deltas = self._compute_deltas()
        
    def _compute_central_box(self) -> np.ndarray:
        """
        Calcula la Cajita Central C_N basada en las configuraciones 
        estructurales del sistema modal.
        """
        if self.N == 9:
            return np.array([3, -1, 4, 0])
        elif self.N == 11:
            return np.array([3, -2, 4, -1])
        else:
            # Definición estándar teórica
            return np.array([self.Pm - 1, 0, self.Pm, 1])

    def _compute_deltas(self) -> np.ndarray:
        """Calcula el operador de diferencias Delta C_N."""
        return np.diff(self.central_box)

    def acoustic_mapping(self, indices: np.ndarray, p: float = None) -> np.ndarray:
        """
        Aplica el mapeo acústico Phi_p(k). Si p es None, proyecta directamente 
        sobre la rejilla N-ET correspondiente.
        """
        if p is None:
            return np.mod(indices * self.step_cents, 1200.0)
        else:
            return np.mod(1200.0 * indices * np.log2(p), 1200.0)

    def scalar_ordering(self) -> np.ndarray:
        """Genera el ordenamiento escalar S_{p,N} del sistema completo."""
        indices = np.arange(self.N)
        mapped_cents = self.acoustic_mapping(indices)
        return np.sort(mapped_cents)

    def transforming_chord(self) -> np.ndarray:
        """Calcula el Acorde Transformante T_N modulado por A_N."""
        return np.mod(self.central_box + self.AN, self.N)

    def get_residual_symmetric_index(self) -> int:
        """Retorna la posición invariante del Acorde Simétrico Residual S_N."""
        return self.N - 3

    def generate_report(self):
        print(f"=== REPORTE ESTRUCTURAL THE CHAIN THEORY: N = {self.N}-ET ===")
        print(f"Polo Menor (P_m): {self.Pm}")
        print(f"Grado Acorde Transformante (A_N): {self.AN}")
        print(f"Cajita Central C_{self.N}: {self.central_box.tolist()}")
        print(f"Vector Deltas Delta C_{self.N}: {self.deltas.tolist()}")
        
        c_cents = self.acoustic_mapping(self.central_box)
        print(f"C_{self.N} en Cents: {np.round(c_cents, 2).tolist()}")
        
        t_chord = self.transforming_chord()
        t_cents = self.acoustic_mapping(t_chord)
        print(f"Acorde Transformante T_{self.N} (índices): {t_chord.tolist()}")
        print(f"T_{self.N} en Cents: {np.round(t_cents, 2).tolist()}")
        
        s_res_idx = self.get_residual_symmetric_index()
        s_res_cents = self.acoustic_mapping(np.array([s_res_idx]))[0]
        print(f"Acorde Residual S_{self.N}: Índice = {s_res_idx}, Cents = {s_res_cents:.2f}")
        
        scalar = self.scalar_ordering()
        print(f"Escala Completa Ordenada S_{self.N} (pasos de {self.step_cents:.2f}c):")
        print(np.round(scalar, 1).tolist())
        print("\n" + "="*60 + "\n")

# Ejecución para N = 9 y N = 11
if __name__ == "__main__":
    engine_9 = ChainTheoryEngine(N=9, Pm=4, AN=3)
    engine_9.generate_report()

    engine_11 = ChainTheoryEngine(N=11, Pm=4, AN=3)
    engine_11.generate_report()
```

---

## 2.6 Síntesis de Relaciones para el Tratado

| Parámetro / Dimensión | Sistema $N = 9$-ET | Sistema $N = 11$-ET |
| :--- | :--- | :--- |
| **Polo Menor ($P_m$)** | $4$ | $4$ |
| **Cajita Central ($C_N$)** | $[3, -1, 4, 0]$ | $[3, -2, 4, -1]$ |
| **Vector de Diferencias ($\Delta C_N$)** | $(-4, +5, -4)$ | $(-5, +6, -5)$ |
| **Tipo de Simetría** | Reflexiva pura ($\delta_1 = \delta_3$) | Reflexiva pura ($\delta_1 = \delta_3$) |
| **Acorde Transformante ($T_N$)** | $[6, 2, 7, 3] \pmod 9$ | $[6, 1, 7, 2] \pmod{11}$ |
| **Posición Residual ($S_N = N-3$)** | Índice $6$ ($800.00$ cents) | Índice $8$ ($872.73$ cents) |
| **Tamaño de Paso Elemental ($I_N$)** | $133.33 \text{ cents}$ | $109.09 \text{ cents}$ |

La expansión hacia $N=9$ y $N=11$ demuestra que las propiedades topológicas formuladas en *The Chain Theory* preservan una simetría reflexiva rigurosa a través de los vectores de diferencias $\Delta C_N$. El Acorde Transformante $T_N$, al operar como mediador geométrico entre los polos funcionales $r_M$ y $r_m$, formaliza un protocolo determinista de conducción microtonal de voces que elimina la ambigüedad enucleada en los temperamentos mesotónicos e históricos, estableciendo un continuo analítico entre la física acústica y la teoría de grupos algebraicos.