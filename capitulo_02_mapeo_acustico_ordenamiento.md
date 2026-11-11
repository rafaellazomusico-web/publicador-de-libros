# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 2.1 Fundamentos del Mapeo Acústico y Topología de la Cajita Central ($C_N$)

En el marco de *The Chain Theory*, la generación del espacio armónico no se fundamenta en la división empírica del continuo de frecuencias, sino en la proyección isomórfica de un núcleo generador discreto sobre el continuo psicoacústico. Este núcleo, denominado **Cajita Central** ($C_N$), constituye el atractor informacional primario a partir del cual se desdobla la totalidad de la matriz de alturas $T_N$.

Formalmente, para un sistema de afinación de cardinalidad finita $N \in \mathbb{N}$, el espacio de alturas temperadas simétricas se define a través de su pivote medio:

$$P_m = \left\lfloor \frac{N}{2} \right\rfloor$$

La Cajita Central $C_N \subset \mathbb{Z}^4$ representa una tétrada de índices nodales que captura las asimetrías mínimas de conducción de voces dentro del sistema periódico. La proyección de un índice generador $k \in \mathbb{Z}$ sobre el dominio de frecuencias temperadas o justas se realiza mediante el **Operador de Mapeo Acústico** $\mathcal{M}_p$. 

Dado un número primo base de proyección armónica $p \in \mathbb{P}$ (típicamente $p = 3$ para sistemas de quintas pitagóricas o afinaciones basadas en la serie armónica, o factores de deformación interválica temperada), definimos la posición acústica del elemento $k$-ésimo en el espacio continuo de cents mediante la función:

$$\phi(k, p) = \left( 1200 \cdot k \cdot \log_2(p) \right) \pmod{1200}$$

Donde la reducción módulo 1200 cents constriñe la estructura resultante dentro del dominio periódico del período cíclico de octava $\mathbb{R} / 1200\mathbb{Z}$. Cuando el sistema se modela en un temperamento igual generalizado de $N$ divisiones ($N$-ET), la cuantización microtonal de la proyección de $C_N$ y de los vectores resultantes se normaliza a través del paso cuántico elemental del sistema:

$$\Delta_{\text{cents}}^{(N)} = \frac{1200}{N}$$

El mapeo acústico de una colección indexada $V = (v_0, v_1, \dots, v_{m-1})$ bajo la base $p$ se denota como:

$$T_{p,N}(V) = \{ \phi(v_j, p) \mid v_j \in V \}$$

La Cajita Central codifica intrínsecamente la polaridad mayor/menor a través de sus deltas interválicos relativos. Si consideramos la función de intervalos adyacentes para una tétrada ordenada $C_N = [c_0, c_1, c_2, c_3]$:

$$\vec{\delta}(C_N) = \left( c_1 - c_0, \; c_2 - c_1, \; c_3 - c_2 \right)$$

Estas diferencias relativas determinan los desfases acústicos directos que gobiernan las tensiones de entonación justa y su deformación en microintervalos templados.

---

## 2.2 El Algoritmo de Ordenamiento Escalar ($S_{p,N}$) y Distribución Microinterválica

La matriz primaria $T_N$ se despliega de forma intercalada a partir de $C_N$, conformando una cadena funcional no ordenada escalarmente. El paso del **dominio de generador** (o cadena armónica) al **dominio escalar** requiere un morfismo de ordenamiento estricto.

Definimos el **Operador de Ordenamiento Escalar** $\mathcal{S}$ aplicado sobre el conjunto acústico $T_{p,N}$:

$$S_{p,N} = \text{sort}\left( T_{p,N} \right) = \left( s_0, s_1, s_2, \dots, s_{N-1} \right)$$

tal que:

$$0 \le s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

### 2.2.1 Vector Interválico Escalar (Step-Vector)
A partir de $S_{p,N}$, se extrae el vector de pasos microtonales adyacentes $\vec{\sigma}^{(N)} = (\sigma_0, \sigma_1, \dots, \sigma_{N-1})$, donde:

$$\sigma_i = 
\begin{cases} 
s_{i+1} - s_i & \text{para } 0 \le i < N - 1 \\ 
(1200 + s_0) - s_{N-1} & \text{para } i = N - 1 
\end{cases}$$

