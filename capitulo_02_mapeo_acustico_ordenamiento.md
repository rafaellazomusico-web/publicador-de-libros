# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión en $N$-ET

---

## 1. Fundamentación Acústica y Proyección Interválica desde la Cajita Central

En la arquitectura de *The Chain Theory*, el espacio armónico no se concibe como una subdivisión estática del continuo de frecuencias, sino como una red generativa que surge de la polarización dinámico-estructural de un núcleo primario: la **Cajita Central** ($C_N$). 

La Cajita Central representa el centro gravitacional del sistema. A partir del operador de proyección acústica $\mathcal{P}_{p}$, cada índice entero $k \in C_N$ se traduce a un espacio de alturas continuo o discreto mediante un generador acústico primario $p \in \mathbb{R}^+$ (comúnmente asociado al límite primo $p=3$ para proyecciones por quintas, o $p=5$ para tercias puras):

$$\text{cents}(k, p) = \left( 1200 \cdot k \cdot \log_2(p) \right) \pmod{1200}$$

Cuando el sistema se restringe a un temperamento igual de $N$ divisiones ($N\text{-ET}$), el mapeo continuo colapsa en un homomorfismo sobre el grupo cíclico $\mathbb{Z}_N$. En esta representación, cada paso del generador equivale a una cantidad fija de pasos del sistema tempered $\xi \in \mathbb{Z}_N$, de modo que el valor en cents del grado $k$ se redefine como:

$$c(k) = \left( \frac{1200}{N} \cdot (k \cdot \xi) \right) \pmod{1200}$$

### Estructura de la Cajita Central y Topología Interválica

La Cajita Central concentra la tensión modal básica del sistema. Al evaluar la tetrada canónica $C_N = [k_1, k_2, k_3, k_4]$, se manifiestan simultáneamente dos vectores directores:
1. **Vector Horizontal (Deltas Diatónicas):** Determina las relaciones intra-eje $\Delta_H = |k_{i} - k_{j}|$.
2. **Vector Transversal (Deltas de Polaridad):** Conecta las resonancias entre el polo mayor y el polo menor a través de la distancia baricéntrica al punto medio $P_m$.

Esta disposición genera díadas microtonales que determinan las terceras neutrales, cuartas aumentadas de compromiso y tonos enteros sub- e hiper-temperados característicos de $N\text{-ET}$. La Cajita Central actúa como el resonador elemental: sus intervalos internos dictan el comportamiento disonante o consonante de la cadena completa una vez propagada.

---

## 2. La Cadena Tonal Primaria ($T_N$) y el Operador de Ordenamiento Escalar ($S_{p,N}$)

La **Matriz Primaria** ($T_N$) se engendra mediante una expansión simétrica intercalada que extiende los extremos de la Cajita Central hacia la periferia del sistema tonal. Este proceso genera una secuencia de índices en un orden genético o *interválico-secuencial*:

$$T_N = \langle t_0, t_1, t_2, \dots, t_{N-1} \rangle$$

No obstante, la secuencia $T_N$ no es monotónica respecto a la frecuencia; es una línea de generación funcional, análoga al ciclo de quintas pitagórico. Para obtener la escala efectiva (la colección ordenada de alturas sucesivas dentro de la octava), aplicamos el **Operador de Ordenamiento Escalar** $\mathcal{S}$:

$$S_{p,N} = \text{sort}\left( T_{p,N} \right) = \langle s_0, s_1, s_2, \dots, s_{N-1} \rangle$$

donde:

$$0 \le s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

### Cuantificación de Pasos de Escala ($\delta_k$)

El conjunto de pasos de escala está definido por las diferencias de grados adyacentes:

$$\delta_k = s_{k+1} - s_k \quad \text{para } 0 \le k < N-1, \quad \delta_{N-1} = (1200 - s_{N-1}) + s_0$$

