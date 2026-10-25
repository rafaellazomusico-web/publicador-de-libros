# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 2.1. Fundamentación Teórica del Mapeo Acústico ($T_{p,N}$)

En el marco de *The Chain Theory*, la generación del espacio sonoro trasciende las limitaciones del temperamento igual tradicional de 12 tonos ($12$-ET) al proyectar matrices estructurales simétricas dentro de espacios temperados genéricos de $N$ divisiones iguales de la octava ($N$-ET / $N$-EDO), o mediante la parametrización de generadores acústicos primos $p \in \mathbb{P}$.

La **Matriz Primaria** ($T_N$) no es una colección arbitraria de alturas, sino un conjunto vectorial proyectado a partir del núcleo morfológico denominado **Cajita Central** ($C_N$). Para vincular la abstracción discreta de $T_N$ con el continuo de frecuencias audibles, se formaliza el operador de mapeo acústico $T_{p,N}$.

Sea $idx \in T_N$ el índice entero asignado a un elemento dentro de la cadena estructural primaria. El mapeo en centésimas de semitono (*cents*) bajo un generador $p$ se define como:

$$\phi_p(idx) = \left( 1200 \cdot idx \cdot \log_2(p) \right) \pmod{1200}$$

Donde:
- $p \ge 2$ representa el número primo generador del espacio acústico (por ejemplo, $p=3$ para proyecciones pitagóricas o de quintas armónicas, $p=5$ para redes de tercera mayor justa).
- Cuando el espacio se reduce al retículo discreto $N$-ET normalizado a la octava (donde el paso elemental es $\delta = \frac{1200}{N}\text{ cents}$), el mapeo para cada nodo $k \in \mathbb{Z}_N$ equivale a:

$$\mu_N(k) = \left( \frac{1200}{N} \cdot k \right) \pmod{1200}$$

La **Cajita Central** $C_N$ actúa como el atractor simétrico de la matriz. Sus deltas internos configuran la curvatura armónica local, dictando no solo la distribución intervalar del centro de gravedad de la cadena, sino también los umbrales de batimiento y disonancia sensorial generados por el solapamiento de armónicos naturales al sintetizarse físicamente.

---

## 2.2. Ordenamiento Escalar ($S_{p,N}$) y Simetría Paramétrica

Aunque la Matriz Primaria $T_N$ se despliega de forma intercalada y simétrica para preservar las relaciones generatrices de conducción armónica, la manifestación pragmática de una afinación exige su reducción a una escala musical estricta: un conjunto cíclico y estrictamente creciente contenido en el intervalo de la octava $[0, 1200)\text{ cents}$.

Definimos el **Vector Escalar Ordenado** $S_{p,N}$ mediante el operador de permutación monótona creciente:

$$S_{p,N} = \text{sort}(T_{p,N}) = \{ s_0, s_1, s_2, \dots, s_{N-1} \}$$

sujeto a la restricción:

$$0 \le s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

A partir de $S_{p,N}$, se extrae el **Vector de Grados de Paso** (Interval Step Vector) $\Delta S_{p,N}$, cuyos elementos revelan la simetría microtonal del sistema:

$$\Delta s_i = s_{i+1} - s_i \quad \text{para } 0 \le i < N-1, \quad \Delta s_{N-1} = (1200 + s_0) - s_{N-1}$$

### Teorema de Simetría Espejada de la Cadena
En sistemas $N$-ET simétricamente balanceados, si el operador de inversión $\mathcal{I}(k) = -k \pmod N$ se aplica sobre el dominio discreto de $T_N$, la secuencia resultante de deltas $\Delta S$ presenta un palíndromo estructural o una propiedad de bi-simetría rotacional. Esto garantiza que cualquier traslación dentro de la matriz dual de funciones $F_N$ posea un comportamiento acústico estrictamente isomorfo tanto en el Eje Mayor como en el Eje Menor.

---

## 2.3. Desglose Estructural Comparado: Casos $N = 9$ y $N = 11$

Analizaremos la aplicación algorítmica para los sistemas microtonales $N = 9$ y $N = 11$, utilizando los parámetros calculados por el motor matemático.

```
          [Matriz Primaria T_N]
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
    Caso N = 9          Caso N = 11
   P_m=4, A_N=3        P_m=4, A_N=3
   C_9=[3,-1,4,0]      C_11=[3,-2,4,-1]
         │                   │
         ▼                   ▼
    Mapeo 9-ET          Mapeo 11-ET
   (Paso: 133.33¢)     (Paso: 109.09¢)
         │                   │
         ▼                   ▼
   Escala S_{p,9}      Escala S_{p,11}
```

