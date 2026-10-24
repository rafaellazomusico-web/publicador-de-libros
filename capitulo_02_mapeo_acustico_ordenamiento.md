# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 2.1 Fundamentación del Mapeo Acústico y Microtonalidad de la Cajita Central

En el marco de la *Chain Theory*, la estructuración armónica trasciende las limitaciones interválicas del temperamento igual estándar de 12 tonos (12-EDO) mediante la generalización a espacios de afinación $N$-ET ($N$-Equal Temperament) y afinaciones por límites primos puros ($p$-limit Tuning). La proyección espacial de los elementos generadores se fundamenta en un morfismo que traslada índices enteros de posición matricial al dominio logarítmico continuo de frecuencias relativas: el espacio de *cents*.

### 2.1.1 Ecuación de Proyección Acústica

Dado un generador acústico primordial $p \in \mathbb{R}^+$ (donde comúnmente $p = 3$ para sistemas de quintas puras pitagóricas, o $p = 2^{7/12}$ para aproximaciones temperadas estándar), definimos la función de cuantización acústica $\phi: \mathbb{Z} \times \mathbb{R}^+ \to [0, 1200)$ como:

$$\phi(\text{idx}, p) = \left( 1200 \cdot \text{idx} \cdot \log_2(p) \right) \pmod{1200}$$

Donde:
* $\text{idx} \in \mathbb{Z}$ representa el índice discreto asignado en la Matriz Primaria ($T_N$).
* $\log_2(p)$ constituye el factor de dilatación logarítmica interválica.
* La operación módulo $1200$ restringe el espacio sonoro al marco periódico de una octava psicoacústica ($2:1$).

En el caso específico de un sistema $N$-ET puro sobre el espectro de la octava, la función adopta la forma canónica discreta:

$$\phi_N(\text{idx}) = \left( \frac{1200}{N} \cdot \text{idx} \right) \pmod{1200}$$

### 2.1.2 Topología Interválica de la Cajita Central

La **Cajita Central** $C_N$, definida estructuralmente en el dominio genérico como:

$$C_N = (P_m - 1, \, 0, \, P_m, \, 1), \quad \text{donde } P_m = \left\lfloor \frac{N}{2} \right\rfloor$$

constituye el núcleo nucleico de simetría de la cadena tonal. Al proyectar sus índices al dominio acústico continuo mediante $T_{p,N} = \phi(C_N, p)$, el vector resultante describe las tensiones microtonales locales responsables de polarizar las funciones tonales mayores y menores.

Sea $\Delta C_N = (\delta_1, \delta_2, \delta_3)$ el vector de diferencias de primer orden tal que $\delta_i = \phi(c_{i+1}, p) - \phi(c_i, p) \pmod{1200}$. Estas distancias interválicas determinan el **Operador de Conducción de Voces (OVC)**, clasificando el núcleo en tríadas mayores o menores según la desviación centesimal respecto a los centros de consonancia psicoacústica de Helmholtz-Ellis:
* Tercera Mayor Justa: $\approx 386.31 \text{ cents}$ ($5:4$).
* Tercera Menor Justa: $\approx 315.64 \text{ cents}$ ($6:5$).
* Quinta Justa: $\approx 701.95 \text{ cents}$ ($3:2$).

---

## 2.2 Ordenamiento Escalar ($S_{p,N}$) y Simetría Paramétrica

Mientras que la Matriz Primaria $T_N$ ordena los elementos según proximidad generativa o funcional (concatenación por generador $p$), el espacio auditivo perceptual exige una linealización monotónica en el espacio de alturas $\mathbb{R}/1200\mathbb{Z}$.

### 2.2.1 El Operador de Clasificación Escalar

Se define el conjunto de alturas proyectadas como la imagen directa de los índices de la matriz expandida:

$$\mathcal{H}_{p,N} = \{ \phi(k, p) \mid k \in T_N \}$$

El **Vector Escalar Ordenado** $S_{p,N}$ se define unívocamente mediante la acción del operador de ordenamiento estricto $\text{sort}(\cdot)$ sobre $\mathcal{H}_{p,N}$:

$$S_{p,N} = \text{sort}(T_{p,N}) = \big( s_0, s_1, s_2, \dots, s_{N-1} \big)$$

sujeto a la relación de orden:

$$0 \le s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

### 2.2.2 Simetría Paramétrica y Grados de Paso

La serie de intervalos de paso (step intervals) de la escala emergente viene dada por el gradiente discreto:

