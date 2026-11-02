# Capítulo 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 2.1. El Isomorfismo Frecuencial y la Topología del Espacio Microtonal

En *The Chain Theory*, la transición desde la abstracción combinatoria de índices enteros hacia la manifestación física del sonido requiere formalizar un operador de proyección acústica. Definimos el espacio microtonal continuo como el cociente topológico $\mathbb{R} / 1200\mathbb{Z}$, correspondiente al toro unísono de octava continua calibrado en cents.

Dado un generador acústico primario $p \in \mathbb{R}^+$ (comúnmente un intervalo consonante no simplificado en la octava, verbigracia $p = 3/2$ para la consonancia de quinta justa pitagórica, o razones superparticulares más complejas como $5/4$ o $7/4$) y un conjunto discreto de índices de la cadena de transformación $T_N \subset \mathbb{Z}$, el **operador de mapeo acústico** $\phi_p: \mathbb{Z} \to [0, 1200)$ se define como:

$$\phi_p(k) = \left( 1200 \cdot k \cdot \log_2(p) \right) \pmod{1200}, \quad \forall k \in T_N$$

La imagen de la Matriz Primaria $T_N$ bajo $\phi_p$ define el conjunto de alturas absolutas $T_{p,N}$:

$$T_{p,N} = \{ \phi_p(k) \mid k \in T_N \}$$

Cuando el sistema se proyecta sobre una división igual de la octava ($N\text{-ET}$ o $N\text{-EDO}$), el parámetro continuo $\log_2(p)$ se sustituye por la aproximación racional canónica del generador dentro del anillo $\mathbb{Z}_N$. En un temperamento igual puro de $N$ particiones, el escalón elemental cuantizado $\operatorname{\text{step}}_N$ es trivialmente:

$$\operatorname{\text{step}}_N = \frac{1200}{N}$$

El mapeo de cualquier índice ordinal $k \in \mathbb{Z}_N$ al plano microtonal abstracto adopta la expresión lineal directa:

$$\psi_N(k) = \left( \frac{1200}{N} \cdot k \right) \pmod{1200}$$

La tensión armónica e interválica de *The Chain Theory* radica en la discrepancia inherente entre la rigidez cíclica del anillo $\mathbb{Z}_N$ y la microestructura acumulativa generada por la expansión de la cadena interválica.

---

## 2.2. La Cajita Central $C_N$ como Núcleo Generativo Interválico

El núcleo sintáctico de todo sistema de orden $N$ está constituido por la **Cajita Central** $C_N$, una 4-tupla de índices definida formalmente como:

$$C_N = (P_m - 1, \; 0, \; P_m, \; 1)$$

donde $P_m = \left\lfloor \frac{N}{2} \right\rfloor$ representa el polo menor del sistema. En implementaciones donde el espacio de proyección modular sufre desfases angulares calculados algorítmicamente mediante el módulo de rotación axial $A_N$, $C_N$ asume configuraciones específicas con traslaciones negativas en sus límites cíclicos.

### El Operador de Vector Armónico (OVC) y Deltas Estructurales

A partir de $C_N = (c_0, c_1, c_2, c_3)$, derivamos el **vector de diferencias finitas** o vector interválico generativo $\Delta C_N$:

$$\Delta C_N = (\delta_0, \delta_1, \delta_2) = (c_1 - c_0, \; c_2 - c_1, \; c_3 - c_2)$$

La proyección de estas distancias generativas sobre el mapeo acústico $\phi_p$ o $\psi_N$ determina las tres clases morfológicas de acordes primarios:

```
                  ┌─────────────────────────────────────┐
                  │          Cajita Central C_N         │
                  │   (c_0,   c_1,     c_2,     c_3)    │
                  └──────┬──────────────┬───────────────┘
                         │              │
             ┌───────────┴────────┐     └────────────┐
             ▼                    ▼                  ▼
      Sub-tríada Mayor     Sub-tríada Menor    Tétrada Residual
     (c_1, c_2, c_3)       (c_0, c_1, c_2)     (c_0, c_1, c_2, c_3)
      Δ_M = (c_2-c_1,       Δ_m = (c_1-c_0,     Δ_S = (δ_0, δ_1, δ_2)
             c_3-c_2)              c_2-c_1)
```

