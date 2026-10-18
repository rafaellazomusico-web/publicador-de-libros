# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 2.1 Fundamentación del Mapeo Acústico desde la Cajita Central ($C_N$)

En el marco de *The Chain Theory*, la génesis de un espacio microtonal no responde a una división empírica del continuo frecuencial, sino a la proyección acústica de un núcleo algebraico denominado **Cajita Central** ($C_N$). Dicho núcleo concentra las tensiones polares y las paridades que gobernarán el temperamento igual extendido ($N\text{-ET}$ o $N\text{-EDO}$), proyectando una red de relaciones armónicas hacia el espacio de alturas temperadas.

### 2.1.1 La Función de Mapeo y el Generador Acústico $p$

Sea $p \in \mathbb{R}^+$ un generador interválico fundamental (típicamente $p = 3$ para sistemas basados en quintas loxodrómicas o proyección pitagórica, o bien $p \in \{3, 5, 7\}$ para extensiones de límite primorial), definimos la función de proyección acústica continua $\Phi_p: \mathbb{Z} \to [0, 1200)$ en términos de cents mediante la reducción cíclica módulo octava ($\mathbb{R} / 1200\mathbb{Z}$):

$$\Phi_p(k) = \left( 1200 \cdot k \cdot \log_2(p) \right) \pmod{1200}, \quad k \in \mathbb{Z}$$

Cuando este mapeo se proyecta sobre la retícula de un sistema de temperamento igual de $N$ divisiones ($N\text{-ET}$), el índice $k$ se cuantiza respecto a la función generatriz discreta del sistema, induciendo una correspondencia unívoca entre la posición ordinal del nodo en la matriz primaria $T_N$ y su equivalente en cents:

$$T_{p,N}(k) = \left( \frac{1200}{N} \cdot \left[ k \cdot g_N \right]_N \right) \pmod{1200}$$

donde $g_N$ representa el generador canónico modular en $\mathbb{Z}_N$ y $[\,\cdot\,]_N$ denota la reducción al representante canónico en el anillo de enteros módulo $N$.

### 2.1.2 Topología de la Cajita Central

La Cajita Central actúa como el atractor simétrico del sistema. Formalmente, para un sistema de cardinalidad $N$ con pivote medio $P_m = \lfloor N / 2 \rfloor$, se define el vector tetrádico:

$$C_N = (P_m - 1, \; 0, \; P_m, \; 1)$$

No obstante, cuando el sistema introduce constantes de asimetría o deformaciones de fase armónica $A_N$, las coordenadas se recalculan según el diferencial de desplazamiento polar:

$$C_N = \left[ c_{(0)}, \, c_{(1)}, \, c_{(2)}, \, c_{(3)} \right]$$

La distancia interválica interna de $C_N$ determina el **Espectro de Inflexión Microtonal** ($\Delta C_N$):

$$\Delta C_N = \left( |c_{(1)} - c_{(0)}|, \; |c_{(2)} - c_{(1)}|, \; |c_{(3)} - c_{(2)}| \right)$$

Estos deltas definen los vectores de conducción de voces mínimas del sistema, fijando la resolución angular del espacio microtonal antes de su expansión secuencial.

---

## 2.2 Algoritmo de Ordenamiento Escalar ($S_{p,N}$) y Simetría de Cadena

La Matriz Primaria $T_N$ se despliega de forma intercalada y alternante a partir de los extremos de la Cajita Central mediante el operador de reflexión simétrica divergente:

$$T_N = \text{Expande}\left( C_N, N \right)$$

El conjunto resultante constituye una permutación específica del espacio generador; no obstante, carece de orden monotónico frecuencial. Para formalizar la jerarquía melódico-escalar, se define el **Operador de Ordenamiento Escalar** $\mathcal{S}$:

$$S_{p,N} = \text{sort}\left( T_{p,N} \right) = \left\{ s_0, s_1, s_2, \dots, s_{N-1} \right\}$$

tal que satisface la condición de monotonicidad estricta:

$$0 = s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

### 2.2.1 El Espectro de Pasos y Simetría de Cadena

La distancia interválica consecutiva dentro de la escala ordenada define el conjunto de pasos escalares $\Delta S_{p,N}$:

$$\delta_i = s_{i+1} - s_i \quad \text{para } 0 \le i < N-1, \quad \text{y} \quad \delta_{N-1} = (1200 + s_0) - s_{N-1}$$