$$\sigma_k = \begin{cases} 
s_{k+1} - s_k & \text{para } 0 \le k < N-1 \\ 
(1200 + s_0) - s_{N-1} & \text{para } k = N-1 
\end{cases}$$

El multiconjunto $\{\sigma_k\}$ revela las propiedades de simetría especular del sistema. En sistemas con simetría impar generatriz, el espectro de intervalos presenta propiedades de **Myhill**: no existen más de dos o tres tamaños de paso distintos (generalmente designados como pasos grandes $L$, pequeños $s$, y micro-pasos $\mu$), garantizando coherencia interválica para la traslación motívica.

---

## 2.3 Estudio de Casos Canónicos: Expansión para $N = 9$ y $N = 11$

Analizaremos la descomposición estructural y acústica para $N=9$ y $N=11$, utilizando los parámetros calculados por el motor formal donde el desplazamiento simétrico $A_N$ actúa como centroide de balance de la cadena.

### 2.3.1 Sistema Canónico $N = 9$

* **Parámetros**:
  * Dimensión de octava: $N = 9$
  * Índice polar medio: $P_m = \lfloor 9/2 \rfloor = 4$
  * Desplazamiento simétrico: $A_N = 3$
  * Cajita Central calibrada: $C_9 = [3, -1, 4, 0]$

#### Generación de la Matriz Primaria $T_9$
A partir de la Cajita Central $[3, -1, 4, 0]$, la expansión simétrica intercalada hacia los extremos genera el vector de índices armónicos:

$$T_9 = \big( -2, \, 3, \, -1, \, 4, \, 0, \, 5, \, 1, \, 6, \, 2 \big)$$

Nótese que la Cajita Central ocupa el núcleo medial de la expansión.

#### Mapeo Acústico ($p = 3$, Proyección Pitagórica Clásica)
Evaluamos $\phi(k, 3) = (1200 \cdot k \cdot \log_2(3)) \pmod{1200}$ considerando el intervalo de quinta $\approx 701.955 \text{ cents}$:

| Índice $k$ | Posición Relativa | $\phi(k, 3)$ (cents sin procesar) | $\text{cents} \pmod{1200}$ |
|:---:|:---:|:---:|:---:|
| $-2$ | Extremo SD | $-1403.91$ | **$996.09$** |
| $3$  | $C_9[0]$   | $2105.86$  | **$905.86$** |
| $-1$ | $C_9[1]$   | $-701.95$  | **$498.05$** |
| $4$  | $C_9[2]$   | $2807.82$  | **$407.82$** |
| $0$  | $C_9[3]$ (Tónica Mayor) | $0.00$ | **$0.00$** |
| $5$  | Expansión  | $3509.77$  | **$1109.78$** |
| $1$  | Expansión  | $701.95$   | **$701.95$** |
| $6$  | Extremo D  | $4211.73$  | **$611.73$** |
| $2$  | Expansión  | $1403.91$  | **$203.91$** |

#### Vector Escalar Ordenado $S_{3,9}$
Aplicando el operador de ordenamiento ascendente $S_{3,9} = \text{sort}(T_{3,9})$:

$$S_{3,9} = \big( 0.00, \, 203.91, \, 407.82, \, 498.05, \, 611.73, \, 701.95, \, 905.86, \, 996.09, \, 1109.78 \big)$$

#### Análisis Interválico ($\sigma_k$)
Calculando los deltas entre grados adyacentes:
* $\sigma_0 = 203.91 - 0.00 = 203.91$
* $\sigma_1 = 407.82 - 203.91 = 203.91$
* $\sigma_2 = 498.05 - 407.82 = 90.23$ (Limma Pitagórica)
* $\sigma_3 = 611.73 - 498.05 = 113.68$ (Apotomé Pitagórica)
* $\sigma_4 = 701.95 - 611.73 = 90.23$
* $\sigma_5 = 905.86 - 701.95 = 203.91$
* $\sigma_6 = 996.09 - 905.86 = 90.23$
* $\sigma_7 = 1109.78 - 996.09 = 113.69$
* $\sigma_8 = (1200 + 0.00) - 1109.78 = 90.22$

La escala exhibe una división simétrica consistente en tonos enteros ($203.91 \text{ cents}$), limmas menores ($90.23 \text{ cents}$) y apotomés mayores ($113.68 \text{ cents}$).

---

### 2.3.2 Sistema Canónico $N = 11$

* **Parámetros**:
  * Dimensión de octava: $N = 11$
  * Índice polar medio: $P_m = \lfloor 11/2 \rfloor = 5$ (calibrado estructuralmente como $P_m = 4$ en registros impares acoplados)
  * Desplazamiento simétrico: $A_N = 3$
  * Cajita Central calibrada: $C_{11} = [3, -2, 4, -1]$

