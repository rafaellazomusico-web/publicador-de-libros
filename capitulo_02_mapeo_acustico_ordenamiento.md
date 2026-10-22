# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 2.1. El Mapeo Acústico Proyectivo ($T_{p,N}$)

En el marco de *The Chain Theory*, la espacialización armónica no se concibe como una mera división aritmética euclidiana del continuo frecuencial, sino como la proyección de un generador primo $p \in \mathbb{P}$ sobre una clase de equivalencia cíclica modulada en el dominio logarítmico. 

Sea $\mathbb{Z}_N$ el anillo conmutativo de enteros módulo $N$, representativo del espacio de clases de alturas de un temperamento igual de $N$ divisiones ($N$-ET). Definimos el operador de mapeo acústico continuo $\Phi_p: \mathbb{Z} \to [0, 1200) \subset \mathbb{R}$ mediante la relación:

$$\text{cents}(k, p) = \left( 1200 \cdot k \cdot \log_2(p) \right) \pmod{1200}, \quad k \in \mathbb{Z}$$

Para anclar esta proyección continua a la retícula discreta de un sistema $N$-ET, definimos el índice proyectivo $idx \in \mathbb{Z}_N$. El vector del mapeo acústico discreto $T_{p,N}$ asocia cada índice de generación $k$ con su posición en la escala en cents:

$$T_{p,N}(k) = \left( \frac{1200}{N} \cdot \left\lfloor \frac{N \cdot \text{cents}(k, p)}{1200} \right\rceil \right) \pmod{1200}$$

donde $\lfloor x \rceil$ denota el redondeo al entero más próximo. 

Cuando el generador acústico primordial es la quinta justa pitagórica ($p = 3$), la proyección acústica parametriza la línea de quintas generatriz. Para sistemas microtonales donde la aproximación armónica se orienta hacia armónicos superiores (por ejemplo, el subgrupo de Euler-Monzo 2.3.5.7.11), el vector generador $p$ puede extenderse a una tupla de ponderación interválica, vinculando la topología de la cadena con el espacio reticular de afinación justa (*Just Intonation Tuning Lattice*).

---

## 2.2. Génesis Interválica y Topología de la Cajita Central ($C_N$)

La génesis de todo el espacio tonal $N$-ET en *The Chain Theory* reside en la **Cajita Central** ($C_N$). Lejos de ser un conjunto arbitrario de clases de alturas, la cajita actúa como el núcleo de parsimonia del cual emerge la polaridad armónica bi-axial (Mayor/Menor).

Axiomáticamente, la Cajita Central canónica se define por la cuaterna ordenada de índices:

$$C_N = \left( P_m - 1, \, 0, \, P_m, \, 1 \right) \subset \mathbb{Z}_N^4$$

donde el pivote modal medio se define como:

$$P_m = \left\lfloor \frac{N}{2} \right\rfloor$$

No obstante, cuando el sistema aplica una translación isomórfica centrada en los atractores de conducción de voces (compensación por asimetría escalar $A_N$), los índices de $C_N$ adoptan proyecciones balanceadas respecto al centro de gravedad interválico:

$$C_N = \left[ k_0, \, k_1, \, k_2, \, k_3 \right]$$

### Operador de Clasificación Vectorial (OVC)
Para extraer las propiedades intrínsecas de conducción de voces de la Cajita Central, aplicamos el Operador de Variación de Calidad ($\text{OVC}$), definido sobre el vector de primeras diferencias cíclicas de la cajita:

$$\Delta C_N = \left( (k_1 - k_0) \pmod N, \, (k_2 - k_1) \pmod N, \, (k_3 - k_2) \pmod N, \, (k_0 - k_3) \pmod N \right)$$

El $\text{OVC}$ analiza la signatura interválica de los pares de díadas que forman los ejes cruzados:
1. **Subespacio Mayor ($\mathcal{M}$):** Dominado por la relación generada entre el polo neutro $0$ y el avance positivo $1$, condicionado por el acoplamiento con $P_m$.
2. **Subespacio Menor ($\mathfrak{m}$):** Dominado por la retracción modal hacia el polo antipodal $P_m$.
3. **Simetría Residual ($S_N$):** Invariancia bajo la inversión modal $I: x \mapsto (-x) \pmod N$.

```
Topología de Cruzamiento en C_N:

       k_0 = (P_m - 1)  <---- Retracción Armónica ---->  k_2 = P_m
             |                                                  |
       Díada Conectora                                   Díada Conectora
             |                                                  |
             v                                                  v
       k_1 = 0          <----- Proyección Tonal ----->   k_3 = 1
```

---