### 2.3.1. Caso $N = 9$ ($9$-ET)
- **Constantes:** $P_m = \lfloor 9 / 2 \rfloor = 4$; $A_N = 3$.
- **Cajita Central:** $C_9 = [3, -1, 4, 0]$.
- **Paso elemental:** $\delta_9 = \frac{1200}{9} \approx 133.333\text{ cents}$.

#### 1. Expansión y Vector de Índices
La Cajita Central normalizada en $\mathbb{Z}_9$ (trasladando $-1 \equiv 8 \pmod 9$) es:
$$C_9 \equiv [3, 8, 4, 0]$$
Deltas interválicos de la Cajita Central:
$$\Delta C_9 = [8 - 3, 4 - 8, 0 - 4] \pmod 9 = [5, 5, 5]$$
Esta periodicidad de $5$ pasos de $9$-ET ($5 \times 133.333 = 666.67\text{ cents}$, intervalo sub-quinta/tritono neutro) dota al sistema de un atractor simétrico característico.

Expandiendo simétricamente hacia la totalidad de $N = 9$ grados para poblar la matriz $T_9$:
$$T_9 = [0, 1, 2, 3, 4, 5, 6, 7, 8]$$

#### 2. Mapeo Acústico en Cents
Multiplicando cada grado discreto por $\delta_9$:

$$T_{cents, 9} = [0.0, 133.33, 266.67, 400.0, 533.33, 666.67, 800.0, 933.33, 1066.67]$$

#### 3. Matriz Operativa Bi-Eje ($F_9$) y Acorde Simétrico Residual ($S_9$)
- **Eje Mayor ($r_M = 0$):** Nodo central en grado $0$ ($0.0\text{ cents}$).
- **Eje Menor ($r_m = P_m = 4$):** Nodo central en grado $4$ ($533.33\text{ cents}$).
- **Acorde Simétrico Residual ($S_9$):** Aislado en la posición $N - 3 = 6$ ($800.0\text{ cents}$).

| Función | Eje Mayor ($r_M = 0$) | Grado ($\mathbb{Z}_9$) | Cents | Eje Menor ($r_m = 4$) | Grado ($\mathbb{Z}_9$) | Cents |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **$SD_2$ ($c=-2$)** | Grado $0 - 2$ | $7$ | $933.33$ | Grado $4 - 2$ | $2$ | $266.67$ |
| **$SD$ ($c=-1$)**   | Grado $0 - 1$ | $8$ | $1066.67$| Grado $4 - 1$ | $3$ | $400.00$ |
| **Tónica ($c=0$)**  | Grado $0$     | $0$ | $0.00$   | Grado $4$     | $4$ | $533.33$ |
| **$D$ ($c=+1$)**    | Grado $0 + 1$ | $1$ | $133.33$ | Grado $4 + 1$ | $5$ | $666.67$ |
| **$D_2$ ($c=+2$)**  | Grado $0 + 2$ | $2$ | $266.67$ | Grado $4 + 2$ | $6$ | $800.00$ |

*Nota:* El Acorde Simétrico Residual $S_9$ reside en el índice $N - 3 = 6$. Se aprecia cómo el Eje Menor en $c=+2$ intersecta la frontera residual del sistema, forzando la polarización simétrica descrita por el Operador OVC.

---

### 2.3.2. Caso $N = 11$ ($11$-ET)
- **Constantes:** $P_m = \lfloor 11 / 2 \rfloor = 4$ (según el motor de cálculo provisto); $A_N = 3$.
- **Cajita Central:** $C_{11} = [3, -2, 4, -1]$.
- **Paso elemental:** $\delta_{11} = \frac{1200}{11} \approx 109.091\text{ cents}$.

#### 1. Expansión e Índices Normalizados
Normalizando los índices negativos en el anillo cíclico $\mathbb{Z}_{11}$:
$$-2 \equiv 9 \pmod{11}, \quad -1 \equiv 10 \pmod{11}$$
Por lo tanto:
$$C_{11} = [3, 9, 4, 10]$$

Deltas interválicos de $C_{11}$:
$$\Delta C_{11} = [9 - 3, 4 - 9, 10 - 4] \pmod{11} = [6, 6, 6]$$
Nótese la regularidad estructural: cada salto interno equivale a $6$ pasos de $11$-ET ($6 \times 109.091 = 654.545\text{ cents}$).

#### 2. Mapeo Acústico de la Escala $S_{p, 11}$
Ordenando de forma estrictamente monótona los $11$ pasos equitemperados:

$$S_{11} = \{ k \cdot \delta_{11} \}_{k=0}^{10}$$

$$S_{11} = \begin{Bmatrix} 
0.00, & 109.09, & 218.18, & 327.27, & 436.36, & 545.45, \\
654.55, & 763.64, & 872.73, & 981.82, & 1090.91 
\end{Bmatrix}\text{ cents}$$

