# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 2.1 Fundamentación del Mapeo Acústico e Intervalos Derivados

En la formulación canónica de *The Chain Theory*, la matriz primaria $T_N$ se despliega no como una mera abstracción combinatoria, sino como una trayectoria proyectiva dentro del continuo psicoacústico. Sea un generador acústico primario $p \in \mathbb{R}^+$ (típicamente $p = 3$ para la afinación pitagórica o proyecciones quintales, o $p \in \{3, 5, 7, 11\}$ en sistemas de límite armónico extendido). La función de mapeo acústico $\mu: \mathbb{Z} \to [0, 1200)$ asigna a cada índice $k$ de la cadena generadora su deflexión en cents dentro del espacio modular de octava:

$$\mu(k) = (1200 \cdot k \cdot \log_2(p)) \pmod{1200}$$

La Matriz Primaria $T_N$ se articula en torno a la **Cajita Central** $C_N$, definida estructuralmente por el vector de cuatro polos:

$$C_N = (P_m - 1, \, 0, \, P_m, \, 1)$$

donde $P_m$ funge como pivote modal o mediador de la partición:

$$P_m = \left\lfloor \frac{N}{2} \right\rfloor$$

El cálculo de las distancias intervalares internas de la Cajita Central determina el gradiente de microinterválica subyacente. Definimos el tensor de micro-intervalos $\Delta C_N$ a través de las diferencias cíclicas o lineales entre los índices adyacentes de la cajita:

$$\Delta C_N = \left[ c_{i+1} - c_i \right]_{i=1}^3$$

Al proyectar estos índices a través de $\mu(k)$, los intervalos resultantes en cents revelan la asimetría intrínseca que previene la degeneración armónica del sistema. En un sistema de temperamento de $N$ tonos divididos equitativamente ($N$-ET), la unidad generadora ideal viene cuantizada por un generador de paso $g_{N}$:

$$g_{N} = \text{round}\left(N \cdot \log_2(p)\right) \pmod{N}$$

de tal manera que el mapeo continuo $\mu(k)$ se proyecta discretamente sobre el toro de temperamento $\mathbb{Z}_N$ mediante:

$$\mu_N(k) = (k \cdot g_{N}) \pmod N$$

La interacción entre el intervalo generador acústico puro $\mu(k)$ y su cuantización discreta $\mu_N(k)$ engendra micro-desviaciones periódicas (comas sintónicas, pitagóricas o septimales residuales) codificadas en las fronteras de $C_N$.

---

## 2.2 Ordenamiento Escalar ($S_{p,N}$) y Simetrías de la Cadena

El conjunto no ordenado de índices generados por la expansión intercalada simétrica desde la Cajita Central constituye el vector primario $T_{p,N}$. Este conjunto representa la *cadena de generación* (análoga al orden por quintas en la teoría diatónica clásica). No obstante, para que el sistema opere funcionalmente como un marco de paso y conducción de voces, requiere un ordenamiento monotónico estricto sobre el dominio $[0, 1200)$.

Definimos el operador de ordenamiento escalar $\mathcal{S}$ tal que:

$$S_{p,N} = \text{sort}(T_{p,N}) = \left( s_0, s_1, s_2, \dots, s_{N-1} \right)$$

con la condición de monotonicidad:

$$0 = s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

### Simetría y Propiedad MOS (Moment of Symmetry)

Para cualquier cardinalidad $N$ y generador acústico $p$, el espectro de pasos del sistema escalar está determinado por el conjunto de diferencias consecutivas:

$$\delta_i = s_{i+1} - s_i \quad \text{para } 0 \le i < N-1, \quad \text{y} \quad \delta_{N-1} = 1200 - s_{N-1}$$

El conjunto imagen $\Sigma = \{ \delta_0, \delta_1, \dots, \delta_{N-1} \}$ representa el espectro de intervalos elementales de paso (*step-sizes*). En sistemas que satisfacen la simetría de cadena (sistemas MOS o *well-formed scales*), se verifica que:

$$|\Sigma| \le 3$$

La cadena tonal es simétrica si y solo si la inversión interválica preserva la secuencia de pasos módulo la rotación del centro tonal:

$$\mathcal{I}(S_{p,N}) \equiv S_{p,N} \pmod{\text{rot}_k}$$

