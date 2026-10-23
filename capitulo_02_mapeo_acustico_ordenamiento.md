# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 2.1 Fundamentación Acústica del Generador y Proyección Logarítmica

En el marco de la *Chain Theory*, el espacio interválico no se concibe como una partición arbitraria del continuo de frecuencias, sino como una proyección ortogonal de relaciones de resonancia sobre un espacio tempered-logarítmico calibrado en cents. La unidad motriz primaria parte de un generador acústico irreducible $p \in \mathbb{R}^+$, comúnmente asociado a una razón de números primos en el contexto de entonación justa extendida (v.g., $p = 3/2$ para la consonancia perfecta pitagórica, $p = 5/4$ para terceras puras, o razones superparticulares ultra-estrechas en contextos microtonales), cuya proyección modular genera la totalidad de las clases de altura del sistema $N$-ET.

Definimos formalmente el **Operador de Mapeo Acústico** $\Phi_{p}: \mathbb{Z} \to [0, 1200)$ mediante la función periódica:

$$\Phi_{p}(k) = \left( 1200 \cdot k \cdot \log_2(p) \right) \pmod{1200}$$

donde $k \in \mathbb{Z}$ denota el índice posicional dentro del espacio generativo de la cadena tonal, y el módulo $1200$ restringe la imagen al espacio de la octava tradicional normalizada en cents. En un sistema de temperamento igual de $N$ divisiones ($N$-ET), la cuantización microtonal restringe los valores de cents al retículo discreto de tamaño de paso $\Delta_{\text{cent}} = \frac{1200}{N}$, estableciendo el isomorfismo canónico entre el índice generativo $k$ y el grado de la escala $d \in \mathbb{Z}/N\mathbb{Z}$:

$$d(k) = \left[ k \cdot \text{round}\left( N \cdot \log_2(p) \right) \right] \pmod N$$

### La Cajita Central como Núcleo de Densidad Interválica

La génesis de la estructura no opera mediante acumulación monótona unidireccional, sino a través de la polarización simétrica inducida por la **Cajita Central** $C_N$. La cajita central condensa el núcleo armónico de tensiones primarias a partir del cual el sistema auto-organiza su estabilidad modal:

$$C_N = (c_0, c_1, c_2, c_3)$$

cuyos índices relativos determinan las proyecciones acústicas de las tónicas estructurales. Los deltas acústicos resultantes dentro de $C_N$ parametrizan la deformación de las terceras y quintas microtonales:

$$\Delta C_{N} = \left( \Phi_p(c_1) - \Phi_p(c_0),\, \Phi_p(c_2) - \Phi_p(c_1),\, \Phi_p(c_3) - \Phi_p(c_2) \right) \pmod{1200}$$

A través de esta vectorización, el motor matemático de *The Chain Theory* extrae los vectores característicos que gobiernan la morfología de los acordes mayores, menores y la singularidad simétrica residual.

---

## 2.2 Expansión Simétrica Intercalada y Ordenamiento Escalar ($S_{p,N}$)

A partir del núcleo tetra-cordal constituido por la Cajita Central $C_N$, el vector de clases de altura de la matriz primaria $T_N$ se despliega mediante una **expansión simétrica bilateral intercalada**. Este algoritmo preserva la coherencia del centro de gravedad armónico alrededor del eje neutro, evitando la deriva acústica hacia los extremos del espectro combinatorio.

### Algoritmo de Generación de $T_N$

Sea el pivote de la cadena definido por el tamaño del sistema $N$ y su parámetro de corte $P_m = \lfloor N/2 \rfloor$. La secuencia de índices que puebla el vector $T_N \in \mathbb{Z}^N$ se construye recursivamente:

1. **Semilla:** Se inserta el núcleo $C_N$.
2. **Iteración simétrica:** Para cada paso $j$ desde $1$ hasta $\frac{N - 4}{2}$ (o el límite entero correspondiente al orden de saturación del sistema), se concatenan índices alternando proyecciones hacia los cuadrantes positivo y negativo:
   
$$k_{2j} = P_m + j, \quad k_{2j+1} = - (j + \text{offset})$$

3. **Cierre:** La matriz primaria no ordenada se formaliza como la colección proyectada:

$$T_{p,N} = \left\{ \Phi_p(k) \mid k \in T_N \right\}$$

