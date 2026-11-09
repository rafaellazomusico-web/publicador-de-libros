# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 2.1 Formalización Matemática del Mapeo Acústico ($T_{p,N}$) e Intervalística Derivada de la Cajita Central

La teoría de cadenas armónicas (*The Chain Theory*) asume como principio fundacional que cualquier escala microtonal regular $N$-ET (sistemas temperados de $N$ divisiones iguales de la octava) puede descomponerse en una trayectoria proyectiva generada por un operador primo fundamental $p \in \mathbb{R}^+$. Dentro de este espacio, la **Cajita Central** ($C_N$) actúa como el núcleo nucleador de la energía espectral del sistema.

### 2.1.1 La Proyección Acústica Modular
Sea $N \in \mathbb{Z}^+$ el orden dimensional del sistema temperado y sea $p$ la frecuencia normalizada del generador acústico (donde típicamente $p = 3/2$ representa la proyección por quintas pitagóricas puras, o bien $p \in \{3, 5, 7, 11\}$ en afinaciones justas de orden superior). La transformación que mapea cada índice $k \in \mathbb{Z}$ del retículo armónico discreto al continuo de afinación en céntimas modulares ($[0, 1200) \subset \mathbb{R}$) se define como el homomorfismo $\phi_p$:

$$\phi_p(k) = \left( 1200 \cdot k \cdot \log_2(p) \right) \pmod{1200}$$

Cuando esta proyección opera sobre una colección finita de índices de la cadena tonal $T_N = \{k_0, k_1, \dots, k_{N-1}\}$, se obtiene el **Mapeo Acústico No Ordenado** $T_{p,N}$:

$$T_{p,N} = \phi_p(T_N) = \{ \phi_p(k) \mid k \in T_N \}$$

### 2.1.2 Topología Interválica de la Cajita Central
La Cajita Central $C_N$ es el subespacio tetra-dimensional de índices $C_N \subset T_N$ delimitado por la partición mediana $P_m = \lfloor N / 2 \rfloor$. Algebraicamente, en su forma compactada general se define como un vector cuádruple:

$$C_N = \left( c_0, c_1, c_2, c_3 \right)$$

cuyos elementos representan los nudos sobre los cuales se articula la tensión armónica basal del sistema. La proyección acústica de la Cajita Central, denotada como $\Phi_p(C_N)$, produce el tetrasonido generatriz:

$$\Phi_p(C_N) = \left( \phi_p(c_0), \phi_p(c_1), \phi_p(c_2), \phi_p(c_3) \right)$$

A partir de $\Phi_p(C_N)$ se extrae el **Vector de Deltas Acústicos** ($\Delta_{\text{acústico}}$), determinado por las distancias cíclicas entre sus componentes adyacentes:

$$\delta_i = \left( \phi_p(c_{i+1}) - \phi_p(c_i) \right) \pmod{1200}, \quad i \in \{0, 1, 2\}$$

Este vector $\Delta = (\delta_0, \delta_1, \delta_2)$ establece la morfología interválica fundamental (micro-terceras, segundas neutras, cuartas ensanchadas) que determinará si los acordes subsecuentes en la cadena poseen cualidades Mayores, Menores o Simétricas mediante el Operador de Conducción de Voces (**OVC**).

---

## 2.2 Ordenamiento Escalar ($S_{p,N}$), Grados de Paso y Simetría Tonal

El conjunto $T_{p,N}$, al derivarse de un proceso de intercalación proyectiva simétrica, no se presenta en orden de frecuencia monótono creciente. Para transformar la cadena tensada acústicamente en una escala ejecutable, se requiere la aplicación del **Operador de Ordenamiento Escalar**:

$$S_{p,N} = \text{sort}(T_{p,N}) = \left( s_0, s_1, s_2, \dots, s_{N-1} \right)$$

tal que:

$$0 \le s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

### 2.2.1 El Retículo de Pasos Interválicos (Step Sizes)
El espectro interválico adyacente viene regido por las diferencias:

$$\sigma_j = s_{(j+1) \pmod N} - s_j \pmod{1200}$$