1. **Calidad Mayor ($M$):** Sub-vector derivado de la tríada superior $(c_1, c_2, c_3) = (0, P_m, 1)$. En el dominio interválico, define el paso generativo ascendente de polo neutro hacia polo menor ($P_m - 0$) y de polo menor a grado unitario ($1 - P_m$). Acústicamente, este vector induce una polaridad consonante abierta.
2. **Calidad Menor ($m$):** Sub-vector derivado de la tríada inferior $(c_0, c_1, c_2) = (P_m - 1, 0, P_m)$. Contiene el intervalo complementario inducido por la relación $(-P_m + 1, P_m)$, configurando una distribución espectral densificada alrededor del polo $P_m$.
3. **Calidad Simétrica Residual ($S$):** El complejo tetrádico integral $C_N$. Sus propiedades de simetría axial generan un baricentro acústico que no pertenece a los atractores mayor ni menor canónicos, actuando como pivote no resolutivo en el espacio interválico.

---

## 2.3. Ordenamiento Escalar $S_{p,N}$ y Simetrías de Cadena

La cadena $T_N$ se despliega mediante una expansión simétrica intercalada que alterna oscilaciones radiales a partir del eje central $C_N$:

$$T_N = \left( k_0, k_1, k_2, \dots, k_{N-1} \right)$$

Este orden de generación temporal o generativo no es monótono respecto al tono fundamental. Por tanto, es axiomático diferenciar la *cadena generativa* de la *escala resultante*.

El **ordenamiento escalar** $S_{p,N}$ se define formalmente como la ordenación monotónica estricta del conjunto imagen acústico dentro del intervalo fundamental $[0, 1200)$:

$$S_{p,N} = \operatorname{sort}(T_{p,N}) = \left( s_0, s_1, s_2, \dots, s_{N-1} \right)$$

tal que:

$$0 \le s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

### El Vector de Grados de Paso (Step-Size Vector)

Dada la escala $S_{p,N}$, definimos el vector de pasos escalares $\vec{\sigma}_{p,N}$:

$$\vec{\sigma}_{p,N} = \left( \sigma_0, \sigma_1, \dots, \sigma_{N-1} \right)$$

donde:

$$\sigma_i = s_{i+1} - s_i \quad (\text{para } 0 \le i < N-1), \qquad \sigma_{N-1} = (1200 + s_0) - s_{N-1}$$

En sistemas $N\text{-ET}$ proyectados mediante generadores pitagóricos o pseudo-pitagóricos, el vector $\vec{\sigma}_{p,N}$ exhibe la propiedad de **Momento de Simetría (MOS)**, particionando el espacio de la octava en como máximo dos o tres intervalos de paso discretos (pasos grandes $L$, pasos pequeños $s$, y pasos medios/ambiguos $\mu$).

La simetría bilateral de la cadena armónica impone que, si la Matriz Primaria $T_N$ es autoinversa bajo una reflexión respecto a su centro coordenado, el vector de pasos $\vec{\sigma}_{p,N}$ satisfará condiciones de palíndromo cíclico:

$$\sigma_i = \sigma_{(N-2-i) \pmod N}$$

---

## 2.4. Estudio de Casos Canónicos: $N = 9$ y $N = 11$

Analizaremos la formulación estricta para dos sistemas de cardinalidad impar provistos por el motor analítico, explorando sus configuraciones paramétricas, mapeos acústicos y matrices resultantes.

---

### Caso 1: Sistema $N = 9$

*Parámetros base:*
*   Cardinalidad: $N = 9$
*   Polo menor: $P_m = \left\lfloor \frac{9}{2} \right\rfloor = 4$
*   Módulo angular de rotación: $A_N = 3$
*   **Cajita Central calculada:** $C_9 = [3, -1, 4, 0]$

