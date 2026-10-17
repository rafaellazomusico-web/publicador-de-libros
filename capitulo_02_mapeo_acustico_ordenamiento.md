# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 2.1 Fundamentación del Mapeo Acústico y Microtonalidad de la Cajita Central

En el marco de *The Chain Theory*, el paso del espacio combinatorio abstracto al dominio psicoacústico se rige por la proyección de índices generadores sobre el continuo de frecuencias. Si bien la topología de la cadena define relaciones de vecindad algebraica en un espacio cíclico unidimensional, la manifestación armónica de estas relaciones exige un operador de mapeo físico.

### 2.1.1 Operador de Mapeo Acústico ($T_{p,N}$)

Sea $k \in \mathbb{Z}$ un índice de la cadena que describe la posición orbital de un elemento respecto al núcleo simétrico, y sea $p \in \mathbb{R}^+$ la razón del intervalo generador proyectivo (típicamente $p = \frac{3}{2}$ para cadenas de quintas pitagóricas o justas, o bien $p = 2^{k/N}$ en el contexto estricto de temperamentos iguales de $N$ divisiones, $N$-ET). Se define la función de mapeo en cents modulo octava como:

$$\text{cents}(k, p) = \left( 1200 \cdot k \cdot \log_2(p) \right) \pmod{1200}$$

Para un sistema discreto cerrado $N$-ET, la proyección canónica normalizada toma como argumento el generador del sistema $g \in \{1, \dots, N-1\}$, tal que:

$$\phi(k) = \left( \frac{1200}{N} \cdot (k \cdot g) \right) \pmod{1200}$$

### 2.1.2 Topología Microtonal de la Cajita Central ($C_N$)

La Cajita Central $C_N$ actúa como el condensador interválico primal de la estructura armónica. En su formulación general, los elementos de la tetrada central expresan las tensiones polares y las distancias que gobiernan la morfología de las terceras y quintas del sistema:

$$C_N = [c_1, c_2, c_3, c_4]$$

Al aplicar la transformación $\phi(c_i)$ sobre cada componente de la cajita, emergen las micro-desviaciones estructurales inherentes al valor de $N$. El cálculo de los deltas consecutivos define la huella microtonal primaria:

$$\Delta C_N = [c_2 - c_1, \; c_3 - c_2, \; c_4 - c_3]$$

Esta huella determina directamente el potencial de batimiento armónico (*roughness*) y clasifica al sistema de acuerdo a su afinidad con los límites justos de Euler ($\text{3-limit}$, $\text{5-limit}$ o temperamentos de orden superior).

---

## 2.2 Ordenamiento Escalar ($S_{p,N}$) y Simetría de la Cadena

La proyección de la Matriz Primaria $T_N$ sobre el espacio de afinación genera un conjunto de alturas desordenadas respecto a su magnitud lineal en cents. El análisis musical de este fenómeno requiere formalizar la transición entre el **Espacio de Cadena** ($\mathcal{K}$-Space) y el **Espacio Escalar** ($\mathcal{S}$-Space).

### 2.2.1 El Operador de Proyección y Ordenamiento

Sea la matriz primaria linealizada como un conjunto multivariable de clases de alturas $T_{p,N} = \{\phi(k_0), \phi(k_1), \dots, \phi(k_{N-1})\}$. Se define el vector escalar $S_{p,N}$ mediante la acción de un operador monotónico de ordenación:

$$S_{p,N} = \text{sort}(T_{p,N}) = \langle s_0, s_1, s_2, \dots, s_{N-1} \rangle$$

tal que:

$$0 \le s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

### 2.2.2 Espectro de Grados de Paso y Simetría Quiral

La periodicidad de $S_{p,N}$ está dictada por el Teorema de Tres Distancias (o Teorema de Steinhaus). Las diferencias de paso adyacentes:

$$\delta_i = s_{i+1} - s_i \quad (\text{con } s_N = s_0 + 1200)$$