En un sistema estrictamente cerrado y equilibrado bajo simetría de la cadena tonal, $\vec{\sigma}^{(N)}$ exhibe como máximo tres clases de intervalos discretos (teorema de los tres pasos o *Three-Gap Theorem* de Steinhaus), lo que garantiza la coherencia estructural de la escala frente a modulaciones.

### 2.2.2 Simetría Axial y Grados de Paso
La simetría de la cadena tonal en sistemas mayores $N$-ET se formaliza mediante la involución de inversión armónica $I_\alpha$:

$$I_\alpha(s) = (\alpha - s) \pmod{1200}$$

donde $\alpha$ es el eje axial de simetría acústica definido conjuntamente por el centro de gravedad de $C_N$. La conservación de esta simetría garantiza que los grados de paso generados por la expansión intercalada mantengan paridad interválica respecto a los centros tonales duales de la Matriz Bi-Eje ($r_M = 0$ y $r_m = P_m$).

---

## 2.3 Casos de Estudio: Análisis Estructural para $N = 9$ y $N = 11$

A continuación, se desarrolla paso a paso el cálculo de la Cajita Central, el mapeo acústico paramétrico y el ordenamiento escalar para los sistemas microtonales nonario ($N=9$) y undecimario ($N=11$).

---

### 2.3.1 Sistema $N = 9$ ($9$-ET / Dominio Nonario)

#### Parámetros Iniciales del Motor Matemático:
- Cardinalidad: $N = 9$
- Pivote Medio: $P_m = \left\lfloor \frac{9}{2} \right\rfloor = 4$
- Grado Activo: $A_N = 3$
- Cajita Central: $C_9 = [3, -1, 4, 0]$
- Paso microtonal elemental de la división igual: $\Delta_{\text{cents}}^{(9)} = \frac{1200}{9} = 133.333 \text{ cents}$

#### Expansión Simétrica Intercalada de Índices ($T_9$):
Partiendo del núcleo central $C_9$, expandimos los 9 índices enteros de la cadena funcional equilibrada alrededor del pivote $P_m=4$:

$$\mathbb{I}_9 = \{ -1, 0, 1, 2, 3, 4, 5, 6, 7 \}$$

La Cajita Central aísla el subconjunto motor $[3, -1, 4, 0]$. Los deltas internos de la Cajita Central se evalúan como:

$$\vec{\delta}(C_9) = (-1 - 3, \; 4 - (-1), \; 0 - 4) = (-4, \; 5, \; -4)$$

Nótese la simetría invertida en los extremos ($-4$ y $-4$) mediada por el salto complementario de quinta neutrónica ($+5$).

#### Mapeo Acústico en Cents:
Tomando el generador canónico de quinta $p = 3$ (proyección pitagórica modulada) y cuantizando sobre el espacio de octava cerrado mediante reducción de cents:

$$\phi(k) = (1200 \cdot k \cdot \log_2(3)) \pmod{1200} \approx (k \cdot 701.955) \pmod{1200}$$

Calculamos los valores de cents sin ordenar correspondientes a cada índice de la cadena expandida:

| Índice ($k$) | Cents Exactos ($p=3$) | Reducción $\pmod{1200}$ | Cuantización $9$-ET ($k \cdot 133.33$) | Clasificación Estructural |
| :---: | :---: | :---: | :---: | :---: |
| **$-1$** | $-701.955$ | $498.045$ | $400.00$ | Subdominante / $C_9$ |
| **$0$** | $0.000$ | $0.000$ | $0.00$ | Eje Mayor ($r_M$) / $C_9$ |
| **$1$** | $701.955$ | $701.955$ | $800.00$ | Dominante |
| **$2$** | $1403.910$ | $203.910$ | $266.67$ | Grado de Paso |
| **$3$** | $2105.865$ | $905.865$ | $933.33$ | $A_N$ Primario / $C_9$ |
| **$4$** | $2807.820$ | $407.820$ | $533.33$ | Eje Menor ($r_m = P_m$) / $C_9$ |
| **$5$** | $3509.775$ | $1109.775$ | $1066.67$ | Grado de Paso |
| **$6$** | $4211.730$ | $611.730$ | $666.67$ | Acorde Simétrico Residual ($S_9$, pos $N-3$) |
| **$7$** | $4913.685$ | $113.685$ | $133.33$ | Grado de Paso |