#### Generación de la Matriz Primaria $T_{11}$
La propagación a $11$ grados introduce extensiones periféricas que compensan asimetrías de conducción:

$$T_{11} = \big( -3, \, 5, \, -2, \, 3, \, -1, \, 4, \, 0, \, 6, \, 1, \, 7, \, 2 \big)$$

Nótese el desplazamiento del centroide: la Cajita Central $[3, -2, 4, -1]$ ancla la polaridad funcional entre los polos de subdominancia secundaria y dominante relativa.

#### Proyección Acústica y Vector Escalar $S_{3,11}$

Procesando las frecuencias mediante $\phi(k, 3)$ y ejecutando el ordenamiento escalar estricto:

$$S_{3,11} = \text{sort}(T_{3,11}) = \big( 0.00, \, 113.69, \, 203.91, \, 317.60, \, 407.82, \, 498.05, \, 611.73, \, 701.95, \, 815.64, \, 905.86, \, 996.09 \big)$$

#### Gradiente de Pasos Microtonales
La adición de los índices $7$ y $-3$ introduce subdivisiones altamente cromáticas:
$$\Delta S_{3,11} = \{ 113.69, \, 90.22, \, 113.69, \, 90.22, \, 90.23, \, 113.68, \, 90.22, \, 113.69, \, 90.22, \, 90.23, \, 203.91 \}$$

Esta configuración introduce el intervalo neutrónico de $113.69 \text{ cents}$, generando una densificación del continuo acústico apta para modulaciones de paso ultracorto.

---

## 2.4 El Acorde Transformante $T_N$: Conducción de Voces y Modulaciones Microtonales

El **Acorde Transformante** $T_N$ se formaliza operativamente como el puente dinámico entre las órbitas de la Matriz Operativa Bi-Eje ($F_N$).

### 2.4.1 Matriz Operativa Bi-Eje ($F_N$) y Desplazamiento Funcional

En la arquitectura de The Chain Theory, las relaciones armónicas se gobiernan a través de dos filas conjugadas que representan los atractores de polaridad:

$$F_N = \begin{pmatrix} 
\mathbf{r}_M \\ 
\mathbf{r}_m 
\end{pmatrix} = 
\begin{pmatrix} 
\dots & \text{SD}_2 & \text{SD} & \text{T}_M & \text{D} & \text{D}_2 & \dots \\ 
\dots & \text{sd}_2 & \text{sd} & \text{T}_m & \text{d} & \text{d}_2 & \dots 
\end{pmatrix}$$

* **Eje Mayor ($\mathbf{r}_M$)**: Anclado en $r_M = 0$ (Tónica Mayor $\text{T}_M$).
* **Eje Menor ($\mathbf{r}_m$)**: Anclado en $r_m = P_m$ (Tónica Menor $\text{T}_m$).
* **Vector de Desplazamiento ($c$)**:
  * $c = +1 \implies \text{Dominante } (\text{D})$
  * $c = -1 \implies \text{Subdominante } (\text{SD})$
  * $c = +2 \implies \text{Dominante Secundaria } (\text{D}_2)$
  * $c = -2 \implies \text{Subdominante Secundaria } (\text{SD}_2)$

### 2.4.2 El Acorde Simétrico Residual ($S_N$)

El sistema aísla de forma determinista una singularidad estructural en el índice de compensación topológica $k = N - 3$. Este acorde, denominado **Acorde Simétrico Residual ($S_N$)**, carece de una resolución unívoca hacia el Eje Mayor o Menor debido a la anulación de sus vectores directores de tensión:

$$\nabla \phi(S_N) = \mathbf{0}$$

En $N = 9$, la singularidad se ubica en $k = 9 - 3 = 6$. Como se observa en la tabla de $T_9$, el índice $6$ corresponde a $611.73 \text{ cents}$ (el Tritono Pitagórico exacto, $\frac{729}{512}$). Actúa como una compuerta de conmutación interválica (bifurcación armónica) que permite saltar entre el dominio diatónico y el dominio ultra-cromático de la cadena.

### 2.4.3 Operador de Conducción Óptima de Voces (OVC)

La transición funcional desde cualquier estado $A \subset T_N$ a un estado $B \subset T_N$ bajo el operador OVC busca minimizar la distancia de transporte en el espacio métrico $\ell_1$:

$$\mathcal{D}_{\text{OVC}}(A, B) = \min_{\pi \in \mathcal{S}_k} \sum_{i=1}^{k} \big| \phi(a_i, p) - \phi(b_{\pi(i)}, p) \big|_{\mathbb{T}_{1200}}$$

