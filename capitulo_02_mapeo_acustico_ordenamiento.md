# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 2.1 Fundamentación Acústica de la Cadena y Proyección Interválica

En el marco de la *Chain Theory*, una escala microtonal no se concibe como una mera subdivisión aritmética del continuo de frecuencias, sino como la proyección en el espacio de alturas de una red relacional gobernada por un generador interválico primario y estructurada alrededor de un núcleo de simetría local: la **Cajita Central** ($C_N$). 

Formalmente, sea $N \in \mathbb{N}$ la cardinalidad del sistema temperado $N$-ET ($N$-Equal Temperament) o el tamaño del ciclo de alturas generado. Definimos el espacio de clases de alturas normalizado módulo $1200$ cents mediante la aplicación de mapeo acústico $\Phi_p$:

$$\Phi_p: \mathbb{Z} \to [0, 1200)$$

$$\Phi_p(k) = (1200 \cdot k \cdot \log_2(p)) \pmod{1200}$$

donde $p \in \mathbb{R}^+$ representa la razón de frecuencia del intervalo generador (frecuentemente $p = 3/2$ para cadenas de quintas pitagóricas o aproximaciones temperadas en $N$-ET donde $p \approx 2^{g/N}$ con $g \in \mathbb{Z}$ coprimo con $N$), y $k$ denota el índice posicional dentro del vector de la cadena $T_N$.

Cuando el sistema se restringe a un temperamento igual finito $N$-ET, el generador continuo $p$ se proyecta sobre el anillo cíclico $\mathbb{Z}_N$. En este dominio discreto, cada índice $k$ se evalúa como una clase de altura dentro de la retícula de paso $\delta = \frac{1200}{N}$ cents:

$$\theta_N(k) = (k \cdot g) \pmod N, \quad \text{cents}(k) = \theta_N(k) \cdot \frac{1200}{N}$$

El conjunto no ordenado de estas alturas generadas constituye la **Matriz Primaria Acústica** $T_{p,N}$. La disposición lineal de $T_{p,N}$ preserva la proximidad en el espacio de afinidad armónica (vecindad por generador $p$), mientras que la proyección escalar en el registro auditivo exige una transformación topológica de ordenamiento.

---

## 2.2 La Cajita Central $C_N$ y Morfogénesis Escalar

El núcleo morfológico de la cadena reside en la **Cajita Central** $C_N$, definida genéricamente por la cuádrupla de índices:

$$C_N = (P_m - 1, 0, P_m, 1)$$

donde $P_m = \lfloor N/2 \rfloor$ representa el polo menor del sistema. En extensiones del modelo para cortes asimétricos o desfasados en sistemas impares específicos, la Cajita Central se expresa como un vector tetracordal:

$$C_N = [c_0, c_1, c_2, c_3] \in \mathbb{Z}_N^4$$

A partir de $C_N$, se define el vector de diferencias interválicas inmediatas $\Delta C_N$:

$$\Delta C_N = (\delta_1, \delta_2, \delta_3) = (c_1 - c_0, c_2 - c_1, c_3 - c_2)$$

El **Operador de Vector de Calidad (OVC)** actúa sobre $\Delta C_N$ proyectando los índices al dominio acústico en cents mediante $\Phi_p$, clasificando la cualidad de las entidades armónicas generadas según la signatura métrica de sus componentes:

$$\operatorname{OVC}(C_N) = \left( \Phi_p(c_1) - \Phi_p(c_0),\, \Phi_p(c_2) - \Phi_p(c_1),\, \Phi_p(c_3) - \Phi_p(c_2) \right) \pmod{1200}$$

La clasificación del acorde resultante obedece a las siguientes condiciones de paridad y simetría interválica:

1. **Calidad Mayor ($\mathcal{M}$):** Si $\operatorname{OVC}_1 > \operatorname{OVC}_2$ y existe consonancia del intervalo externo $\operatorname{OVC}_1 + \operatorname{OVC}_2 \approx \text{quinta justa}$.
2. **Calidad Menor ($\mathfrak{m}$):** Si $\operatorname{OVC}_1 < \operatorname{OVC}_2$ bajo el mismo marco de inversión de la tercera generadora.
3. **Calidad Simétrica ($\mathcal{S}$):** Si $\operatorname{OVC}_1 = \operatorname{OVC}_3$ o si la suma total subdivide de forma equidistante un intervalo canónico (tritono, octava).