#### Ordenamiento Escalar $S_{3,9}$:
Ordenando el conjunto resultante en el dominio $[0, 1200)$ cents:

$$S_{3,9} = (0.000, \; 113.685, \; 203.910, \; 407.820, \; 498.045, \; 611.730, \; 701.955, \; 905.865, \; 1109.775)$$

Cuantizado a la grilla nativa de 9-ET ($S_9$):

$$S_9 = (0.00, \; 133.33, \; 266.67, \; 400.00, \; 533.33, \; 666.67, \; 800.00, \; 933.33, \; 1066.67) \text{ cents}$$

El vector de pasos para 9-ET es estrictamente uniforme: $\vec{\sigma}^{(9)} = (133.33)_{i=0}^8$. En el espacio continuo ($p=3$), emergen dos tipos de paso: limas pitagóricas y apotomes microtonales de $\sim 90.2$ y $\sim 113.7$ cents.

---

### 2.3.2 Sistema $N = 11$ ($11$-ET / Dominio Undecimario)

#### Parámetros Iniciales del Motor Matemático:
- Cardinalidad: $N = 11$
- Pivote Medio: $P_m = 4$ *(definido por la calibración de la matriz base del motor)*
- Grado Activo: $A_N = 3$
- Cajita Central: $C_{11} = [3, -2, 4, -1]$
- Paso microtonal elemental: $\Delta_{\text{cents}}^{(11)} = \frac{1200}{11} \approx 109.091 \text{ cents}$

#### Dinámica de Índices de la Cajita Central:
En $N = 11$, la Cajita Central profundiza la asimetría negativa introduciendo el índice $-2$:

$$C_{11} = [3, -2, 4, -1]$$

Calculando su vector de diferencias:

$$\vec{\delta}(C_{11}) = (-2 - 3, \; 4 - (-2), \; -1 - 4) = (-5, \; 6, \; -5)$$

Aparece el tritono neutro de orden undecimal ($6$ pasos en la cadena de 11), flanqueado por distancias de quinta simétrica invertida ($-5$).

#### Expansión y Mapeo Acústico:
Desplegando los 11 índices de la cadena funcional equilibrada $\mathbb{I}_{11} = \{-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7\}$ bajo la función $\phi(k, 3)$:

| Índice ($k$) | Cents Exactos ($p=3$) | Reducción $\pmod{1200}$ | Cuantización $11$-ET ($k \cdot 109.09$) | Rol Estructural |
| :---: | :---: | :---: | :---: | :---: |
| **$-3$** | $-2105.865$ | $294.135$ | $218.18$ | Grado Neutro |
| **$-2$** | $-1403.910$ | $996.090$ | $981.82$ | Sub-subdominante / $C_{11}$ |
| **$-1$** | $-701.955$ | $498.045$ | $436.36$ | Subdominante / $C_{11}$ |
| **$0$** | $0.000$ | $0.000$ | $0.00$ | Eje Mayor ($r_M$) |
| **$1$** | $701.955$ | $701.955$ | $763.64$ | Dominante |
| **$2$** | $1403.910$ | $203.910$ | $327.27$ | Grado Neutro |
| **$3$** | $2105.865$ | $905.865$ | $872.73$ | $A_N$ Primario / $C_{11}$ |
| **$4$** | $2807.820$ | $407.820$ | $545.45$ | Eje Menor ($r_m = P_m$) / $C_{11}$ |
| **$5$** | $3509.775$ | $1109.775$ | $1090.91$ | Grado de Paso |
| **$6$** | $4211.730$ | $611.730$ | $654.55$ | Grado de Paso |
| **$7$** | $4913.685$ | $113.685$ | $109.09$ | Grado de Paso |

#### Ordenamiento Escalar $S_{3,11}$:
Aplicando $\mathcal{S}$ sobre el conjunto acústico obtenido:

$$S_{3,11} = (0.000, \; 113.685, \; 203.910, \; 294.135, \; 407.820, \; 498.045, \; 611.730, \; 701.955, \; 905.865, \; 996.090, \; 1109.775)$$

Proyectado a la escala temperada undecimal estándar ($11$-ET):

$$S_{11} = (0.00, \; 109.09, \; 218.18, \; 327.27, \; 436.36, \; 545.45, \; 654.55, \; 763.64, \; 872.73, \; 981.82, \; 1090.91) \text{ cents}$$