adoptan a lo sumo tres valores distintos, denotados $\{\alpha, \beta, \gamma\}$. La preservación de la simetría quiral de la cadena exige que la palabra interválica resultante de $\Delta S_{p,N} = \langle \delta_0, \delta_1, \dots, \delta_{N-1} \rangle$ sea estrictamente palindrómica salvo una rotación circular de orden finito, demostrando que el ordenamiento de alturas preserva la invarianza especular original de la Cajita Central.

---

## 2.3 Análisis Estructural Exhaustivo: Modelos $N = 9$ y $N = 11$

Se examinan en detalle los sistemas $N = 9$ y $N = 11$, utilizando los parámetros estructurales precisos computados por el motor matemático de *The Chain Theory*.

```
         ESPACIO DE CADENA (Topología)         ESPACIO ESCALAR (Acústica)
         
         [ c1 ] --- [ c2 ] --- [ c3 ]          s_0 < s_1 < s_2 < ... < s_{N-1}
                 Cajita Central                             |
                       |                                    v
                       v                           Matriz de Grados
               Expansión Simétrica                     de Paso
```

---

### 2.3.1 Sistema $N = 9$
- **Parámetros:** $P_m = 4$, $A_N = 3$.
- **Cajita Central:** $C_9 = [3, -1, 4, 0]$.
- **Paso angular básico ($9$-ET):** $\kappa_9 = \frac{1200}{9} = 133.333 \text{ cents}$.

#### A. Expansión de la Matriz Primaria $T_9$
A partir de la Cajita Central $[3, -1, 4, 0]$, la expansión simétrica intercalada genera la secuencia de índices de la cadena:

$$T_9(\text{índices}) = [k_0, k_1, \dots, k_8]$$

Aplicando los índices dados por el motor combinatorio:

$$T_9 = [3, -1, 4, 0, 2, -2, 5, -3, 1] \pmod 9 \equiv [3, 8, 4, 0, 2, 7, 5, 6, 1]$$

#### B. Mapeo Acústico de la Cajita Central ($C_9$)
Calculamos la afinación en cents mod $1200$ para cada componente $c_i \in C_9$ con $g=1$ (unidad de paso microtonal en $9$-ET):

$$\phi(3) = 3 \times 133.333 = 400.00 \text{ cents (Tercera Mayor pitagórica pura en 9-ET)}$$
$$\phi(-1) \equiv \phi(8) = 8 \times 133.333 = 1066.67 \text{ cents}$$
$$\phi(4) = 4 \times 133.333 = 533.33 \text{ cents (Cuarta aumentada / Quinta disminuida neutra)}$$
$$\phi(0) = 0 \times 133.333 = 0.00 \text{ cents (Tónica fundamental)}$$

El cálculo de los deltas internos en el espacio modular $\mathbb{Z}_9$:
$$\Delta C_9 = [(-1 - 3) \bmod 9, \; (4 - (-1)) \bmod 9, \; (0 - 4) \bmod 9] = [-4 \bmod 9, \; 5 \bmod 9, \; -4 \bmod 9] = [5, 5, 5]$$

La homogeneidad de $\Delta C_9 = [5, 5, 5]$ revela que en $N = 9$, la Cajita Central genera un subespacio de simetría cíclica regular bajo el generador de quinta neutra ($5 \times 133.333 = 666.67\text{ cents}$, el tritono estricto de $9$-ET).

#### C. Ordenamiento Escalar $S_{p,9}$
Mapeando todos los índices a cents absolutos:
- $k = 0 \to 0.00\text{ cents}$
- $k = 1 \to 133.33\text{ cents}$
- $k = 2 \to 266.67\text{ cents}$
- $k = 3 \to 400.00\text{ cents}$
- $k = 4 \to 533.33\text{ cents}$
- $k = 5 \to 666.67\text{ cents}$
- $k = 6 \to 800.00\text{ cents}$
- $k = 7 \to 933.33\text{ cents}$
- $k = 8 \to 1066.67\text{ cents}$