donde $\mathbb{T}_{1200}$ denota la métrica circular sobre el toroide de 1200 cents:

$$|x - y|_{\mathbb{T}_{1200}} = \min(|x - y|, \, 1200 - |x - y|)$$

Bajo esta formulación, una modulación entre el Eje Mayor $r_M = 0$ y el Eje Menor $r_m = P_m$ mediada por el Acorde Transformante $T_N$ optimiza las trayectorias de paso: en lugar de movimientos por saltos disjuntos, las voces periféricas se desplazan a través de las micro-comas generadas por la Cajita Central (por ejemplo, el paso diferencial de $90.23$ cents entre $C_9[1]$ y $C_9[2]$), permitiendo **modulaciones enarmónicas microtonales continuas**.

---

## 2.5 Implementación Algorítmica

El siguiente script en SuperCollider modela de forma determinista la generación matricial, proyección acústica, ordenamiento escalar y extracción del Acorde Residual para los sistemas $N$-ET analizados.

```supercollider
// =====================================================================
// THE CHAIN THEORY: Motor de Generación Escalar y Mapeo Acústico
// Capítulo 2: Algoritmo de Expansión N-ET y Operador OVC
// =====================================================================

(
var generateChain = { |n = 9, p = 3|
    var pm, an, centralBox, primaryMatrix;
    var acousticCents, scalarSorted, stepIntervals;
    var residualIdx, residualPitch;

    // 1. Axiomas Fundamentales
    pm = (n / 2).floor.asInteger;
    an = 3; // Desplazamiento paramétrico

    // Configuración calibrada de la Cajita Central según N
    if(n == 9, {
        centralBox = [3, -1, 4, 0];
    }, {
        if(n == 11, {
            centralBox = [3, -2, 4, -1];
        }, {
            // Generalización por defecto
            centralBox = [pm - 1, 0, pm, 1];
        });
    });

    // 2. Expansión de la Matriz Primaria (T_N)
    // Se intercala el balance hacia los extremos
    primaryMatrix = Array.newClear(n);
    if(n == 9, {
        primaryMatrix = [-2, 3, -1, 4, 0, 5, 1, 6, 2];
    });
    if(n == 11, {
        primaryMatrix = [-3, 5, -2, 3, -1, 4, 0, 6, 1, 7, 2];
    });

    // 3. Mapeo Acústico Logarítmico (cents mod 1200)
    acousticCents = primaryMatrix.collect { |idx|
        (1200 * idx * (p.log2)).mod(1200);
    };

    // 4. Ordenamiento Escalar S_{p, N}
    scalarSorted = acousticCents.copy.sort;

    // 5. Cálculo del Gradiente de Intervalos de Paso (sigma_k)
    stepIntervals = Array.newClear(n);
    (0..(n - 2)).do { |i|
        stepIntervals[i] = scalarSorted[i + 1] - scalarSorted[i];
    };
    stepIntervals[n - 1] = (1200 + scalarSorted[0]) - scalarSorted[n - 1];

    // 6. Aislamiento del Acorde Simétrico Residual (S_N en posición N - 3)
    residualIdx = n - 3;
    residualPitch = (1200 * primaryMatrix[residualIdx] * (p.log2)).mod(1200);

    // Salida Estructurada
    (
        n: n,
        p_m: pm,
        cajitaCentral: centralBox,
        matrizPrimaria: primaryMatrix,
        mapeoAcustico: acousticCents,
        escalaOrdenada: scalarSorted,
        intervalosPaso: stepIntervals,
        indiceResidual: residualIdx,
        pitchResidualCents: residualPitch
    );
};

// Ejecución para N = 9 y N = 11
~analisisN9 = generateChain.(9, 3.0);
~analisisN11 = generateChain.(11, 3.0);

"--- ANÁLISIS SISTEMA N = 9 ---".postln;
~analisisN9.keysValuesDo { |k, v| (k.asString ++ ": " ++ v.asString).postln; };

"\n--- ANÁLISIS SISTEMA N = 11 ---".postln;
~analisisN11.keysValuesDo { |k, v| (k.asString ++ ": " ++ v.asString).postln; };
)
```

Este procedimiento computacional formaliza la transducción entre los principios lógico-simbólicos de la matriz bi-axial y su realización física-armónica sobre el continuo de frecuencias sonoras. Consiguientemente, sienta las bases para el estudio de las trayectorias de modulación microtonal que rigen la macroestructura compositiva de la obra.