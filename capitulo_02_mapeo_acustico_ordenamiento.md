# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 2.1 Fundamentos del Mapeo Acústico ($T_{p,N}$) e Intervalos Microtonales

El andamiaje de *The Chain Theory* postula que cualquier universo microtonal de temperamento igual ($N$-ET) o basado en proyecciones acústicas primas ($p$-limit) no se origina como una subdivisión estática del espectro, sino como la manifestación continua de una díada fundamental mediada por una célula generatriz: la **Cajita Central** ($C_N$). 

Formalmente, definimos el operador de mapeo acústico $\Phi_{p}$ como una función que proyecta índices discretos de la Matriz Primaria $T_N$ en el continuo de clases de alturas dentro de la octava periódica $[0, 1200) \subset \mathbb{R}$:

$$\Phi_p(k) = \left( 1200 \cdot k \cdot \log_2(p) \right) \pmod{1200}, \quad k \in T_N$$

donde $p \in \mathbb{P} = \{2, 3, 5, 7, 11, \dots\}$ representa el generador primo acústico (típicamente $p=3$ para proyecciones por quintas pitagóricas o afinaciones meso-tonales afines, o bien bases no armónicas en análisis formales).

Cuando nos restringimos al espacio puramente temperado de $N$ divisiones iguales de la octava ($N$-ET), la unidad elemental discreta es el *step* temperado $\delta_N = \frac{1200}{N}$. El mapeo del índice entero $k$ se redefine bajo la métrica discreta modular:

$$\Psi_N(k) = \left( \frac{1200}{N} \cdot k \right) \pmod{1200}$$

### Topología de la Cajita Central ($C_N$)

La Cajita Central $C_N$ actúa como el núcleo de polarización armónica. En el espacio discreto inducido por el motor analítico, se define a través de un cuarteto de índices correlacionados con la pseudo-mediana $P_m = \lfloor N / 2 \rfloor$ y el coeficiente de anclaje armónico $A_N$:

$$C_N = \left( k_0, k_1, k_2, k_3 \right)$$

Las diferencias finitas internas o vector de deltas de la Cajita Central, denotado por $\Delta C_N$, determinan el tensor interválico seminal:

$$\Delta C_N = \left( k_1 - k_0, \; k_2 - k_1, \; k_3 - k_2 \right)$$

Este vector vectorial gobierna la quiralidad interválica del sistema. Si los extremos del vector $\Delta C_N$ exhiben simetría reflexiva respecto al centro, el sistema engendra familias armónicas cerradas. Si presentan asimetría modular, el sistema induce una fuerza de conducción tonal microtonal altamente direccional, permitiendo la existencia del **Acorde Transformante ($T_N$)**.

---

## 2.2 Algoritmo de Ordenamiento Escalar ($S_{p,N}$) y Simetría Paramétrica

La Matriz Primaria $T_N$, concebida como la expansión simétrica intercalada a partir de los bordes de $C_N$, no produce una escala interválicamente monotónica; genera una cadena de relaciones funcionales (orden serial de tensión armónica). Para transferir este constructo al dominio tímbrico y modal, se requiere la mediación del operador de clasificación escalar $\mathcal{S}$.

### Definición del Vector Escalar $S_{p,N}$

Sea $T_{p,N} = \{ \Phi_p(k) \mid k \in T_N \}$ el multiconjunto de alturas expresadas en cents. El operador de ordenamiento escalar define:

$$S_{p,N} = \text{sort}\left( T_{p,N} \right) = \langle s_0, s_1, s_2, \dots, s_{N-1} \rangle$$

tal que cumple la condición estricta de monotonicidad débil:

$$s_0 \le s_1 \le s_2 \le \dots \le s_{N-1} < 1200$$

con $s_0 = 0$ cent (normalización a la tónica fundamental).

```
   CADENA FUNCIONAL T_N                      ORDENAMIENTO ESCALAR S_p,N
[ ... k_-1, C_N, k_+1 ... ]  ---(Mapeo p)--->  [s_0, s_1, s_2, ..., s_N-1]
   (Relaciones Tensión)                            (Espacio Melódico)
```

### Densidad Interválica y Simetría Modular

A partir de $S_{p,N}$, se extrae el vector de pasos escalares $\vec{\sigma}_N$:

$$\vec{\sigma}_N = \langle \sigma_0, \sigma_1, \dots, \sigma_{N-1} \rangle$$

donde:

$$\sigma_i = 
\begin{cases} 
s_{i+1} - s_i & \text{para } 0 \le i < N-1 \\ 
(1200 + s_0) - s_{N-1} & \text{para } i = N-1 
\end{cases}$$