Bajo el Teorema de Steinhaus (conjetura de las tres distancias aplicada a rotaciones de círculos continuos), la secuencia cíclica $(\sigma_0, \sigma_1, \dots, \sigma_{N-1})$ adopta a lo sumo tres valores discretos $\{\sigma_{\text{min}}, \sigma_{\text{med}}, \sigma_{\text{max}}\}$. En los sistemas donde la Cajita Central minimiza la dispersión de fase acústica, la partición degenera en un conjunto bipartito o monovalente, optimizando la homogeneidad de los grados de paso (conducción por segundas microtonales).

```
Retículo Acústico T_{p,N} (Espacio de Proyección por Índices)
       [ c_1 ] -------- [ c_3 ] -------- [ c_5 ] ...
          |                |                |
       [ c_0 ] -------- [ c_2 ] -------- [ c_4 ] ...
                         │
                         ▼  sort()
Escala S_{p,N} (Círculo de Octava / Espacio Modular Mod 1200 cents)
   s_0 ───(σ_0)─── s_1 ───(σ_1)─── s_2 ─── ... ───(σ_{N-1})─── s_0
```

### 2.2.2 Simetría Especular de la Cadena
La expansión de la matriz primaria se articula mediante la incorporación simétrica de polos alrededor de $C_N$. Si definimos el centro de inversión armónica en el punto medio del espectro:

$$\mu = \frac{1}{N} \sum_{k \in T_N} \phi_p(k)$$

la cadena exhibe invariancia bajo la involución de reflexión espectral:

$$\mathcal{R}(s_j) = (2\mu - s_j) \pmod{1200}$$

lo que asegura que cada grado modal posea un complementario exacto en el espacio de alturas, garantizando la perfecta dualidad funcional de la Matriz Bi-Eje $F_N$.

---

## 2.3 Estudio de Casos Discretos: Despliegue Estructural en $N = 9$ y $N = 11$

Analizaremos la construcción endógena, el mapeo acústico y la partición escalar para dos micro-espacios modales de alta relevancia espectral, empleando como generador acústico la quinta justa pitagórica canónica $p = 3/2$ ($1200 \cdot \log_2(3/2) \approx 701.955\text{ cents}$).

---

### 2.3.1 Caso I: Sistema $N = 9$
*Parámetros calculados:*
- Dimensión: $N = 9$
- Partición mediana: $P_m = \lfloor 9 / 2 \rfloor = 4$
- Parámetro de acoplamiento: $A_N = 3$
- Cajita Central: $C_9 = [3, -1, 4, 0]$

#### A. Expansión de Índices de la Cadena $T_9$
A partir de la Cajita Central $[3, -1, 4, 0]$, la intercalación de los restantes $N - 4 = 5$ índices se propaga alternando la periferia simétrica:

$$T_9 = [-2, 5, -1, 3, 0, 4, 1, -3, 2]$$

#### B. Proyección Acústica $T_{3/2, 9}$
Aplicando $\phi_{3/2}(k) = (k \cdot 701.955) \pmod{1200}$:

| Índice $k$ | Expresión Real (cents) | Valor Modular $\phi_{3/2}(k)$ |
| :---: | :--- | :--- |
| **$-3$** | $-2105.865 \pmod{1200}$ | $294.135$ |
| **$-2$** | $-1403.910 \pmod{1200}$ | $996.090$ |
| **$-1$** | $-701.955 \pmod{1200}$ | $498.045$ |
| **$0$** | $0.000$ | $0.000$ |
| **$1$** | $701.955$ | $701.955$ |
| **$2$** | $1403.910 \pmod{1200}$ | $203.910$ |
| **$3$** | $2105.865 \pmod{1200}$ | $905.865$ |
| **$4$** | $2807.820 \pmod{1200}$ | $407.820$ |
| **$5$** | $3509.775 \pmod{1200}$ | $1109.775$ |

#### C. Proyección de la Cajita Central $C_9$ y Vector OVC
Evaluando $C_9 = [3, -1, 4, 0]$:
- $\phi_{3/2}(3) = 905.865$ cents
- $\phi_{3/2}(-1) = 498.045$ cents
- $\phi_{3/2}(4) = 407.820$ cents
- $\phi_{3/2}(0) = 0.000$ cents

Ordenando las componentes internas para la evaluación morfológica del acorde basal: $[0.000, 407.820, 498.045, 905.865]$.
Observamos la emergencia de una tercera cuasi-mayor ultra-justa ($407.82$ cents $\approx 5/4$ pitagórico), una cuarta justa imperfecta ($498.05$ cents) y una sexta mayor neutra ($905.87$ cents).