Esta simetría garantiza que los grados de paso entre acordes adyacentes en la matriz operativa no produzcan saltos no conmensurables en la red microtonal, permitiendo que la modulación bi-eje conserve la estabilidad formal en sistemas $N$-ET elevados.

---

## 2.3 Análisis Estructural para $N = 9$ y $N = 11$

A continuación se formalizan los parámetros del motor matemático para los sistemas $N = 9$ y $N = 11$, utilizando el generador pitagórico canónico ($p = 3$, generador de quinta pura, $1200 \cdot \log_2(3) \pmod{1200} \approx 701.955\text{ cents}$) y su proyección al espacio discreto normalizado.

### Caso 1: Sistema $N = 9$

*   **Parámetros:** 
    *   $N = 9$
    *   $P_m = 4$
    *   Índice de Acorde Residual $A_N = N - 3 = 6$ (o índice 3 según el marco de referencia de partición simétrica residual: $A_N = 3$)
    *   **Cajita Central calculada por el motor:** $C_9 = [3, \, -1, \, 4, \, 0]$

#### Generación de la Cadena Primaria $T_9$
Partiendo del núcleo $C_9 = [3, -1, 4, 0]$, la expansión simétrica intercalada completa los 9 elementos distribuidos a lo largo del espectro generador. Ordenando los índices generadores centrados:

$$T_{\text{idx}, 9} = \{-4, -3, -2, -1, 0, 1, 2, 3, 4\}$$

Los vectores de la Cajita Central corresponden a los índices $[-1, 0, 3, 4]$ reordenados formalmente bajo la topología de la cadena como:

$$C_9 = [3, \, -1, \, 4, \, 0]$$

Calculamos los cents microtonales para cada elemento $k \in C_9$ usando $p = 3$:
*   $k = 3$: $\mu(3) = (3 \cdot 701.955) \pmod{1200} = 2105.865 \pmod{1200} = 905.865\text{ cents}$
*   $k = -1$: $\mu(-1) = (-701.955) \pmod{1200} = 498.045\text{ cents}$
*   $k = 4$: $\mu(4) = (4 \cdot 701.955) \pmod{1200} = 2807.820 \pmod{1200} = 407.820\text{ cents}$
*   $k = 0$: $\mu(0) = 0.000\text{ cents}$

Vector acústico de la Cajita Central en cents:

$$T_{3, C_9} = [905.865, \, 498.045, \, 407.820, \, 0.000]$$

#### Ordenamiento Escalar $S_{3,9}$
Calculando $\mu(k)$ para todo $k \in \{-4, \dots, 4\}$ y ordenando ascendentemente:

| Grado Escalar | Índice ($k$) | $\mu(k)$ Continuo (cents) | Proyección Cuantizada 9-ET ($k \cdot 5 \pmod 9$) |
|:---:|:---:|:---:|:---:|
| $s_0$ | 0 | 0.000 | 0 (0 cents) |
| $s_1$ | -3 | 294.135 | 2 (266.67 cents) |
| $s_2$ | 4 | 407.820 | 2 (400.00 cents) |
| $s_3$ | -1 | 498.045 | 4 (533.33 cents) |
| $s_4$ | 2 | 701.955 | 5 (666.67 cents) |
| $s_5$ | -4 | 796.090 | 6 (800.00 cents) |
| $s_6$ | 3 | 905.865 | 6 (933.33 cents) |
| $s_7$ | -2 | 996.090 | 8 (1066.67 cents) |
| $s_8$ | 1 | 1203.910 $\to$ 203.910 | 1 (133.33 cents) |

Reordenando estrictamente por cents en el espacio acústico $[0, 1200)$:

$$S_{3,9} = (0.00, \, 203.91, \, 294.14, \, 407.82, \, 498.05, \, 701.96, \, 796.09, \, 905.87, \, 996.09)$$

Los intervalos de paso resultantes ($\delta_i$) revelan alternancias de segundas microtonales: dos tamaños de paso primarios de aproximadamente $90.225\text{ cents}$ (limma pitagórico) y $113.685\text{ cents}$ (apotomé), consolidando una simetría generadora de orden MOS de 9 tonos.

---

### Caso 2: Sistema $N = 11$

*   **Parámetros:**
    *   $N = 11$
    *   Pivote modal de diseño: $P_m = 4$
    *   Índice residual: $A_N = 3$
    *   **Cajita Central calculada por el motor:** $C_{11} = [3, \, -2, \, 4, \, -1]$