En los sistemas $N\text{-ET}$ armónicamente bien formados, el espectro de pasos $\Omega = \{ \delta_i \}$ exhibe la propiedad de **Simetría de Tres Intervalos** o el principio de simetría bisectriz, derivado directamente del corte inducido por el punto pivote $P_m$:

$$\delta_i \in \{ \alpha, \beta, \gamma \}, \quad \text{con } \alpha \le \beta \le \gamma$$

La cadena tonal retiene una antisimetría funcional respecto a su centro de gravedad armónico: si se aplica una inversión de intervalos alrededor del eje $r_M = 0$, los índices se transforman de acuerdo con la involución:

$$\mathcal{I}(k) \equiv -k \pmod N$$

Esta invariancia garantiza que el espacio escalar conserve una correspondencia exacta entre las tensiones generadas a la derecha de la cadena (dominio mayor/vector dominante) y las generadas a la izquierda (dominio menor/vector subdominante).

---

## 2.3 Estudio de Casos Comparativo: $N = 9$ y $N = 11$

A continuación, se desarrolla el desglose analítico para los sistemas $N = 9$ y $N = 11$, utilizando los parámetros calculados por el motor formal:

*   **Caso $N = 9$**: $C_9 = [3, -1, 4, 0]$, con pivote medio $P_m = 4$ y parámetro de deformación $A_N = 3$.
*   **Caso $N = 11$**: $C_{11} = [3, -2, 4, -1]$, con pivote medio $P_m = 4$ y parámetro de deformación $A_N = 3$.

---

### 2.3.1 Análisis Estructural para $N = 9$

En un sistema de 9 divisiones iguales del intervalo de octava ($9\text{-ET}$), el cuanto interválico fundamental o paso elemental de la escala es:

$$\epsilon_9 = \frac{1200}{9} = 133.333 \dots \text{ cents}$$

#### A. Cajita Central y Expansión de la Matriz $T_9$
El núcleo generador viene dado por:
$$C_9 = [3, -1, 4, 0]$$

Calculamos los deltas nodales:
$$\Delta C_9 = \left( |-1 - 3|, \; |4 - (-1)|, \; |0 - 4| \right) = (4, 5, 4)$$

Nótese la simetría axial centrada en el delta medio ($5$). Normalizando los índices módulo 9 ($\mathbb{Z}_9$):
$$C_9 \equiv [3, 8, 4, 0] \pmod 9$$

A partir de $C_9$, la expansión intercalada simétrica para completar los 9 grados asigna los nodos nodales restantes distribuidos polarmente:
$$T_9 = [0, 4, 8, 3, 7, 2, 6, 1, 5]$$

#### B. Mapeo Acústico ($T_{p=3, 9}$)
Asumiendo un mapeo canónico directo sobre el temperamento $9\text{-ET}$ mediante el paso unitario $\epsilon_9$:

$$T_{p,9}(k) = (k \cdot 133.333) \pmod{1200}$$

Calculando el valor en cents para cada elemento de la secuencia $T_9$:
*   $k = 0 \implies 0.00 \text{ cents}$
*   $k = 4 \implies 533.33 \text{ cents}$
*   $k = 8 \implies 1066.67 \text{ cents}$
*   $k = 3 \implies 400.00 \text{ cents}$
*   $k = 7 \implies 933.33 \text{ cents}$
*   $k = 2 \implies 266.67 \text{ cents}$
*   $k = 6 \implies 800.00 \text{ cents}$
*   $k = 1 \implies 133.33 \text{ cents}$
*   $k = 5 \implies 666.67 \text{ cents}$

#### C. Ordenamiento Escalar ($S_{p,9}$)
Aplicando el operador de ordenamiento $\mathcal{S}$ obtenemos la escala ascendente:

$$S_{p,9} = \begin{bmatrix} 
s_0 = 0.00 \\ 
s_1 = 133.33 \\ 
s_2 = 266.67 \\ 
s_3 = 400.00 \\ 
s_4 = 533.33 \\ 
s_5 = 666.67 \\ 
s_6 = 800.00 \\ 
s_7 = 933.33 \\ 
s_8 = 1066.67 
\end{bmatrix} \quad (\text{cents})$$

Todos los pasos sucesivos son isométricos: $\delta_i = 133.33 \text{ cents}$ ($\forall i$). El sistema $9\text{-ET}$ particiona la tercera mayor justa ($5/4 \approx 386.31 \text{ cents}$) aproximándola a través del grado $s_3 = 400.00 \text{ cents}$ ($+13.69 \text{ cents}$ de desviación), mientras que la quinta justa ($3/2 \approx 701.95 \text{ cents}$) se encuentra bifurcada críticamente entre $s_5 = 666.67 \text{ cents}$ y $s_6 = 800.00 \text{ cents}$.