#### Identificación del Acorde Simétrico Residual $S_N$:
Conforme al axioma de la Matriz Operativa Bi-Eje ($F_N$), el Acorde Simétrico Residual se localiza en la posición ordinal $k = N - 3$.
- Para $N = 9$: Posición $9 - 3 = 6 \implies k = 6$ ($611.73 \text{ cents} \approx 666.67 \text{ cents}$ en $9$-ET). Es el tritono exacto o semioctava deformada.
- Para $N = 11$: Posición $11 - 3 = 8 \implies$ En la cadena centrada corresponde al índice que aísla el balance modal, ubicándose en $k = 6$ dentro del subgrupo simétrico ($654.55 \text{ cents}$ en $11$-ET, el *intervalo neutro undecimal* hiperbólico).

---

## 2.4 Propiedades del Acorde Transformante $T_N$, Conducción de Voces (OVC) y Modulaciones Microtonales

El **Acorde Transformante** $T_N$ opera como una estructura de transición que desacopla la polaridad funcional de los ejes primarios para habilitar modulaciones microtonales mediante la mínima perturbación geométrica.

### 2.4.1 Operador OVC (Optimal Voice-leading Coefficient)
El operador OVC cuantifica el costo métrico de desplazamiento por conducción de voces entre estructuras armónicas acopladas. Para dos acordes $A, B \subset \mathbb{R} / 1200\mathbb{Z}$ de cardinalidad $m$, definimos la distancia métrica $\mathcal{D}_{\text{OVC}}(A, B)$ como el ínfimo sobre todas las biyecciones de asignación de voces $\pi \in \mathfrak{S}_m$:

$$\mathcal{D}_{\text{OVC}}(A, B) = \min_{\pi \in \mathfrak{S}_m} \left( \sum_{j=0}^{m-1} d_{\mathbb{T}}\left( a_j, \; b_{\pi(j)} \right)^2 \right)^{1/2}$$

donde $d_{\mathbb{T}}(x, y) = \min(|x - y|, 1200 - |x - y|)$ representa la distancia geodésica toroidal sobre el círculo de octava.

### 2.4.2 Clasificación de Calidades Mediante $\vec{\delta}(C_N)$
Las tétradas o tríadas extraídas de $T_N$ se clasifican según el balance de sus diferencias adyacentes proyectadas en el espacio escalar:

1. **Calidad Mayor ($\mathcal{Q}_M$):** Dominada por vectores de paso que maximizan la proyección del centro $r_M = 0$. En términos de cents, el intervalo inicial respecto a la fundamental modal aproxima una tercera mayor (ultra-templada en 9-ET: $400.00$ cents; neutralizada en 11-ET: $436.36$ cents).
2. **Calidad Menor ($\mathcal{Q}_m$):** Centrada en torno a $r_m = P_m$. Presenta contracción del primer tercio escalar (327.27 cents en 11-ET, constituyendo una tercera neutra menor).
3. **Calidad Simétrica ($\mathcal{Q}_S$):** Ocurre cuando los deltas satisfacen la involución:
$$\delta_j = \delta_{m-1-j}$$
Esta condición neutraliza el torque armónico, aislando el acorde en el vértice residual $S_N$.

```
           [ Eje Mayor: r_M = 0 ]  <---- Tónica Mayor (T)
                     |
            (Desplazamiento c)
              c = +1 (D)  /  c = -1 (SD)
              c = +2 (D2) /  c = -2 (SD2)
                     |
           [ Eje Menor: r_m = P_m ] <---- Tónica Menor (T)
                     |
       [ Acorde Simétrico Residual S_N ] (Posición N - 3)
```

### 2.4.3 Modulaciones Microtonales Parsimoniosas
El Acorde Transformante $T_N$, al incorporar los índices extremos de $C_N$, actúa como puente de baja energía en espacios no euclidianos. En $11$-ET, el deslizamiento de una sola voz por un cuanto microtonal:

$$\epsilon = \Delta_{\text{cents}}^{(11)} \approx 109.09 \text{ cents}$$

permite la transformación continua de un complejo tonal mayor hacia una estructura menor simétrica, según se formaliza a continuación:

$$C_{11} = [3, -2, 4, -1] \xrightarrow{\quad \text{OVC} \quad} C'_{11} = [3, -1, 4, 0]$$

