# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 1. Fundamentación Acústica del Operador de Mapeo ($T_{p,N}$)

En el marco de la *Chain Theory*, el espacio pitch-class no se concibe como una partición abstracta y homogénea *a priori*, sino como la proyección sobre el continuo frecuencial de un conjunto finito de índices generados por la Matriz Primaria ($T_N$). Para vincular la combinatoria estructural de la cadena con el dominio psicoacústico y físico de los intervalos, se define el **Operador de Mapeo Acústico** $\Phi_p$.

Sea $x \in \mathbb{Z}$ un índice posicional perteneciente a la cadena de afinación y sea $p \in \mathbb{R}^+$ un generador interválico fundamental expresado como razón de frecuencia (frecuentemente $p = 3/2$ para proyecciones de quinta justa, o ratios microtonales primos $p \in \{5/4, 7/4, 11/8\}$). La función de mapeo al espacio logarítmico modular de cents $\mathbb{R} / 1200\mathbb{Z}$ se formula:

$$\Phi_p(x) = \left( 1200 \cdot x \cdot \log_2(p) \right) \pmod{1200}$$

Dado un vector de índices discretos de una cadena de longitud $N$, denominado $I_N = \{x_0, x_1, \dots, x_{N-1}\}$, el conjunto de alturas proyectadas en cents constituye el vector acústico no ordenado $T_{p,N}$:

$$T_{p,N} = \Phi_p(I_N) = \{ \Phi_p(x) \mid x \in I_N \}$$

### 1.1 Microtonalidad Derivada de la Cajita Central ($C_N$)

La génesis de todo el sistema de afinación reside en el núcleo armónico denominado **Cajita Central** ($C_N$), cuya disposición de índices determina la polaridad y simetría interválica de partida:

$$C_N = [k_1, k_2, k_3, k_4]$$

Al aplicar $\Phi_p$ sobre las componentes de $C_N$, obtenemos un cuadricorde fundamental en cents:

$$\Omega_p(C_N) = \left[ \Phi_p(k_1), \Phi_p(k_2), \Phi_p(k_3), \Phi_p(k_4) \right]$$

Las diferencias acústicas consecutivas definen el vector de deltas interválicos $\Delta C_N$:

$$\Delta_{i,j} = |\Phi_p(k_i) - \Phi_p(k_j)| \pmod{1200}$$

Estos deltas dictan el comportamiento del **Operador de Vector de Calidad (OVC)**. La tensión intrínseca de la Cajita Central no depende exclusivamente del temperamento igual estándar (12-EDO), sino de los desvíos fraccionarios (comas microtonales) que surgen cuando $\log_2(p) \notin \mathbb{Q}$. En arquitecturas $N$-ET más amplias, estos deltas parametrizan microintervalos críticos: diésis, comas sintónicas y cuartos de tono exactos generados por el solapamiento oclusivo de la cadena.

---

## 2. Ordenamiento Escalar ($S_{p,N}$) y Topología Microtonal

Mientras que la Matriz Primaria $T_N$ despliega los elementos según un principio de proximidad funcional generativa (expansión simétrica intercalada), el espacio de interpretación melódica y de conducción de voces requiere un espacio topológico monotónico creciente.

### 2.1 Monotonía y Operador de Ordenación

Se define el **Operador de Ordenamiento Escalar** $\mathcal{S}$ como una biyección que actúa sobre $T_{p,N}$ tal que:

$$S_{p,N} = \mathcal{S}(T_{p,N}) = \text{sort}(T_{p,N}) = (\lambda_0, \lambda_1, \lambda_2, \dots, \lambda_{N-1})$$

donde:

$$0 \le \lambda_0 < \lambda_1 < \lambda_2 < \dots < \lambda_{N-1} < 1200$$

### 2.2 Grados de Paso y Simetría de la Cadena

El conjunto ordenado $S_{p,N}$ conforma la escala microtonal efectiva de $N$ alturas dentro de la octava. La distancia entre grados contiguos define el espectro de pasos melódicos:

$$\sigma_k = \begin{cases} 
\lambda_{k+1} - \lambda_k & \text{para } 0 \le k < N-1 \\ 
(1200 + \lambda_0) - \lambda_{N-1} & \text{para } k = N-1 
\end{cases}$$