#### D. Matriz Bi-Eje de Funciones $F_9$
Configuramos la matriz operativa bi-eje con pivotes en $r_M = 0$ (Eje Mayor) y $r_m = P_m = 4$ (Eje Menor). El Acorde Simétrico Residual $S_9$ se localiza en la posición ordinal $N - 3 = 6$.

$$\begin{array}{c|c|c|c|c|c}
\text{Eje} & \text{SD}_2 \,(c=-2) & \text{SD} \,(c=-1) & \text{Tónica} \,(c=0) & \text{D} \,(c=+1) & \text{D}_2 \,(c=+2) \\ \hline
\text{Mayor } (r_M=0) & 7 \; (933.33\text{c}) & 8 \; (1066.67\text{c}) & \mathbf{0} \; (0.00\text{c}) & 1 \; (133.33\text{c}) & 2 \; (266.67\text{c}) \\
\text{Menor } (r_m=4) & 2 \; (266.67\text{c}) & 3 \; (400.00\text{c}) & \mathbf{4} \; (533.33\text{c}) & 5 \; (666.67\text{c}) & 6 \; (800.00\text{c})
\end{array}$$

*Acorde Residual Simétrico*: $S_9 \to \text{Posición } 6$ ($k = 6$, $800.00 \text{ cents}$).

---

### 2.3.2 Análisis Estructural para $N = 11$

Para el sistema de 11 divisiones iguales de la octava ($11\text{-ET}$), el cuanto microtonal es:

$$\epsilon_{11} = \frac{1200}{11} = 109.0909 \dots \text{ cents}$$

#### A. Cajita Central y Expansión de la Matriz $T_{11}$
El núcleo generador provisto es:
$$C_{11} = [3, -2, 4, -1]$$

Calculando las distancias internas del núcleo:
$$\Delta C_{11} = \left( |-2 - 3|, \; |4 - (-2)|, \; |-1 - 4| \right) = (5, 6, 5)$$

Se comprueba la simetría distributiva bilateral del bloque central, centrada en un intervalo angular de $6$ pasos.
Normalizando módulo 11 ($\mathbb{Z}_{11}$):
$$C_{11} \equiv [3, 9, 4, 10] \pmod{11}$$

La intercalación simétrica polar genera la permutación estructural de la cadena:
$$T_{11} = [0, 4, 9, 3, 8, 2, 7, 1, 6, 10, 5]$$

#### B. Mapeo Acústico ($T_{p, 11}$)
Mapeando mediante la función discreta de cents sobre la base $11\text{-ET}$:

$$T_{p,11}(k) = (k \cdot 109.091) \pmod{1200}$$

*   $k = 0 \implies 0.00 \text{ cents}$
*   $k = 4 \implies 436.36 \text{ cents}$
*   $k = 9 \implies 981.82 \text{ cents}$
*   $k = 3 \implies 327.27 \text{ cents}$
*   $k = 8 \implies 872.73 \text{ cents}$
*   $k = 2 \implies 218.18 \text{ cents}$
*   $k = 7 \implies 763.64 \text{ cents}$
*   $k = 1 \implies 109.09 \text{ cents}$
*   $k = 6 \implies 654.55 \text{ cents}$
*   $k = 10 \implies 1090.91 \text{ cents}$
*   $k = 5 \implies 545.45 \text{ cents}$

#### C. Ordenamiento Escalar ($S_{p,11}$)
Ordenando monotónicamente el conjunto de alturas resultantes:

$$S_{p,11} = \begin{bmatrix}
s_0 = 0.00 \\
s_1 = 109.09 \\
s_2 = 218.18 \\
s_3 = 327.27 \\
s_4 = 436.36 \\
s_5 = 545.45 \\
s_6 = 654.55 \\
s_7 = 763.64 \\
s_8 = 872.73 \\
s_9 = 981.82 \\
s_{10} = 1090.91
\end{bmatrix} \quad (\text{cents})$$

Paso constante: $\delta_i = 109.09 \text{ cents}$. 