---

## 2.3 Ordenamiento Escalar ($S_{p,N}$) y Topología de Grados de Paso

La cadena $T_N$ se expande a partir de $C_N$ mediante un proceso de **expansión simétrica intercalada** bidireccional:

$$T_N = (x_{-K}, \dots, x_{-1}, C_N, x_1, \dots, x_M)$$

con cardinalidad $|T_N| = N$. Los elementos de $T_N$ representan posiciones generativas (cadena de quintas, terceras o distancias interválicas constantes). Para transitar de la afinidad armónica a la proximidad melódica, se aplica el **Operador de Ordenamiento Escalar**:

$$S_{p,N} = \operatorname{sort}\left( \Phi_p(T_N) \right) = \{ s_0, s_1, s_2, \dots, s_{N-1} \}$$

tal que:

$$0 \le s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

### Espectro de Grados de Paso (Step-Spectrum)
El conjunto de intervalos de grado adyacente viene dado por:

$$\sigma_i = s_{(i+1) \pmod N} - s_i \pmod{1200}, \quad \forall i \in \{0, \dots, N-1\}$$

En sistemas bien formados (*Well-Formed Scales*) o escalas tipo MOS (*Moment of Symmetry*), el conjunto $\{\sigma_i\}$ asume a lo sumo dos o tres valores discretos (usualmente designados como pasos $L$ [Large], $s$ [Small] y ocasionalmente $m$ [Medium]). La distribución de estos pasos define la rugosidad melódica y determina la viabilidad de la conducción de voces dentro del sistema temperado.

---

## 2.4 Análisis Estructural y Aplicación Práctica: $N = 9$ y $N = 11$

### 2.4.1 Sistema $N = 9$
Datos del motor:
- **Parámetros:** $N = 9$, $P_m = 4$, $A_N = 3$.
- **Cajita Central:** $C_9 = [3, -1, 4, 0]$.
- **Paso temperado:** $\delta = \frac{1200}{9} \approx 133.333$ cents.

#### 1. Expansión y normalización de la cadena:
Tomando el generador canónico para $9$-ET equivalente a una quinta aproximada (donde $g = 5$, ya que $5 \times \frac{1200}{9} = 666.67$ cents, o $g = 2$ para cuartas neutras/terceras mayores puras):

Evaluamos los índices de $C_9$ módulo $9$:
$$c_0 = 3 \pmod 9 = 3$$
$$c_1 = -1 \pmod 9 = 8$$
$$c_2 = 4 \pmod 9 = 4$$
$$c_3 = 0 \pmod 9 = 0$$

Vector de índices normalizado:
$$C_9 \equiv [3, 8, 4, 0]$$

#### 2. Mapeo acústico directo ($\delta = 133.33$ cents por grado de índice):
Suponiendo mapeo directo del índice de retícula ($k \cdot 133.33$ cents):
- $\Phi(c_3 = 0) = 0.00$ cents
- $\Phi(c_0 = 3) = 3 \cdot 133.333 = 400.00$ cents
- $\Phi(c_2 = 4) = 4 \cdot 133.333 = 533.33$ cents
- $\Phi(c_1 = 8) = 8 \cdot 133.333 = 1066.67$ cents

Vector acústico de la Cajita Central:
$$\operatorname{Acous}(C_9) = [400.00,\, 1066.67,\, 533.33,\, 0.00] \text{ cents}$$

Diferencias interválicas ($\Delta C_9$ cíclico):
- $\delta_1 = 1066.67 - 400.00 = 666.67$ cents (quinta neutra/temperada en 9-ET)
- $\delta_2 = 533.33 - 1066.67 = -533.33 \equiv 666.67$ cents
- $\delta_3 = 0.00 - 533.33 = -533.33 \equiv 666.67$ cents

*Observación:* $C_9$ codifica una proyección hiper-simétrica equidistante bajo el generador de $666.67$ cents ($g = 5 \equiv -4 \pmod 9$), polarizada entre el punto neutro $0$ y el centro modal $A_N = 3$.