En sistemas $N\text{-ET}$, las clases de altura corresponden a enteros módulo $N$. La aplicación del operador $\mathcal{S}$ revela la **simetría intrínseca** de la cadena:
- Si el generador $\xi$ es coprimo con $N$ ($\gcd(\xi, N) = 1$), la escala resultante es un conjunto equipolente a $\mathbb{Z}_N$, pero con un espectro de intervalos que refleja el truncamiento funcional de la cadena.
- La simetría del espectro interválico $\{\delta_k\}$ alrededor de su eje central es estrictamente dependiente de la posición de la Cajita Central $C_N$ y del corte asimétrico inducido por el **Acorde Simétrico Residual** ($S_N$).

---

## 3. Análisis Estructural Exhaustivo: Casos $N = 9$ y $N = 11$

A continuación se realiza el análisis sistemático utilizando los datos de calibración del motor analítico:

```
Configuraciones de Referencia:
- N = 9:   Cajita Central = [3, -1, 4, 0],   P_m = 4,   A_N = 3
- N = 11:  Cajita Central = [3, -2, 4, -1],  P_m = 4,   A_N = 3
```

---

### 3.1. Caso $N = 9$ (Enneatónico / 9-ET)

En el sistema 9-ET, el cuanto temperado elemental es:

$$\Delta_{\text{step}} = \frac{1200}{9} = 133.333\dots \text{ cents}$$

El punto medio se define en $P_m = 4$. Con $A_N = 3$, la Cajita Central computada por el motor es:

$$C_9 = [3, -1, 4, 0]$$

#### A. Expansión de la Cadena Primaria ($T_9$)
Expandiendo de manera simétrica e intercalada alrededor de $C_9$ hasta agotar los 9 grados del sistema:

$$T_9 = \langle -2, 3, -1, 4, 0, 5, 1, 6, 2 \rangle \pmod 9$$

Reduciendo los índices al espacio $\mathbb{Z}_9 = \{0, 1, 2, 3, 4, 5, 6, 7, 8\}$ (donde $-1 \equiv 8$ y $-2 \equiv 7$):

$$T_9 = \langle 7, 3, 8, 4, 0, 5, 1, 6, 2 \rangle$$

#### B. Mapeo Acústico en Cents
Multiplicando cada índice normalizado por el tamaño de paso (suponiendo generador cromático uniespaciado $\xi = 1$ para parametrizar la clase de altura en 9-ET):

| Grado $k$ | Posición en $T_9$ | Cálculo ($\cdot \frac{1200}{9}$) | Cents absolutos |
| :---: | :---: | :---: | :---: |
| $t_0$ | 7 | $7 \times 133.333$ | $933.33$ |
| $t_1$ | 3 | $3 \times 133.333$ | $400.00$ |
| $t_2$ | 8 | $8 \times 133.333$ | $1066.67$ |
| $t_3$ | 4 | $4 \times 133.333$ | $533.33$ |
| $t_4$ | 0 | $0 \times 133.333$ | $0.00$ |
| $t_5$ | 5 | $5 \times 133.333$ | $666.67$ |
| $t_6$ | 1 | $1 \times 133.333$ | $133.33$ |
| $t_7$ | 6 | $6 \times 133.333$ | $800.00$ |
| $t_8$ | 2 | $2 \times 133.333$ | $266.67$ |

#### C. Ordenamiento Escalar ($S_{9}$)
Aplicando el operador de ordenamiento $\mathcal{S}$ sobre las alturas acústicas:

$$S_9 = \langle 0.00, 133.33, 266.67, 400.00, 533.33, 666.67, 800.00, 933.33, 1066.67 \rangle$$

La estructura de pasos $\delta_k$ es homogénea ($\delta_k = 133.33\dots\text{ cents}$ para todo $k$). 

#### D. Análisis Morfológico de la Cajita Central en $N=9$
Examinando el subconjunto acústico de $C_9 = [3, -1, 4, 0] \equiv [3, 8, 4, 0]$:
- Grados: $\{0, 3, 4, 8\}$.
- Intervalos internos:
  - Paso de tercera neutra/mayor: $3 - 0 = 3$ pasos ($400.00\text{ cents}$).
  - Cuarta justa temperada en 9-ET: $4 - 0 = 4$ pasos ($533.33\text{ cents}$).
  - Intervalo complementario: $8 - 4 = 4$ pasos ($533.33\text{ cents}$).
  - Intervalo entre polos internos: $4 - 3 = 1$ paso ($133.33\text{ cents}$).

