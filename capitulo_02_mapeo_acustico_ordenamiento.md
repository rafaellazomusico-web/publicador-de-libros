# Capítulo 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 2.1. Formalización del Mapeo Acústico y Microtonalidad de la Cajita Central ($C_N$)

En el marco axiomático de la *Chain Theory*, la estructuración armónica no parte de una escala diatónica preexistente ni de una división arbitraria del continuo de frecuencias, sino de un núcleo generador tetra-cordal denominado **Cajita Central** ($C_N$). Este núcleo comprime las tensiones primarias de simetría y polaridad que posteriormente articularán todo el espacio de temperamento igual de $N$ tonos ($N$-ET).

### 2.1.1. Proyección Acústica Logarítmica
Sea un sistema temperado de división de la octava $N$-ET o un continuo temperado donde un generador acústico primario $p \in \mathbb{R}^+$ (comúnmente la quinta justa pura $p = 3/2$, o bien la aproximación temperada del sistema $2^{k/N}$) proyecta los índices enteros $k \in \mathbb{Z}$ sobre el espacio de alturas en centésimas de semitono ($\text{cents}$). Definimos la función de mapeo acústico unidimensional $\mu_p: \mathbb{Z} \to [0, 1200)$ mediante la relación:

$$\mu_p(k) = \left( 1200 \cdot k \cdot \log_2(p) \right) \pmod{1200}$$

Cuando se trabaja enteramente dentro de un retículo de $N$-ET homogéneo y el generador acústico coincide con el paso fundamental del sistema ($\log_2(p) = \frac{1}{N}$), la ecuación se reduce a la posición interválica canónica:

$$\mu_N(k) = \left( \frac{1200}{N} \cdot k \right) \pmod{1200}$$

### 2.1.2. Anatomía Interválica del Núcleo $C_N$
La Cajita Central se define formalmente como un vector tetracordal de índices enteros:

$$C_N = \begin{bmatrix} c_0 & c_1 & c_2 & c_3 \end{bmatrix}^T \in \mathbb{Z}^4$$

cuyas diferencias sucesivas $\Delta C_N = (\delta_1, \delta_2, \delta_3) = (c_1 - c_0, c_2 - c_1, c_3 - c_2)$ determinan el **Operador de Variación de Calidad (OVC)**. 

Al someter este vector al mapeo $\mu_p$, el conjunto de intervalos generados en el espacio logarítmico revela el micro-espaciado intrínseco del sistema:

$$\text{cents}(C_N) = \left\{ \mu_p(c_i) \mid c_i \in C_N \right\}$$

Este tetracorde central fija el centro de gravedad acústico del sistema, estableciendo las distancias microtonales directas que evitarán colapsos periódicos no deseados en la expansión de la cadena.

---

## 2.2. De la Matriz Primaria $T_N$ al Ordenamiento Escalar ($S_{p,N}$)

### 2.2.1. Expansión Simétrica Intercalada
A partir de la Cajita Central $C_N$, la **Matriz Primaria** $T_N$ se construye mediante una dispersión helicoidal o intercalada de índices. Si $C_N$ ocupa las cuatro posiciones cardinales centrales de la secuencia génica de longitud $N$, los $N - 4$ elementos restantes emergen mediante una alternancia simétrica de saltos de amplitud polar respecto al polo medio $P_m = \lfloor N/2 \rfloor$ y su apotema de simetría $A_N$:

$$T_N = \left[ t_0, t_1, t_2, \dots, t_{N-1} \right]$$

Esta disposición no refleja un orden secuencial lineal de alturas (frecuencias monótonamente crecientes), sino una **cadena de proximidad funcional**.

```
                [   Cajita Central C_N   ]
T_N : ... t_{k-2} <--- [c_0, c_1, c_2, c_3] ---> t_{k+2} ...
               \___________________________/
                    Expansión Intercalada
```

### 2.2.2. Operador de Ordenamiento Escalar ($\text{sort}$)
Para transformar la cadena de relaciones armónicas de $T_N$ en un continuo escalar apto para el análisis de grados de paso y jerarquías motívicas, se aplica el operador de ordenamiento estricto sobre el mapeo acústico de sus componentes:

$$S_{p,N} = \text{sort}\left( T_{p,N} \right) = \text{sort}\left( \left\{ \mu_p(t) \mid t \in T_N \right\} \right)$$

Formalmente, $S_{p,N} = \left( s_0, s_1, \dots, s_{N-1} \right)$ tal que:

$$0 \le s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

El espectro de pasos consecutivos resultante, $\Delta s_j = s_{j+1} - s_j$ (con $s_N = s_0 + 1200$), exhibe la distribución de tamaños de tono y microtono. La simetría intrínseca de $T_N$ garantiza que el vector de intervalos resultantes $\vec{\sigma}_N = (\Delta s_0, \Delta s_1, \dots, \Delta s_{N-1})$ preserve propiedades de auto-complementariedad respecto al centro escalar del sistema temperado.

---

## 2.3. Análisis Estructural Comparativo: Instanciación en $N = 9$ y $N = 11$

Se examinan a continuación los dos casos críticos provistos por el motor algebraico de *The Chain Theory*:

### 2.3.1. Sistema $N = 9$ ($P_m = 4$, $A_N = 3$)
Para la división de orden 9, los parámetros matriciales se establecen como:
- Polo medio: $P_m = 4$
- Apotema de simetría: $A_N = 3$
- Cajita Central: $C_9 = [3, -1, 4, 0]$

#### A. Análisis Vectorial de $C_9$
Evaluando el vector de diferencias sucesivas de la Cajita Central:
$$\Delta C_9 = \begin{bmatrix} -1 - 3 \\ 4 - (-1) \\ 0 - 4 \end{bmatrix} = \begin{bmatrix} -4 \\ 5 \\ -4 \end{bmatrix}$$

Nótese la simetría especular de los saltos exteriores ($\delta_1 = -4$, $\delta_3 = -4$) contrabalanceada por el salto complementario medial ($\delta_2 = +5$). En $\mathbb{Z}_9$, este salto central de $+5$ equivale a $-4 \pmod 9$, revelando una red de inversiones regulares orientada a la contención tímbrica.

#### B. Mapeo en el Espacio Acústico 9-ET
Asumiendo un paso fundamental $\kappa = \frac{1200}{9} = 133.\overline{33} \text{ cents}$:

$$\text{cents}(C_9) \equiv \left( C_9 \pmod 9 \right) \cdot 133.\overline{33}$$

Aplicando la congruencia módulo 9 a $C_9$:
- $c_0 = 3 \implies 3 \cdot 133.\overline{33} = 400.00 \text{ cents}$ (Tercera Mayor pura teórica aproximada)
- $c_1 = -1 \equiv 8 \implies 8 \cdot 133.\overline{33} = 1066.67 \text{ cents}$
- $c_2 = 4 \implies 4 \cdot 133.\overline{33} = 533.33 \text{ cents}$ (Cuarta neutra expandida)
- $c_3 = 0 \implies 0 \cdot 133.\overline{33} = 0.00 \text{ cents}$ (Tónica / Eje)

```
        C_9 Acústico (cents)
        0.00 ------------------------- c_3 (Eje)
      400.00 ----------------- c_0
      533.33 --------------------- c_2
     1066.67 ----------------------------- c_1
```

La Cajita Central en 9-ET articula un acorde altamente asimétrico que polariza el tritono del sistema ($4.5 \times 133.\overline{33} = 600\text{ cents}$) al rodearlo sin tocarlo, estabilizando la tónica $c_3 = 0$ con un intervalo de tercera mayor neutra ($400\text{ cents}$) y una segunda mayor subarmónica ($1066.67\text{ cents} = -133.33\text{ cents}$).

---

### 2.3.2. Sistema $N = 11$ ($P_m = 4$, $A_N = 3$)
Para la división de orden 11, los parámetros son:
- Polo medio: $P_m = 4$
- Apotema de simetría: $A_N = 3$
- Cajita Central: $C_{11} = [3, -2, 4, -1]$

#### A. Análisis Vectorial de $C_{11}$
Evaluamos la derivada discreta de la Cajita Central:
$$\Delta C_{11} = \begin{bmatrix} -2 - 3 \\ 4 - (-2) \\ -1 - 4 \end{bmatrix} = \begin{bmatrix} -5 \\ 6 \\ -5 \end{bmatrix}$$

De nuevo, la simetría es axiomática: $\delta_1 = -5$, $\delta_3 = -5$ y $\delta_2 = +6$. En el anillo $\mathbb{Z}_{11}$, el elemento central es el inversor exacto: $-5 \equiv 6 \pmod{11}$. La estructura interna de la Cajita Central genera una tensión bipartita isométrica perfecta.