En los sistemas $N$-ET bien templados, el multiconjunto de pasos $\Sigma_N = \{\sigma_0, \sigma_1, \dots, \sigma_{N-1}\}$ exhibe la propiedad de Tres Pasos (teorema de los tres intervalos de Steinhaus) o se reduce estrictamente a dos pasos característicos ($L$ = Large, $s$ = small), demostrando que la expansión intercalada de la *Chain Theory* maximiza la regularidad distribucional (propiedad de *Well-formedness* y *Myhill's Property*).

---

## 3. Descomposición Estructural: Casos $N = 9$ y $N = 11$

A continuación, se analizan los datos de referencia provistos por el motor analítico formal, empleando un generador pitagórico/armónico $p = 3/2$, con $\log_2(3/2) \approx 0.5849625$, implicando un paso de quinta de $\approx 701.955$ cents.

---

### 3.1 Análisis Estructural para $N = 9$

**Parámetros:**
- Longitud del sistema: $N = 9$
- Eje polar menor: $P_m = 4$
- Grado de asíntota/asimetría: $A_N = 3$
- Cajita Central: $C_9 = [3, -1, 4, 0]$

```
                Cajita Central (N=9)
          [  3,   -1,    4,    0  ]
             |     |     |     |
Índice:     k1    k2    k3    k4
```

#### Paso 1: Mapeo Acústico de la Cajita Central ($p = 3/2$)
Aplicando $\Phi_{3/2}(x) = (1200 \cdot x \cdot \log_2(1.5)) \pmod{1200} = (x \cdot 701.955) \pmod{1200}$:

$$\begin{aligned}
\Phi(3)  &= (3 \cdot 701.955) \pmod{1200} = 2105.865 \pmod{1200} = 905.87 \text{ cents (La)} \\
\Phi(-1) &= (-1 \cdot 701.955) \pmod{1200} = -701.955 \equiv 498.04 \text{ cents (Fa)} \\
\Phi(4)  &= (4 \cdot 701.955) \pmod{1200} = 2807.820 \pmod{1200} = 407.82 \text{ cents (Mi)} \\
\Phi(0)  &= (0 \cdot 701.955) \pmod{1200} = 0.00 \text{ cents (Do)}
\end{aligned}$$

Vector Acústico de $C_9$:
$$\Omega_{3/2}(C_9) = [905.87, 498.04, 407.82, 0.00]$$

#### Paso 2: Evaluación OVC (Vector de Calidad)
Calculamos las distancias internas entre los nodos estructurales mayor y menor definidos en $C_9$:
- Base fundamental: $k_4 = 0$ ($0.00$ cents)
- Tercera/inversión: $k_3 = 4$ ($407.82$ cents $\approx$ Tercera Mayor Ditónica)
- Subdominante/Pivote: $k_2 = -1$ ($498.04$ cents $\approx$ Cuarta Justa)
- Extensión modal: $k_1 = 3$ ($905.87$ cents $\approx$ Sexta Mayor)

El par diferencial $(\Phi(4) - \Phi(0)) = 407.82$ cents revela una clara calidad **Mayor** hiper-afinada (excediendo el temperamento igual por $+7.82$ cents), mientras que el par $(\Phi(3) - \Phi(-1)) = 407.82$ cents establece una simetría paralela exacta de traslación generativa.

#### Paso 3: Expansión y Ordenamiento Escalar ($S_{3/2, 9}$)
La cadena completa de 9 tonos se expande simétricamente desde los índices de la cajita:
$$I_9 = \{-2, -1, 0, 1, 2, 3, 4, 5, 6\}$$
(centrada contextualmente con $A_N=3$ y $P_m=4$).

Calculando $T_{3/2, 9}$ y ordenando:

| Índice ($x$) | Pitch Acústico (cents) | Grado Escalar ($S_{3/2, 9}$) | Paso ($\sigma_k$) |
|:---:|:---:|:---:|:---:|
| 0 | 0.00 | $\lambda_0 = 0.00$ | 113.69 |
| 5 | 1109.78 | $\lambda_1 = 203.91$ | 90.22 |
| -2 | 996.09 | $\lambda_2 = 294.13$ | 113.69 |
| 3 | 905.87 | $\lambda_3 = 407.82$ | 90.22 |
| -1 | 498.04 | $\lambda_4 = 498.04$ | 203.91 |
| 4 | 407.82 | $\lambda_5 = 701.96$ | 113.69 |
| 1 | 701.96 | $\lambda_6 = 905.87$ | 90.22 |
| 6 | 611.73 | $\lambda_7 = 996.09$ | 113.69 |
| 2 | 203.91 | $\lambda_8 = 1109.78$ | 90.22 |

El sistema produce una escala asimétrica de 9 alturas caracterizada por pasos elementales de Limma ($\approx 90.22$ cents), Apotome/Semitono Mayor ($\approx 113.69$ cents) y una discontinuidad de paso doble ($\approx 203.91$ cents) que actúa como la "brecha residual" del sistema $N=9$.

---

### 3.2 Análisis Estructural para $N = 11$

**Parámetros:**
- Longitud del sistema: $N = 11$
- Eje polar menor: $P_m = 4$
- Grado de asíntota/asimetría: $A_N = 3$
- Cajita Central: $C_{11} = [3, -2, 4, -1]$

```
               Cajita Central (N=11)
          [  3,   -2,    4,   -1  ]
             |     |     |     |
Índice:     k1    k2    k3    k4
```

#### Paso 1: Mapeo Acústico de la Cajita Central ($p = 3/2$)
Aplicamos la transformación $\Phi_{3/2}$ a los nuevos límites:

$$\begin{aligned}
\Phi(3)  &= 905.87 \text{ cents} \\
\Phi(-2) &= (-2 \cdot 701.955) \pmod{1200} = -1403.91 \equiv 996.09 \text{ cents (Sib)} \\
\Phi(4)  &= 407.82 \text{ cents} \\
\Phi(-1) &= 498.04 \text{ cents}
\end{aligned}$$

Vector Acústico de $C_{11}$:
$$\Omega_{3/2}(C_{11}) = [905.87, 996.09, 407.82, 498.04]$$

#### Paso 2: Análisis de Diferenciales Microtonales (OVC)
Nótese el cambio radical en la distribución morfológica respecto a $N=9$:
- $\Delta(k_2, k_4) = |\Phi(-2) - \Phi(-1)| = |996.09 - 498.04| = 498.05$ cents (Intervalo de Cuarta Justa invariante).
- $\Delta(k_1, k_3) = |\Phi(3) - \Phi(4)| = |905.87 - 407.82| = 498.05$ cents.
- El acoplamiento cruzado:
  $$|\Phi(4) - \Phi(-1)| = |407.82 - 498.04| = 90.22 \text{ cents (Limma Pitagórico, } \approx \text{semitono diatónico)}$$
  $$|\Phi(-2) - \Phi(3)| = |996.09 - 905.87| = 90.22 \text{ cents}$$

El Operador OVC detecta aquí una estructura **Simétrica Residual de Doble Eje**, donde la Cajita Central comprime dos diadas separadas exactamente por una cuarta justa ($498.05$ cents), interconectadas melódicamente por micro-intervalos de $90.22$ cents. La asimetría $A_N = 3$ compensa la desviación polar estabilizando el centro armónico sobre el eje menor ($P_m = 4$).

#### Paso 3: Densidad Cromática y Ordenamiento ($S_{3/2, 11}$)
Añadiendo dos nodos a la cadena de proyección:
$$I_{11} = \{-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7\}$$

La ordenación monotónica $S_{3/2, 11}$ produce la siguiente partición:

$$\begin{aligned}
S_{3/2, 11} = (&0.00, 113.69, 203.91, 317.60, 407.82, 498.04, \\
               &611.73, 701.96, 815.64, 905.87, 1019.56)
\end{aligned}$$

El paso de $203.91$ cents presente en $N=9$ se ha subdividido microtonalmente mediante la introducción de la altura $317.60$ cents (índice $-3$), resolviendo la brecha escalar:

$$317.60 - 203.91 = 113.69 \text{ cents}$$
$$407.82 - 317.60 = 90.22 \text{ cents}$$

La escala resultante en $N=11$ es estrictamente binaria en cuanto a sus pasos melódicos: está compuesta exclusivamente por $\sigma \in \{90.22, 113.69\}$ cents (a excepción del cierre residual del marco generativo), validando la estabilidad estructural del sistema.

---

## 4. El Acorde Transformante ($T_N$), Conducción de Voces y Modulaciones Microtonales

El comportamiento dinámico de la *Chain Theory* se articula mediante el **Acorde Transformante** $T_N$, el cual opera en el vértice de transición entre los ejes de la **Matriz Operativa Bi-Eje ($F_N$)**.

### 4.1 La Matriz Operativa Bi-Eje ($F_N$)

Recordando la estructura formal de $F_N$:
- **Fila 1 (Eje Mayor):** Centrado en $r_M = 0$ (Tónica Mayor $T$).
- **Fila 2 (Eje Menor):** Centrado en $r_m = P_m$ (Tónica Menor $T$).
- **Desplazamiento horizontal ($c$):**
  - $c = +1 \implies \text{Dominante } (D)$
  - $c = -1 \implies \text{Subdominante } (SD)$
  - $c = +2 \implies \text{Dominante Secundaria } (D_2)$
  - $c = -2 \implies \text{Subdominante Secundaria } (SD_2)$
- **Posición $N-3$:** Aloja el **Acorde Simétrico Residual** ($S_N$).

Para $N=9$ ($P_m = 4$):
- Eje Mayor: $r_M = 0$
- Eje Menor: $r_m = 4$
- Acorde Simétrico Residual: Columna indexada en $N - 3 = 6$.

Para $N=11$ ($P_m = 4$):
- Eje Mayor: $r_M = 0$
- Eje Menor: $r_m = 4$
- Acorde Simétrico Residual: Columna en $N - 3 = 8$.

```
Matriz Operativa Bi-Eje (Esquema conceptual):
            SD_2   SD     T      D     D_2        S_N (Residuo)
Eje Mayor: [ -2 ][ -1 ][  0  ][ +1 ][ +2 ] ... [ N - 3 ]
Eje Menor: [Pm-2][Pm-1][ Pm  ][Pm+1][Pm+2] ... [ N - 3 ]
```

### 4.2 Mecánica de Conducción Parsimoniosa de Voces (Voice Leading)

El Acorde Transformante $T_N$ se define como el operador de reconfiguración interválica mínima que mapea un acorde del Eje Mayor en su correspondiente simétrico sobre el Eje Menor, o transmuta la polaridad funcional mediante traslaciones parsimoniosas. 

Sean dos acordes $\mathbf{u}, \mathbf{v} \in \mathbb{R}^4$ expresados en cents. La métrica de distorsión o desplazamiento por conducción de voces $\mathcal{D}(\mathbf{u}, \mathbf{v})$ se define mediante la norma $\ell_1$:

$$\mathcal{D}(\mathbf{u}, \mathbf{v}) = \sum_{i=1}^{4} |\mathbf{u}_i - \mathbf{v}_{\pi(i)}|$$

donde $\pi$ es la permutación de asignación de voces que minimiza la suma.

Dado que en $N=11$ la diferencia entre los polos fundamentales (por ejemplo, entre el centro menor $P_m = 4$ y el grado adyacente en la cajita) es de un Limma ($90.22$ cents), el Acorde Transformante permite modulaciones microtonales fluidas:

$$T_{11}: \Omega(C_{11}) \longrightarrow \Omega(C_{11}) + \mathbf{\delta}$$

donde $\mathbf{\delta} = [0, 90.22, 0, -90.22]$ cents.

Esta operación preserva dos alturas pivote (invarianza de enlace armónico) mientras desplaza las dos voces restantes en direcciones contrarias por un micro-semitono pitagórico, generando una modulación parsimoniosa que traslada el centro gravitacional del Eje Mayor ($r_M = 0$) al Eje Menor ($r_m = 4$) sin ruptura acústica perceptual.

### 4.3 Modulaciones por Desplazamiento Vectorial ($c$)

Cuando el sistema ejecuta una modulación funcional mediada por un desplazamiento de columna $c \in \{\pm 1, \pm 2\}$:

1. **Modulación Dominante ($c = +1$):**
   Todos los índices de la cajita se incrementan en una unidad generativa ($\Delta x = +1$). En el plano acústico, esto equivale a una transposición exacta de $+701.955$ cents. En el espacio modificado de la escala $S_{p,N}$, la jerarquía de los pasos $\sigma_k$ rota cíclicamente.
2. **Modulación al Acorde Simétrico Residual ($S_N$ en $N-3$):**
   Al alcanzar la posición $N-3$, el acorde resultante pierde la diferenciación binaria de tercera mayor/menor evaluada por el operador OVC. Su interválica interna colapsa en una estructura simétrica cuasi-disminuida o de cuartas aumentadas, actuando como un agujero negro armónico ("hub" de dispersión microtonal). Desde $S_N$, el compositor algorítmico puede re-orientar el vector de polaridad $P_m$ hacia un nuevo sistema $N$-ET superpuesto.

---

## 5. Implementación Algorítmica

El siguiente script en SuperCollider modela de forma determinista la generación del espacio escalar $S_{p,N}$, el cálculo de la Cajita Central y el motor de síntesis microtonal para los casos $N=9$ y $N=11$.

```supercollider
// =====================================================================
// The Chain Theory: Generador de Afinaciones N-ET y Matriz Acústica
// Capítulo 2: Mapeo y Ordenamiento Escalar
// =====================================================================

(
var calcChain = { |n, pm, cBox, pRatio = 1.5|
    var generatorCents, rawCents, sortedScale, intervals;
    
    // Cálculo del paso angular del generador en cents
    generatorCents = 1200 * log2(pRatio);
    
    // Mapeo Acústico de la Cajita Central (Phi_p)
    "--- ANÁLISIS DE CAJITA CENTRAL N=% ---".format(n).postln;
    cBox.do { |idx, i|
        var cVal = (idx * generatorCents) % 1200;
        if(cVal < 0) { cVal = cVal + 1200 };
        "Nodo k%: Índice = %, Cents = %".format(i+1, idx, cVal.round(0.001)).postln;
    };
    
    // Generación de la Cadena Expandida (Indices simétricos)
    // Para modelado computacional, tomamos la ventana centrada de tamaño N
    rawCents = Array.fill(n, { |i|
        var idx = i - floor(n / 2); // Dispersión centrada
        var cents = (idx * generatorCents) % 1200;
        if(cents < 0) { cents = cents + 1200 };
        cents;
    });
    
    // Ordenamiento Escalar S_{p, N}
    sortedScale = rawCents.copy.sort;
    
    // Cálculo de pasos (sigma_k)
    intervals = Array.fill(n, { |i|
        if(i < (n - 1)) {
            sortedScale[i+1] - sortedScale[i];
        } {
            (1200 + sortedScale[0]) - sortedScale[i];
        };
    });
    
    "\n--- ESCALA ORDENADA S_{p, %} ---".format(n).postln;
    sortedScale.do { |cents, i|
        "Grado %: % cents (Delta = % cents)".format(
            i, cents.round(0.01), intervals[i].round(0.01)
        ).postln;
    };
    
    sortedScale;
};

// 1. Ejecutar análisis para N = 9
~scale9 = calcChain.value(9, 4, [3, -1, 4, 0], 1.5);

// 2. Ejecutar análisis para N = 11
~scale11 = calcChain.value(11, 4, [3, -2, 4, -1], 1.5);
)

// Síntesis auditiva de la escala ordenada N=11 (Cluster Microtonal de Paso)
(
SynthDef(\chainTone, { |out = 0, freq = 440, amp = 0.1, gate = 1|
    var env = EnvGen.kr(Env.asr(0.05, 1, 0.2), gate, doneAction: 2);
    var sig = SinOsc.ar(freq) * env * amp;
    Out.ar(out, sig ! 2);
}).add;
)

// Reproducción en arpegio de la escala S_{3/2, 11} tomando Base = 261.63 Hz (Do central)
(
Routine({
    var baseFreq = 261.63;
    ~scale11.do { |cents|
        var freq = baseFreq * (2 ** (cents / 1200));
        var synth = Synth(\chainTone, [\freq, freq, \amp, 0.15]);
        0.25.wait;
        synth.set(\gate, 0);
    };
}).play;
)
```

---

## 6. Conclusiones Estructurales

1. **Invarianza Funcional:** La Cajita Central $C_N$ actúa como el genotipo interválico del sistema. Las transformaciones de $N=9$ a $N=11$ demuestran cómo la adición de grados en los extremos de la cadena absorbe las brechas disonantes grandes ($\approx 204$ cents en $N=9$), colapsándolas en micro-pasos simétricos de Limma ($90.22$ cents) y Apotome ($113.69$ cents).
2. **Puente Transicional ($T_N$):** Las modulaciones microtonales en la *Chain Theory* están gobernadas por el vector de diferencia dentro de $F_N$. El desplazamiento armónico no requiere saltos abruptos de centro acústico, sino reconfiguraciones oblicuas locales donde la conducción de voces se optimiza mediante desplazamientos mínimos inferiores a un semitono temperado común.
3. **El Residuo Simétrico ($S_N$):** La asignación estructural del acorde residual en la coordenada $N-3$ proporciona una válvula de escape topológica indispensable para neutralizar el desvío pitagórico acumulado, ofreciendo un eje simétrico neutral sobre el cual redefinir la polaridad mayor/menor del sistema.