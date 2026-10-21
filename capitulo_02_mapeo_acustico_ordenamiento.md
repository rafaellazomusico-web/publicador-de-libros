# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 1. Fundamentación Acústica y Proyección Logarítmica de la Cadena

El modelado formal de *The Chain Theory* postula que cualquier sistema armónico puede representarse como una trayectoria estructurada sobre una variedad discreta. Para proyectar dicha construcción abstracta en el continuo psicoacústico, definimos el operador de mapeo acústico $T_{p,N}$, el cual proyecta un índice de altura discreto $k \in \mathbb{Z}$ al espacio continuo de cents en la escala temperada logarítmica:

$$\Phi_{p}(k) = \left( 1200 \cdot k \cdot \log_2(p) \right) \pmod{1200}$$

donde $p \in \mathbb{R}^+$ representa la base de proyección armónica (típicamente $p = 3$ para sistemas de derivación pitagórica/por quintas, o $p = 5$ para proyecciones sintónicas/tercianas). 

En el marco de una discretización de temperamento igual de $N$ divisiones de la octava ($N\text{-ET}$), el tamaño fundamental del paso escalar elemental se denota como:

$$\tau_N = \frac{1200}{N} \quad [\text{cents}]$$

Bajo esta parametrización, el mapeo de una clase de altura generada modularmente dentro del sistema $N\text{-ET}$ se formula a través de la relación:

$$T_{p,N}(k) = \left( k \cdot \tau_N \right) \pmod{1200} = \left( \frac{1200 \cdot k}{N} \right) \pmod{1200}$$

Cuando se superpone la base acústica $p$, el índice entero $k$ se modula por el factor logarítmico del intervalo generador en relación al espacio cíclico de octava ($2/1$).

```
Índice Modular k  ───►  [ Proyección p ]  ───►  T_{p,N}(k)  ───►  Espacio Escalar S_{p,N}
      (Z_N)                  log2(p)               (cents)                (Ordenado)
```

### 1.1. Topología de la Cajita Central ($C_N$)

La génesis de la matriz armónica parte de la **Cajita Central** $C_N$, definida axiomáticamente como la 4-tupla:

$$C_N = (\delta_1, \delta_2, \delta_3, \delta_4)$$

donde sus componentes representan los índices primarios que anclan las relaciones de simetría axial del sistema:

$$C_N = \left( P_m - 1, \, 0, \, P_m, \, 1 \right), \quad \text{con } P_m = \left\lfloor \frac{N}{2} \right\rfloor$$

Sin embargo, al considerar desplazamientos modulares y tensiones espectrales centradas en la polaridad cromática, la Cajita Central puede expresarse mediante coordenadas generalizadas centradas en cero mediante la transformación $C_N \in \mathbb{Z}_N^4$:

$$C_N = \left[ c_0, \, c_1, \, c_2, \, c_3 \right]$$

Los intervalos generados entre los puntos nodales de la cajita establecen las diferencias vectoriales:

$$\Delta_{i,j} = (c_j - c_i) \pmod N$$

Estas diferencias determinan los armónicos funcionales locales (subdiatónicos, neutros o supradiatónicos) que actuarán como vectores de transformación de fase armónica.

---

## 2. Ordenamiento Escalar ($S_{p,N}$) y Morfología de Grados de Paso

La matriz primaria $T_N$ se despliega mediante una expansión simétrica intercalada a partir de los elementos internos de $C_N$. Esta estructura expandida no se organiza a priori de forma monotónica lineal, sino que se genera siguiendo el orden funcional de tensión y resolución entre los polos de subdominante y dominante.

Para derivar la escala subyacente que percibe el oído humano como continuo diatónico microtonal, es mandatorio aplicar el **Operador de Ordenamiento Escalar** $\mathcal{S}$, definido formalmente como:

$$S_{p,N} = \text{sort}\left( T_{p,N} \right) = \left\{ s_0, s_1, s_2, \dots, s_{N-1} \right\}$$

tal que satisface la condición estricta de orden:

$$0 \le s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

### 2.1. Vector de Intervalos Escalares (Pasos de Conducción)