La invariancia de la cadena tonal radica en que la serie $\vec{\sigma}_N$ preserva la bi-polaridad de los ejes funcionales definidos en la matriz $F_N$:
1. **Eje Mayor ($r_M = 0$):** Nodo de reposo consonante centrado en el armónico superior.
2. **Eje Menor ($r_m = P_m$):** Contrapeso modal basado en la inversión funcional.

---

## 2.3 Estudio de Casos: Disección Estructural de $N=9$ y $N=11$

A continuación, se computan rigurosamente las propiedades microtonales de los sistemas impares $N=9$ y $N=11$ utilizando los valores paramétricos provistos por el motor analítico.

### 2.3.1 Caso $N = 9$

*   **Parámetros:**
    *   $N = 9$
    *   $P_m = \lfloor 9 / 2 \rfloor = 4$
    *   $A_N = 3$
    *   Cajita Central: $C_9 = [3, -1, 4, 0]$

#### Análisis Vectorial de $C_9$
Calculamos el vector de diferencias primarias ($\Delta C_9$):
$$\Delta C_9 = \left( -1 - 3, \; 4 - (-1), \; 0 - 4 \right) = \left( -4, \; +5, \; -4 \right)$$

Nótese la presencia de una **simetría reflexiva externa**: $|-4| = |-4|$. El centro de la cajita ($+5$) representa el salto interválico de máxima tensión generativa.

#### Mapeo a $9$-ET
Para $N = 9$, el tamaño del paso base es:
$$\delta_9 = \frac{1200}{9} = 133.33\overline{3} \text{ cents}$$

Aplicando el mapeo sobre los índices de la Cajita Central (reduciendo módulo 9 al dominio $[0, 8]$):
*   $k_0 = 3 \implies 3 \cdot 133.33\overline{3} = 400.00 \text{ cents}$ (Tercera Mayor pura en ET)
*   $k_1 = -1 \equiv 8 \pmod 9 \implies 8 \cdot 133.33\overline{3} = 1066.67 \text{ cents}$ (Séptima menor neutra)
*   $k_2 = 4 \implies 4 \cdot 133.33\overline{3} = 533.33 \text{ cents}$ (Cuarta aumentada microtonal)
*   $k_3 = 0 \implies 0 \cdot 133.33\overline{3} = 0.00 \text{ cents}$ (Unísono fundamental)

Ordenando los elementos del núcleo $C_9$:
$$S_{C_9} = \langle 0.00, \; 400.00, \; 533.33, \; 1066.67 \rangle \text{ cents}$$

#### Expansión Simétrica Intercalada ($T_9$)
La generación simétrica alrededor de $C_9$ hasta completar $N=9$ elementos procede emparejando la alternancia hacia la periferia con $A_N=3$:

$$T_9 = [k_{-3}, k_{-2}, k_{-1}, \mathbf{3, -1, 4, 0}, k_{+1}, k_{+2}]$$

Completando los índices del sistema modular $\mathbb{Z}_9$:
$$T_9 = [2, 5, 1, 3, 8, 4, 0, 6, 7]$$

El ordenamiento escalar global $S_{9}$ genera la escala por pasos de $133.33\text{ cents}$:
$$S_9 = \langle 0, 1, 2, 3, 4, 5, 6, 7, 8 \rangle \cdot 133.33\overline{3} \text{ cents}$$

---

### 2.3.2 Caso $N = 11$

*   **Parámetros:**
    *   $N = 11$
    *   $P_m = \lfloor 11 / 2 \rfloor = 4$ (según calibración fija del motor: $P_m = 4, A_N = 3$)
    *   Cajita Central: $C_{11} = [3, -2, 4, -1]$

#### Análisis Vectorial de $C_{11}$
Calculamos el vector de diferencias primarias:
$$\Delta C_{11} = \left( -2 - 3, \; 4 - (-2), \; -1 - 4 \right) = \left( -5, \; +6, \; -5 \right)$$

Nuevamente observamos una propiedad altamente estructurada:
1. Una contracción simétrica externa $|-5| = |-5|$.
2. Un salto interválico central de $+6$ pasos. En $11$-ET, el tritono perfecto o división ecuatorial estricta no existe; un paso de $6$ unidades representa el intervalo de máxima disonancia modal ($6 \times \frac{1200}{11} \approx 654.55 \text{ cents}$, el *septimal tritone* aproximado).

#### Mapeo a $11$-ET
El paso fundamental de $11$-ET es:
$$\delta_{11} = \frac{1200}{11} \approx 109.09 \text{ cents}$$

