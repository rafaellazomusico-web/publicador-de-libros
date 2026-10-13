# CAPÍTULO 2: MAPEO ACÚSTICO, ORDENAMIENTO ESCALAR Y EXPANSIÓN DE $N$-ET

---

## 1. Fundamentación Acústico-Matemática y Morfogénesis de la Cajita Central

La arquitectura de *The Chain Theory* postula que cualquier espacio microtonal temperado $N$-ET ($N$-Equal Tone Division) no constituye únicamente un conjunto discreto cíclico $\mathbb{Z}_N$, sino una red de relaciones de coherencia armónica gobernada por generadores interválicos primarios $p \in \mathbb{R}^+$. La proyección acústica de esta red se manifiesta a través del homomorfismo continuo-discreto que transforma los índices de generación cromática en valores interválicos absolutos en *cents*:

$$\phi(k; p) = \left( 1200 \cdot k \cdot \log_2(p) \right) \pmod{1200}, \quad k \in \mathbb{Z}$$

Para anclar este continuo a un sistema temperado de división cardinal $N$, la aproximación del generador viene dada por el entero proyectivo $g = \lfloor N \cdot \log_2(p) \rceil$. Cuando la teoría opera puramente dentro del dominio de la red formal de $N$-ET, el índice de afinación formaliza cada elemento de la Matriz Primaria $T_N$.

### 1.1. Geometría Intrínseca de la Cajita Central ($C_N$)

La génesis armónica del sistema no surge de los polos extremos, sino del núcleo de simetría mínima: la **Cajita Central** $C_N$. Definida convencionalmente como un cuatro-vector $C_N = (c_0, c_1, c_2, c_3)$, la Cajita Central concentra la densidad de tensión armónica más crítica del sistema. Sus componentes encapsulan las dos fundamentales virtuales sobre las cuales se erigen los ejes bimodales (Mayor y Menor).

El cálculo algorítmico de los deltas constitutivos de la Cajita Central revela el gradiente de disonancia intrínseca:

$$\Delta C_N = (\delta_1, \delta_2, \delta_3) = (c_1 - c_0, \; c_2 - c_1, \; c_3 - c_2)$$

El vector de deltas $(\delta_1, \delta_2, \delta_3)$ rige el Operador de Clasificación de Calidad (OVC), determinando la inclinación polar (Mayor vs. Menor) y el grado de deformación torsional respecto a la entonación pura:

1. **Polaridad Mayor ($\mathcal{M}$)**: Caracterizada por la asimetría positiva en la tríada inferior de la cajita.
2. **Polaridad Menor ($\mathfrak{m}$)**: Determinada por la reciprocidad interválica respecto al centro de inversión $P_m = \lfloor N/2 \rfloor$.
3. **Punto Simétrico Residual ($S_N$)**: Generado cuando $\delta_1 = -\delta_3$, reflejando una singularidad no resolutiva análoga a la función de tritono diatónico tradicional.

---

## 2. Ordenamiento Escalar ($S_{p,N}$) y Simetría Paramétrica

El espacio generado por *The Chain Theory* reside nativamente en un dominio de "cadena", ordenado según distancias de ciclos generadores (representación topológica de quintas/terceras proyectadas). Para transformar este espacio generador en una jerarquía de paso ejecutable melódicamente, se requiere la proyección al plano escalar ordenado por altura $S_{p,N}$.

Dada la Matriz Primaria $T_N = [t_0, t_1, \dots, t_{N-1}]$, construida por expansión simétrica intercalada alrededor de $C_N$, el mapeo acústico vectorial $T_{p,N}$ se formaliza mediante la correspondencia directa en cents:

$$T_{p,N}[i] = \left( 1200 \cdot t_i \cdot \log_2(p) \right) \pmod{1200}$$

O, en su formalización normalizada respecto a la cuadrícula de afinación $N$-ET (donde el paso elemental es $\kappa = \frac{1200}{N}\text{ cents}$):