A partir del conjunto ordenado $S_{p,N}$, deducimos el vector de pasos diferenciales:

$$\vec{\sigma}_N = \left( \sigma_0, \sigma_1, \dots, \sigma_{N-1} \right)$$

donde:

$$\sigma_i = \begin{cases} 
s_{i+1} - s_i & \text{para } 0 \le i < N-1 \\ 
(1200 + s_0) - s_{N-1} & \text{para } i = N-1 
\end{cases}$$

En los sistemas $N\text{-ET}$ homogéneos, $\sigma_i = \tau_N = \frac{1200}{N}$, preservando una periodicidad isotrópica. No obstante, en la proyección generatriz acústica determinada por $p \neq 2$, el operador de módulo genera un espectro de intervalos escalares pseudo-periódicos con propiedades comáticas de segundo y tercer orden.

### 2.2. Simetría Espejo de la Cadena

La cadena $T_N$ posee un centro de simetría reflejada respecto a su eje de división modular. Definimos el operador de inversión de orden armónico $\mathcal{I}$ tal que:

$$\mathcal{I}(k) = (-k) \pmod N$$

La aplicación de $\mathcal{I}$ sobre los componentes de la matriz proyectada mapea las funciones del eje mayor directamente a las del eje menor, verificando la dualidad estructural de Riemann dentro del marco $N\text{-ET}$.

---

## 3. Análisis Estructural y Aplicación: $N = 9$ y $N = 11$

### 3.1. Caso $N = 9$

#### Parámetros Iniciales
- Dimensión modular: $N = 9$.
- Paso escalar elemental: $\tau_9 = \frac{1200}{9} \approx 133.333 \text{ cents}$.
- Parámetro de partición: $P_m = \left\lfloor \frac{9}{2} \right\rfloor = 4$.
- Amplitud del núcleo: $A_N = 3$.
- **Cajita Central**: $C_9 = [3, -1, 4, 0]$.

Representando $C_9$ en clases de equivalencia positiva en $\mathbb{Z}_9$:
$$C_9 = [3, \, 8, \, 4, \, 0]$$

```
                   Eje Modular N = 9
      8 (-1) ──── 0 ──── 3 ──── 4
      [SD]       [T]    [D]   [D_2]
```

#### Vector de Diferencias Locales ($\Delta$)
- $\Delta_{0,1} = (-1 - 3) \equiv -4 \equiv 5 \pmod 9$
- $\Delta_{1,2} = (4 - (-1)) = 5 \equiv 5 \pmod 9$
- $\Delta_{2,3} = (0 - 4) = -4 \equiv 5 \pmod 9$

Se evidencia una periodicidad estricta del generador interválico $\delta = 5$ (la «cuarta justa» en $9\text{-ET}$, que equivale a $5 \times 133.333 = 666.67 \text{ cents}$).

#### Mapeo Acústico en Cents para $N = 9$
Calculando $T_{9}(k) = (k \cdot \tau_9) \pmod{1200}$:

| Índice $k$ | Clase $\mathbb{Z}_9$ | Valor en Cents ($T_9$) | Función Modal ($F_9$) |
|:---:|:---:|:---:|:---:|
| $0$ | $0$ | $0.00$ | Tónica Mayor ($T_M$) |
| $1$ | $1$ | $133.33$ | Dominante ($D$) |
| $2$ | $2$ | $266.67$ | Dominante Sec. ($D_2$) |
| $3$ | $3$ | $400.00$ | Núcleo $C_9$ / Tercera Neutra |
| $4$ | $4$ | $533.33$ | Tónica Menor ($T_m$) |
| $5$ | $5$ | $666.67$ | Subdominante Sec. ($SD_2$) |
| $6$ | $6$ | $800.00$ | Acorde Simétrico ($S_9$) |
| $7$ | $7$ | $933.33$ | Grado de Paso |
| $8$ | $8$ ($-1$) | $1066.67$ | Subdominante ($SD$) |

El Acorde Simétrico Residual $S_N$ se localiza estrictamente en la posición teórica:

$$\text{pos}(S_N) = N - 3 = 9 - 3 = 6$$

Correspondiendo al índice $k = 6$ ($800.00 \text{ cents}$).

---

### 3.2. Caso $N = 11$

#### Parámetros Iniciales
- Dimensión modular: $N = 11$.
- Paso escalar elemental: $\tau_{11} = \frac{1200}{11} \approx 109.091 \text{ cents}$.
- Parámetro de partición: $P_m = \left\lfloor \frac{11}{2} \right\rfloor = 5$ (para la expansión regular), calibrado operativamente a $P_m = 4$ con $A_N = 3$.
- **Cajita Central**: $C_{11} = [3, -2, 4, -1]$.

Normalizando $C_{11}$ a $\mathbb{Z}_{11}$:
$$C_{11} = [3, \, 9, \, 4, \, 10]$$

```
                   Eje Modular N = 11
      9 (-2) ──── 10 (-1) ──── 3 ──── 4
      [SD_2]       [SD]       [D]   [D_2]
```

#### Vector de Diferencias Locales ($\Delta$)
- $\Delta_{0,1} = (-2 - 3) = -5 \equiv 6 \pmod{11}$
- $\Delta_{1,2} = (4 - (-2)) = 6 \equiv 6 \pmod{11}$
- $\Delta_{2,3} = (-1 - 4) = -5 \equiv 6 \pmod{11}$

El generador interno de la cajita es $\delta = 6$, que proyecta un intervalo de $6 \times 109.091 = 654.545 \text{ cents}$ (el tritono/cuarta hiper-extendida característica del temperamento de 11 divisiones).

#### Mapeo Acústico en Cents para $N = 11$
Calculando $T_{11}(k) = (k \cdot \tau_{11}) \pmod{1200}$:

| Índice $k$ | Clase $\mathbb{Z}_{11}$ | Valor en Cents ($T_{11}$) | Función Bi-Eje ($F_{11}$) |
|:---:|:---:|:---:|:---:|
| $0$ | $0$ | $0.00$ | Tónica Mayor ($r_M = 0$) |
| $1$ | $1$ | $109.09$ | Dominante ($D$) |
| $2$ | $2$ | $218.18$ | Dominante Sec. ($D_2$) |
| $3$ | $3$ | $327.27$ | Borde $C_{11}$ |
| $4$ | $4$ | $436.36$ | Tónica Menor ($r_m = P_m$) |
| $5$ | $5$ | $545.45$ | Grado Neutral |
| $6$ | $6$ | $654.55$ | Eje Tritonal Microtonal |
| $7$ | $7$ | $763.64$ | Grado Neutro Superior |
| $8$ | $8$ | $872.73$ | Acorde Simétrico ($S_{11}$, pos $N-3$) |
| $9$ | $9$ ($-2$) | $981.82$ | Subdominante Sec. ($SD_2$) |
| $10$ | $10$ ($-1$) | $1090.91$ | Subdominante ($SD$) |

El Acorde Simétrico Residual se confirma en:

$$\text{pos}(S_{11}) = 11 - 3 = 8 \quad (872.73 \text{ cents})$$

---

## 4. Matriz Operativa Bi-Eje ($F_N$) y Operador OVC

La Matriz Operativa Bi-Eje formaliza las relaciones funcionales mediante dos niveles acoplados: el Eje Mayor (fila 1, centrado en la tónica mayor $r_M = 0$) y el Eje Menor (fila 2, centrado en la tónica menor $r_m = P_m$).

$$F_N = \begin{pmatrix}
(r_M - 2) & (r_M - 1) & r_M & (r_M + 1) & (r_M + 2) \\
(r_m - 2) & (r_m - 1) & r_m & (r_m + 1) & (r_m + 2)
\end{pmatrix} \pmod N$$

Sustituyendo las funciones tonales para las columnas $c \in \{-2, -1, 0, 1, 2\}$:

$$F_N = \begin{pmatrix}
SD_2 & SD & T_M & D & D_2 \\
sd_2 & sd & T_m & d & d_2
\end{pmatrix}$$