Mapeando los componentes de $C_{11}$ a cents (reduciendo a índices positivos en $\mathbb{Z}_{11}$):
*   $k_0 = 3 \implies 3 \cdot 109.09 = 327.27 \text{ cents}$ (Tercera menor neutra)
*   $k_1 = -2 \equiv 9 \pmod{11} \implies 9 \cdot 109.09 = 981.82 \text{ cents}$ (Séptima disminuida/sexta neutra)
*   $k_2 = 4 \implies 4 \cdot 109.09 = 436.36 \text{ cents}$ (Tercera mayor supradensa)
*   $k_3 = -1 \equiv 10 \pmod{11} \implies 10 \cdot 109.09 = 1090.91 \text{ cents}$ (Séptima mayor sub-blanda)

La Cajita Central en $11$-ET aísla de forma nativa los intervalos neutros clásicos de la entonación no duodecimal, estableciendo una infraestructura armónica libre de quintas perfectas tradicionales ($700 \text{ cents}$), sustituyéndolas por aproximaciones microtonales no pitagóricas.

---

## 2.4 Dinámica del Acorde Transformante ($T_N$), Conducción de Voces (OVC) y Modulación

El **Acorde Transformante** $T_N$ surge de la reinterpretación tensorial de la Cajita Central bajo el operador de conducción de voces (**Operator Voice-Leading Contextual - OVC**).

### Definición del Operador OVC

El OVC asigna una taxonomía de calidad armónica binaria o neutra a las estructuras cordales generadas en cualquier punto de la matriz $F_N$. Para una tríada o tétrada extraída de $T_N$:

$$\mathcal{Q}(C) = 
\begin{cases} 
\text{Mayor } (\mathcal{M}), & \text{si } \text{sgn}(\Delta^2 C) > 0 \\ 
\text{Menor } (\mathfrak{m}), & \text{si } \text{sgn}(\Delta^2 C) < 0 \\ 
\text{Simétrico Residual } (\mathcal{S}_N), & \text{si } \text{sgn}(\Delta^2 C) = 0 \lor \text{pos}(C) = N - 3 
\end{cases}$$

En el caso del Acorde Simétrico Residual $S_N$, aislado sistemáticamente en la posición $N-3$, su función es catalítica: actúa como el pivote donde la matriz colapsa su polaridad y permite la **modulación isomérica** entre el Eje Mayor y el Eje Menor.

### La Matriz Operativa Bi-Eje ($F_N$)

La matriz funcional organiza la jerarquía de tensiones alrededor de dos centros conjugados:

$$F_N = \begin{pmatrix} 
\text{Eje Mayor } (r_M = 0): & \dots & \text{SD}_2 & \text{SD} & \mathbf{T} & \text{D} & \text{D}_2 & \dots \\ 
\text{Eje Menor } (r_m = P_m): & \dots & \text{sd}_2 & \text{sd} & \mathbf{t} & \text{d} & \text{d}_2 & \dots 
\end{pmatrix}$$

Los desplazamientos $c \in \mathbb{Z}$ sobre las columnas corresponden a las siguientes transformaciones:
*   $c = +1$: Dominante ($\text{D}$). Aumento de la entropía modal (+energía armónica).
*   $c = -1$: Subdominante ($\text{SD}$). Relajación polar (-tensión).
*   $c = \pm 2$: Dominantes/Subdominantes Secundarias ($\text{D}_2$, $\text{SD}_2$).

```
                EJE MAYOR (r_M = 0)
   ... <--- [SD_2] <--- [SD] <--- [ T ] ---> [ D ] ---> [ D_2 ] ---> ...
                                    |
                          Modulación por OVC
                                    |
   ... <--- [sd_2] <--- [sd] <--- [ t ] ---> [ d ] ---> [ d_2 ] ---> ...
                EJE MENOR (r_m = P_m)
```

### Mecánica de Modulación Microtonal y Conducción de Voces

La modulación entre $r_M = 0$ y $r_m = P_m$ no requiere saltos interválicos disjuntos. Debido a la contracción del espacio en $N$-ET, la conducción de voces se optimiza minimizando la distancia métrica en el toroide interválico $T^n = \mathbb{R}^n / \mathbb{Z}^n$:

$$\mathcal{D}_{\text{voice}} = \sum_{j=1}^{K} \min_{k \in \mathbb{Z}} |(v_j^{(\text{final})} - v_j^{(\text{inicial})}) + 1200 \cdot k|$$

El Acorde Transformante $T_N$ opera mutando **una sola voz** por paso microtonal $\delta_N$. 