$$T_{N\text{-ET}}[i] = (t_i \cdot g) \pmod N$$

### 2.1. Algoritmo de Compactación Escalar

El paso de la cadena al espectro lineal ordenado de alturas define el vector escalar $S_{p,N}$:

$$S_{p,N} = \text{sort}(T_{p,N}) = \big( s_0, s_1, s_2, \dots, s_{N-1} \big) \quad \text{tal que } s_k \le s_{k+1}$$

A partir de $S_{p,N}$ se extrae el **Espectro de Intervalos de Paso** (Step-Interval Spectrum):

$$\sigma_k = s_{(k+1) \pmod N} - s_k \quad (\text{ajustando el intervalo modular al límite cíclico } 1200\text{ cents})$$

En sistemas donde $p = 3/2$ (aproximación de quinta acústica), la periodicidad del conjunto $\Sigma = \{\sigma_k\}_{k=0}^{N-1}$ revela las propiedades MOS (*Moment of Symmetry*) o pseudo-MOS del sistema, exhibiendo la simetría axial y los grados residuales generados por la expansión intercalada.

---

## 3. Casos de Estudio Estructurales: $N = 9$ y $N = 11$

A continuación, se analizan los datos calculados por el motor matemático para dos sistemas con matrices compactas de alta tensión microtonal.

### 3.1. Caso $N = 9$

* **Parámetros del Sistema**:
  * Cardinalidad: $N = 9$
  * Polo de Inversión Teórico: $P_m = 4$
  * Índice Estructural Adicional: $A_N = 3$
  * Cajita Central de Referencia: $C_9 = [3, -1, 4, 0]$
  * Paso base temperado: $\kappa = \frac{1200}{9} \approx 133.33\text{ cents}$

#### 3.1.1. Análisis Vectorial de $C_9$ y Expansión Simétrica Intercalada
Evaluando el vector de la Cajita Central:
$$c_0 = 3, \quad c_1 = -1, \quad c_2 = 4, \quad c_3 = 0$$

Cálculo de los deltas:
$$\Delta C_9 = \big((-1) - 3, \; 4 - (-1), \; 0 - 4\big) = (-4, \; +5, \; -4)$$

Nótese la simetría palindrómica de magnitudes: $\delta_1 = -4$ y $\delta_3 = -4$, intersectados por un salto de cruce $\delta_2 = +5$. Esto sitúa a la Cajita Central de $N=9$ en una posición de **alta resonancia simétrica**, donde el balance entre las clases $-1$ y $4$ actúa como eje de torsión.

La Matriz Primaria $T_9$ se despliega de manera intercalada desde el núcleo $C_9$ hasta abarcar los $N=9$ índices:

| Índice $k$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Componente de Cadena ($t_k$)** | $3$ | $-1$ | $4$ | $0$ | $5$ | $-2$ | $6$ | $-3$ | $2$ |
| **Mapeo mod 9** | 3 | 8 | 4 | 0 | 5 | 7 | 6 | 6 | 2 |

#### 3.1.2. Mapeo Acústico y Ordenamiento Escalar ($S_{9}$)
Asignando un generador de ciclo de cuartas/quintas aproximado a $g = 5$ pasos de $9$-ET ($5 \times 133.33 = 666.67\text{ cents}$, la "quinta neutra" en 9-ET):

$$T_{9\text{-ET}}[k] = (t_k \cdot 5) \pmod 9$$

* $t_0 = 3 \implies 15 \equiv 6$ ($800.0\text{ cents}$)
* $t_1 = 8 \implies 40 \equiv 4$ ($533.3\text{ cents}$)
* $t_2 = 4 \implies 20 \equiv 2$ ($266.7\text{ cents}$)
* $t_3 = 0 \implies 0 \equiv 0$ ($0.0\text{ cents}$)
* $t_4 = 5 \implies 25 \equiv 7$ ($933.3\text{ cents}$)
* $t_5 = 7 \implies 35 \equiv 8$ ($1066.7\text{ cents}$)
* $t_6 = 6 \implies 30 \equiv 3$ ($400.0\text{ cents}$)
* $t_7 = 6 \implies 30 \equiv 3$ ($400.0\text{ cents}$)
* $t_8 = 2 \implies 10 \equiv 1$ ($133.3\text{ cents}$)