El vector resultante es estrictamente isocrónico:

$$S_{9} = \langle 0.0, 133.33, 266.67, 400.0, 533.33, 666.67, 800.0, 933.33, 1066.67 \rangle$$

La estructura de pasos es uniforme: $\delta_i = 133.33 \text{ cents} \; \forall i$. El sistema $N=9$ se comporta como una escala microtonal no focalizada de tipo neutro, donde las funciones tonales se desplazan a través de tritonos temperados ($666.67 \text{ cents}$).

---

### 2.3.2 Sistema $N = 11$
- **Parámetros:** $P_m = 4$, $A_N = 3$.
- **Cajita Central:** $C_{11} = [3, -2, 4, -1]$.
- **Paso angular básico ($11$-ET):** $\kappa_{11} = \frac{1200}{11} \approx 109.091 \text{ cents}$.

#### A. Expansión de la Matriz Primaria $T_{11}$
Con $C_{11} = [3, -2, 4, -1]$ como núcleo generativo, el vector de índices expandido incorpora alternancias simétricas bilaterales:

$$T_{11}(\text{índices}) = [3, -2, 4, -1, 2, -3, 5, 0, 1, -4, 6] \pmod{11}$$
$$T_{11} \equiv [3, 9, 4, 10, 2, 8, 5, 0, 1, 7, 6]$$

#### B. Mapeo Acústico de la Cajita Central ($C_{11}$)
Evaluamos acústicamente los cuatro nodos de la tetrada central en $11$-ET:

$$\phi(3) = 3 \times 109.091 = 327.27 \text{ cents (Tercera menor supra-temperada o 'neutra alta')}$$
$$\phi(-2) \equiv \phi(9) = 9 \times 109.091 = 981.82 \text{ cents (Séptima menor sub-temperada)}$$
$$\phi(4) = 4 \times 109.091 = 436.36 \text{ cents (Tercera mayor ultra-pitagórica)}$$
$$\phi(-1) \equiv \phi(10) = 10 \times 109.091 = 1090.91 \text{ cents (Séptima mayor baja)}$$

Calculamos los deltas diferenciales:
$$\Delta C_{11} = [(-2 - 3) \bmod 11, \; (4 - (-2)) \bmod 11, \; (-1 - 4) \bmod 11] = [-5 \bmod 11, \; 6 \bmod 11, \; -5 \bmod 11] = [6, 6, 6]$$

Nuevamente surge una invarianza angular interna: el intervalo constante entre los elementos cruzados es de $6$ pasos de $11$-ET ($6 \times 109.091 = 654.55 \text{ cents}$), que representa la aproximación en $11$-ET al tritono o "quinta deprimida".

#### C. Ordenamiento Escalar $S_{p,11}$
La ordenación monotónica de los índices mapeados $T_{11}$ restituye la escala cromática de $11$ divisiones iguales:

$$S_{11} = \langle 0.00, 109.09, 218.18, 327.27, 436.36, 545.45, 654.55, 763.64, 872.73, 981.82, 1090.91 \rangle$$

Aquí, $\delta_i = 109.091 \text{ cents} \; \forall i$. La distribución de clases de paso es homogénea en frecuencia logarítmica, pero la asimetría de la inserción de las componentes de $C_{11}$ dentro de la cadena induce polarizaciones modulatorias no triviales.

---

### 2.3.3 Cuadro Comparativo Estructural

| Parámetro | Sistema $N = 9$ | Sistema $N = 11$ |
| :--- | :--- | :--- |
| **Cajita Central ($C_N$)** | $[3, -1, 4, 0]$ | $[3, -2, 4, -1]$ |
| **Constante de Partición ($P_m$)** | $4$ | $4$ |
| **Amplitud Modular ($A_N$)** | $3$ | $3$ |
| **Delta Interno ($\Delta C_N$)** | $[5, 5, 5] \pmod 9$ | $[6, 6, 6] \pmod{11}$ |
| **Intervalo Generador Central** | $666.67 \text{ cents}$ (Tritono puro) | $654.55 \text{ cents}$ (Undecimal infra-quinta) |
| **Ancho de Paso ($\delta$)** | $133.33 \text{ cents}$ | $109.09 \text{ cents}$ |