```
                [SD_2] <─── [SD] <─── [ T ] ───> [ D ] ───> [D_2]
Eje Mayor:       N - 2      N - 1       0          1          2
                   ▲          ▲         ▲          ▲          ▲
                   │          │   OVC   │          │          │
                   ▼          ▼         ▼          ▼          ▼
Eje Menor:       P_m - 2    P_m - 1    P_m       P_m + 1    P_m + 2
```

### 4.1. Operador OVC (Optimal Voice-Leading Coefficient)

El **Operador OVC** evalúa la conducción de voces óptima calculando el desplazamiento mínimo absoluto en el espacio métrico circular $\mathbb{T}_{1200}$:

$$\text{OVC}(A, B) = \min_{\pi \in \Pi} \sum_{i=1}^k d_{\mathbb{T}}\left( a_i, \, b_{\pi(i)} \right)$$

donde $d_{\mathbb{T}}(x, y) = \min(|x - y|, 1200 - |x - y|)$, y clasifica la cualidad armónica de cada estructura triádica o tetrádica derivada de la Cajita Central en tres clases:

$$\text{Clase}(X) = \begin{cases} 
\mathbb{M} \text{ (Mayor)} & \text{si } \Delta C_N \text{ exhibe asimetría dextrógira} \\
\mathbb{M}^{-1} \text{ (Menor)} & \text{si } \Delta C_N \text{ exhibe asimetría levógira} \\
\mathbb{S} \text{ (Simétrico)} & \text{si } \Delta_{0,1} = \Delta_{2,3} \text{ y } X \text{ coincide con la órbita de } S_N
\end{cases}$$

---

## 5. Dinámica del Acorde Transformante $T_N$, Conducción de Voces y Modulaciones

El **Acorde Transformante** $T_N$ se comporta como un conector de fase en el retículo armónico. Debido a que el vector de diferencias $\Delta C_N$ comparte factores de escala tanto con el eje dominante como con el eje subdominante, actúa como una singularidad de curvatura nula en el espacio interválico.

### 5.1. Conducción Parsimoniosa Microtonal

En un sistema convencional de doce semitonos ($12\text{-ET}$), los movimientos parsimoniosos (transformaciones neo-riemannianas $P, L, R$) operan por desplazamientos de 1 o 2 semitonos ($100$ o $200 \text{ cents}$). En $N\text{-ET}$, la transformación parsimoniosa elemental mediada por $T_N$ requiere únicamente un desplazamiento de:

$$\delta_{\text{parsimonia}} = \tau_N = \frac{1200}{N} \text{ cents}$$

Para $N=11$, este desplazamiento es de tan solo $\approx 109.09 \text{ cents}$, lo que permite una reorientación del centro tonal sin discontinuidad en la percepción espectral del continuo armónico.

### 5.2. Mecánica de Modulación por Giro Axial

Para modular de la Tónica Mayor $r_M = 0$ a la Tónica Menor $r_m = P_m$ utilizando el Acorde Transformante $T_N$:

1. **Estado Inicial**: Se establece la estabilidad mediante el ciclo $T_M \to D \to T_M$.
2. **Inflexión por Inserción**: Se introduce $C_N$, cuyos armónicos contienen simultáneamente los componentes $0$ ($T_M$) y $P_m$ ($T_m$).
3. **Colapso Simétrico**: Se aplica una transposición interválica hacia el Acorde Simétrico Residual $S_N$ ($k = N - 3$). Al carecer $S_N$ de una tercera polarizada preferente, suspende el vector de inercia funcional.
4. **Resolución en Nuevo Eje**: Mediante un paso unielemental de $\tau_N$, el complejo armónico colapsa sobre $r_m$, consolidando el nuevo centro sin recurrir al ciclo de quintas tradicional.

---

## 6. Implementación Algorítmica

El siguiente bloque de código en **SuperCollider** (`sclang`) formaliza el cálculo del mapeo acústico $T_{p,N}$, la Cajita Central $C_N$, el ordenamiento escalar $S_{p,N}$ y la síntesis con afinación directa en cents para cualquier configuración de $N$.