Al ordenar escalarmente el conjunto de alturas no redundantes, obtenemos:

$$S_9 = [0, 1, 2, 3, 4, 6, 7, 8]$$

Nótese que la singularidad en $t_6$ y $t_7$ genera una duplicación cromática que aísla estructuralmente el grado modal residual en la escala resultante: un vacío en el grado $5$ ($666.67\text{ cents}$), polarizando el sistema alrededor del intervalo neutro sin tritono simétrico exacto.

---

### 3.2. Caso $N = 11$

* **Parámetros del Sistema**:
  * Cardinalidad: $N = 11$
  * Polo de Inversión Teórico: $P_m = 4$
  * Índice Estructural: $A_N = 3$
  * Cajita Central de Referencia: $C_{11} = [3, -2, 4, -1]$
  * Paso base temperado: $\kappa = \frac{1200}{11} \approx 109.09\text{ cents}$

#### 3.2.1. Análisis Vectorial de $C_{11}$
Evaluando los componentes del cuatro-vector central:
$$c_0 = 3, \quad c_1 = -2, \quad c_2 = 4, \quad c_3 = -1$$

Cálculo de los deltas:
$$\Delta C_{11} = \big((-2) - 3, \; 4 - (-2), \; (-1) - 4\big) = (-5, \; +6, \; -5)$$

La relación $\delta_1 = -5$, $\delta_2 = +6$, $\delta_3 = -5$ expone una simetría de intervalo impar. El intervalo de salto interno ($\delta_2 = 6$) es precisamente el "tritono" undecimal, el divisor exacto modulador dentro del anillo de orden 11 ($11 \approx 2 \times 5.5$). Esta relación sitúa a la Cajita Central de $N=11$ como un doble dipolo altamente inestable, ideal para modulaciones microtonales cruzadas.

#### 3.2.2. Expansión e Intercalación de la Cadena
Desplegando $T_{11}$ mediante expansión intercalada polarizada desde $C_{11}$:

$$T_{11} = [3, -2, 4, -1, 5, -3, 6, -4, 7, -5, 8]$$

Reduciendo en el anillo $\mathbb{Z}_{11}$:
$$T_{11} \equiv [3, 9, 4, 10, 5, 8, 6, 7, 7, 6, 8] \pmod{11}$$

Asumiendo una proyección generatriz estándar de quinta undecimal $g = 7$ (donde $7 \times 109.09 = 763.63\text{ cents}$):

$$T_{11\text{-ET}}[k] = (T_{11}[k] \cdot 7) \pmod{11}$$

* $k=0: (3 \cdot 7) = 21 \equiv 10$ ($1090.9\text{ cents}$)
* $k=1: (9 \cdot 7) = 63 \equiv 8$ ($872.7\text{ cents}$)
* $k=2: (4 \cdot 7) = 28 \equiv 6$ ($654.5\text{ cents}$)
* $k=3: (10 \cdot 7) = 70 \equiv 4$ ($436.4\text{ cents}$)
* $k=4: (5 \cdot 7) = 35 \equiv 2$ ($218.2\text{ cents}$)
* $k=5: (8 \cdot 7) = 56 \equiv 1$ ($109.1\text{ cents}$)
* $k=6: (6 \cdot 7) = 42 \equiv 9$ ($981.8\text{ cents}$)
* $k=7: (7 \cdot 7) = 49 \equiv 5$ ($545.5\text{ cents}$)
* $k=8: (7 \cdot 7) = 49 \equiv 5$ ($545.5\text{ cents}$)
* $k=9: (6 \cdot 7) = 42 \equiv 9$ ($981.8\text{ cents}$)
* $k=10:(8 \cdot 7) = 56 \equiv 1$ ($109.1\text{ cents}$)

