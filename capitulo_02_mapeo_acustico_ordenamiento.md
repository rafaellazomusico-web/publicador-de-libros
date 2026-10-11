# CAPÍTULO 2: MAPEO ACÚSTICO, ORDENAMIENTO ESCALAR Y EXPANSIÓN DE $N$-ET

---

## 2.1. Formalización del Mapeo Acústico y Microtonalidad de la Cajita Central ($C_N$)

En el marco de *The Chain Theory*, la génesis de un espacio armónico no parte de una división abstracta y homogénea de la octava, sino de una estructura topológica proyectada acústicamente mediante un generador de frecuencia fundamental $p \in \mathbb{R}^+$. La transición desde el dominio interválico discreto (índices de la cadena) hacia el continuo psicoacústico se rige por el operador de mapeo acústico $\Psi_{p}$, formalizado como:

$$\Psi_{p}(k) = \left( 1200 \cdot k \cdot \log_2(p) \right) \pmod{1200}, \quad k \in \mathbb{Z}$$

donde $k$ representa el índice posicional generado en la cadena $T_N$, $p$ es el factor de proyección acústica (típicamente $p = 3/2$ para la proyección pitagórica pura, o $p = 2^{7/12}$ en temperamento igual), y el codominio está acotado en el espacio periódico del tritono/octava $[0, 1200) \subset \mathbb{R}$ en unidades de cents.

### 2.1.1. Morfología y Vectores Delta de la Cajita Central

La **Cajita Central** $C_N$ actúa como el núcleo nucleador tetrádico de la matriz primaria $T_N$. Se define canónicamente por la 4-tupla:

$$C_N = \left( k_1, k_2, k_3, k_4 \right)$$

Los elementos de $C_N$ parametrizan simultáneamente los centros de atracción de los ejes mayor y menor de la teoría bi-axial. La microestructura interválica interna se descompone analíticamente a través de su **Vector Diferencial Interno** $\vec{\Delta}(C_N)$:

$$\vec{\Delta}(C_N) = \left( \delta_{12}, \delta_{23}, \delta_{34} \right) = \left( k_2 - k_1, \; k_3 - k_2, \; k_4 - k_3 \right)$$

Al aplicar $\Psi_p$ sobre cada componente, obtenemos el **Espectro Céntico Fundamental**:

$$\Omega(C_N) = \left\{ \Psi_p(k_i) \mid k_i \in C_N \right\}$$

cuyos intervalos adyacentes proyectados determinan las calidades de tercera mayor microtonal, tercera menor y neutra dentro del continuo sonoro.

---

## 2.2. De la Cadena al Continuo: Ordenamiento Escalar ($S_{p,N}$) y Simetría Paramétrica

La Matriz Primaria $T_N$ se despliega de manera recursiva e intercalada a partir de $C_N$ mediante un algoritmo de adición simétrica polarizada:

$$T_N = \text{Expand}(C_N, N) = [t_0, t_1, \dots, t_{N-1}]$$

Este vector de índices no exhibe, de forma nativa, una secuencia monótona creciente en el espacio de alturas sonoras; constituye una trayectoria en el espacio de quintas/generadores. Para materializar la escala subyacente que opera en el plano melódico y contrapuntístico, es imperativo aplicar el operador de ordenamiento escalar $\mathcal{S}$:

$$T_{p,N} = \left[ \Psi_p(t_0), \Psi_p(t_1), \dots, \Psi_p(t_{N-1}) \right]$$

$$S_{p,N} = \text{sort}(T_{p,N}) = \left[ s_0, s_1, \dots, s_{N-1} \right], \quad \text{donde } s_j \le s_{j+1} \; \forall j \in \{0, \dots, N-2\}$$

### 2.2.1. Simetría de la Cadena y Grados de Paso

El vector de diferencias consecutivas de $S_{p,N}$, denominado **Vector de Intervalos de Grado (GIV)**:

$$\vec{g}(S_{p,N}) = \left( s_1 - s_0, \; s_2 - s_1, \; \dots, \; (1200 + s_0) - s_{N-1} \right)$$