```supercollider
// =====================================================================
// THE CHAIN THEORY: Mapeo Acústico y Expansión N-ET
// Implementación: Generador de Matrices Tp,N y Síntesis Microtonal
// =====================================================================

(
var calculateChain = { |n = 11, p = 3|
    var tau, pm, an, centralBox, fullChain, scalarOrder, centsTuning;

    tau = 1200.0 / n;
    pm = (n / 2).floor.asInteger;
    an = 3; // Amplitud del núcleo

    // 1. Axioma de la Cajita Central
    // C_N = [pm - 1, 0, pm, 1] normalizado
    centralBox = [pm - 1, 0, pm, 1];

    // 2. Generación de la Matriz Primaria (T_N)
    fullChain = Array.fill(n, { |i|
        (i * tau) % 1200.0;
    });

    // 3. Mapeo Acústico con generador armónico p
    centsTuning = Array.fill(n, { |k|
        (1200.0 * k * p.log2) % 1200.0;
    });

    // 4. Ordenamiento Escalar (S_{p,N})
    scalarOrder = centsTuning.copy.sort;

    postf("\n=== ANÁLISIS ESTRUCTURAL N-ET: %-ET ===\n", n);
    postf("Paso elemental (tau): % cents\n", tau.round(0.001));
    postf("P_m: % | A_N: %\n", pm, an);
    postf("Cajita Central (C_N): %\n", centralBox);
    postf("Acorde Simétrico Residual (S_N en N-3): pos % (% cents)\n", 
        n - 3, (fullChain[n - 3]).round(0.001));
    postf("Matriz Primaria T_% (cents): %\n", n, fullChain.round(0.01));
    postf("Escala Ordenada S_{%,%} (cents): %\n", p, n, scalarOrder.round(0.01));

    // Retorna estructura con datos
    (
        n: n,
        tau: tau,
        centralBox: centralBox,
        fullChain: fullChain,
        scalarOrder: scalarOrder
    );
};

// Ejecución para N = 9 y N = 11
~data9 = calculateChain.value(9, 3);
~data11 = calculateChain.value(11, 3);

// ---------------------------------------------------------------------
// Motor de Síntesis: Reproducción de Conducción de Voces Parsimoniosa
// ---------------------------------------------------------------------
SynthDef(\chainVoice, { |out = 0, freq = 440, amp = 0.1, gate = 1, pan = 0|
    var env = EnvGen.kr(Env.adsr(0.4, 0.2, 0.7, 0.8), gate, doneAction: 2);
    var sig = Saw.ar(freq * [0.999, 1.001]) * 0.5;
    sig = sig + SinOsc.ar(freq, 0, 0.5);
    sig = LPF.ar(sig, freq * 4);
    Out.ar(out, Pan2.ar(sig * env * amp, pan));
}).add;

Routine({
    var baseFreq = 220.0; // La3 base
    s.sync;

    "\nIniciando secuencia de modulación axial en 11-ET...".postln;

    // Transición: Tónica Mayor -> Cajita Central -> Acorde Simétrico -> Tónica Menor
    [
        [0, 4, 7],      // Proyección Tónica
        [3, 9, 4, 10],  // Cajita Central C_11
        [8, 1, 6],      // Acorde Simétrico Residual S_11
        [4, 8, 11]      // Resolución Tónica Menor P_m
    ].do { |chordIndices|
        var synths = chordIndices.collect { |idx|
            var freq = baseFreq * (2.pow((idx * (1200.0 / 11)) / 1200.0));
            Synth(\chainVoice, [\freq, freq, \amp, 0.08]);
        };
        1.5.wait;
        synths.do(_.set(\gate, 0));
        0.3.wait;
    };
    "Secuencia completada.".postln;
}).play;
)
```

Este entorno algorítmico materializa las propiedades cinemáticas de la modulación descritas formalmente: el espacio de clases de alturas no se somete a aproximaciones temperadas ad hoc, sino que las tensiones de la cadena gobiernan de forma unívoca la posición armónica de cada evento sonoro.