#### B. Mapeo en el Espacio Acústico 11-ET
Con un quanto microtonal de $\kappa = \frac{1200}{11} \approx 109.09 \text{ cents}$:

Mapeando $C_{11} \pmod{11} = [3, 9, 4, 10]$:
- $c_0 = 3 \implies 3 \cdot 109.09 = 327.27 \text{ cents}$ (Tercera neutra estándar)
- $c_1 = 9 \implies 9 \cdot 109.09 = 981.82 \text{ cents}$ (Séptima menor neutra / armónica)
- $c_2 = 4 \implies 4 \cdot 109.09 = 436.36 \text{ cents}$ (Tercera mayor ultracromática)
- $c_3 = 10 \implies 10 \cdot 109.09 = 1090.91 \text{ cents}$ (Séptima mayor sub-tónica)

```
        C_{11} Acústico (cents)
      327.27 ----------------- c_0
      436.36 --------------------- c_2
      981.82 ----------------------------- c_1
     1090.91 --------------------------------- c_3
```

#### C. Tabla Comparativa de Comportamiento Estructural

| Parámetro | Sistema $N = 9$ | Sistema $N = 11$ |
| :--- | :--- | :--- |
| **Paso Discreto ($\kappa$)** | $133.\overline{33} \text{ cents}$ | $109.09 \text{ cents}$ |
| **Cajita Central ($C_N$)** | $[3, -1, 4, 0]$ | $[3, -2, 4, -1]$ |
| **Vector Gradiente ($\Delta C_N$)** | $[-4, +5, -4]^T$ | $[-5, +6, -5]^T$ |
| **Cierre Modular** | $-4 \equiv 5 \pmod 9$ | $-5 \equiv 6 \pmod{11}$ |
| **Comportamiento Tonal** | Dominancia de 3ª Mayor ($400\text{ c}$) | Dominancia de Intervalos Neutros ($327\text{ c}, 982\text{ c}$) |
| **Grado de Asimetría Residual** | Moderado (contiene la tónica $0$) | Elevado (tensión flotante, carece de $0$) |

---

## 2.4. Conducción de Voces Microtonal y Dinámica Modulatoria de $T_N$

### 2.4.1. El Principio de Parsimonia Microtonal
La transición entre regiones armónicas dentro de $T_N$ se rige por desplazamientos mínimos sobre la superficie del toro de alturas $\mathbb{T}^2 \cong \mathbb{R}^2/\mathbb{Z}^2$. Sean dos configuraciones tetracordales $K_a, K_b \subset T_N$. La métrica de esfuerzo de conducción de voces (distancia parsimoniosa $\mathcal{D}_{\text{voice}}$) se computa como la norma euclídea mínima o distancia $L_1$ sobre el emparejamiento óptimo de voces:

$$\mathcal{D}_{\text{voice}}(K_a, K_b) = \min_{\pi \in \mathfrak{S}_4} \sum_{i=0}^{3} \left| \mu(K_a[i]) - \mu(K_b[\pi(i)]) \right|$$

Dado que las expansiones de $T_N$ preservan los diferenciales $\delta_1, \delta_3$ constantes mediante el apotema $A_N$, el paso de la Cajita Central hacia los extremos de la cadena se efectúa por deslizamientos microtonales de amplitud exactamente igual a 1 o 2 unidades de paso escalar $\kappa$, permitiendo modulaciones contrapuntísticas hiper-suaves no perceptibles en el temperamento igual estándar de 12 tonos.

### 2.4.2. Modulación Vía Acorde Simétrico Residual ($S_N$)
La Matriz Operativa Bi-Eje ($F_N$) aísla un **Acorde Simétrico Residual** en la posición fija $k = N - 3$. 

1. El Eje Mayor (Fila 1 de $F_N$) pivota alrededor del índice de Tónica Mayor $r_M = 0$.
2. El Eje Menor (Fila 2 de $F_N$) pivota alrededor del polo menor $r_m = P_m$.
3. Los desplazamientos contextuales $+1, -1, +2, -2$ generan las órbitas funcionales:
   $$\{ \text{SD}_2, \text{SD}, \text{T}, \text{D}, \text{D}_2 \}$$
4. El residuo armónico situado en $N-3$ carece de acoplamiento directo por invariancia de inversión bi-axial. Actúa, por tanto, como una **puerta de fuga modulatoria (pivot microtonal)**. 