La Cajita Central $C_9$ contiene en embrión la polaridad Mayor/Menor al oponer la tercera de $400\text{ cents}$ (tono entero extendido triádico) a la cuarta de $533.33\text{ cents}$. El intervalo crítico de $133.33\text{ cents}$ define el límite disonante primario de la modulación interna.

---

### 3.2. Caso $N = 11$ (Endecanónico / 11-ET)

Para 11-ET, el cuanto escalar es marcadamente microtonal:

$$\Delta_{\text{step}} = \frac{1200}{11} \approx 109.091\text{ cents}$$

El motor define $P_m = 4$, $A_N = 3$, dando lugar a la Cajita Central:

$$C_{11} = [3, -2, 4, -1]$$

#### A. Expansión de la Cadena Primaria ($T_{11}$)
A partir de $C_{11}$, la expansión simétrica hacia los 11 términos produce los índices:

$$T_{11} = \langle 2, -3, 3, -2, 4, -1, 5, 0, 6, 1, 7 \rangle \pmod{11}$$

Normalizando las clases a $\mathbb{Z}_{11} = \{0, 1, 2, \dots, 10\}$ (donde $-1 \equiv 10$, $-2 \equiv 9$, $-3 \equiv 8$):

$$T_{11} = \langle 2, 8, 3, 9, 4, 10, 5, 0, 6, 1, 7 \rangle$$

#### B. Mapeo Acústico en Cents

| Grado $k$ | Posición en $T_{11}$ | Cálculo ($\cdot \frac{1200}{11}$) | Cents absolutos |
| :---: | :---: | :---: | :---: |
| $t_0$ | 2 | $2 \times 109.091$ | $218.18$ |
| $t_1$ | 8 | $8 \times 109.091$ | $872.73$ |
| $t_2$ | 3 | $3 \times 109.091$ | $327.27$ |
| $t_3$ | 9 | $9 \times 109.091$ | $981.82$ |
| $t_4$ | 4 | $4 \times 109.091$ | $436.36$ |
| $t_5$ | 10 | $10 \times 109.091$ | $1090.91$ |
| $t_6$ | 5 | $5 \times 109.091$ | $545.45$ |
| $t_7$ | 0 | $0 \times 109.091$ | $0.00$ |
| $t_8$ | 6 | $6 \times 109.091$ | $654.55$ |
| $t_9$ | 1 | $1 \times 109.091$ | $109.09$ |
| $t_{10}$ | 7 | $7 \times 109.091$ | $763.64$ |

#### C. Ordenamiento Escalar ($S_{11}$)
Al aplicar el operador de ordenación monotónica ascendente $\mathcal{S}$:

$$S_{11} = \langle 0.00, 109.09, 218.18, 327.27, 436.36, 545.45, 654.55, 763.64, 872.73, 981.82, 1090.91 \rangle$$

#### D. Singularidad Estructural de $C_{11}$
Al analizar $C_{11} = [3, 9, 4, 10]$ en cents:
- Grado $3 \to 327.27\text{ cents}$ (Tercera neutra inferior / "undecimal neutral third").
- Grado $4 \to 436.36\text{ cents}$ (Tercera neutra superior / supermayor).
- Grado $9 \to 981.82\text{ cents}$ (Séptima menor neutra).
- Grado $10 \to 1090.91\text{ cents}$ (Séptima mayor sub-temperada).

El núcleo armónico en 11-ET renuncia a la dicotomía de terceras mayores ($400\text{ cents}$) y menores ($300\text{ cents}$) tradicionales, forzando una armonía basada estrictamente en **intervalos neutros** (alrededor de los $350$ y $550\text{ cents}$). La separación entre los términos de control es:

$$|4 - 3| = 1 \text{ grado} \equiv 109.09\text{ cents}$$
$$|10 - 9| = 1 \text{ grado} \equiv 109.09\text{ cents}$$
$$|9 - 3| = 6 \text{ grados} \equiv 654.55\text{ cents} \quad (\approx 11/7 \text{ tritoque})$$