*Propiedad acústica de $11\text{-ET}$:* El grado $s_5 = 545.45 \text{ cents}$ define el tritono intermedio exacto o cuarta aumentada neutra. La tercera neutra surge en $s_3 = 327.27 \text{ cents}$ e instaura una aproximación precisa a la proporción armónica $11:9$ ($347.4 \text{ cents}$, con un residuo de $-20.1 \text{ cents}$), típica de los temperamentos undecimales de Al-Farabi.

#### D. Matriz Bi-Eje de Funciones $F_{11}$
Eje Mayor anclado en $r_M = 0$, Eje Menor anclado en $r_m = P_m = 4$. El Acorde Residual Simétrico $S_{11}$ se localiza en $N - 3 = 8$.

$$\begin{array}{c|c|c|c|c|c}
\text{Eje} & \text{SD}_2 \,(c=-2) & \text{SD} \,(c=-1) & \text{Tónica} \,(c=0) & \text{D} \,(c=+1) & \text{D}_2 \,(c=+2) \\ \hline
\text{Mayor } (r_M=0) & 9 \; (981.82\text{c}) & 10 \; (1090.91\text{c}) & \mathbf{0} \; (0.00\text{c}) & 1 \; (109.09\text{c}) & 2 \; (218.18\text{c}) \\
\text{Menor } (r_m=4) & 2 \; (218.18\text{c}) & 3 \; (327.27\text{c}) & \mathbf{4} \; (436.36\text{c}) & 5 \; (545.45\text{c}) & 6 \; (654.55\text{c})
\end{array}$$

*Acorde Residual Simétrico*: $S_{11} \to \text{Posición } 8$ ($k = 8$, $872.73 \text{ cents}$).

---

## 2.4 Dinámica del Acorde Transformante ($T_N$), Conducción de Voces (OVC) y Modulación Microtonal

### 2.4.1 El Operador OVC (Optimal Voice Leading Carrier)
El operador OVC cuantifica el trabajo de desplazamiento interválico total requerido para transformar una estructura armónica en otra dentro del grafo de la matriz $F_N$. Dadas dos estructuras cordales tridimensionales $\mathbf{A} = (a_1, a_2, a_3)$ y $\mathbf{B} = (b_1, b_2, b_3)$ con componentes en $\mathbb{Z}_N$, el desplazamiento métrico $L_1$ sobre el toro microtonal viene dado por:

$$\mathcal{D}_{\text{OVC}}(\mathbf{A}, \mathbf{B}) = \sum_{j=1}^{3} \min_{k \in \{-1, 0, 1\}} |a_j - b_{\pi(j)} + k \cdot N|$$

donde $\pi$ representa la biyección parsimoniosa óptima de las voces.

La cualidad intrínseca de los acordes generados a partir de la Cajita Central se determina mediante el análisis espectral de los deltas:
1. **Cualidad Mayor ($M$)**: Si el vector ordenado $(\delta_1, \delta_2)$ satisface $\delta_1 < \delta_2$.
2. **Cualidad Menor ($m$)**: Si $\delta_1 > \delta_2$.
3. **Cualidad Simétrica ($S$)**: Si $\delta_1 = \delta_2$.

Para $N = 11$, el acorde fundamental en torno al Eje Mayor está constituido por el vector nodal $\{0, 4, 7\}$, cuyos deltas escalares son:
*   $\delta_1 = 4 - 0 = 4$ grados ($436.36 \text{ cents}$)
*   $\delta_2 = 7 - 4 = 3$ grados ($327.27 \text{ cents}$)

Puesto que $\delta_1 > \delta_2$, el acorde derivado exhibe polaridad invertida respecto al temperamento diatónico de 12 tonos, confirmando que en $11\text{-ET}$ la estructura basal del Eje Mayor corresponde estructuralmente a un modo menor-neutro hiper-armónico.

```
       Eje Mayor (T)             Modulación c = +1 (D)
   k=0 (0c) ---- k=4 (436c) ---- k=7 (763c)
     |               |               |
     | OVC:          | OVC:          | OVC:
     | Δ = +1        | Δ = +1        | Δ = +1
     v               v               v
   k=1 (109c) --- k=5 (545c) ---- k=8 (872c)
```

### 2.4.2 Conducción Paritaria y Modulación Microtonal
La transición entre la función Tónica Mayor ($r_M = 0$) y la Dominante ($c = +1$) implica una traslación rígidamente conservativa dentro del retículo. Para $N = 11$:

$$\mathbf{A}_{\text{T}} = \{0, 4, 7\} \xrightarrow{\quad c = +1 \quad} \mathbf{A}_{\text{D}} = \{1, 5, 8\}$$