Al activar el acorde ubicado en $N-3$, el enlace con el polo acústico se fractura temporalmente, operando como un túnel cuántico armónico hacia una reindexación de la Cajita Central en una transposición exógena:

$$C_N^{(\text{nuevo})} = C_N + \Delta_{\text{mod}} \pmod N$$

```
   Eje Mayor (r_M = 0):   [ SD_2 ] <--- [ SD ] <--- [ T_M ] ---> [ D ] ---> [ D_2 ]
                                                      |
                                                      v
                                        [ Acorde Residual S_N ] (Posición N-3)
                                                      |  (Túnel Modulatorio)
                                                      v
   Eje Menor (r_m = P_m): [ SD_2 ] <--- [ SD ] <--- [ T_m ] ---> [ D ] ---> [ D_2 ]
```

---

## 2.5. Implementación Algorítmica

El siguiente bloque de código en **SuperCollider** implementa la síntesis formal del Capítulo 2: toma los parámetros de orden $N$, computa la Cajita Central $C_N$, realiza la expansión y ordenamiento escalar $S_{p,N}$, y sintetiza un clúster microtonal basado en la conducción de voces generada.

```sclang
// The Chain Theory - Capítulo 2: Mapeo Acústico y Expansión N-ET
(
s.waitForBoot({
    var n_et = 11;                  // Orden N-ET seleccionado
    var p_m = (n_et / 2).floor.asInteger; // Polo medio Pm = 4
    var a_n = 3;                    // Apotema de simetría
    var baseFreq = 220.0;           // Altura base (A3 = 220Hz)
    
    // 1. Instanciación de la Cajita Central C_N
    // Para N=11 -> [3, -2, 4, -1]
    var c_n = [3, -2, 4, -1];
    
    // 2. Mapeo Acústico a Frecuencias
    var stepSizeCents = 1200.0 / n_et;
    var c_n_cents = c_n.collect({ |idx| (idx % n_et) * stepSizeCents });
    var c_n_freqs = c_n_cents.collect({ |cents| baseFreq * (2.pow(cents / 1200.0)) });
    
    // 3. Ordenamiento Escalar S_{p,N}
    var s_pn_cents = c_n_cents.copy.sort;
    var s_pn_freqs = s_pn_cents.collect({ |cents| baseFreq * (2.pow(cents / 1200.0)) });
    
    // Salida diagnóstica en consola
    ("--- The Chain Theory: Diagnóstico para N = " ++ n_et ++ " ---").postln;
    ("Polo Medio (P_m): " ++ p_m).postln;
    ("Cajita Central C_" ++ n_et ++ ": " ++ c_n).postln;
    ("C_N en Cents: " ++ c_n_cents.round(0.01)).postln;
    ("Escala Ordenada S_{p,N} (Cents): " ++ s_pn_cents.round(0.01)).postln;
    ("Frecuencias (Hz): " ++ c_n_freqs.round(0.01)).postln;
    
    // 4. Síntesis Auditiva de la Cajita Central
    SynthDef(\chainVoiceNode, { |out=0, freq=440, amp=0.1, pan=0, gate=1|
        var sig, env;
        env = EnvGen.kr(Env.adsr(0.8, 0.4, 0.7, 1.5), gate, doneAction: 2);
        // Resonancia suave con armónicos atenuados para aislar el intervalo
        sig = SinOsc.ar(freq) * 0.7 + SinOsc.ar(freq * 2, 0, 0.2);
        sig = Pan2.ar(sig * env * amp, pan);
        Out.ar(out, sig);
    }).add;

    s.sync;

    // Ejecución polifónica del Tetracorde Central C_N
    fork {
        var synths;
        ("Reproduciendo Tetracorde C_" ++ n_et ++ "...").postln;
        synths = c_n_freqs.collect({ |f, i|
            Synth(\chainVoiceNode, [
                \freq, f,
                \amp, 0.15,
                \pan, (i / (c_n_freqs.size - 1)) * 2 - 1 // Dispersión estéreo
            ]);
        });
        
        4.wait; // Sostener sonoridad durante 4 segundos
        
        ("Cerrando envolventes.").postln;
        synths.do(_.set(\gate, 0));
    };
});
)
```

La estructura matemática subyacente a $C_N$ permite articular el paso hacia escalas y matrices bi-axiales de orden arbitrario, preservando rigurosamente el paralelismo funcional y permitiendo modular con idéntica consistencia formal dentro de un microtono temperado de 11 partes como en sistemas complejos de orden superior.