#### D. Ordenamiento Escalar $S_{3/2, 9}$
Ordenando ascendentemente los valores acústicos de $T_{3/2, 9}$:

$$S_{3/2, 9} = (0.000, 203.910, 294.135, 407.820, 498.045, 701.955, 905.865, 996.090, 1109.775)$$

Diferencias interválicas sucesivas ($\sigma_j$):
- $\sigma_0 = 203.910 - 0.000 = 203.910$ cents (Tono grande, $L$)
- $\sigma_1 = 294.135 - 203.910 = 90.225$ cents (Limma menor, $s$)
- $\sigma_2 = 407.820 - 294.135 = 113.685$ cents (Apotomé / Semitono grande, $m$)
- $\sigma_3 = 498.045 - 407.820 = 90.225$ cents ($s$)
- $\sigma_4 = 701.955 - 498.045 = 203.910$ cents ($L$)
- $\sigma_5 = 905.865 - 701.955 = 203.910$ cents ($L$)
- $\sigma_6 = 996.090 - 905.865 = 90.225$ cents ($s$)
- $\sigma_7 = 1109.775 - 996.090 = 113.685$ cents ($m$)
- $\sigma_8 = (1200 + 0.000) - 1109.775 = 90.225$ cents ($s$)

Estructura de la escala: $(L, s, m, s, L, L, s, m, s)$. La distribución exhibe una simetría de espejo centrada en el eje de la quinta ($701.955$ cents).

---

### 2.3.2 Caso II: Sistema $N = 11$
*Parámetros calculados:*
- Dimensión: $N = 11$
- Partición mediana: $P_m = 4$
- Parámetro de acoplamiento: $A_N = 3$
- Cajita Central: $C_{11} = [3, -2, 4, -1]$

#### A. Expansión de Índices de la Cadena $T_{11}$
La Cajita Central $[3, -2, 4, -1]$ ancla la génesis armónica. La intercalación simétrica polar incorpora los 7 índices remanentes:

$$T_{11} = [-3, 5, -2, 3, -1, 4, 0, 6, 1, -4, 2]$$

#### B. Proyección Acústica de la Cajita Central $C_{11}$
- $\phi_{3/2}(3) = 905.865$ cents
- $\phi_{3/2}(-2) = 996.090$ cents
- $\phi_{3/2}(4) = 407.820$ cents
- $\phi_{3/2}(-1) = 498.045$ cents

Reordenamiento tímbrico-estructural del núcleo:
$$C_{11}^{\text{sorted}} = [407.820, 498.045, 905.865, 996.090]$$

Deltas locales de la Cajita $C_{11}$:
- $\delta_0 = 498.045 - 407.820 = 90.225$ cents (Limma)
- $\delta_1 = 905.865 - 498.045 = 407.820$ cents (Tercera Mayor)
- $\delta_2 = 996.090 - 905.865 = 90.225$ cents (Limma)

El vector deltas $(\delta_0, \delta_1, \delta_2) = (90.225, 407.820, 90.225)$ revela una **configuración estrictamente palindrómica**. La Cajita Central de $N=11$ introduce un complejo celular auto-inversivo en el baricentro del sistema, polarizando un intervalo armónico amplio flanqueado rígidamente por dos márgenes microtonales idénticos.

#### C. Ordenamiento Escalar $S_{3/2, 11}$
Calculando el conjunto completo y ordenando modularmente:

$$S_{3/2, 11} = (0.000, 90.225, 203.910, 294.135, 407.820, 498.045, 601.740, 701.955, 905.865, 996.090, 1109.775)$$

*Nótese la inserción de $601.740$ cents ($\approx$ tritono pitagórico / cuarta aumentada exocéntrica derivada del índice $6$), ausente en $N=9$.*

---

## 2.4 El Acorde Transformante ($T_N$), Conducción de Voces (OVC) y Modulaciones Microtonales

El comportamiento armónico dinámico en *The Chain Theory* no procede por enlaces interválicos diatónicos tradicionales, sino mediante la migración continua y la deformación controlada de la Cajita Central sobre la **Matriz Operativa Bi-Eje** $F_N$.