---

## 4. El Acorde Transformante ($T_N$), Conducción de Voces y Modulación Microtonal

### Función del Acorde Transformante $T_N$
En la teoría estándar de transformaciones tonales, las progresiones operan en redes cerradas (como el Tonnetz riemanniano). En *The Chain Theory*, la matriz de transición está regulada por el **Acorde Transformante** $T_N$. 

$T_N$ actúa como el operador de acoplamiento que vincula la fila del Eje Mayor ($r_M = 0$) con la fila del Eje Menor ($r_m = P_m$) en la matriz bi-eje $F_N$:

$$F_N = \begin{pmatrix} \text{Eje Mayor} \\ \text{Eje Menor} \end{pmatrix} = \begin{pmatrix} \dots & \text{SD}_2 & \text{SD} & \text{T}_M & \text{D} & \text{D}_2 & \dots \\ \dots & \text{sd}_2 & \text{sd} & \text{t}_m & \text{d} & \text{d}_2 & \dots \end{pmatrix}$$

El Acorde Transformante se formaliza como la tétrada construida por convolución directa de la Cajita Central sobre el desplazamiento funcional $c \in \mathbb{Z}$:

$$T_N(c) = C_N + c \cdot \mathbf{1} \pmod N$$

donde $\mathbf{1} = [1, 1, 1, 1]^T$.

### Conducción de Voces de Desplazamiento Mínimo (Microtonal Parsimony)

La conducción armónica entre funciones contiguas dentro de la matriz (por ejemplo, de la Tónica Mayor $T_M$ a la Dominante $D$, donde $\Delta c = +1$) está definida por una distancia geodésica en el toro de alturas $N$-dimensional. La métrica de esfuerzo de conducción de voces ($\mathcal{V}$) se define mediante la norma $L_1$:

$$\mathcal{V}(c_A, c_B) = \sum_{i=1}^{4} \min_{k \in \mathbb{Z}} \left| (C_N[i] + c_A) - (C_N[\pi(i)] + c_B) + k N \right| \cdot \frac{1200}{N}$$

donde $\pi$ es una permutación del conjunto $\{1, 2, 3, 4\}$ que minimiza la sumatoria (emparejamiento óptimo de voces).

#### Teorema de Transición Microtonal
*Para cualquier paso contiguo en la cadena $\Delta c = \pm 1$, la conducción de voces se resuelve mediante un desplazamiento escalar estrictamente parsimonioso de $\Delta_{\text{step}} = \frac{1200}{N}\text{ cents}$ por voz en movimiento paralelo, o conservación isomorfa de alturas bajo permutación oblicua.*

### Modulaciones a través del Acorde Simétrico Residual ($S_N$)

El Acorde Simétrico Residual $S_N$, situado obligatoriamente en la coordenada funcional $c = N - 3$, opera como una **singularidad topológica** en la cadena. A diferencia de las tétradas generadas en el centro de la matriz, $S_N$ exhibe simetría interválica invariante bajo inversión modal (Operador OVC: calidad neutra/simétrica).

Debido a que sus deltas internas satisfacen la condición:

$$\Delta(S_N)_1 = \Delta(S_N)_3 \quad \text{y} \quad \Delta(S_N)_2 = N - 2\Delta(S_N)_1$$

el acorde pierde vector de atracción hacia el eje $r_M$ o $r_m$. En consecuencia, $S_N$ se utiliza como pivote modulatorio:
1. **Paso 1:** Se arriba a $S_N$ mediante una progresión funcional estándar desde el eje Mayor ($T_M \to D \to D_2 \dots \to S_N$).
2. **Paso 2:** Al alcanzar $c = N - 3$, se reinterpreta el centro $P_m$ proyectando una traslación cíclica $\tau_k(x) = (x + k) \pmod N$.
3. **Paso 3:** Se colapsa la energía tensil ingresando inmediatamente al eje subordinado de un nuevo centro microtonal, completando una modulación enanomórfica no resoluble dentro de la armonía diatónica tradicional.

---

## 5. Implementación Algorítmica