```
                     Sistema N = 9
      Índices C_9:   [  3,   -1,    4,    0 ]
                        \   /  \   /  \  /
      Deltas (ΔC_9):     -4     +5    -4
```

#### 1. Expansión y Cadena Generativa
La cadena $T_9$ parte de los cuatro elementos centrales de $C_9$ y se expande simétricamente hacia la periferia en $\mathbb{Z}_9$:

$$C_9 \equiv [3, 8, 4, 0] \pmod 9$$

Completando la órbita de 9 elementos según el algoritmo de intercalación radial convergente:

$$T_9 = [7, 2, 6, 3, 8, 4, 0, 5, 1]$$

#### 2. Mapeo Acústico ($p = 3/2$ en temperamento 9-EDO estándar)
El paso elemental para $N = 9$ es:

$$\operatorname{\text{step}}_9 = \frac{1200}{9} \approx 133.333 \text{ cents}$$

Calculamos los valores acústicos de cada elemento ordenado $k \in \mathbb{Z}_9$:

$$\psi_9(k) = k \cdot 133.333 \text{ cents}$$

| Índice ($k$) | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Cents** | $0.00$ | $133.33$ | $266.67$ | $400.00$ | $533.33$ | $666.67$ | $800.00$ | $933.33$ | $1066.67$ |

#### 3. Vector de Pasos e Intervalos de la Cajita
Evaluando $C_9 = [3, -1, 4, 0] \equiv [3, 8, 4, 0] \pmod 9$:
*   $c_0 = 3 \implies 400.00\text{ cents}$ (Tercera Mayor pitagórica pura en 9-ET)
*   $c_1 = 8 \implies 1066.67\text{ cents}$ (Séptima Menor sub-baja)
*   $c_2 = 4 \implies 533.33\text{ cents}$ (Cuarta aumentada / Quinta disminuida neutra)
*   $c_3 = 0 \implies 0.00\text{ cents}$ (Tónica / Unísono)

Deltas modulares en $\mathbb{Z}_9$:
$$\Delta C_9 = (8 - 3, \; 4 - 8, \; 0 - 4) \equiv (5, \; 5, \; 5) \pmod 9$$

Nótese que en el espacio $\mathbb{Z}_9$, los deltas exhiben una periodicidad isotrópica basada en el generador elemental $g = 5$, revelando que la Cajita Central en $N = 9$ opera acústicamente como una proyección equi-interválica hiper-simétrica de pasos de $5 \times 133.333 = 666.667\text{ cents}$ (el tritono/quinta neutra de 9-ET).

#### 4. Matriz Operativa Bi-Eje ($F_9$)
Construimos la matriz de funciones $F_9$ con los ejes centrados en $r_M = 0$ y $r_m = 4$. El acorde simétrico residual $S_9$ queda aislado en el índice cardinal $N - 3 = 6$:

$$F_9 = \begin{pmatrix}
\text{Eje Mayor } (r_M = 0): & SD_2 \; (k=7) & SD \; (k=8) & \mathbf{T} \; (k=0) & D \; (k=1) & D_2 \; (k=2) \\
\text{Eje Menor } (r_m = 4): & sd_2 \; (k=2) & sd \; (k=3) & \mathbf{t} \; (k=4) & d \; (k=5) & d_2 \; (k=6)
\end{pmatrix}$$

El elemento simétrico residual $S_9$ se extrae en el locus $k = 9 - 3 = 6$, que interseca funcionalmente con la dominante secundaria menor $d_2$, desestabilizando el cierre del eje secundario y forzando una fuga armónica microtonal.

---

### Caso 2: Sistema $N = 11$

*Parámetros base:*
*   Cardinalidad: $N = 11$
*   Polo menor: $P_m = 4$
*   Módulo angular de rotación: $A_N = 3$
*   **Cajita Central calculada:** $C_{11} = [3, -2, 4, -1]$