#### 3. Ordenamiento Escalar Completo ($S_{p,9}$):
Expandiendo la cadena simétricamente hasta abarcar $\mathbb{Z}_9$:
$$T_9 = \{0, 1, 2, 3, 4, 5, 6, 7, 8\}$$
$$S_{p,9} = [0, 133.33, 266.67, 400.00, 533.33, 666.67, 800.00, 933.33, 1066.67] \text{ cents}$$
Espectro de pasos unívoco: $\sigma_i = 133.33$ cents $\forall i$.

```
Cents:   0     133.3   266.7   400.0   533.3   666.7   800.0   933.3   1066.7  1200
Escala:  s0 ---- s1 ---- s2 ---- s3 ---- s4 ---- s5 ---- s6 ---- s7 ---- s8 ---- (s0)
                 C_9:   [ c3 ]  [ c0 ]  [ c2 ]                  [ c1 ]
                          0      400     533                     1066
```

---

### 2.4.2 Sistema $N = 11$
Datos del motor:
- **Parámetros:** $N = 11$, $P_m = 4$, $A_N = 3$.
- **Cajita Central:** $C_{11} = [3, -2, 4, -1]$.
- **Paso temperado:** $\delta = \frac{1200}{11} \approx 109.091$ cents.

#### 1. Expansión y normalización de la cadena:
Normalizando módulo $11$:
$$c_0 = 3 \pmod{11} = 3$$
$$c_1 = -2 \pmod{11} = 9$$
$$c_2 = 4 \pmod{11} = 4$$
$$c_3 = -1 \pmod{11} = 10$$

Vector de índices:
$$C_{11} \equiv [3, 9, 4, 10]$$

#### 2. Mapeo acústico directo ($\delta = 109.091$ cents):
- $\Phi(c_0 = 3) = 3 \cdot 109.091 = 327.27$ cents (tercera neutra menor)
- $\Phi(c_2 = 4) = 4 \cdot 109.091 = 436.36$ cents (tercera neutra mayor)
- $\Phi(c_1 = 9) = 9 \cdot 109.091 = 981.82$ cents (séptima menor sub-diminuta)
- $\Phi(c_3 = 10) = 10 \cdot 109.091 = 1090.91$ cents (séptima mayor estrecha)

Deltas estructurales ($\Delta C_{11}$):
- $\delta_1 = 9 - 3 = 6$ pasos ($6 \times 109.091 = 654.55$ cents, tritono/quinta lobo)
- $\delta_2 = 4 - 9 = -5 \equiv 6$ pasos ($654.55$ cents)
- $\delta_3 = 10 - 4 = 6$ pasos ($654.55$ cents)

*Observación morfológica:* En $N = 11$, la Cajita Central se auto-organiza en un ciclo recurrente de tritonos temperados ($6 \times \frac{1200}{11} \approx 654.55$ cents). Este fenómeno evidencia que el vector $[-2, 4, -1, 3]$ actúa como un atractor de máxima ambigüedad armónica en el sistema impar, constituyendo el motor generador de tensiones modulatorias.

---

## 2.5 El Acorde Transformante $T_N$, Conducción de Voces y Modulaciones Microtonales

El **Acorde Transformante** $T_N$ se erige sobre la estructura de la Cajita Central mediante la recombinación dinámica de sus deltas a lo largo de la **Matriz Operativa Bi-Eje** $F_N$. Definida formalmente como:

$$F_N = \begin{pmatrix} r_{M, -2} & r_{M, -1} & r_{M, 0} & r_{M, +1} & r_{M, +2} \\ r_{m, -2} & r_{m, -1} & r_{m, 0} & r_{m, +1} & r_{m, +2} \end{pmatrix}$$

donde la Fila 1 ($r_M$) está anclada a la Tónica Mayor en $r_M = 0$, y la Fila 2 ($r_m$) se centra en el polo menor $r_m = P_m$.

```
                 SD_2       SD         T         D         D_2
             (c = -2)   (c = -1)   (c = 0)   (c = +1)   (c = +2)
           ┌──────────┬──────────┬──────────┬──────────┬──────────┐
Eje Mayor: │ r_{M,-2} │ r_{M,-1} │  r_M = 0 │ r_{M,+1} │ r_{M,+2} │
           ├──────────┼──────────┼──────────┼──────────┼──────────┤
Eje Menor: │ r_{m,-2} │ r_{m,-1} │ r_m = P_m│ r_{m,+1} │ r_{m,+2} │
           └──────────┴──────────┴──────────┴──────────┴──────────┘
Residual:   S_N en pos (N - 3)
```