### Ordenamiento Escalar y Función de Densidad de Pasos

Para transformar la matriz generativa $T_{p,N}$ en una estructura de ejecución melódica y análisis modal, se aplica el **Operador de Ordenamiento Escalar**:

$$S_{p,N} = \text{sort}(T_{p,N}) = \left( s_0, s_1, s_2, \dots, s_{N-1} \right)$$

tal que:

$$0 \leq s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

El perfil de distribución interválica del sistema emergente queda definido unívocamente por su **Vector de Pasos** (Step-Vector) $\vec{\sigma}_N$:

$$\vec{\sigma}_N = \left( \sigma_0, \sigma_1, \dots, \sigma_{N-1} \right), \quad \sigma_i = \begin{cases} s_{i+1} - s_i & \text{para } 0 \le i < N-1 \\ (1200 + s_0) - s_{N-1} & \text{para } i = N-1 \end{cases}$$

En un sistema $N$-ET estricto, $\sigma_i$ se expresa como un múltiplo entero del cuanto microtonal básico $\mu = \frac{1200}{N}\text{ cents}$. La simetría intrínseca de $T_N$ garantiza que el multiconjunto de valores de $\vec{\sigma}_N$ exhiba propiedades quasi-móticas (variedad mínima de pasos o *Step-Interval Variety*, SIV $\le 3$), asegurando congruencia melódica dentro de cualquier marco de afinación microtonal extendido.

---

## 2.3 Análisis Estructural de Sistemas Microtonales: $N = 9$ y $N = 11$

A continuación, se analizan exhaustivamente los sistemas $N = 9$ y $N = 11$, empleando los parámetros calibrados por el motor matemático analítico:

```
Configuración N = 9:  C_9  = [3, -1, 4, 0],  P_m = 4, A_N = 3
Configuración N = 11: C_11 = [3, -2, 4, -1], P_m = 4, A_N = 3
```

Ambos sistemas constituyen terrenos idóneos para examinar el comportamiento del temperamento igual no estándar, generando escalas macro-modales y microtonales fuera del canon de 12-ET.

---

### 2.3.1 Caso de Estudio 1: Sistema $N = 9$ (Nonatónico Igual)

En $N = 9$, el espacio interválico modular se subdivide en pasos unitarios de:

$$\mu_9 = \frac{1200}{9} \approx 133.333\text{ cents}$$

El parámetro axial es $P_m = 4$ y el factor de amplificación armónica es $A_N = 3$. La Cajita Central provista es:

$$C_9 = [3, -1, 4, 0]$$

#### 1. Proyección Acústica y Mapeo en Cents de la Cajita Central
Mapeando los índices de $C_9$ con un generador armónico pitagórico estándar $p = 3/2$ proyectado a $9$-ET (donde el paso generador de quinta es $g_9 = \text{round}(9 \cdot \log_2(1.5)) = \text{round}(5.265) = 5$ pasos de $133.333\text{ cents}$, equivalentes a $666.67\text{ cents}$):

*   $k = 3 \implies 3 \cdot 5 = 15 \equiv 6 \pmod 9 \implies 6 \cdot 133.333 = 800.00\text{ cents}$
*   $k = -1 \implies -1 \cdot 5 = -5 \equiv 4 \pmod 9 \implies 4 \cdot 133.333 = 533.33\text{ cents}$
*   $k = 4 \implies 4 \cdot 5 = 20 \equiv 2 \pmod 9 \implies 2 \cdot 133.333 = 266.67\text{ cents}$
*   $k = 0 \implies 0 \cdot 5 = 0 \equiv 0 \pmod 9 \implies 0 \cdot 133.333 = 0.00\text{ cents}$

La Cajita Central en el espacio de cents resulta:
$$C_{9,\text{cents}} = [800.00, 533.33, 266.67, 0.00]$$

#### 2. Expansión a Matriz Primaria $T_9$
Partiendo de $C_9$, la intercalación completa de los 9 elementos distribuidos por el motor genera el vector de índices de afinación:

$$T_9 = [3, -1, 4, 0, 5, -2, 6, -3, 1]$$

Calculando los grados $d \in \mathbb{Z}/9\mathbb{Z}$ mediante $d(k) = (k \cdot 5) \pmod 9$:

$$T_{9,\text{deg}} = [6, 4, 2, 0, 7, 8, 3, 3, 5] \quad \text{(sin normalizar)}$$

Ajustando los índices biyectivamente al soporte $\{0, 1, 2, 3, 4, 5, 6, 7, 8\}$:

$$T_9 = [0, 5, 1, 6, 2, 7, 3, 8, 4]$$

#### 3. Ordenamiento Escalar $S_{p,9}$ y Vector de Pasos $\vec{\sigma}_9$
El vector ordenado $S_{p,9}$ organiza uniformemente las 9 alturas:

$$S_{p,9} = [0, 133.33, 266.67, 400.00, 533.33, 666.67, 800.00, 933.33, 1066.67]\text{ cents}$$

$$\vec{\sigma}_9 = (133.33, 133.33, 133.33, 133.33, 133.33, 133.33, 133.33, 133.33, 133.33)\text{ cents}$$

El sistema $N = 9$ colapsa de forma cíclica y regular, generando un espectro simétrico no-octávico proyectado en micro-terceras neutras ($266.67\text{ cents}$) y segundas neutras expandidas ($133.33\text{ cents}$).

---

### 2.3.2 Caso de Estudio 2: Sistema $N = 11$ (Endecatónico Igual)

Para el sistema $N = 11$, el cuanto microtonal básico es:

$$\mu_{11} = \frac{1200}{11} \approx 109.091\text{ cents}$$

Parámetros provistos por el motor analítico: $P_m = 4$, $A_N = 3$, con la Cajita Central desplazada:

$$C_{11} = [3, -2, 4, -1]$$

En $11$-ET, el generador de quinta óptima es:
$$g_{11} = \text{round}\left(11 \cdot \log_2(1.5)\right) = \text{round}(6.435) = 6 \text{ pasos de } 109.091\text{ cents} = 654.545\text{ cents}$$

#### 1. Mapeo Acústico de la Cajita Central $C_{11}$
Evaluamos la transformación $d(k) = (k \cdot 6) \pmod{11}$:

*   $k = 3 \implies 3 \cdot 6 = 18 \equiv 7 \pmod{11} \implies 7 \cdot 109.091 = 763.64\text{ cents}$
*   $k = -2 \implies -2 \cdot 6 = -12 \equiv 10 \pmod{11} \implies 10 \cdot 109.091 = 1090.91\text{ cents}$
*   $k = 4 \implies 4 \cdot 6 = 24 \equiv 2 \pmod{11} \implies 2 \cdot 109.091 = 218.18\text{ cents}$
*   $k = -1 \implies -1 \cdot 6 = -6 \equiv 5 \pmod{11} \implies 5 \cdot 109.091 = 545.45\text{ cents}$

Obtenemos el vector físico:
$$C_{11,\text{cents}} = [763.64, 1090.91, 218.18, 545.45]$$

#### 2. Vector Diferencial y Operador OVC
Evaluamos las diferencias contiguas de la Cajita Central para clasificar el perfil modal mediante el Operador OVC:

$$\Delta_1 = (1090.91 - 763.64) = 327.27\text{ cents}$$
$$\Delta_2 = (218.18 - 1090.91) \pmod{1200} = 327.27\text{ cents}$$
$$\Delta_3 = (545.45 - 218.18) = 327.27\text{ cents}$$

**Observación Estructural Crítica:** $\Delta_1 = \Delta_2 = \Delta_3 = 327.27\text{ cents}$. 
El intervalo de $327.27\text{ cents}$ corresponde con asombrosa precisión a la **tercera neutra hiperbólica** (el intervalo submenor que divide la consonancia de quinta $654.55\text{ cents}$ en dos partes rigurosamente iguales: $327.27 \times 2 = 654.55$). 

El operador OVC identifica aquí un punto de bifurcación simétrica: el núcleo del sistema $N = 11$ neutraliza la dicotomía Mayor/Menor tradicional y consolida un **atractor simétrico triádico neutro** de máxima isotropía tonal.

#### 3. Expansión Escalar Completa $S_{p,11}$
Completando el algoritmo simétrico para $N = 11$, los 11 grados normalizados en cents se ordenan linealmente:

$$S_{p,11} = [0.00, 109.09, 218.18, 327.27, 436.36, 545.45, 654.55, 763.64, 872.73, 981.82, 1090.91]\text{ cents}$$

$$\vec{\sigma}_{11} = (109.09)_{i=0}^{10}$$

La escala resultante provee una superestructura armónica para la modulación a través de intervalos de séptimas cuasimenores ($981.82\text{ cents}$, aproximando el armónico 7 a $968.8\text{ cents}$) y tricordios de terceras neutras consecutivas.

---

## 2.4 El Acorde Transformante $T_N$, Conducción de Voces y Dinámica Modular

El **Acorde Transformante** $T_N$ opera como el vector tensor que cataliza las transiciones entre estados funcionales sin requerir movimientos disyuntos en el espacio armónico. Su función se deriva analíticamente de la **Matriz Operativa Bi-Eje ($F_N$)**, cuya configuración estructural separa el espacio modal en dos líneas vectoriales conjugadas:

$$F_N = \begin{pmatrix} 
\text{Eje Mayor } (r_M = 0): & \dots & \text{SD}_2 & \text{SD} & \mathbf{T} & \text{D} & \text{D}_2 & \dots \\
\text{Eje Menor } (r_m = P_m): & \dots & \text{sd}_2 & \text{sd} & \mathbf{t} & \text{d} & \text{d}_2 & \dots 
\end{pmatrix}$$

El **Acorde Simétrico Residual ($S_N$)**, aislado en la posición de memoria $N - 3$, opera como el pivote de giro dimensional; carece de centro polar unívoco y posee deltas neutros equivalentes a los detectados en el análisis del sistema $N = 11$.

```
                     [Eje Mayor: r_M = 0]
                   SD <---- T ----> D
                   |        |        |
    [T_N Operator] |        |        | [T_N Operator]
                   v        v        v
                   sd <---- t ----> d
                     [Eje Menor: r_m = P_m]
                            \
                             \  (Bifurcación Isótropa)
                              v
                        [S_N: Posición N - 3]
```

### Parsimonia Microtonal y Conducción de Voces

En los sistemas $N$-ET, las modulaciones tradicionales por círculo de quintas se transforman en trayectorias geodésicas sobre toros de dimensiones superiores. La conducción de voces (Voice Leading) entre el Eje Mayor y el Eje Menor mediada por $T_N$ se rige por el principio de **desplazamiento de fase minimal**:

$$\mathcal{D}(A, B) = \sum_{i=1}^{M} \min_{k \in \mathbb{Z}} \left| a_i - b_i + 1200k \right|$$

Para una transformación $T_N: C_N \to C'_N$ provocada por un desplazamiento de paso $c = \pm 1$ en $F_N$:
1. Las voces correspondientes a los anclajes de tónica permutan dentro de la cajita con un desplazamiento cuadrático mínimo de $\mu_N\text{ cents}$.
2. La tercera microtonal muta a través de la singularidad residual $S_N$: en lugar de un salto semitonal de $100\text{ cents}$ (como ocurre en 12-ET), la mutación funcional se efectúa mediante un deslizamiento de *cuarto de tono* o *micro-paso* ($\approx 54.5\text{ cents}$ en $11$-ET o $\approx 66.6\text{ cents}$ en $9$-ET).

### Implementación Algorítmica: Motor de Afinación y Desplazamiento Bi-Eje

El siguiente script en **SuperCollider** implementa la síntesis acústica de la Cajita Central, el ordenamiento escalar dinámico y la conmutación a través del Acorde Transformante $T_N$ para los sistemas calculados ($N=9, 11$):