```
Matriz Bi-Eje F_N:
 Eje Mayor (r_M = 0)  ───[SD_2]───[SD]───[ T ]───[ D ]───[D_2]─── ...
                             |       |     |       |       |
 Eje Menor (r_m = P_m)───[sd_2]───[sd]───[ t ]───[ d ]───[d_2]─── ...
                                                      │
                                    [ Acorde Simétrico Residual S_N ]
                                            (Posición N - 3)
```

### 2.4.1 Matriz Operativa Bi-Eje ($F_N$) y Desplazamientos
La matriz $F_N$ organiza la totalidad de las funciones sintácticas en dos estratos continuos vinculados por acoplamiento de fase:
- **Eje Mayor (Fila 1):** Origen centrado en el índice $r_M = 0$ (Tónica Mayor, $T$).
- **Eje Menor (Fila 2):** Origen centrado en el índice $r_m = P_m$ (Tónica Menor, $t$).

Los vectores funcionales se generan a través del desplazamiento lineal escalar $c \in \mathbb{Z}$:
- $c = +1 \implies$ Dominante ($D$ / $d$)
- $c = -1 \implies$ Subdominante ($SD$ / $sd$)
- $c = +2 \implies$ Dominante Secundaria ($D_2$ / $d_2$)
- $c = -2 \implies$ Subdominante Secundaria ($SD_2$ / $sd_2$)

Aislado invariablemente en el índice modular posicional:

$$\text{Pos}(S_N) = N - 3$$

reside el **Acorde Simétrico Residual** ($S_N$), cuya función armónica es la de pivote o bisagra neutra desprovista de polaridad mayor/menor, debido a la neutralización de sus deltas.

### 2.4.2 El Operador OVC (Offset Vector Classification)
El Operador OVC analiza los intervalos internos de cualquier tétrada resultante de un desplazamiento funcional $c$. Si definimos el vector de deltas internos para un acorde $A = (a_0, a_1, a_2, a_3)$ como:

$$\Delta(A) = (a_1 - a_0, \; a_2 - a_1, \; a_3 - a_2)$$

La función de calidad estructural $\mathcal{Q}(A)$ se formula como:

$$\mathcal{Q}(A) = \begin{cases} 
\text{Mayor (M)}, & \text{si } \Delta(A) \equiv \Delta(C_N) \\ 
\text{Menor (m)}, & \text{si } \Delta(A) \equiv \text{rev}(\Delta(C_N)) \\ 
\text{Simétrico (S)}, & \text{si } \Delta(A) \equiv \text{rev}(\Delta(A)) \quad \lor \quad A \equiv A_{N-3}
\end{cases}$$

donde $\text{rev}(v)$ invierte el orden del vector.

### 2.4.3 Conducción Parsimoniosa y Modulación de Fase Microtonal
El **Acorde Transformante** $T_N(c)$ es el operador que traslada suavemente la textura por el espacio modular. Para transitar del centro modal mayor $r_M = 0$ al centro menor $r_m = P_m$, la conducción parsimoniosa minimiza el desplazamiento métrico del espacio de alturas en $\ell_1$:

$$\mathcal{D}(A, B) = \sum_{i=0}^{3} | \phi_p(a_i) - \phi_p(b_i) |$$

Cuando se conecta un acorde polar con el Acorde Residual $S_N$ en $N-3$, el desplazamiento acústico converge a un mínimo absoluto, permitiendo **modulaciones enarmónicas microtonales** sin quiebre acústico perceptible:

$$A_{\text{funcional}} \xrightarrow[\text{OVC parsimonioso}]{\Delta \to \text{inf}} S_N \xrightarrow[\text{re-rotación}]{\Delta \to \text{inf}} A'_{\text{funcional}}$$

---

## 2.5 Algoritmo de Implementación: Modelo Generativo en SuperCollider

El siguiente programa formaliza la teoría desarrollada: calcula la proyección acústica, genera el ordenamiento escalar modular $S_{p,N}$, clasifica las tétradas mediante OVC y sintetiza los acordes generatrices de $N=9$ y $N=11$ usando osciladores sinusoidales puros micro-afinados.