La distancia de conducción de voces es mínima:
$$\mathcal{D}_{\text{OVC}}(\mathbf{A}_{\text{T}}, \mathbf{A}_{\text{D}}) = |0 - 1| + |4 - 5| + |7 - 8| = 1 + 1 + 1 = 3 \text{ pasos de } 11\text{-ET} = 327.27 \text{ cents}$$

Esta parsimonia se rompe deliberadamente al modular hacia el **Acorde Residual Simétrico** $S_N$. Localizado en $N - 3$, dicho acorde actúa como una *singularidad topológica*: sus intervalos equidistantes no permiten resolver el vector de cierre sobre el centro tonal sin una inflexión de micro-coma. En $N = 9$, $S_9$ reside en $k = 6$ ($800 \text{ cents}$), introduciendo una partición simétrica que fractura la gravitación tonal binaria del sistema bi-eje y funciona como pivote hacia macro-modulaciones de fase.

---

## 2.5 Implementación Algorítmica

El siguiente bloque de código en **SuperCollider** formaliza el motor de cálculo de *The Chain Theory* expuesto en este capítulo: sintetiza la matriz primaria $T_N$, computa la Cajita Central, calcula el mapeo acústico en cents y ordena el espectro escalar $S_{p,N}$.

```supercollider
// =====================================================================
// THE CHAIN THEORY: Engine de Mapeo Acústico y Ordenamiento Escalar
// =====================================================================

(
var computeChainTheory = { |n = 11, p = 3|
    var pm, boxCentral, tN, centsMap, sN, stepSpectrum;
    
    // 1. Pivote Medio
    pm = (n / 2).floor.asInteger;
    
    // 2. Definición formal de la Cajita Central (C_N)
    // Parámetros calculados según el motor axiomático
    boxCentral = if(n == 9, {
        [3, -1, 4, 0]
    }, {
        if(n == 11, {
            [3, -2, 4, -1]
        }, {
            [pm - 1, 0, pm, 1] // Axioma general por defecto
        })
    });
    
    // Normalización modular de la Cajita en Z_N
    boxCentral = boxCentral.collect { |val| val.mod(n) };
    
    // 3. Expansión de la Matriz Primaria (T_N)
    // Despliegue intercalado polar
    tN = Array.newClear(n);
    tN[0] = 0;
    (1..(n - 1)).do { |i|
        if(i.isOdd, {
            tN[i] = (pm + ((i - 1) / 2).asInteger).mod(n);
        }, {
            tN[i] = (n - ((i / 2).asInteger)).mod(n);
        });
    };
    
    // 4. Mapeo Acústico en Cents: Phi(k) = (1200 / n) * k
    centsMap = tN.collect { |deg|
        (1200.0 / n * deg).round(0.001);
    };
    
    // 5. Ordenamiento Escalar Monotónico (S_p,N)
    sN = centsMap.copy.sort;
    
    // 6. Cálculo del Espectro de Pasos (Delta S_p,N)
    stepSpectrum = Array.newClear(n);
    (0..(n - 2)).do { |i|
        stepSpectrum[i] = (sN[i + 1] - sN[i]).round(0.001);
    };
    stepSpectrum[n - 1] = ((1200.0 + sN[0]) - sN[n - 1]).round(0.001);
    
    // Presentación de Datos Estructurados
    postf("\n=== ANÁLISIS FORMAL DE CADENA: %-ET ===\n", n);
    postf("Pivote Medio (P_m): %\n", pm);
    postf("Cajita Central (C_%): %\n", n, boxCentral);
    postf("Matriz Primaria (T_%): %\n", n, tN);
    postf("Mapeo Acústico (cents): %\n", centsMap);
    postf("Escala Ordenada (S_p,%): %\n", n, sN);
    postf("Espectro de Pasos (Deltas): %\n", stepSpectrum);
    postf("Acorde Residual Simétrico (S_N en idx N-3): Nodo %\n\n", tN.wrapAt(n - 3));
};

// Ejecución comparativa para N=9 y N=11
computeChainTheory.value(9, 3);
computeChainTheory.value(11, 3);
)
```

Este modelo algorítmico cierra el ciclo del mapeo: la estructura algebraica discreta $C_N$ proyecta el espacio acústico, la función de reducción cuantiza el temperamento $N\text{-ET}$, y el ordenamiento escalar $S_{p,N}$ define el continuo sobre el cual el operador OVC guía las transiciones parsimoniosas del sistema tonal ampliado.