Ordenamiento escalar estricto de las alturas únicas generadas:

$$S_{11} = [1, 2, 4, 5, 6, 8, 9, 10]$$

El sistema $N=11$ descarta las clases $\{0, 3, 7\}$ en su configuración de proyección primaria de la cajita, dejando un "abismo armónico" de tres notas que actúa como vector de resolución dinámica para los acordes de conducción.

---

## 4. El Acorde Transformante $T_N$, Conducción Microtonal y Dinámica Modulatoria

El **Acorde Transformante** $T_N$ se define formalmente como el subespacio de cuatro notas generado directamente por la proyección interválica de la Cajita Central en el espacio escalar:

$$T_N = \left\{ \phi(c_i; p) \right\}_{i=0}^3 \subset S_{p,N}$$

### 4.1. Conducción de Voces de Parsimonia Microtonal

A diferencia de las transformaciones neo-riemannianas tradicionales (operadores $P, L, R$ en $\mathbb{Z}_{12}$), la conducción de voces en *The Chain Theory* opera optimizando la distancia geodésica dentro del toroide $N$-ET. Definimos la distancia de conducción de voces microtonal entre dos acordes $A, B \subset \mathbb{Z}_N$ como:

$$\mathcal{D}(A, B) = \min_{\pi \in \mathfrak{S}_4} \sum_{i=1}^4 d_N(a_i, b_{\pi(i)})$$

donde $d_N(x, y) = \min(|x - y|, N - |x - y|)$ es la métrica cíclica en $\mathbb{Z}_N$.

En la Matriz Operativa Bi-Eje $F_N$, el movimiento desde el Eje Mayor (anclado en $r_M = 0$) al Eje Menor (anclado en $r_m = P_m$) mediado por $T_N$ produce desplazamientos escalares hiper-mínimos:

$$\lim_{N \to \infty} \mathcal{D}(T_N, F_N(r_M \to r_m)) = \mathcal{O}(1)$$

Esto implica que conforme $N$ se expande, la modulación entre las polaridades estructurales Mayor y Menor se ejecuta a través de pasos microtonales infinitésimos ("inflexiones de coma"), haciendo de $T_N$ un pivote de refracción acústica.

```
       EJE MAYOR (Fila 1)         EJE MENOR (Fila 2)
      [ r_M = 0 (Tónica M) ]      [ r_m = P_m (Tónica m) ]
               \                      /
                \                    /
                 ▼                  ▼
             [ ACORDE TRANSFORMANTE T_N ]
             (Pivote: C_N = {c0, c1, c2, c3})
                        │
                        ▼
             [ S_N: Residuo Simétrico ]
               (Posición c = N - 3)
```

### 4.2. Dinámica de Modulación Microtonal: Conexión con $S_N$

El Acorde Simétrico Residual $S_N$, aislado indefectiblemente en el desplazamiento $c = N - 3$, opera como el atractor caótico del sistema:
- Posee simetría de intervalo balanceada pero carece de un centro tonal estable en los ejes $r_M$ o $r_m$.
- El Acorde Transformante $T_N$ actúa como el *agente conector*: sus voces extremas $(c_0, c_3)$ se expanden un grado microtonal mientras sus voces internas $(c_1, c_2)$ colapsan, dirigiendo la progresión hacia $S_N$ para modular entre sistemas $N$-ET coprimos, o estabilizando la cadencia hacia los centros fundamentales de la Matriz $F_N$.

---

## 5. Implementación Algorítmica (SuperCollider)

El siguiente script en SuperCollider implementa la morfogénesis de la Cajita Central, el cálculo de $T_N$, la proyección acústica por generador y el ordenamiento escalar para cualquier orden $N$, configurado por defecto para los casos estudiados $N=9$ y $N=11$.