#### 3. Matriz Operativa Bi-Eje ($F_{11}$) y Acorde Simétrico Residual ($S_{11}$)
- **Eje Mayor ($r_M = 0$):** Grado $0$ ($0.0\text{ cents}$).
- **Eje Menor ($r_m = 4$):** Grado $4$ ($436.36\text{ cents}$, neutro-tercera mayor microtonal).
- **Acorde Residual ($S_{11}$):** Situado estrictamente en $N - 3 = 11 - 3 = 8$ ($872.73\text{ cents}$).

| Función | Eje Mayor ($r_M = 0$) | Grado ($\mathbb{Z}_{11}$) | Cents | Eje Menor ($r_m = 4$) | Grado ($\mathbb{Z}_{11}$) | Cents |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **$SD_2$ ($c=-2$)** | $0 - 2$ | $9$ | $981.82$ | $4 - 2$ | $2$ | $218.18$ |
| **$SD$ ($c=-1$)**   | $0 - 1$ | $10$| $1090.91$| $4 - 1$ | $3$ | $327.27$ |
| **Tónica ($c=0$)**  | $0$     | $0$ | $0.00$   | $4$     | $4$ | $436.36$ |
| **$D$ ($c=+1$)**    | $0 + 1$ | $1$ | $109.09$ | $4 + 1$ | $5$ | $545.45$ |
| **$D_2$ ($c=+2$)**  | $0 + 2$ | $2$ | $218.18$ | $4 + 2$ | $6$ | $654.55$ |

El Acorde Simétrico Residual $S_{11}$ (aislado en grado $8 = 872.73\text{ cents}$) opera como bisagra de indeterminación funcional, impidiendo el colapso diatónico y preservando la topología toroidal del sistema microtonal extendido.

---

## 2.4. Dinámica de Conducción de Voces y Modulación Microtonal vía $T_N$

El papel fundamental del constructo transformante $T_N$ radica en optimizar el **Principio de Parsimonia Microtonal**: transicionar entre complejos armónicos minimizando la distancia métrica en el espacio de alturas $\mathbb{R}^k / 1200\mathbb{Z}$.

### 2.4.1. Métrica de Desplazamiento de Voz
Sean dos acordes tetrádicos $A, B \subset T_N$ parametrizados por sus vectores de afinación en cents $A = (a_1, a_2, a_3, a_4)$ y $B = (b_1, b_2, b_3, b_4)$. La distancia de conducción de voces se evalúa mediante la norma de Manhattan ($L_1$):

$$\mathcal{D}_{L_1}(A, B) = \sum_{i=1}^{4} \min_{k \in \mathbb{Z}} |(a_i - b_{\sigma(i)}) + 1200k|$$

donde $\sigma$ representa la biyección permutacional que minimiza la sumatoria (conducción de voces más cercana o *smoothest voice leading*).

Bajo la matriz $F_N$, el tránsito del Eje Mayor al Eje Menor se formaliza mediante la modulación del pivote central:

$$\Delta_{\text{mod}} = |r_M - r_m| \cdot \delta_N = P_m \cdot \frac{1200}{N}$$

Para $N = 9$:
$$\Delta_{\text{mod}} = 4 \cdot \frac{1200}{9} = 533.33\text{ cents}$$
Para $N = 11$:
$$\Delta_{\text{mod}} = 4 \cdot \frac{1200}{11} = 436.36\text{ cents}$$

Estos desplazamientos definen modulaciones de paso neutro imposibles en sistemas pitagóricos convencionales, permitiendo el enlace sin fisuras entre regiones polares de la cadena.

---

## 2.5. Implementación Algorítmica (SuperCollider)

El siguiente script en SuperCollider implementa el motor de síntesis aditiva y conducción modal basado en las fórmulas del Capítulo 2: define la Cajita Central para $N=9$ y $N=11$, computa la escala $S_{p,N}$ en cents y Hertz, y ejecuta una secuencia parsimoniosa basada en la Matriz Dual $F_N$.