---

## 2.4 El Acorde Transformante $T_N$: Conducción de Voces y Dinámica Modulatoria

El **Acorde Transformante** $T_N$ no es simplemente una colección estática de alturas en $\mathcal{S}$-Space; es una matriz de permutación continua que viabiliza transiciones parsimoniosas a lo largo de los ejes armónicos bi-axiales.

### 2.4.1 Operador OVC (Optimal Voice-leading Coefficient)

Para clasificar la calidad morfológica de los acordes que componen la matriz y asegurar una conducción de voces de mínima resistencia motriz, se formaliza el operador de conducción de voces óptima (OVC).

Dadas dos tetradas contiguas en la cadena de funciones, $A = [a_1, a_2, a_3, a_4]$ y $B = [b_1, b_2, b_3, b_4]$, el coeficiente OVC $\mathcal{D}(A, B)$ se define como la distancia métrica mínima inducida por el grupo de permutaciones $\mathfrak{S}_4$ sobre el toro microtonal $\mathbb{T}^N$:

$$\mathcal{D}(A, B) = \min_{\sigma \in \mathfrak{S}_4} \left( \sum_{i=1}^{4} \left| a_i - b_{\sigma(i)} \right|_{\mathbb{T}^N} \right)$$

donde $|x - y|_{\mathbb{T}^N} = \min(|x - y|, N - |x - y|)$.

#### Clasificación Cualitativa Derivada de $C_N$
A partir de los deltas de la Cajita Central, los acordes se particionan en tres órbitas cualitativas:
1. **Calidad Mayor ($\mathcal{M}$):** Dominada por la subsecuencia que contiene el paso generador de tercera infra-neutra (intervalo de mayor resolución polar positiva).
2. **Calidad Menor ($m$):** Centrada sobre el polo reflejo $P_m$, cuya suma interválica contra la raíz exhibe deflexión negativa.
3. **Calidad Simétrica ($\mathcal{S}$):** Acordes residuales donde el balance modal se neutraliza:

$$\sum_{i=1}^3 (-1)^i \Delta c_i = 0$$

### 2.4.2 El Acorde Simétrico Residual ($S_N$) como Pivote Microtonal

Conforme a los axiomas de la matriz bi-eje $F_N$, el acorde simétrico residual $S_N$ queda invariablemente confinado a la posición orbital:

$$\text{pos}(S_N) = N - 3$$

En $N = 9$: $\text{pos}(S_9) = 9 - 3 = 6$.  
En $N = 11$: $\text{pos}(S_{11}) = 11 - 3 = 8$.

Debido a que el acorde $S_N$ minimiza la polaridad quiral (su proyección no proyecta gradiente vectorial hacia el eje mayor ni hacia el eje menor), actúa como el conducto de transición o túnel de modulación microtonal. Un desplazamiento de fase en $S_N$ mediante un incremento commático permite reorientar el centro gravitacional del sistema hacia dominios $N$-ET alternativos sin salto abrupto de voz armónica ($\mathcal{D}(A, B) \le 2$).

---

## 2.5 Implementación Algorítmica: Generador de Red y Cálculo de OVC

El siguiente script en SuperCollider sintetiza los operadores analíticos formalizados: calcula la matriz primaria, el mapeo acústico en cents, y computa el OVC entre la Cajita Central y sus traslaciones.