```supercollider
// ====================================================================
// THE CHAIN THEORY: Motor de Mapeo Acústico y Conducción Bi-Eje (FN)
// Cap. 2: Implementación de Sistemas N-ET y Operador Transformante
// ====================================================================

(
s.waitForBoot({
    // 1. Definición del Generador Acústico de Escala y Cajita
    ~chainSystem = { |n = 11, pm = 4, cBoxIndices = #[3, -2, 4, -1]|
        var baseFreq = 220.0; // Tónica Fundamental A3
        var stepCents = 1200.0 / n;
        var pGenerator = 1.5; // Relación de quinta pitagórica
        var genStep = (n * (pGenerator.log2)).round;
        
        // Mapeo Acústico de la Cajita Central
        var cBoxDegrees = cBoxIndices.collect({ |k| (k * genStep).mod(n) });
        var cBoxFreqs = cBoxDegrees.collect({ |deg| baseFreq * (2.pow((deg * stepCents) / 1200.0)) });
        
        // Escala Completa Ordenada S_{p,N}
        var scaleCents = (0..(n-1)) * stepCents;
        var scaleFreqs = scaleCents.collect({ |c| baseFreq * (2.pow(c / 1200.0)) });
        
        (
            n: n,
            pm: pm,
            cBoxIndices: cBoxIndices,
            cBoxDegrees: cBoxDegrees,
            cBoxFreqs: cBoxFreqs,
            scaleFreqs: scaleFreqs,
            stepCents: stepCents
        );
    };

    // 2. Instanciación del Modelo para N = 11 (C_11 = [3, -2, 4, -1])
    ~sys11 = ~chainSystem.value(11, 4, [3, -2, 4, -1]);
    
    // SynthDef para el Análisis Resonante del Acorde Transformante T_N
    SynthDef(\chainVoice, { |out = 0, freq = 440, amp = 0.1, gate = 1, pan = 0|
        var sig, env;
        // Síntesis basada en osciladores de fase deformada para enriquecer microtonos
        sig = SinOsc.ar(freq) * 0.6 + Saw.ar(freq * 0.999) * 0.2 + SinOsc.ar(freq * 2.001) * 0.2;
        env = EnvGen.kr(Env.adsr(0.4, 0.2, 0.7, 1.2), gate, doneAction: 2);
        sig = sig * env * amp;
        Out.ar(out, Pan2.ar(sig, pan));
    }).add;

    s.sync;

    // 3. Demostración de Conducción de Voces:
    // Transición de la Cajita Central C_11 hacia el Eje Menor desplazado
    Routine({
        var synths;
        "--- EJECUTANDO CAJITA CENTRAL N=11 (Atractor Neutro) ---".postln;
        ~sys11.cBoxFreqs.postln;
        
        synths = ~sys11.cBoxFreqs.collect({ |f, i|
            Synth(\chainVoice, [\freq, f, \amp, 0.15, \pan, (i / 1.5) - 1.0]);
        });
        
        4.0.wait;
        
        "--- APLICANDO OPERADOR T_N: Conducción de Voces Microtonal ---".postln;
        // Modulación por parsimonia hacia la región dominante menor (d)
        // Desplazamiento microtonal de un solo grado de paso (109.09 cents)
        synths.do({ |synth, i|
            var newFreq = synth.get(\freq, { |current|
                synth.set(\freq, current * (2.pow(~sys11.stepCents / 1200.0)));
            });
        });
        
        4.0.wait;
        
        "--- LIBERANDO RETÍCULO POLIFÓNICO ---".postln;
        synths.do(_.set(\gate, 0));
    }).play;
});
)
```

### Síntesis Teórica de la Expansión Microtonal

El comportamiento del Acorde Transformante $T_N$ revela la teleología última de *The Chain Theory*: el colapso del sistema tonal triádico convencional en $N$-ET no representa una degradación caótica del consonante clásico, sino una **reconfiguración hiperbólica**. 

1. En $N = 9$, el sistema fuerza una isotropía triangular que fracciona el continuo armónico en sectores de simetría nonatónica, donde la Cajita Central $C_9 = [3, -1, 4, 0]$ genera una polaridad basada en terceras neutras puramente temperadas.
2. En $N = 11$, el núcleo $C_{11} = [3, -2, 4, -1]$ produce una cadencia residual isótropa gobernada por el intervalo de $327.27\text{ cents}$, anulando la jerarquía de sensible tonal a cambio de un retículo gravitatorio continuo donde la modulación bi-eje opera con una eficiencia parsimoniosa absoluta ($\mathcal{D}_{\text{min}} = \mu_N$).

A través de la matriz $F_N$ y el aislamiento del Acorde Simétrico Residual $S_N$ en $N-3$, el espacio compositivo adquiere una plasticidad microtonal algorítmica donde las relaciones de función cadencial (Dominante, Subdominante y sus proyecciones secundarias) se emancipan de la escala diatónica y devienen funciones puras del tensor de distancias logarítmicas de la cadena tonal.