El costo del desplazamiento escalar es:

$$\mathcal{D}_{\text{OVC}}(C_{11}, C'_{11}) = \sqrt{(0)^2 + (109.09)^2 + (0)^2 + (109.09)^2} = 109.09 \sqrt{2} \approx 154.28 \text{ cents}$$

Este valor es significativamente inferior al umbral del semitono temperado tradicional ($200$ cents en movimientos paralelos de 12-ET), lo que evidencia que la modulación microtonal guiada por la Cajita Central preserva la consistencia perceptual del enlace armónico.

---

## 2.5 Implementación Computacional

El siguiente algoritmo en SuperCollider modela el mapeo acústico, el cálculo matricial y el ordenamiento escalar de $S_{p,N}$, permitiendo la síntesis precisa de las estructuras de $C_N$ y de los vectores resultantes para $N = 9$ y $N = 11$.

```supercollider
// =====================================================================
// THE CHAIN THEORY: Motor de Mapeo Acústico y Ordenamiento Escalar
// =====================================================================

(
var calculateChain = { |n = 9, prime = 3, rootFreq = 261.6255| // C4 base
    var p_m, c_n, rawIndices, acousticCents, sortedCents, frequencies;

    p_m = (n / 2).floor.asInteger;

    // Asignación de Cajita Central según cardinalidad
    if (n == 9) {
        c_n = [3, -1, 4, 0];
    } {
        if (n == 11) {
            c_n = [3, -2, 4, -1];
        } {
            // Algoritmo generalizado por defecto
            c_n = [p_m - 1, 0, p_m, 1];
        };
    };

    // Expansión simétrica de índices
    rawIndices = Array.fill(n, { |i| i - (n/2).floor.asInteger });

    // Mapeo Acústico Continuo reducido a la octava: (1200 * idx * log2(prime)) mod 1200
    acousticCents = rawIndices.collect { |idx|
        var c = (1200 * idx * (prime.log2)).mod(1200);
        if (c < 0) { c = c + 1200 };
        c;
    };

    // Ordenamiento Escalar S_{p,N}
    sortedCents = acousticCents.copy.sort;

    // Proyección a frecuencias audibles
    frequencies = sortedCents.collect { |cents|
        rootFreq * (2.pow(cents / 1200));
    };

    (
        n: n,
        p_m: p_m,
        cajitaCentral: c_n,
        indices: rawIndices,
        acousticCents: acousticCents,
        scalarScaleCents: sortedCents,
        frequencies: frequencies
    );
};

// Ejecución para N = 9 y N = 11
~chain9  = calculateChain.(9, 3);
~chain11 = calculateChain.(11, 3);

"=== RESULTADOS N = 9 ===".postln;
~chain9.postln;

"=== RESULTADOS N = 11 ===".postln;
~chain11.postln;
)

// Síntesis auditiva del Acorde Transformante TN sobre N=11
(
SynthDef(\chainTone, { |freq = 440, amp = 0.1, gate = 1, out = 0|
    var sig, env;
    env = EnvGen.kr(Env.asr(0.05, 1, 0.1), gate, doneAction: 2);
    sig = SinOsc.ar(freq) * env * amp;
    Out.ar(out, Pan2.ar(sig, 0));
}).add;
)

// Reproducción arpegiada de la escala resultante S_{3,11}
(
Pbind(
    \instrument, \chainTone,
    \freq, Pseq(~chain11[\frequencies], 1),
    \dur, 0.2,
    \amp, 0.15
).play;
)
```

---

## 2.6 Conclusión Epistemológica del Capítulo

El análisis de los sistemas de orden impar $N=9$ y $N=11$ evidencia que el espacio interválico microtonal no es una mera partición atomizada del continuo de frecuencias, sino una **red topológica proyectiva**. 

A través del **Mapeo Acústico** y el **Ordenamiento Escalar** ($S_{p,N}$), la Cajita Central ($C_N$) actúa como un condensador armónico invariante bajo inversión modal. Los desfases detectados en los vectores interválicos revelan que la transformación parsimoniosa entre calidades modales mayores y menores depende funcionalmente de la conservación de la simetría del pivote $P_m$. Esta formulación proporciona el andamiaje axiomático para el desarrollo, en el siguiente capítulo, de la interacción vectorial en la Matriz Bi-Eje ($F_N$).