```supercollider
// =====================================================================
// THE CHAIN THEORY: Engine de Mapeo Acústico, Ordenamiento y Conducción
// =====================================================================

(
var computeChain = { |n = 11, p_m = 4, c_box|
    var chainIndices, acousticCents, sortedScale, stepSizes, ovcMetric;
    var stepInCents = 1200.0 / n;

    // 1. Vector de la Cajita Central
    postf("\n=== PROCESANDO SISTEMA N = %-ET ===\n", n);
    postf("Cajita Central C_%: %\n", n, c_box);
    postf("P_m: %, Paso unitario: % cents\n", p_m, stepInCents.round(0.001));

    // 2. Mapeo Acústico de la Cajita Central mod 1200
    acousticCents = c_box.collect { |idx|
        (idx * stepInCents).mod(1200.0);
    };
    postf("Mapeo Acústico C_% (cents): %\n", n, acousticCents.round(0.01));

    // 3. Simulación de Expansión de Cadena (Indices Modulares)
    // Se genera la secuencia intercalada desde la Cajita
    chainIndices = Array.newClear(n);
    c_box.do { |val, i| chainIndices[i] = val.mod(n) };
    
    // Relleno simétrico residual (ejemplo heurístico del motor)
    (4..(n - 1)).do { |i|
        chainIndices[i] = (chainIndices[i - 1] + p_m).mod(n);
    };
    postf("Matriz Primaria T_% (indices mod %): %\n", n, n, chainIndices);

    // 4. Proyección al Espacio Escalar (S_p,N)
    sortedScale = chainIndices.collect { |k| (k * stepInCents).mod(1200.0) }.sort;
    postf("Escala Ordenada S_%: %\n", n, sortedScale.round(0.01));

    // 5. Cálculo del Espectro de Pasos Interválicos (delta_i)
    stepSizes = Array.fill(n, { |i|
        var next = if(i < (n - 1), { sortedScale[i + 1] }, { sortedScale[0] + 1200.0 });
        (next - sortedScale[i]).round(0.001);
    });
    postf("Deltas de Paso (Grados de Paso): %\n", stepSizes);

    // 6. Demostración de Cálculo OVC entre C_N y una traslación cíclica (D_1)
    // Distancia toroidal mínima sobre Z_n
    ovcMetric = { |chordA, chordB, modN|
        var diffSum = 0;
        chordA.do { |valA, i|
            var valB = chordB[i];
            var direct = (valA - valB).abs;
            var circular = modN - direct;
            diffSum = diffSum + min(direct, circular);
        };
        diffSum;
    };

    postf("OVC Métrica [C_% -> Shift(+1)]: % pasos microtonales\n", 
        n, ovcMetric.value(c_box.mod(n), (c_box + 1).mod(n), n));
    postf("------------------------------------------------------------\n");
};

// Ejecución con los datos de referencia
s.waitForBoot({
    computeChain.value(9, 4, [3, -1, 4, 0]);
    computeChain.value(11, 4, [3, -2, 4, -1]);
});
)
```

---

## 2.6 Síntesis Estructural del Capítulo

1. **Afinidad Acústica:** El comportamiento de $C_9$ converge de manera unívoca hacia simetrías tritónicas neutras ($666.67\text{ cents}$), estableciendo una infraestructura armónica isométrica que anula la polaridad diatónica en favor de una red puramente cíclica.
2. **Deflexión Microtonal en $11$-ET:** En contraposición, $C_{11}$ instaura una microtonalidad de corte undecimal mediada por un intervalo de acoplamiento de $654.55\text{ cents}$, generando el marco óptimo para la ramificación bi-axial de funciones tonales mayores y menores con una resolución parsimoniosa cuantificada por un coeficiente $\mathcal{D}(A, B)$ mínimo.
3. **Continuidad de Conducción:** El ordenamiento escalar $S_{p,N}$ preserva la estricta regularidad del continuo microtonal, demostrando que la complejidad interválica de *The Chain Theory* no es caótica, sino el resultado riguroso de proyectar geometrías multidimensionales enrolladas en la Cajita Central sobre la línea unidimensional de las frecuencias audibles.