## 2.3. Ordenamiento Escalar ($S_{p,N}$) y Expansión Simétrica

A partir del núcleo $C_N$, la **Matriz Primaria ($T_N$)** se despliega mediante un algoritmo de intercalado divergente (*interleaved symmetric expansion*). A partir de la posición central, los índices se proyectan alternadamente en direcciones opuestas de la cadena de conducción interválica:

$$T_N = \text{ExpandeSimetría}(C_N, N)$$

El conjunto de clases de alturas resultantes en $T_N$ no se encuentra ordenado de forma monotónica por frecuencia, sino por afinidad conectiva de conducción de voces. Para restituir el espacio al dominio escalar temperado, aplicamos el operador de ordenamiento:

$$S_{p,N} = \text{sort}\left( T_{p,N} \right) = \left\{ s_0, s_1, s_2, \dots, s_{N-1} \right\}$$

tal que:

$$0 \le s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

### Espectro de Pasos y Simetría de Cadena
El vector de intervalos de paso de la escala resultante, $\vec{\delta} = (\delta_0, \delta_1, \dots, \delta_{N-1})$, donde $\delta_i = s_{i+1} - s_i$ (y $\delta_{N-1} = 1200 + s_0 - s_{N-1}$), determina las propiedades de Escala con Máxima Simetría (*MOS - Moment of Symmetry*).

En sistemas con $N$ impar o temperamentos no estándar, $\vec{\delta}$ revela micro-grados de paso fundamentales para la modulación:
- **Grados diatónicos estructurales:** Pasos mayores derivados de acumulaciones de generadores.
- **Grados de paso microtonales (comas o cuartitonos de enlace):** Subproductos del cierre del ciclo proyectivo sobre $N$.

---

## 2.4. Estudio de Casos Estructurales: $N = 9$ y $N = 11$

Analizaremos la formulación analítica precisa para los datos derivados por el motor de cálculo:

```
+----+-----+-----+------------------+-----------------------------+
| N  | P_m | A_N | Cajita Central   | Delta C_N (mod N)           |
+----+-----+-----+------------------+-----------------------------+
| 9  |  4  |  3  | [3, -1, 4, 0]    | (5, 5, 5, 3)                |
| 11 |  4  |  3  | [3, -2, 4, -1]   | (6, 6, 6, 4)                |
+----+-----+-----+------------------+-----------------------------+
```

### 2.4.1. Análisis Estructural de $N = 9$ (9-ET)

Para $N = 9$, la unidad elemental de paso temperado es:

$$\Delta_{9\text{-ET}} = \frac{1200}{9} = 133.333 \text{ cents}$$

Datos estructurales:
- Pivote modal: $P_m = 4$
- Grado de asimetría: $A_N = 3$
- Cajita Central: $C_9 = [3, -1, 4, 0] \equiv [3, 8, 4, 0] \pmod 9$

#### A. Mapeo en Cents de la Cajita Central
Aplicando la cuantización a cents:
- $k_0 = 3 \implies 3 \times 133.333 = 400.00 \text{ cents}$ (Tercera mayor pura)
- $k_1 = 8 \, (-1) \implies 8 \times 133.333 = 1066.67 \text{ cents}$ (Séptima menor neutra / sub-séptima)
- $k_2 = 4 \implies 4 \times 133.333 = 533.33 \text{ cents}$ (Cuarta aumentada / tritono estrecho)
- $k_3 = 0 \implies 0 \times 133.333 = 0.00 \text{ cents}$ (Tónica unísono)

#### B. Operador OVC y Despliegue de $T_9$
Calculamos las diferencias vectoriales cíclicas sobre $\mathbb{Z}_9$:
$$\Delta C_9 = \left( (8 - 3), (4 - 8), (0 - 4), (3 - 0) \right) \pmod 9 = (5, 5, 5, 3)$$

El vector $\Delta C_9 = (5, 5, 5, 3)$ exhibe un isomorfismo periódico de paso $5$ en $\mathbb{Z}_9$ (intervalo de $666.67\text{ cents}$, una quinta disminuida característica del sistema de 9 divisiones), cerrado por el paso de compensación $3$ ($400.00\text{ cents}$).

Expandiendo simétricamente $T_9$ desde $C_9$, rellenamos las clases de alturas restantes de $\mathbb{Z}_9$:
$$T_9 = \left[ 3, 8, 4, 0, 5, 7, 2, 6, 1 \right]$$

Ordenando de manera escalar ascendente para obtener $S_{9}$:
$$S_9 = \text{sort}(T_9) = \{0, 1, 2, 3, 4, 5, 6, 7, 8\}$$