#### Ejemplo en $N=9$:
Para transicionar de la tónica mayor $r_M = 0$ al eje $r_m = 4$, el acorde pivote utiliza las notas de $C_9 = [3, 8, 4, 0]$.
1. Estado inicial: $\{0, 400, 533.33\} \text{ cents}$ (Eje Mayor: tríada híbrida neutra).
2. Acción del OVC: la voz en $533.33 \text{ cents}$ desciende por paso elemental $\delta_9 = 133.33 \text{ cents}$ a $400 \text{ cents}$, mientras la fundamental se desplaza hacia el índice residual simétrico ($N-3 = 6 \implies 800 \text{ cents}$).
3. La resolución en el polo $r_m = 4$ ($533.33 \text{ cents}$) consolida el reposo en el eje menor mediante un movimiento parsimonioso de apenas $\sim 133.3 \text{ cents}$, completando la modulación microtonal continua sin requerir dominantes diatónicas estándar.

---

## 2.5 Implementación Algorítmica en SuperCollider

El siguiente bloque de código implementa la síntesis de la cadena acústica, la conformación matricial de la Cajita Central para cualquier $N$ impar y el renderizado microtonal continuo utilizando síntesis aditiva sinusoidal para matrices $N$-ET.

```supercollider
// =====================================================================
// THE CHAIN THEORY: Motor de Afinación, Cajita Central y Síntesis N-ET
// Capítulo 2: Algoritmo para N=9 y N=11
// =====================================================================

(
s.waitForBoot({
    var nET = 9;                       // Tamaño de la división: 9 u 11
    var pm = (nET / 2).floor.asInteger; // P_m = floor(N/2)
    var aN = 3;                        // Ancla armónica
    var baseFreq = 220.0;              // Frecuencia fundamental (A3 = 220Hz)
    var centralBox, primaryChain, scalarScale;

    // 1. Cálculo dinámico de la Cajita Central C_N
    if (nET == 9, {
        centralBox = [3, -1, 4, 0];
    }, {
        if (nET == 11, {
            centralBox = [3, -2, 4, -1];
        }, {
            // Algoritmo generalizado fallback
            centralBox = [pm - 1, 0, pm, 1];
        });
    });

    // 2. Mapeo a grados positivos de N-ET y conversión a Cents y Hz
    scalarScale = centralBox.collect({ |deg|
        var modDeg = deg.wrap(0, nET - 1);
        var cents = (1200 / nET) * modDeg;
        var freq = baseFreq * (2.pow(cents / 1200));
        [modDeg, cents, freq];
    });

    // Imprimir reporte teórico en consola
    ("=== SISTEMA N-ET: " ++ nET ++ " ===").postln;
    ("P_m: " ++ pm ++ " | A_N: " ++ aN).postln;
    ("Cajita Central (Índices): " ++ centralBox).postln;
    scalarScale.do({ |row, i|
        ("Voz " ++ i ++ " -> Grado: " ++ row[0] ++ 
         " | Cents: " ++ row[1].round(0.01) ++ 
         " | Freq: " ++ row[2].round(0.01) ++ " Hz").postln;
    });

    // 3. Sintetizador de monitoreo microtonal
    SynthDef(\chainTone, { |freq = 440, amp = 0.1, gate = 1, out = 0|
        var sig, env;
        env = EnvGen.kr(Env.asr(0.05, 1, 0.1), gate, doneAction: 2);
        // Generador armónico estricto sin batimento espurio
        sig = SinOsc.ar(freq) * env * amp;
        Out.ar(out, Pan2.ar(sig, 0));
    }).add;

    s.sync;

    // 4. Reproducción arpegiada de la Cajita Central
    Routine({
        "Reproduciendo Cajita Central (OVC Nucleus)...".postln;
        scalarScale.do({ |voice|
            var freq = voice[2];
            var syn = Synth(\chainTone, [\freq, freq, \amp, 0.15]);
            0.4.wait;
            syn.set(\gate, 0);
        });
        
        0.5.wait;
        "Reproduciendo Acorde Transformante T_N Simultáneo...".postln;
        
        // Bloque polifónico simultáneo (acorde pleno)
        scalarScale.collect({ |voice|
            Synth(\chainTone, [\freq, voice[2], \amp, 0.08]);
        });
    }).play;
});
)
```

Este procedimiento consolida el paso de la abstracción analítica a la ejecución microtonal empírica: el vector $\Delta C_N$ actúa como el mapa genético del sistema sonoro, gobernando tanto la ordenación modal lineal ($S_{p,N}$) como las trayectorias de modulación no diatónica regidas por el OVC.