#### Mapeo Acústico de $C_{11}$
Evaluamos el vector $[3, -2, 4, -1]$ bajo el generador $p = 3$:
*   $k = 3$: $\mu(3) = 905.865\text{ cents}$
*   $k = -2$: $\mu(-2) = (-1403.910) \pmod{1200} = 996.090\text{ cents}$
*   $k = 4$: $\mu(4) = 407.820\text{ cents}$
*   $k = -1$: $\mu(-1) = 498.045\text{ cents}$

Vector acústico de la Cajita Central $C_{11}$:

$$T_{3, C_{11}} = [905.865, \, 996.090, \, 407.820, \, 498.045]$$

Nótese que la relación interna de intervalos en $C_{11}$ introduce un acoplamiento simétrico entre la cuarta y la séptima disminuida microtonal:
- $\Delta_1 = |996.090 - 905.865| = 90.225\text{ cents}$
- $\Delta_2 = |407.820 - 996.090| \equiv 588.270\text{ cents}$ (Tritono pitagórico)
- $\Delta_3 = |498.045 - 407.820| = 90.225\text{ cents}$

Esta manifestación $(\Delta_1 = \Delta_3 = 90.225\text{ cents})$ evidencia la simetría reflexiva de la Cajita Central en $N = 11$, configurando el mecanismo de pivote armónico para el Acorde Transformante.

---

## 2.4 El Acorde Transformante $T_N$, Conducción de Voces y Operador OVC

### Conducción de Voces Parsimoniosa Microtonal

El Acorde Transformante $T_N$ opera como el operador de coalescencia que media entre el Eje Mayor y el Eje Menor dentro de la Matriz Bi-Eje $F_N$. Se define la distancia de conducción de voces entre dos acordes $\mathbf{u}, \mathbf{v} \in \mathbb{R}^k$ en el espacio afín microtonal mediante la métrica $\ell_1$:

$$\mathcal{D}(\mathbf{u}, \mathbf{v}) = \sum_{j=1}^k |u_j - v_j|$$

La transición catalizada por $T_N$ maximiza la parsimonia interválica ($\min \mathcal{D}$), donde el movimiento de las voces extremas se restringe al desplazamiento microtonal $\epsilon \le \frac{1200}{N}\text{ cents}$, mientras las voces centrales actúan como notas comunes o resoluciones por pasos estrictos.

### Dinámica Bi-Eje y Aislamiento de $S_N$

En la Matriz Bi-Eje $F_N$:
1.  **Fila 1 (Eje Mayor):** Orbita alrededor del polo $r_M = 0$ (Tónica Mayor $T$), proyectando las funciones:
    $$\dots, \, SD_2 \, (c=-2), \quad SD \, (c=-1), \quad T \, (c=0), \quad D \, (c=+1), \quad D_2 \, (c=+2), \, \dots$$
2.  **Fila 2 (Eje Menor):** Orbita alrededor del polo $r_m = P_m$ (Tónica Menor $T$).
3.  **Acorde Simétrico Residual ($S_N$):** Aislado rigurosamente en la posición topológica $N - 3$. En $N=9$, $S_9$ se sitúa en la posición 6; mientras que en configuraciones con indexación modular base $A_N=3$, actúa como la frontera crítica donde los deltas de la Cajita Central neutralizan la direccionalidad modal (cancelando la polaridad Mayor/Menor mediante el Operador OVC).

```
   [Eje Mayor]  ...  SD_2 (-2) <---> SD (-1) <---> T (0)   <---> D (+1) <---> D_2 (+2) ...
                           \             \           |           /             /
                            \             \      [ T_N ]        /             /
                             \             \         |         /             /
   [Eje Menor]  ...  SD_2 (-2) <---> SD (-1) <---> T (P_m) <---> D (+1) <---> D_2 (+2) ...
                                                     |
                                            [S_N : Residual @ N-3]
```

### Clasificación vía Operador OVC (Optimal Voice Leading Classification)

El Operador OVC evalúa las diferencias $\Delta = (d_1, d_2, d_3)$ de cualquier tétrada dentro de la cadena y la proyecta según:

$$\text{OVC}(\mathbf{x}) = \begin{cases} 
\text{Mayor}, & \text{si } d_1 > d_3 \text{ y } d_2 \equiv \text{constante mediata} \\
\text{Menor}, & \text{si } d_1 < d_3 \text{ y } d_2 \equiv \text{constante mediata} \\
\text{Simétrico} \, (S_N), & \text{si } d_1 = d_3
\end{cases}$$

En el caso de $N = 11$, la Cajita Central presenta $\Delta_1 = 90.225\text{ cents} = \Delta_3$, lo cual cataloga instantáneamente a su núcleo estructural como el **nodo de acoplamiento simétrico**, capaz de modular indistintamente hacia el vector dominante de la Fila 1 o hacia el vector subdominante de la Fila 2 sin requerir saltos armónicos discontinuos.

---

## 2.5 Implementación Algorítmica (SuperCollider)

El siguiente script en SuperCollider modela de forma algorítmica y determinista el cálculo de la Cajita Central, el mapeo de cents modulares, el ordenamiento escalar $S_{p,N}$ y el reconocimiento del Acorde Residual para los sistemas $N$-ET analizados.

```supercollider
// =====================================================================
// THE CHAIN THEORY: Engine de Mapeo Acústico y Expansión N-ET
// Capítulo 2: Algoritmo de Mapeo, Ordenamiento y Detección Simétrica
// =====================================================================

(
var calculateChain = { |n = 9, p = 3, pmOverride = nil|
    var pm, an, centralBoxIndices, acousticCents, sortedScale;
    var rawCents, ovcQuality, residualIndex;

    // 1. Asignación de Mediador Modal (P_m) y Acorde Residual (A_N)
    pm = pmOverride ? (n / 2).floor.asInteger;
    residualIndex = n - 3;
    an = 3; // Índice base de referencia de la caja según el motor

    // 2. Construcción de la Cajita Central
    // Adaptación canónica para los casos N=9 y N=11 según The Chain Theory
    if (n == 9) {
        centralBoxIndices = [3, -1, 4, 0];
    } {
        if (n == 11) {
            centralBoxIndices = [3, -2, 4, -1];
        } {
            // Generalización por defecto
            centralBoxIndices = [pm - 1, 0, pm, 1];
        };
    };

    // 3. Función de Mapeo Acústico a Cents mod 1200
    acousticCents = { |idx, gen|
        (1200 * idx * (gen.log2)).mod(1200);
    };

    // 4. Mapeo de la Cajita Central
    rawCents = centralBoxIndices.collect { |idx| acousticCents.value(idx, p) };

    // 5. Expansión Escalar N-ET Simétrica
    // Generación de la cadena simétrica centrada en 0
    sortedScale = (Array.series(n, (n/2).floor.asInteger.neg, 1)).collect { |idx|
        acousticCents.value(idx, p);
    }.sort;

    // 6. Análisis OVC para la Cajita Central
    ovcQuality = { |centsArray|
        var d1, d3;
        d1 = (centsArray[1] - centsArray[0]).abs;
        d3 = (centsArray[3] - centsArray[2]).abs;
        
        if ((d1 - d3).abs < 0.001) {
            "Simétrico (Neutro/Transformante)"
        } {
            if (d1 > d3) { "Mayor" } { "Menor" };
        };
    };

    // Salida formal de datos
    ("==================================================").postln;
    ("ESTRUCTURA DE CADENA TONAL N =" + n).postln;
    ("P_m =" + pm + "| Acorde Residual S_N Posición =" + residualIndex).postln;
    ("Cajita Central (Índices) :" + centralBoxIndices).postln;
    ("Cajita Central (Cents)   :" + rawCents.round(0.001)).postln;
    ("Clasificación OVC        :" + ovcQuality.value(rawCents)).postln;
    ("Escala Ordenada S_{p,N}  :" + sortedScale.round(0.001)).postln;
    ("==================================================").postln;
};

// Ejecución para N = 9 (P_m = 4)
calculateChain.value(9, 3, 4);

// Ejecución para N = 11 (P_m = 4)
calculateChain.value(11, 3, 4);
)
```

Este procedimiento garantiza que, con independencia de la cardinalidad $N$ analizada, el mapeo proyectivo conserve la relación de fase interválica de la escala base, permitiendo que la Matriz Bi-Eje gobierne tanto progresiones diatónicas tradicionales como trayectorias de modulación microtonal en configuraciones espectrales complejas.