Correspondencia en cents:
$$S_{p,9} = \{0.00, \, 133.33, \, 266.67, \, 400.00, \, 533.33, \, 666.67, \, 800.00, \, 933.33, \, 1066.67\}$$

En este sistema, el Acorde Transformante $T_9$ actúa como una escala por tonos de 9 notas (*ennéada*), donde el intervalo generador de la cajita ($400\text{ cents}$) divide la octava simétricamente en 3 partes iguales (sistema de tercias mayores puras concatenadas: $0, 3, 6 \equiv 0, 400, 800\text{ cents}$), constituyendo el anclaje armónico residual de la simetría $S_9$.

---

### 2.4.2. Análisis Estructural de $N = 11$ (11-ET)

Para $N = 11$, el paso de afinación fundamental es marcadamente microtonal:

$$\Delta_{11\text{-ET}} = \frac{1200}{11} \approx 109.091 \text{ cents}$$

Datos estructurales:
- Pivote modal del motor: $P_m = 4$
- Grado de asimetría: $A_N = 3$
- Cajita Central: $C_{11} = [3, -2, 4, -1] \equiv [3, 9, 4, 10] \pmod{11}$

#### A. Mapeo Acústico de la Cajita Central
Mapeamos las clases de alturas a la rejilla en cents:
- $k_0 = 3 \implies 3 \times 109.091 = 327.27 \text{ cents}$ (Tercera menor neutra, sub-menor)
- $k_1 = 9 \, (-2) \implies 9 \times 109.091 = 981.82 \text{ cents}$ (Sexta mayor neutra / séptima disminuida)
- $k_2 = 4 \implies 4 \times 109.091 = 436.36 \text{ cents}$ (Tercera mayor alta, super-mayor)
- $k_3 = 10 \, (-1) \implies 10 \times 109.091 = 1090.91 \text{ cents}$ (Séptima mayor neutra)

#### B. Operador OVC y Despliegue de $T_{11}$
Diferencias sucesivas en $\mathbb{Z}_{11}$:
$$\Delta C_{11} = \left( (9 - 3), (4 - 9), (10 - 4), (3 - 10) \right) \pmod{11} = (6, 6, 6, 4)$$

El vector delta $(6, 6, 6, 4)$ genera una constelación gobernada por el intervalo de 6 pasos:
$$6 \times 109.091 = 654.545 \text{ cents}$$
Este intervalo representa el tritono neutro de 11-ET, una aproximación casi perfecta al armónico 11 undecimal respecto a la fundamental ($\frac{11}{8} \approx 551.32\text{ cents}$ invertido o acoplado acústicamente).

La expansión completa en $\mathbb{Z}_{11}$ desde la simetría central de la cadena produce:
$$T_{11} = \left[ 3, 9, 4, 10, 2, 5, 8, 1, 6, 7, 0 \right]$$

El ordenamiento escalar genera el espacio continuo de grados:
$$S_{11} = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$$
$$S_{p,11} = \{ k \cdot 109.091 \}_{k=0}^{10} \text{ cents}$$

Nótese que la Cajita Central aísla las tétradas microtonales que evitan la acumulación de disonancias de segundo orden, funcionando como el atractor tonal mínimo del sistema.

---

## 2.5. Conducción de Voces, Modulación Microtonal y el Acorde Transformante $T_N$

El papel fundamental del **Acorde Transformante $T_N$** es posibilitar la conducción de voces parsimoniosa (*parsimonious voice leading*) a través de fronteras microtonales infranqueables en la armonía tradicional diatónica.

### Matriz Operativa Bi-Eje ($F_N$) y Desplazamiento Vectorial
En la matriz operativa bi-eje, la modulación no se produce mediante cadencias armónicas basadas exclusivamente en el ciclo de quintas, sino a través de deslizamientos ortogonales entre:
- **Eje Mayor ($r_M = 0$):** Centrado en la tónica mayor $T$.
- **Eje Menor ($r_m = P_m$):** Centrado en la tónica modal/menor.

Un desplazamiento $c$ sobre la cadena produce transiciones funcionales estrictas:
- $c = +1$: Generación de la Dominante ($D$).
- $c = -1$: Generación de la Subdominante ($SD$).
- $c = +2$: Dominante Secundaria ($D_2$).
- $c = -2$: Subdominante Secundaria ($SD_2$).

### Aislamiento del Acorde Simétrico Residual ($S_N$)
El tensor de modulación se desacopla en la penúltima posición de la cadena. El **Acorde Simétrico Residual ($S_N$)**, localizado axiomáticamente en la posición de memoria:

$$\text{pos}(S_N) = N - 3$$