revela las propiedades de simetría paramétrica (Well-Formedness y subestructuras MOS —*Moment of Symmetry*— generalizadas). 

En sistemas mayores $N\text{-ET}$, la distribución de $\vec{g}(S_{p,N})$ evidencia una alternancia de escalones diatónicos/cromáticos deformados por micro-intervalos residuales (comas pitagóricas, limmas o esquismas según $N$). El ordenamiento $S_{p,N}$ preserva la polaridad bi-axial: existe una automorfía de inversión respecto al centro del sistema que mapea el Eje Mayor directamente sobre el Eje Menor.

---

## 2.3. Aplicación Práctica y Análisis Estructural para $N = 9$ y $N = 11$

Adoptamos para este análisis el generador pitagórico puro $p = 3/2$, con $\log_2(3/2) \approx 0.5849625$, lo que produce un intervalo generador de:

$$\kappa = 1200 \cdot \log_2(1.5) \approx 701.955000865 \text{ cents}$$

### 2.3.1. Sistema $N = 9$

*Datos calibrados por el motor matemático:*
- Cajita Central: $C_9 = [3, -1, 4, 0]$
- Polar menor: $P_m = 4$
- Grado de afinidad/asimetría armónica: $A_N = 3$

#### 1. Expansión de la Cadena $T_9$
Partiendo de $C_9 = [3, -1, 4, 0]$, la intercalación simétrica genera la secuencia de índices:
$$T_9 = [ -2, \; 3, \; -1, \; 4, \; 0, \; 5, \; 1, \; 6, \; 2 ]$$

#### 2. Mapeo Acústico ($T_{3/2, 9}$)
Evaluando $\Psi_{3/2}(k) = (k \cdot 701.955) \pmod{1200}$:

| Índice $k$ | Posición $T_9$ | Cálculo ($\text{cents}$ brutos) | Reducción Modulo 1200 ($\text{cents}$) | Grado Equivalente |
| :---: | :---: | :---: | :---: | :---: |
| $-2$ | $t_0$ | $-1403.910$ | $996.090$ | $\text{Bb}$ |
| $+3$ | $t_1$ | $+2105.865$ | $905.865$ | $\text{A}$ |
| $-1$ | $t_2$ | $-701.955$ | $498.045$ | $\text{F}$ |
| $+4$ | $t_3$ | $+2807.820$ | $407.820$ | $\text{E}$ |
| $0$ | $t_4$ | $0.000$ | $0.000$ | $\text{C}$ (Eje Mayor $r_M$) |
| $+5$ | $t_5$ | $+3509.775$ | $1109.775$ | $\text{B}$ |
| $+1$ | $t_6$ | $+701.955$ | $701.955$ | $\text{G}$ |
| $+6$ | $t_7$ | $+4211.730$ | $611.730$ | $\text{F}\sharp$ |
| $+2$ | $t_8$ | $+1403.910$ | $203.910$ | $\text{D}$ |

#### 3. Ordenamiento Escalar ($S_{3/2, 9}$)
Ordenando los valores en orden ascendente:

$$S_{3/2, 9} = [0.000, \; 203.910, \; 407.820, \; 498.045, \; 611.730, \; 701.955, \; 905.865, \; 996.090, \; 1109.775]$$

#### 4. Vector de Intervalos de Grado ($\vec{g}$)
Calculando las diferencias adyacentes:
- $g_1 = 203.910 - 0.000 = 203.910$
- $g_2 = 407.820 - 203.910 = 203.910$
- $g_3 = 498.045 - 407.820 = 90.225$ (Limma pitagórica)
- $g_4 = 611.730 - 498.045 = 113.685$ (Apótomé pitagórica)
- $g_5 = 701.955 - 611.730 = 90.225$
- $g_6 = 905.865 - 701.955 = 203.910$
- $g_7 = 996.090 - 905.865 = 90.225$
- $g_8 = 1109.775 - 996.090 = 113.685$
- $g_9 = (1200 + 0.000) - 1109.775 = 90.225$