```
                     Sistema N = 11
      Índices C_11:  [  3,   -2,    4,   -1 ]
                        \   /  \   /  \  /
      Deltas (ΔC_11):    -5     +6    -5
```

#### 1. Expansión y Normalización Modular
Normalizamos la Cajita Central a $\mathbb{Z}_{11}$:

$$C_{11} = [3, -2, 4, -1] \equiv [3, 9, 4, 10] \pmod{11}$$

Deltas modulares en $\mathbb{Z}_{11}$:
$$\delta_0 = 9 - 3 = 6$$
$$\delta_1 = 4 - 9 = -5 \equiv 6 \pmod{11}$$
$$\delta_2 = 10 - 4 = 6$$

$$\Delta C_{11} = (6, 6, 6) \pmod{11}$$

La Cajita Central en $N = 11$ genera un acoplamiento coherente: el intervalo generador es unívocamente $6 \times \frac{1200}{11} \approx 654.545\text{ cents}$ (el tritono extendido de 11-ET).

#### 2. Mapeo Acústico (11-ET)
El paso elemental para $N = 11$ es:

$$\operatorname{\text{step}}_{11} = \frac{1200}{11} \approx 109.091\text{ cents}$$

| Índice ($k$) | Cents | Índice ($k$) | Cents |
| :---: | :---: | :---: | :---: |
| **0** | $0.00$ | **6** | $654.55$ |
| **1** | $109.09$ | **7** | $763.64$ |
| **2** | $218.18$ | **8** | $872.73$ |
| **3** | $327.27$ | **9** | $981.82$ |
| **4** | $436.36$ | **10** | $1090.91$ |
| **5** | $545.45$ | | |

#### 3. Análisis Estructural de la Escala $S_{p, 11}$
Mapeando $C_{11}$ a cents continuos:
*   $c_0 = 3 \implies 327.27\text{ cents}$ (Tercera menor neutra / Intervalo sub-menor)
*   $c_1 = 9 \implies 981.82\text{ cents}$ (Séptima menor neutra / Armónico 7 deformado)
*   $c_2 = 4 \implies 436.36\text{ cents}$ (Tercera mayor superdensa)
*   $c_3 = 10 \implies 1090.91\text{ cents}$ (Séptima mayor baja)

El conjunto generado despliega una escala simétrica de 11 sonidos donde no existen ni la quinta justa temperada ($700\text{ cents}$) ni la cuarta justa ($500\text{ cents}$); el sistema gravita alrededor de la polaridad $\approx 436.36\text{ cents}$ y $\approx 654.55\text{ cents}$, generando una gramática puramente intrínseca a la física de 11-ET.

#### 4. Matriz Operativa Bi-Eje ($F_{11}$)
Con $r_M = 0$, $r_m = 4$, y residuo aislado $S_{11}$ en $N - 3 = 8$:

$$F_{11} = \begin{pmatrix}
\text{Eje Mayor } (r_M = 0): & SD_2 \; (k=9) & SD \; (k=10) & \mathbf{T} \; (k=0) & D \; (k=1) & D_2 \; (k=2) \\
\text{Eje Menor } (r_m = 4): & sd_2 \; (k=2) & sd \; (k=3) & \mathbf{t} \; (k=4) & d \; (k=5) & d_2 \; (k=6)
\end{pmatrix}$$

El elemento simétrico $S_{11}$ ($k = 8$) queda exterior a la proyección inmediata de ambas funciones tónicas y dominantes primarias, operando como un **agujero negro armónico** que media entre las modulaciones no enarmónicas:

```
    Eje Mayor:  [9] <──> [10] <──> [ 0 ] <──> [1] <──> [2]
                                     ▲                 ▲
                                     │     S_{11}      │
                                     │     [ 8 ]       │
                                     ▼                 ▼
    Eje Menor:  [2] <──> [ 3] <──> [ 4 ] <──> [5] <──> [6]
```

---

## 2.5. El Acorde Transformante $T_N$: Conducción de Voces y Modulaciones Microtonales