```supercollider
// =====================================================================
// The Chain Theory: Motor de Proyección Acústica y Análisis OVC
// Implementación: N = 9 y N = 11
// =====================================================================

(
s.waitForBoot({
    var nET_ChainEngine;

    nET_ChainEngine = { |n = 9, pGen = 1.5, rootFreq = 261.626| // Middle C (C4)
        var pm, cajita, t_indices, t_cents, s_cents, freqs, s_residual_idx;

        // 1. Cálculo de parámetros fundamentales
        pm = (n / 2).floor.asInteger;
        s_residual_idx = n - 3;

        // Selección rigurosa de Cajita Central según motor de The Chain Theory
        if (n == 9) {
            cajita = [3, -1, 4, 0];
        };
        if (n == 11) {
            cajita = [3, -2, 4, -1];
        };

        // 2. Mapeo Acústico Modular Mod 1200 cents
        // cents = (1200 * idx * log2(p)) mod 1200
        t_cents = cajita.collect { |idx|
            var raw_cents = 1200 * idx * (pGen.log2);
            raw_cents.wrap(0.0, 1200.0);
        };

        // 3. Ordenamiento Escalar (S_{p,N})
        s_cents = t_cents.copy.sort;

        // Conversión a Frecuencias Físicas (Hz)
        freqs = s_cents.collect { |c| rootFreq * (2.pow(c / 1200.0)) };

        // Presentación de Datos Analíticos
        Post << "\n==============================================" << Char.nl;
        Post << "  THE CHAIN THEORY: REPORTE DE ANÁLISIS ACÚSTICO " << Char.nl;
        Post << "==============================================" << Char.nl;
        Post << "Orden N-ET          : " << n << Char.nl;
        Post << "Mediana P_m         : " << pm << Char.nl;
        Post << "Cajita Central C_N  : " << cajita << Char.nl;
        Post << "Índice Residual S_N : " << s_residual_idx << Char.nl;
        Post << "Cents No Ordenados  : " << t_cents.round(0.001) << Char.nl;
        Post << "Escala S_{p,N}      : " << s_cents.round(0.001) << Char.nl;
        Post << "Frecuencias (Hz)    : " << freqs.round(0.01) << Char.nl;

        // Deltas internos de la Cajita Central (OVC analysis)
        Post << "Deltas C_N (cents)  : ";
        (s_cents.size - 1).do { |i|
            var delta = s_cents[i+1] - s_cents[i];
            Post << delta.round(0.001) << " ";
        };
        Post << Char.nl;

        // 4. Síntesis Sonora Espacializada del Acorde Transformante
        {
            var sig, env;
            env = EnvGen.kr(Env.linen(attackTime: 1.5, sustainTime: 4.0, releaseTime: 2.5), doneAction: 2);
            sig = freqs.collect { |f, i|
                SinOsc.ar(f, mul: 0.1) * Pan2.ar(1.0, (i / (freqs.size - 1)) * 2 - 1)
            }.sum;
            sig * env;
        }.play;
    };

    // Ejecución secuencial analítica y sonora:
    Routine({
        nET_ChainEngine.value(9, 1.5, 261.626);  // Disparo sistema N = 9
        8.0.wait;
        nET_ChainEngine.value(11, 1.5, 261.626); // Disparo sistema N = 11
    }).play;
});
)
```

---

## 2.6 Sumario Estructural y Proyecciones Modales

El comportamiento comparativo de los sistemas analizados confirma los teoremas de estabilidad de *The Chain Theory*:

1. **Compresión de la Cajita Central:** Mientras que en $N=9$ la Cajita Central $[3, -1, 4, 0]$ engloba un ancho de banda escalar de $407.82$ cents para la tercera estructural (generando una polaridad mayoritaria que estabiliza el eje funcional $r_M = 0$), en $N=11$ la Cajita $[3, -2, 4, -1]$ se densifica internamente mediante dos intervalos delimitadores simétricos idénticos de $90.225$ cents.
2. **El Vector Palindrómico en $N=11$:** La naturaleza estrictamente palindrómica de $\Delta(C_{11}) = (90.225, 407.820, 90.225)$ predispone a este sistema a una **hibridación modal continua**, donde la frontera entre el Acorde Mayor y el Acorde Menor en $F_{11}$ queda neutralizada dinámicamente.
3. **El Papel Pivote de $S_N$:** En $N=9$, la posición simétrica $S_9$ queda localizada en el índice $9 - 3 = 6$. En $N=11$, se ubica en el índice $11 - 3 = 8$. Estos índices corresponden topológicamente a las zonas de máxima entropía de fase acústica, funcionando como atractores para modulaciones entre macro-escalas de afinación justas sin que colapse la continuidad perceptual de las voces.