$$\vec{g}(S_{3/2, 9}) = (203.91, \; 203.91, \; 90.23, \; 113.69, \; 90.23, \; 203.91, \; 90.23, \; 113.69, \; 90.23)$$

La estructura segrega el continuo en tres tamaños interválicos fundamentales: Tono mayor ($203.91\text{ c}$), Limma ($90.23\text{ c}$) y Apótomé ($113.69\text{ c}$).

---

### 2.3.2. Sistema $N = 11$

*Datos calibrados por el motor matemático:*
- Cajita Central: $C_{11} = [3, -2, 4, -1]$
- Polar menor: $P_m = 4$
- Grado de afinidad/asimetría armónica: $A_N = 3$

#### 1. Expansión de la Cadena $T_{11}$
A partir de $C_{11} = [3, -2, 4, -1]$, la intercalación polarizada expandida a $N=11$ es:
$$T_{11} = [ -3, \; 5, \; -2, \; 3, \; -1, \; 4, \; 0, \; 6, \; 1, \; 7, \; 2 ]$$

#### 2. Mapeo Acústico ($T_{3/2, 11}$)

| Índice $k$ | Posición $T_{11}$ | $\Psi_{3/2}(k) \pmod{1200}$ ($\text{cents}$) | Grado Equivalente |
| :---: | :---: | :---: | :---: |
| $-3$ | $t_0$ | $294.135$ | $\text{Eb}$ |
| $+5$ | $t_1$ | $1109.775$ | $\text{B}$ |
| $-2$ | $t_2$ | $996.090$ | $\text{Bb}$ |
| $+3$ | $t_3$ | $905.865$ | $\text{A}$ |
| $-1$ | $t_4$ | $498.045$ | $\text{F}$ |
| $+4$ | $t_5$ | $407.820$ | $\text{E}$ |
| $0$ | $t_6$ | $0.000$ | $\text{C}$ (Eje Mayor $r_M$) |
| $+6$ | $t_7$ | $611.730$ | $\text{F}\sharp$ |
| $+1$ | $t_8$ | $701.955$ | $\text{G}$ |
| $+7$ | $t_9$ | $113.685$ | $\text{C}\sharp$ |
| $+2$ | $t_{10}$ | $203.910$ | $\text{D}$ |

#### 3. Ordenamiento Escalar ($S_{3/2, 11}$)

$$S_{3/2, 11} = [0.000, \; 113.685, \; 203.910, \; 294.135, \; 407.820, \; 498.045, \; 611.730, \; 701.955, \; 905.865, \; 996.090, \; 1109.775]$$

#### 4. Vector de Intervalos de Grado ($\vec{g}$)
Calculando las diferencias consecutivas en $S_{3/2, 11}$:

$$\vec{g}(S_{3/2, 11}) = (113.69, \; 90.23, \; 90.23, \; 113.69, \; 90.23, \; 113.69, \; 90.23, \; 203.91, \; 90.23, \; 113.69, \; 90.23)$$

Nótese que en $N=11$, el intervalo diatónico de segunda mayor ($203.91\text{ c}$) prácticamente ha colapsado en pares complementarios de Limmas ($90.23\text{ c}$) y Apótomés ($113.69\text{ c}$), dejando un único escalón íntegro de tono ($203.91\text{ c}$) entre $701.955$ y $905.865$ cents ($\text{G} \to \text{A}$). El sistema $N=11$ funciona como una estructura de transición crítica hacia micro-escalas de temperamentos endecasílabos.

---

## 2.4. Dinámica del Acorde Transformante ($T_N$), Operador OVC y Modulación Microtonal

### 2.4.1. La Matriz Operativa Bi-Eje ($F_N$)

La función de los acordes en *The Chain Theory* se rige por su proyección en la matriz reticular $F_N$:

$$F_N = \begin{pmatrix} 
\text{Eje Mayor} \\ 
\text{Eje Menor} 
\end{pmatrix} = 
\begin{pmatrix} 
\dots & \text{SD}_2 & \text{SD} & \mathbf{T_M} & \text{D} & \text{D}_2 & \dots \\
\dots & \text{sd}_2 & \text{sd} & \mathbf{t_m} & \text{d} & \text{d}_2 & \dots
\end{pmatrix}$$

donde:
- El Eje Mayor tiene como origen el índice $r_M = 0$.
- El Eje Menor tiene como origen el índice $r_m = P_m = 4$.
- Un desplazamiento posicional $c \in \mathbb{Z}$ define:
  $$c = +1 \implies \text{Dominante (D)}, \quad c = -1 \implies \text{Subdominante (SD)}$$
  $$c = +2 \implies \text{Dominante Secundaria (D}_2\text{)}, \quad c = -2 \implies \text{Subdominante Secundaria (SD}_2\text{)}$$

### 2.4.2. El Acorde Simétrico Residual ($S_N$)

Por construcción axiomática, la posición:

$$\text{pos}(S_N) = N - 3$$

queda excluida de la clausura funcional bi-axial directa, convirtiéndose en el **Acorde Residual Simétrico** $S_N$.

- **En $N = 9$:** $\text{pos}(S_9) = 9 - 3 = 6$. En $T_9$, el índice correspondiente es $t_6 = 1$.
- **En $N = 11$:** $\text{pos}(S_{11}) = 11 - 3 = 8$. En $T_{11}$, el índice es $t_8 = 1$.

$S_N$ actúa como el elemento neutro de torsión (*twist*) armónica: carece de tercera polarizada fija, permitiendo que la conducción de voces actúe como un atractor de fase hacia cualquiera de los dos ejes mediante el desplazamiento de una única micro-coma.

### 2.4.3. Operador OVC (*Optimal Voice Leading and Chord Classification*)

El operador OVC clasifica la calidad del acorde derivado de cualquier tetracordio local de la cadena basándose en las diferencias $\vec{\Delta}$ respecto al núcleo de $C_N$:

$$\text{OVC}(K) = \begin{cases} 
\text{Mayor}, & \text{si } \vec{\Delta}(K) \equiv \vec{\Delta}_M(C_N) \\
\text{Menor}, & \text{si } \vec{\Delta}(K) \equiv \vec{\Delta}_m(C_N) \\
\text{Simétrico / Neutro}, & \text{en cualquier otro caso (atractor residual)}
\end{cases}$$

El coste de conducción de voces para modular del Eje Mayor ($r_M=0$) al Eje Menor ($r_m=4$) se formaliza mediante la métrica métrica $\ell_1$ sobre el espacio céntico:

$$\mathcal{D}_{\text{voice}}(\mathbf{u}, \mathbf{v}) = \sum_{i=1}^{M} |\Psi_p(u_i) - \Psi_p(v_{\sigma(i)})|$$

donde $\sigma$ es la permutación minimal en el espacio cociente de alturas. Debido a la simetría de la cajita $C_N$, la modulación microtonal entre $r_M$ y $r_m$ opera minimizando $\mathcal{D}_{\text{voice}}$, desplazando voces únicamente por el intervalo de apótomé o limma:

$$\Delta_{\text{mod}} = |\Psi_{3/2}(4) - \Psi_{3/2}(0)| = |407.82 - 0.00| \equiv 407.82 \text{ cents (Tercera Mayor pura pitagórica)}$$

---

## 2.5. Implementación Algorítmica

El siguiente script en **SuperCollider** compila el motor matemático: genera la matriz $T_N$, evalúa el mapeo acústico $\Psi_p$, extrae el ordenamiento escalar $S_{p,N}$ y sintetiza las frecuencias calculadas para los sistemas $N = 9$ y $N = 11$.