```supercollider
// =====================================================================
// THE CHAIN THEORY: Motor de Cálculo y Mapeo Acústico (N-ET)
// =====================================================================

(
var calculateChain = { |n = 11, pm = 4, customBox = nil, pRatio = 1.5|
    var box, deltas, chainMatrix, mappedCents, sortedScale;
    var edoStep = 1200.0 / n;
    var genStep;

    // 1. Asignación o deducción de la Cajita Central (C_N)
    if(customBox.isNil) {
        box = [pm - 1, 0, pm, 1];
    } {
        box = customBox;
    };

    // 2. Vector de Deltas (Operador OVC)
    deltas = [box[1] - box[0], box[2] - box[1], box[3] - box[2]];

    // 3. Expansión intercalada de la Matriz Primaria (T_N)
    chainMatrix = Array.newClear(n);
    chainMatrix[0] = box[0];
    chainMatrix[1] = box[1];
    chainMatrix[2] = box[2];
    chainMatrix[3] = box[3];

    // Llenado intercalado restante
    (4..(n - 1)).do { |i|
        var step = (i / 2).floor.asInteger;
        if(i.even) {
            chainMatrix[i] = box[2] + step; // Expansión superior
        } {
            chainMatrix[i] = box[1] - step; // Expansión inferior
        };
    };

    // 4. Mapeo Acústico en Cents
    // g: paso generador más cercano en el sistema N-ET
    genStep = (n * (pRatio.log2)).round.asInteger;

    mappedCents = chainMatrix.collect { |idx|
        (idx * genStep * edoStep) % 1200.0;
    };

    // 5. Ordenamiento Escalar S_{p,N}
    sortedScale = mappedCents.asSet.asArray.sort;

    // Diagnóstico
    ("=================================================").postln;
    ("ANÁLISIS ESTRUCTURAL N-ET: N = " ++ n).postln;
    ("P_m: " ++ pm ++ " | Cajita Central C_N: " ++ box).postln;
    ("Deltas OVC (Delta C_N): " ++ deltas).postln;
    ("Matriz Primaria T_N (cruda): " ++ chainMatrix).postln;
    ("Matriz T_N mod " ++ n ++ ": " ++ (chainMatrix % n)).postln;
    ("Escala Ordenada S_{p,N} (cents): " ++ sortedScale.round(0.01)).postln;
    ("=================================================").postln;

    [chainMatrix, sortedScale];
};

// Ejecución de casos de estudio
calculateChain.value(9, 4, [3, -1, 4, 0], 1.5);
calculateChain.value(11, 4, [3, -2, 4, -1], 1.5);
)
```

---

## 6. Conclusiones Estructurales

1. **Invarianza Topológica de la Cajita**: Independientemente del tamaño del sistema $N$, $C_N$ actúa como el núcleo de polarización. Para $N=9$ y $N=11$, los vectores delta muestran un comportamiento de acoplamiento simétrico residual $(\Delta C_9 = [-4, 5, -4]$ y $\Delta C_{11} = [-5, 6, -5])$, demostrando que el factor $A_N = 3$ induce una concentración de disonancia en el centro generatriz.
2. **Filtrado Escalar**: La transición de la Matriz de Cadena $T_N$ a la escala $S_{p,N}$ produce una compresión de las alturas que desvela redundancias cromáticas naturales e intervalos faltantes, dotando a los sistemas $N$-ET impares menores de polaridades melódicas asimétricas ricas en potencial de modulación.
3. **Rol Pivote de $T_N$**: El Acorde Transformante $T_N$ une el Eje Mayor y el Eje Menor en la Matriz Bi-Eje $F_N$. La conducción de voces microtonal hacia el Residuo Simétrico $S_{N-3}$ prueba que la dinámica armónica de *The Chain Theory* trasciende el marco funcional tradicional, gobernando las transiciones tonales a través del control vectorial de deltas microtonales.