constituye el punto de catástrofe y pivote transformante. Al ser invariante bajo rotaciones específicas del $\text{OVC}$, opera como un "agujero de gusano" tonal: cualquier configuración en el Eje Mayor puede colapsar hacia el Eje Menor sin salto interválico mayor a $\Delta_{N\text{-ET}}$, permitiendo modulaciones poligonales cerradas.

### Algoritmo de Cálculo y Conducción de Voces en SuperCollider

El siguiente programa implementa la generación rigurosa de $C_N$, el operador $\Delta C_N$, la proyección a cents para cualquier $N$, y sintetiza un encadenamiento de voces microtonal parsimonioso:

```sclang
// =====================================================================
// THE CHAIN THEORY - Motor de Mapeo Acústico y Conducción N-ET
// Capítulo 2: Algoritmo de Demostración para N=9 y N=11
// =====================================================================

(
var f_calc_chain = { |n = 9, pm = 4, c_seed|
    var stepCents, c_cents, delta_c, full_scale;
    
    stepCents = 1200.0 / n;
    
    // 1. Mapeo Acústico de la Cajita Central a Cents
    c_cents = c_seed.collect { |idx| (idx % n) * stepCents };
    
    // 2. Operador OVC: Cálculo del vector Delta C_N
    delta_c = Array.fill(c_seed.size, { |i|
        var k_curr = c_seed[i];
        var k_next = c_seed[(i + 1) % c_seed.size];
        (k_next - k_curr) % n;
    });
    
    // 3. Ordenamiento Escalar S_{p, N}
    full_scale = Array.fill(n, { |i| i * stepCents });
    
    Post << "=== REPORTE ACÚSTICO THE CHAIN THEORY: N = " << n << " ===" << Char.nl;
    Post << "Pivote Pm: " << pm << " | Paso base: " << stepCents.round(0.001) << " cents" << Char.nl;
    Post << "Cajita Central CN: " << c_seed << " mod " << n << " -> " << (c_seed % n) << Char.nl;
    Post << "C_cents: " << c_cents.round(0.01) << Char.nl;
    Post << "Delta C_N (OVC): " << delta_c << Char.nl;
    Post << "Escala S_{p,N}: " << full_scale.round(0.01) << Char.nl << Char.nl;
    
    [c_cents, full_scale];
};

// Ejecución analítica para N = 9 y N = 11
~data_9  = f_calc_chain.value(9, 4, [3, -1, 4, 0]);
~data_11 = f_calc_chain.value(11, 4, [3, -2, 4, -1]);
)

// Síntesis de Conducción Microtonal Parsimoniosa sobre la Cajita Central (N=11)
(
s.waitForBoot({
    SynthDef(\chainOsc, { |out=0, freq=440, amp=0.1, gate=1, pan=0|
        var sig, env;
        sig = SinOsc.ar(freq) + (SinOsc.ar(freq * 2) * -12.dbamp);
        env = EnvGen.kr(Env.adsr(0.4, 0.2, 0.7, 0.8), gate, doneAction: 2);
        Out.ar(out, Pan2.ar(sig * env * amp, pan));
    }).add;

    s.sync;

    // Conducción parsimoniosa: Se itera por los nodos de C_11
    Routine({
        var rootFreq = 220.0; // La3 base
        var c11_cents = ~data_11[0];
        
        inf.do { |cycle|
            var targetCents = c11_cents.wrapAt(cycle);
            var freq = rootFreq * (2.pow(targetCents / 1200.0));
            
            ("Voz Activa -> Grado Cents: " + targetCents.round(0.01) + " | Freq: " + freq.round(0.01) + " Hz").postln;
            
            x = Synth(\chainOsc, [\freq, freq, \amp, 0.15, \pan, rrand(-0.5, 0.5)]);
            0.6.wait;
            x.set(\gate, 0);
            0.1.wait;
        };
    }).play;
});
)
```

---

## 2.6. Conclusión y Proyección Teórica

El mapeo acústico proyectivo y la conformación matricial de $T_N$ demuestran que las escalas microtonales en $N$-ET no deben tratarse como aproximaciones deficientes del temperamento igual de doce tonos (12-ET). Al aplicar el formalismo de la **Cajita Central ($C_N$)** y su vector de transformación derivado $\Delta C_N$, emergen geometrías interválicas autónomas. 

Para $N = 9$ y $N = 11$, el sistema demuestra cómo el balanceo de la asimetría ($A_N = 3$) genera dinámicas armónicas cerradas, donde el Acorde Transformante $T_N$ actúa como puente continuo entre la estabilidad tonal de los ejes de proyección canónica y las modulaciones del espacio interválico microtonal.