```supercollider
// ====================================================================
// THE CHAIN THEORY - ENGINE CAPÍTULO 2: N-ET & Voice Leading
// ====================================================================

(
s.waitForBoot({
    var calculateN_ET, playVoiceLeadingSequence;

    // Función constructora del espacio escalar y de la Cajita Central
    calculateN_ET = { |n = 9, baseFreq = 261.6255| // baseFreq = C4 (261.63 Hz)
        var pm, centralBox, scaleDegrees, centsArray, freqsArray;

        pm = (n / 2).floor.asInteger;

        // Selección de Cajita Central según derivaciones analíticas
        if(n == 9, {
            centralBox = [3, -1, 4, 0];
        }, {
            if(n == 11, {
                centralBox = [3, -2, 4, -1];
            }, {
                // Caso general Axiomático
                centralBox = [pm - 1, 0, pm, 1];
            });
        });

        // Generación de escala N-ET completa [0 .. N-1]
        scaleDegrees = (0 .. (n - 1));
        centsArray = scaleDegrees * (1200.0 / n);
        freqsArray = centsArray.collect { |c| baseFreq * (2.pow(c / 1200.0)) };

        (
            n: n,
            pm: pm,
            cajita: centralBox,
            cents: centsArray,
            freqs: freqsArray,
            stepCents: 1200.0 / n,
            residualIdx: n - 3
        )
    };

    // Sintetizador microtonal con envolvente armónica suave
    SynthDef(\chainOsc, { |out = 0, freq = 440, amp = 0.1, gate = 1, pan = 0, rel = 1.5|
        var sig, env;
        env = EnvGen.kr(Env.asr(0.05, 1, rel), gate, doneAction: Done.freeSelf);
        // Generador enriquecido armónicamente
        sig = SinOsc.ar(freq) * 0.7 + SinOsc.ar(freq * 2) * 0.2 + SinOsc.ar(freq * 3) * 0.1;
        sig = sig * env * amp;
        Out.ar(out, Pan2.ar(sig, pan));
    }).add;

    s.sync;

    // Rutina de demostración: Modulación y Voice Leading bi-eje en N=9 y N=11
    playVoiceLeadingSequence = {
        Routine({
            [9, 11].do { |currentN|
                var netData, freqs, rM_idx, rm_idx, residual_idx;
                
                netData = calculateN_ET.value(currentN, 220.0); // La 220 Hz base (A3)
                freqs = netData.freqs;
                rM_idx = 0;
                rm_idx = netData.pm;
                residual_idx = netData.residualIdx;

                (">>> CARGANDO SISTEMA N-ET: " ++ currentN).postln;
                ("Paso elemental (cents): " ++ netData.stepCents).postln;
                ("Cajita Central: " ++ netData.cajita).postln;
                ("Acorde Residual S_N índice: " ++ residual_idx).postln;

                // 1. Acorde Eje Mayor (Tónica r_M, Dominante c=+1, Subdominante c=-1)
                "1. Emitiendo Eje Mayor (r_M)...".postln;
                [
                    freqs[rM_idx.wrap(0, currentN - 1)],
                    freqs[(rM_idx + 1).wrap(0, currentN - 1)],
                    freqs[(rM_idx - 1).wrap(0, currentN - 1)]
                ].collect { |f| Synth(\chainOsc, [\freq, f, \amp, 0.08, \rel, 2.0]) };

                2.5.wait;

                // 2. Modulación microtonal parsimoniosa al Eje Menor (r_m)
                "2. Transición Parsimoniosa al Eje Menor (r_m)...".postln;
                [
                    freqs[rm_idx.wrap(0, currentN - 1)],
                    freqs[(rm_idx + 1).wrap(0, currentN - 1)],
                    freqs[(rm_idx - 1).wrap(0, currentN - 1)]
                ].collect { |f| Synth(\chainOsc, [\freq, f, \amp, 0.08, \rel, 2.0]) };

                2.5.wait;

                // 3. Polarización hacia el Acorde Simétrico Residual (S_N)
                "3. Polarización en Acorde Simétrico Residual...".postln;
                [
                    freqs[residual_idx.wrap(0, currentN - 1)],
                    freqs[(residual_idx + 2).wrap(0, currentN - 1)],
                    freqs[(residual_idx - 2).wrap(0, currentN - 1)]
                ].collect { |f| Synth(\chainOsc, [\freq, f, \amp, 0.08, \rel, 3.0]) };

                3.5.wait;
            };
            "DEMOSTRACIÓN TEÓRICA FINALIZADA.".postln;
        }).play;
    };

    // Iniciar ejecución
    playVoiceLeadingSequence.value;
});
)
```

---

## 2.6. Corolario Analítico: El Espacio Toroidal de las Cadenas

La proyección de $T_N$ en el continuo de afinación demuestra que la simetría de la **Cajita Central** trasciende la mera consonancia diádica. A través de la Matriz Operativa Bi-Eje $F_N$, el espacio adquiere una curvatura homóloga a un toroide no euclidiano $\mathbb{T}^2 \cong S^1 \times S^1$, en el cual:

1. El primer círculo de curvatura está gobernado por el ciclo del paso templado $\delta_N$, ordenado por el vector $S_{p,N}$.
2. El segundo círculo de curvatura se despliega mediante el salto axial constante $P_m = \lfloor N / 2 \rfloor$, posibilitando el intercambio instantáneo entre modalidades sin requerir una tonalidad diatónica de anclaje.
3. El **Acorde Simétrico Residual** ($S_N$), posicionado axiomáticamente en $N - 3$, opera como el punto de deflexión donde la polaridad modal colapsa, abriendo pasajes directos hacia macro-modulaciones en sistemas $N$-ET concurrentes.