### Mecánica de Conducción de Voces Parsimoniosa (Microtonal Voice Leading)
La conducción de voces en el espacio $N$-ET minimiza la distancia total de desplazamiento entre clases de alturas consecutivas. Definimos la distancia métrica $\mathcal{D}_1$ entre dos configuraciones de acordes $\mathbf{u}, \mathbf{v} \in \mathbb{Z}_N^k$ bajo el emparejamiento óptimo $\pi \in \mathfrak{S}_k$:

$$\mathcal{D}_1(\mathbf{u}, \mathbf{v}) = \min_{\pi \in \mathfrak{S}_k} \sum_{j=1}^k \min\Big( |u_j - v_{\pi(j)}|,\, N - |u_j - v_{\pi(j)}| \Big)$$

La transición entre el Acorde Mayor de Tónica $\mathcal{M}_0$ y su contraparte Menor $\mathfrak{m}_0$ implica una traslación oblicua mediada por el vector de la Cajita Central:

$$\mathcal{M}_0 \xrightarrow{\text{OVC}} \mathfrak{m}_0 \implies \mathcal{D}_1(\mathcal{M}_0, \mathfrak{m}_0) = 1 \text{ paso microtonal } (\delta)$$

```
        Voz 1:   [ c0 ] ───────────── (0 pasos) ─────────────> [ c0 ]
        Voz 2:   [ c2 ] ───────── (-1 paso: δ) ──────────────> [ c2 - 1 ]
        Voz 3:   [ c1 ] ───────────── (0 pasos) ─────────────> [ c1 ]
```

El decremento en un único grado microtonal ($\delta = 1200/N$ cents) opera la inversión modal de polaridad sin requerir desplazamientos de semitono diatónico, permitiendo transiciones casi continuas (modulaciones por deriva microtonal).

### Modulaciones a través del Acorde Simétrico Residual ($S_N$)
El Acorde Simétrico Residual $S_N$, confinado a la coordenada $N - 3$, actúa como un **eje de reorientación vectorial**. Dado que sus intervalos internos reproducen simetrías invariantes bajo rotaciones de $\frac{N \pm 1}{2}$ grados:

1. El sistema resuelve el tensor armónico hacia $S_N$ mediante un desplazamiento de dominante secundaria ($c = +2$).
2. Se reinterpreta el eje del sistema: $r'_M = S_N \pmod N$.
3. Se proyecta una nueva Cajita Central $C'_N = C_N + r'_M$.

Este mecanismo permite modular instantáneamente entre regiones de micro-tonalidad tonalmente disjuntas sin romper la coherencia del ciclo de afinidad.

---

## 2.6 Implementación Algorítmica en SuperCollider

El siguiente programa compila la teoría expuesta: calcula la Cajita Central para un $N$ arbitrario, computa los vectores acústicos, realiza el ordenamiento escalar ($S_{p,N}$) y genera una textura auditiva de la escala y sus acordes transformantes derivados.