El constructo fundamental de transición armónica en esta teoría es el **Acorde Transformante** $T_N$. A diferencia de un acorde pivote diatónico clásico, $T_N$ es una entidad multicapa móvil cuyos vectores directores fuerzan un desplazamiento parsimonioso mínimo (*Minimal Parsimonious Voice Leading*) a lo largo de las trayectorias topológicas de la matriz $F_N$.

### Métrica de Conducción de Voces Microtonal

Definimos la distancia de conducción de voces $D_{\text{VL}}$ entre dos complejos armónicos $A, B \subset \mathbb{Z}_N$ de igual cardinalidad $m$ mediante el acoplamiento biespectral optimizado sobre el toro de alturas:

$$D_{\text{VL}}(A, B) = \min_{\pi \in \mathfrak{S}_m} \sum_{i=1}^{m} \operatorname{dist}_N(A_i, B_{\pi(i)})$$

donde $\operatorname{dist}_N(x, y) = \min(|x - y|, N - |x - y|)$ representa la distancia geodésica en el grafo cíclico $\mathbb{Z}_N$, y $\mathfrak{S}_m$ es el grupo simétrico de permutaciones de tamaño $m$.

El Acorde Transformante $T_N(c)$ correspondiente a un desplazamiento funcional $c \in \mathbb{Z}$ a lo largo de la matriz $F_N$ se define formalmente como:

$$T_N(c) = C_N \oplus c = (c_0 + c, \; c_1 + c, \; c_2 + c, \; c_3 + c) \pmod N$$

### Modulación Bi-Eje Vectorial

La modulación entre el Eje Mayor y el Eje Menor se ejecuta a través de la intersección funcional de $T_N(c)$. Observando las matrices $F_9$ y $F_{11}$, los nodos de colisión cromática (p. ej., $k = 2$ en $F_9$, que ejerce simultáneamente como $D_2$ Mayor y $sd_2$ Menor) definen **hiper-pivotes interválicos**.

El vector de traslación que conmuta el eje mayor al eje menor está parametrizado por el vector de fase:

$$\vec{\omega}_{M \to m} = (P_m - r_M) \equiv P_m \pmod N$$

En $N = 11$, esta traslación equivale a un salto de $+4$ pasos de escala ($+436.36\text{ cents}$). Una modulación gobernada por el Acorde Transformante despliega las cuatro voces de la siguiente manera:

```
C_11 (Tónica Mayor)     ──────────>     C_11 ⊕ 4 (Tónica Menor)
c_0 = 3   (327.3¢)      ──[ +436.4¢ ]──>     7   (763.6¢)
c_1 = 9   (981.8¢)      ──[ +436.4¢ ]──>     2   (218.2¢)
c_2 = 4   (436.4¢)      ──[ +436.4¢ ]──>     8   (872.7¢)  <-- Absorción por S_11
c_3 = 10 (1090.9¢)      ──[ +436.4¢ ]──>     3   (327.3¢)
```

Nótese que la voz que parte de $c_2 = 4$ colisiona con el nodo residual aislado $S_{11} = 8$, transfiriendo la energía armónica de la cadena hacia el espacio espectral no polarizado.

---

## 2.6. Implementación Algorítmica en SuperCollider

El siguiente programa formaliza la síntesis de la escala $S_{p,N}$, la instanciación de la Cajita Central $C_N$, el mapeo en cents y el motor de conducción de voces para los sistemas $N = 9$ y $N = 11$ en el entorno de desarrollo SuperCollider 3.