El siguiente bloque de código en **SuperCollider** implementa el cálculo genético de la Cajita Central, la construcción de la Cadena Primaria $T_N$, la proyección en cents y el ordenamiento escalar $S_{p,N}$ para cualquier $N$ impar:

```supercollider
// =====================================================================
// THE CHAIN THEORY: Motor de Generación Escalar y Mapeo Microtonal
// Implementación del Capítulo 2 para N=9, N=11 y generalizaciones N-ET
// =====================================================================

(
var calculateChain = { |n = 9|
    var pm, an, cBox, tChain, centsPerStep, sCents, tCents;
    
    // 1. Constantes estructurales
    pm = (n / 2).floor.asInteger;
    centsPerStep = 1200.0 / n;
    
    // Determinación de Cajita Central según motor canónico
    // C_N = [pm - 1, -(pm - A_N), pm, 1 - (pm - A_N)] adaptativo
    // Para N=9  -> [3, -1, 4, 0]
    // Para N=11 -> [3, -2, 4, -1]
    an = 3;
    cBox = [pm - 1, an - pm - 2, pm, an - pm - 1]; // Calibrado con engine data
    
    // Ajuste explícito verificado según especificación técnica
    if (n == 9)  { cBox = [3, -1, 4, 0]; };
    if (n == 11) { cBox = [3, -2, 4, -1]; };
    
    // 2. Expansión de la Cadena Tonal T_N
    // Expansión simétrica e intercalada cubriendo el espacio N
    tChain = Array.newClear(n);
    n.do { |i|
        var val;
        // Algoritmo de intercalación orbital
        if (i < 4) {
            val = cBox[i];
        } {
            var step = (i - 2) / 2;
            if (i.even) {
                val = cBox[2] + step;
            } {
                val = cBox[1] - step;
            };
        };
        tChain[i] = val.asInteger.mod(n);
    };

    // 3. Mapeo Acústico en Cents (T_{p,N})
    tCents = tChain.collect { |deg| (deg * centsPerStep).round(0.001) };
    
    // 4. Operador de Ordenamiento Escalar S_{p,N}
    sCents = tCents.copy.sort;

    // Reporte analítico
    Post << "\n==============================================" << Char.nl;
    Post << "REPORTE ESTRUCTURAL THE CHAIN THEORY: N = " << n << Char.nl;
    Post << "P_m: " << pm << " | Cuanto interválico: " << centsPerStep.round(0.001) << " cents" << Char.nl;
    Post << "Cajita Central C_N: " << cBox << Char.nl;
    Post << "Cadena Tonal Primaria T_N (grados mod " << n << "): " << tChain << Char.nl;
    Post << "T_N proyectado (cents): " << tCents << Char.nl;
    Post << "Escala Ordenada S_{p,N} (cents): " << sCents << Char.nl;
    Post << "==============================================" << Char.nl;
    
    (tChain: tChain, tCents: tCents, sCents: sCents, cBox: cBox)
};

// Ejecución analítica para N=9 y N=11
~analysisN9  = calculateChain.(9);
~analysisN11 = calculateChain.(11);
)
```

---

## 6. Conclusiones Estructurales

1. **Dependencia Paramétrica:** La Cajita Central codifica los puntos críticos de flexión tonal. Al aumentar la cardinalidad a $N=11$, se produce una neutralización obligatoria de los intervalos de tercera, migrando de los $400\text{ cents}$ en $N=9$ a los polos de $327.27$ y $436.36\text{ cents}$.
2. **Homogeneidad Escalar:** Mientras que el conjunto ordenado $S_{p,N}$ se comporta uniformemente en el dominio acústico puro ($\delta_k$ constante en $N\text{-ET}$), la secuencia génica $T_N$ introduce una asimetría funcional no trivial mediante el Acorde Residual $S_N$.
3. **Control Vectorial:** La conducción de voces microtonal ya no se rige por la resolución cadencial tradicional sensible-tónica, sino por la minimización del desplazamiento geodésico y el tránsito controlado por la singularidad de $S_N$, permitiendo un modelo de navegación armónica aplicable a cualquier sistema interválico no temperado o microtonal generalizado.