```supercollider
// =====================================================================
// THE CHAIN THEORY: Motor de Cálculo y Síntesis de N-ET
// Capítulo 2: Mapeo Acústico, Ordenamiento Escalar y Síntesis de C_N
// =====================================================================

(
s.waitForBoot({
    var nET, pRatio, p_m, a_N, cajitaCentral, t_N, s_pN;
    var stepCents, baseFreq, scaleFreqs;

    // 1. Parámetros de entrada
    nET = 11;                    // Seleccionar orden N (ej. 9 u 11)
    baseFreq = 220.0;           // Altura fundamental (Hz) correspondiente a 0 cents
    pRatio = 3/2;               // Generador armónico (quinta acústica)

    // 2. Cálculos Matriciales Axiales
    p_m = (nET / 2).floor.asInteger;
    a_N = 3; // Ancla armónica canónica

    // Selección de Cajita Central paramétrica según el motor
    cajitaCentral = switch(nET,
        9,  { [3, -1, 4, 0] },
        11, { [3, -2, 4, -1] },
        { [p_m - 1, 0, p_m, 1] } // Caso genérico por defecto
    );

    // Normalización modular sobre Z_N
    cajitaCentral = cajitaCentral.collect({ |val| val.mod(nET) });

    // 3. Mapeo Acústico y Discretización
    stepCents = 1200.0 / nET;
    
    // Generación de la Cadena Primaria T_N (Espacio-Cadena)
    t_N = Array.fill(nET, { |i| (i * (p_m + 1)).mod(nET) });

    // Ordenamiento Escalar S_{p,N} (Espacio-Altura)
    s_pN = (0..(nET - 1)).collect({ |deg| deg * stepCents });
    scaleFreqs = s_pN.collect({ |cents| baseFreq * (2.pow(cents / 1200.0)) });

    // Presentación analítica en consola
    "==================================================".postln;
    ("ESTRUCTURA DE CADENA PARA N-ET: " ++ nET).postln;
    ("P_m: " ++ p_m ++ " | A_N: " ++ a_N).postln;
    ("Cajita Central C_N (índices mod " ++ nET ++ "): " ++ cajitaCentral).postln;
    ("Tamaño de paso microtonal (cents): " ++ stepCents.round(0.001)).postln;
    ("Frecuencias resultantes (Hz): " ++ scaleFreqs.round(0.01)).postln;
    "==================================================".postln;

    // 4. Síntesis Auditiva: Sonificación del Ordenamiento Escalar y Acorde Transformante
    SynthDef(\chainTone, { |out = 0, freq = 440, amp = 0.1, gate = 1, pan = 0, rel = 1.5|
        var env = EnvGen.ar(Env.perc(0.02, rel), gate, doneAction: Done.freeSelf);
        var sig = SinOsc.ar(freq) * 0.6 + Formant.ar(freq, freq * 2, freq * 1.5) * 0.4;
        sig = sig * env * amp;
        Out.ar(out, Pan2.ar(sig, pan));
    }).add;

    s.sync;

    // Rutina de demostración:
    // 1. Escala ordenada ascendente (S_{p,N})
    // 2. Acorde de la Cajita Central (C_N) sonando en simultáneo
    Routine({
        "1. Reproduciendo Escala Ordenada S_{p,N}...".postln;
        scaleFreqs.do({ |f|
            Synth(\chainTone, [\freq, f, \amp, 0.15, \rel, 0.8]);
            0.18.wait;
        });

        1.0.wait;

        "2. Reproduciendo Acorde Transformante (Cajita Central C_N)...".postln;
        cajitaCentral.do({ |idx|
            var chordFreq = baseFreq * (2.pow((idx * stepCents) / 1200.0));
            Synth(\chainTone, [\freq, chordFreq, \amp, 0.2, \rel, 3.5, \pan, rrand(-0.5, 0.5)]);
        });
    }).play;
});
)
```

---

## 2.7 Conclusiones Teóricas del Capítulo

1. **Dualidad Topológica:** La serie $T_{p,N}$ organiza los tonos en función de su afinidad armónica proyectada por el generador $p$, mientras que $S_{p,N}$ redistribuye dicha red en el espacio lineal de frecuencias mediante $\operatorname{sort}(\Phi_p(T_N))$. Esta dualidad desacopla la consonancia estructural de la proximidad melódica.
2. **Invariancia Funcional de la Cajita:** Para $N = 9$ y $N = 11$, la Cajita Central $C_N$ concentra los máximos armónicos y las tensiones críticas (tritonos neutros e intervalos simétricos) que polarizan el sistema, sirviendo como núcleo tanto para acordes de reposo modal como para la generación del Acorde Residual $S_N$ en $N - 3$.
3. **Mecanismo de Modulación por Paso Mínimo:** La mutación funcional en $F_N$ no precisa de saltos cromáticos mayores ($> 100$ cents). Al explotar vectores $\Delta C_N$, las progresiones armónicas transmutan sus calidades modales ($\mathcal{M} \leftrightarrow \mathfrak{m} \leftrightarrow \mathcal{S}$) a través de un único desplazamiento diferencial $\delta = \frac{1200}{N}$, formalizando un modelo de conducción de voces microtonalmente óptimo.