```supercollider
// =====================================================================
// THE CHAIN THEORY: Motor de Mapeo Acústico y Conducción Escalar
// Módulo: N-ET Core Engine (N=9, N=11)
// =====================================================================

(
s.waitForBoot({
    var calculateChain = { |n, pm, c_init|
        var nSteps, scaleCents, cBoxCents, sortedScale;
        
        // 1. Vector de partición uniforme de la octava
        nSteps = (0..(n - 1));
        scaleCents = nSteps * (1200.0 / n);
        
        // 2. Mapeo modular de la Cajita Central
        cBoxCents = c_init.collect { |idx|
            var modIdx = idx.mod(n);
            scaleCents[modIdx];
        };
        
        // 3. Ordenamiento escalar canónico
        sortedScale = scaleCents.copy.sort;
        
        (
            n: n,
            pm: pm,
            cBoxIndices: c_init.mod(n),
            scaleCents: scaleCents,
            cBoxCents: cBoxCents,
            sortedScale: sortedScale,
            stepSize: 1200.0 / n
        );
    };

    // Computación de datos canónicos para N = 9 y N = 11
    ~sys9  = calculateChain.value(9,  4, [3, -1, 4,  0]);
    ~sys11 = calculateChain.value(11, 4, [3, -2, 4, -1]);

    "==================================================".postln;
    "SISTEMA N = 9:".postln;
    "Cajita Central C_9 (cents): %".format(~sys9.cBoxCents).postln;
    "Paso de Escala: % cents".format(~sys9.stepSize).postln;
    "--------------------------------------------------".postln;
    "SISTEMA N = 11:".postln;
    "Cajita Central C_11 (cents): %".format(~sys11.cBoxCents).postln;
    "Paso de Escala: % cents".format(~sys11.stepSize).postln;
    "==================================================".postln;

    // SynthDef para síntesis aditiva microtonal estricta
    SynthDef(\chainVoice, { |out = 0, freq = 440, amp = 0.1, gate = 1, pan = 0, rel = 3.0|
        var env, sig;
        env = EnvGen.kr(Env.asr(releaseTime: rel), gate, doneAction: Done.freeSelf);
        sig = SinOsc.ar(freq) * env * amp;
        sig = Pan2.ar(sig, pan);
        Out.ar(out, sig);
    }).add;

    s.sync;

    // Rutina de demostración: Modulación Par-Eje en N = 11 usando T_N
    Routine({
        var baseFreq = 220.0; // Fundamental: La 220Hz
        var nSys = ~sys11;
        var playChord = { |indices, dur = 4|
            var synths;
            var freqs = indices.collect { |idx|
                var modIdx = idx.mod(nSys.n);
                var cents = nSys.scaleCents[modIdx];
                baseFreq * (2.pow(cents / 1200.0));
            };
            
            "Reproduciendo Acorde T_11 (Índices: %) -> Frecuencias: %".format(indices, freqs.round(0.01)).postln;
            
            synths = freqs.collect { |f, i|
                Synth(\chainVoice, [
                    \freq, f, 
                    \amp, 0.08, 
                    \pan, ((i / (indices.size - 1)) * 2) - 1
                ]);
            };
            
            dur.wait;
            synths.do { |syn| syn.set(\gate, 0); };
        };

        1.wait;
        // 1. Acorde Tónica Mayor (C_11 base)
        playChord.value(nSys.cBoxIndices, 4);
        
        // 2. Modulación Par-Eje a Tónica Menor (Shift modular +Pm = +4)
        playChord.value(nSys.cBoxIndices + nSys.pm, 4);
        
        // 3. Resolución al Acorde Transformante del Residuo Simétrico S_11 (k=8)
        // Desplazamiento inducido que forza la colisión en el cluster residual
        playChord.value([8, 9, 2, 3], 6);

    }).play;
});
)
```

---

## 2.7. Conclusiones Estructurales

1. **Invarianza Isomorfa:** El comportamiento interválico derivado de la Cajita Central $C_N$ es independiente del sistema de afinación físico subyacente; las propiedades de simetría y resolución se conservan íntegramente en el espacio afín proyectivo $\mathbb{Z}_N$.
2. **Propiedades de Singularidad en Cardinalidades Impares:** Como demuestran los análisis de $N=9$ y $N=11$, los sistemas impares imponen la presencia ineludible de un centro residual simétrico disjunto ($S_N$ en el locus $N-3$). Este elemento impide la cristalización tonal binaria, asegurando una conducción microtonal dinámica que es el rasgo distintivo de la modulación bi-eje en *The Chain Theory*.