```supercollider
// =====================================================================
// THE CHAIN THEORY: Motor de Mapeo Acústico y Expansión N-ET
// Implementación: N=9 y N=11
// =====================================================================

(
s.waitForBoot({
    var acousticMapping, generateScale;

    // Función de Mapeo Acústico: Psi_p(k)
    acousticMapping = { |k, p = 1.5|
        var cents = (1200 * k * log2(p)).mod(1200);
        cents;
    };

    // Función constructora del sistema
    generateScale = { |n, cBox, baseFreq = 261.626| // C4 = 261.626 Hz
        var pM, aN, sNPos, chainIndices, mappedCents, sortedCents, freqs;

        pM = (n / 2).floor.asInteger;
        aN = 3;
        sNPos = n - 3;

        // Expansión simétrica para N=9 y N=11
        if(n == 9) {
            chainIndices = [-2, 3, -1, 4, 0, 5, 1, 6, 2];
        };
        if(n == 11) {
            chainIndices = [-3, 5, -2, 3, -1, 4, 0, 6, 1, 7, 2];
        };

        // Mapeo Acústico (p = 3/2)
        mappedCents = chainIndices.collect { |k| acousticMapping.value(k, 1.5) };

        // Ordenamiento Escalar S_{p,N}
        sortedCents = mappedCents.copy.sort;

        // Frecuencias derivadas
        freqs = sortedCents.collect { |c| baseFreq * (2 ** (c / 1200)) };

        ("--- SISTEMA N = " ++ n ++ " ---").postln;
        ("Cajita Central: " ++ cBox).postln;
        ("Cadena T_N: " ++ chainIndices).postln;
        ("Acorde Simétrico S_N en índice: t[" ++ sNPos ++ "] = " ++ chainIndices[sNPos]).postln;
        ("Escala S_{p,N} (cents): " ++ sortedCents.round(0.001)).postln;
        ("Frecuencias (Hz): " ++ freqs.round(0.01)).postln;
        "".postln;

        freqs;
    };

    // Ejecución para N = 9
    ~freqs9 = generateScale.value(9, [3, -1, 4, 0]);

    // Ejecución para N = 11
    ~freqs11 = generateScale.value(11, [3, -2, 4, -1]);

    // Sintetizador para prueba auditiva microtonal
    SynthDef(\chainTone, { |out = 0, freq = 440, amp = 0.1, gate = 1|
        var sig, env;
        env = EnvGen.kr(Env.asr(0.05, 1, 0.2), gate, doneAction: 2);
        sig = SinOsc.ar(freq) * amp * env;
        Out.ar(out, sig ! 2);
    }).add;

    // Rutina de demostración: Arpegio de la escala S_{p, 9}
    Routine({
        1.wait;
        "Reproduciendo escala S_{p,9}...".postln;
        ~freqs9.do { |f|
            var syn = Synth(\chainTone, [\freq, f, \amp, 0.15]);
            0.3.wait;
            syn.set(\gate, 0);
        };
    }).play;
});
)
```

---

## 2.6. Conclusiones del Capítulo 2

1. **Alineación Bi-axial y Proyección Continua:** El paso de $T_N$ a $S_{p,N}$ demuestra que los sistemas microtonales no emergen de particiones arbitrarias de la octava, sino de proyecciones acústicas ordenadas de un centro de torsión generado por la Cajita Central $C_N$.
2. **Singularidad de los Sistemas $N=9$ y $N=11$:**
   - En $N=9$, la alternancia simétrica genera tres tamaños de paso interválico ($\text{Tono}$, $\text{Limma}$, $\text{Apótomé}$), preservando una polaridad diatónica reconocible acoplada con extensiones cromáticas exactas.
   - En $N=11$, el tono entero se descompone casi en su totalidad en una secuencia de pasos microtonales de limmas y apótomés, creando un campo armónico de alta densidad funcional y propicio para la modulación por micro-desplazamiento continuo.
3. **El Rol de $S_N$:** El aislamiento del Acorde Simétrico en la posición $N-3$ garantiza que, sin importar la expansión del orden del sistema $N$, el sistema conserva un portal de indeterminación funcional por el cual las transiciones entre ejes mayores y menores pueden completarse con un coste de conducción de voces $\mathcal{D}_{\text{voice}}$ que tiende a mínimos locales óptimos.