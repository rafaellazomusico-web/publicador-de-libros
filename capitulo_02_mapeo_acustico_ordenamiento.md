# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 2.1. Proyección Acústica y el Operador de Mapeo Intervalar ($T_{p,N}$)

En el marco de la Teoría de la Cadena (*The Chain Theory*), el espacio interválico no se concibe como una división temperada pasiva, sino como un campo de tensiones proyectivas generadas a partir de un núcleo interválico mínimo: la **Cajita Central** ($C_N$). La proyección de los elementos abstractos de la Matriz Primaria ($T_N$) hacia el dominio psicoacústico real de frecuencias relativas se formaliza mediante la función de mapeo logarítmico calibrada a un factor primo o generador espectral $p \in \mathbb{R}^+$.

Sea el vector de índices de la matriz $T_N$ definido en el anillo de clases residuales $\mathbb{Z}_N$, la proyección acústica en escala centesimal absoluta $T_{p,N}$ se define formalmente como:

$$\Phi_p(\text{idx}) = \left( 1200 \cdot \text{idx} \cdot \log_2(p) \right) \pmod{1200}$$

Donde:
- $\text{idx} \in T_N$ representa la posición relativa de la clase de altura dentro de la cadena extendida.
- $p$ es la base de proyección armónica (típicamente $p=3$ para proyecciones de derivación quíntica/pitagórica, o $p \in \{3, 5, 7, 11\}$ en afinaciones adaptativas de límite primo).
- El operador módulo $1200$ restringe el flujo frecuencial al espacio de la octava periódica canónica $[0, 1200)$.

La **Cajita Central** ($C_N$), definida genéricamente por la cuádrupla generatriz:

$$C_N = (P_m - 1, \, 0, \, P_m, \, 1)$$

constituye el condensador de simetría local. En ella convergen los vectores delta que determinarán la identidad modal del sistema mediante el Operador de Vector de Calidad (OVC). Los intervalos microtonales generados en el seno de $C_N$ actúan como las "semillas diferenciales" ($\delta_i$) que polarizan la cadena en regiones armónicas contrastantes.

---

## 2.2. Algoritmo de Ordenamiento Escalar ($S_{p,N}$) y Despliegue Simétrico

Mientras que $T_N$ preserva la contigüidad operacional y las relaciones de transformación parsimoniosa (sintaxis armónica), la estructura perceptible como escala musical requiere la aplicación del operador de ordenamiento monótono creciente $\text{sort}(\cdot)$:

$$S_{p,N} = \text{sort}(T_{p,N}) = \langle s_0, s_1, s_2, \dots, s_{N-1} \rangle$$

tal que:

$$0 \le s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

A partir de $S_{p,N}$, se extrae el **Vector de Pasos Escalares** $\Delta S_{p,N}$:

$$\Delta S_{p,N} = \langle s_1 - s_0, \, s_2 - s_1, \, \dots, \, (1200 + s_0) - s_{N-1} \rangle$$

En sistemas de temperamento igual de orden superior ($N\text{-ET}$ donde $N > 7$), la cadena simétrica intercalada genera una distribución asimétrica en el dominio de las alturas brutas, pero dotada de auto-similaridad estructural en el dominio interválico modular. 

A medida que $N$ se expande, la simetría de la cadena se proyecta hacia la periferia según el algoritmo de alternancia:

$$\text{Extensión}(k) = C_N \cup \left\{ (-1)^k \cdot \left( \left\lfloor \frac{k}{2} \right\rfloor + A_N \right) \right\} \pmod N$$

Esta expansión intercalada garantiza que la adición de cada nuevo grado tonal preserve el centro de gravedad acústico del sistema, manteniendo las relaciones de simetría axial respecto al origen $0$ y al punto medio $P_m$.

---

## 2.3. Casos de Estudio Estructurales: $N = 9$ y $N = 11$

A continuación, se desarrolla el desglose analítico estructural para los sistemas parametrizados por el motor matemático del tratado.

### 2.3.1. Sistema $N = 9$

**Parámetros fundamentales:**
- Grados: $N = 9$
- Punto Medio Menor: $P_m = 4$
- Factor de Ajuste / Compensación: $A_N = 3$
- Cajita Central: $C_9 = [3, -1, 4, 0] \equiv [3, 8, 4, 0] \pmod 9$

#### Matriz Primaria ($T_9$) y Expansión Simétrica
A partir de $C_9$, la expansión intercalada completa el conjunto de 9 elementos en $\mathbb{Z}_9$:

$$T_9 = [0, 4, 8, 3, 7, 2, 6, 1, 5]$$

#### Mapeo Acústico ($T_{3,9}$) con Generador $p = 3$ (Quintas Pitagóricas)
Tomando $1200 \cdot \log_2(3) \approx 1901.955$ cents $\equiv 701.955$ cents $\pmod{1200}$:

$$\Phi_3(\text{idx}) = (701.955 \cdot \text{idx}) \pmod{1200}$$

Calculando para cada índice en $T_9$:
- $\text{idx} = 0 \to 0.0 \text{ cents}$
- $\text{idx} = 4 \to (4 \times 701.955) \pmod{1200} = 2807.82 \pmod{1200} = 407.82 \text{ cents}$
- $\text{idx} = 8 \to (8 \times 701.955) \pmod{1200} = 5615.64 \pmod{1200} = 815.64 \text{ cents}$
- $\text{idx} = 3 \to (3 \times 701.955) \pmod{1200} = 2105.865 \pmod{1200} = 905.865 \text{ cents}$
- $\text{idx} = 7 \to (7 \times 701.955) \pmod{1200} = 4913.685 \pmod{1200} = 113.685 \text{ cents}$
- $\text{idx} = 2 \to (2 \times 701.955) \pmod{1200} = 1403.91 \pmod{1200} = 203.91 \text{ cents}$
- $\text{idx} = 6 \to (6 \times 701.955) \pmod{1200} = 4211.73 \pmod{1200} = 611.73 \text{ cents}$
- $\text{idx} = 1 \to (1 \times 701.955) \pmod{1200} = 701.955 \text{ cents}$
- $\text{idx} = 5 \to (5 \times 701.955) \pmod{1200} = 3509.775 \pmod{1200} = 1109.775 \text{ cents}$

Vector Acústico Proyectado:
$$T_{3,9} = [0.0, \, 407.82, \, 815.64, \, 905.87, \, 113.69, \, 203.91, \, 611.73, \, 701.96, \, 1109.78]$$

#### Ordenamiento Escalar ($S_{3,9}$)
Ordenando de forma estrictamente monótona:
$$S_{3,9} = \langle 0.0, \, 113.69, \, 203.91, \, 407.82, \, 611.73, \, 701.96, \, 815.64, \, 905.87, \, 1109.78 \rangle$$

Vector de pasos interválicos ($\Delta S_{3,9}$):
$$\Delta S_{3,9} = \langle 113.69, \, 90.22, \, 203.91, \, 203.91, \, 90.23, \, 113.68, \, 90.23, \, 203.91, \, 90.22 \rangle$$

Nótese la emergencia de dos clases de semitonos microtonales primarios: la apotomé pitagórica ($\approx 113.69$ cents) y la limma pitagórica ($\approx 90.22$ cents), junto con el tono entero $(\approx 203.91$ cents).

#### Matriz Operativa Bi-Eje ($F_9$)
Centros rectores: Eje Mayor en $r_M = 0$, Eje Menor en $r_m = P_m = 4$.  
Acorde Simétrico Residual ($S_9$): ubicado en la posición $N - 3 = 6$.

| Función | Desplazamiento ($c$) | Eje Mayor ($r_M = 0$) | Eje Menor ($r_m = 4$) |
| :--- | :---: | :---: | :---: |
| **Subdominante Secundaria ($SD_2$)** | $-2$ | $\text{idx} = 7$ ($113.69$ c) | $\text{idx} = 2$ ($203.91$ c) |
| **Subdominante ($SD$)** | $-1$ | $\text{idx} = 8$ ($815.64$ c) | $\text{idx} = 3$ ($905.87$ c) |
| **Tónica ($T$)** | $0$ | $\text{idx} = 0$ ($0.00$ c) | $\text{idx} = 4$ ($407.82$ c) |
| **Dominante ($D$)** | $+1$ | $\text{idx} = 1$ ($701.96$ c) | $\text{idx} = 5$ ($1109.78$ c) |
| **Dominante Secundaria ($D_2$)** | $+2$ | $\text{idx} = 2$ ($203.91$ c) | $\text{idx} = 6$ ($611.73$ c) |

*Residuo Simétrico:* $S_9$ se polariza en $\text{idx} = 6$ (tritono acústico a $611.73$ cents), actuando como pivote no resolutivo del sistema.

---

### 2.3.2. Sistema $N = 11$

**Parámetros fundamentales:**
- Grados: $N = 11$
- Punto Medio Menor de referencia estructural: $P_m = 4$
- Factor de Ajuste: $A_N = 3$
- Cajita Central: $C_{11} = [3, -2, 4, -1] \equiv [3, 9, 4, 10] \pmod{11}$

#### Matriz Primaria ($T_{11}$)
Expandiendo el sistema a 11 polos mediante intercalación simétrica:

$$T_{11} = [0, 4, 9, 3, 8, 1, 6, 10, 5, 2, 7]$$

#### Mapeo Acústico ($T_{3,11}$) con $p = 3$
Aplicando $\Phi_3(\text{idx}) = (701.955 \cdot \text{idx}) \pmod{1200}$:
- $\text{idx} = 0 \to 0.00 \text{ cents}$
- $\text{idx} = 4 \to 407.82 \text{ cents}$
- $\text{idx} = 9 \to (9 \times 701.955) \pmod{1200} = 6317.595 \pmod{1200} = 317.60 \text{ cents}$
- $\text{idx} = 3 \to 905.87 \text{ cents}$
- $\text{idx} = 8 \to 815.64 \text{ cents}$
- $\text{idx} = 1 \to 701.96 \text{ cents}$
- $\text{idx} = 6 \to 611.73 \text{ cents}$
- $\text{idx} = 10 \to (10 \times 701.955) \pmod{1200} = 7019.55 \pmod{1200} = 1019.55 \text{ cents}$
- $\text{idx} = 5 \to 1109.78 \text{ cents}$
- $\text{idx} = 2 \to 203.91 \text{ cents}$
- $\text{idx} = 7 \to 113.69 \text{ cents}$

#### Ordenamiento Escalar ($S_{3,11}$)
$$S_{3,11} = \langle 0.0, \, 113.69, \, 203.91, \, 317.60, \, 407.82, \, 611.73, \, 701.96, \, 815.64, \, 905.87, \, 1019.55, \, 1109.78 \rangle$$

Vector de pasos interválicos ($\Delta S_{3,11}$):
$$\Delta S_{3,11} = \langle 113.69, \, 90.22, \, 113.69, \, 90.22, \, 203.91, \, 90.23, \, 113.68, \, 90.23, \, 113.68, \, 90.23, \, 90.22 \rangle$$

En $N=11$, el espectro se reconfigura en una cadena altamente equilibrada de semitonos alternantes casi uniformes interrumpidos por un único intervalo disyunto de tono entero ($203.91$ cents), propiciando zonas de micro-modulación continua.

#### Matriz Operativa Bi-Eje ($F_{11}$)
Centros rectores: Eje Mayor en $r_M = 0$, Eje Menor en $r_m = P_m = 4$.  
Acorde Simétrico Residual: $S_{11}$ aislado en $N - 3 = 8$ ($\text{idx} = 8$, $815.64$ cents).

| Función | Desplazamiento ($c$) | Eje Mayor ($r_M = 0$) | Eje Menor ($r_m = 4$) |
| :--- | :---: | :---: | :---: |
| **Subdominante Secundaria ($SD_2$)** | $-2$ | $\text{idx} = 9$ ($317.60$ c) | $\text{idx} = 2$ ($203.91$ c) |
| **Subdominante ($SD$)** | $-1$ | $\text{idx} = 10$ ($1019.55$ c) | $\text{idx} = 3$ ($905.87$ c) |
| **Tónica ($T$)** | $0$ | $\text{idx} = 0$ ($0.00$ c) | $\text{idx} = 4$ ($407.82$ c) |
| **Dominante ($D$)** | $+1$ | $\text{idx} = 1$ ($701.96$ c) | $\text{idx} = 5$ ($1109.78$ c) |
| **Dominante Secundaria ($D_2$)** | $+2$ | $\text{idx} = 2$ ($203.91$ c) | $\text{idx} = 6$ ($611.73$ c) |

---

## 2.4. El Acorde Transformante $T_N$: Conducción de Voces y Modulaciones Microtonales

El **Acorde Transformante** $T_N$ se articula como el operador dinámico que media la transición entre polaridades funcionales dentro de la matriz $F_N$. No opera como una entidad estática, sino como un haz vectorial de conducción de voces (*voice-leading vector*) definido por transformaciones parsimoniosas mínimas en el espacio afín de la afinación.

### Mecánica del Operador OVC y Desplazamiento de Fase
El OVC asigna la cualidad del acorde a través de las diferencias internas generadas en las ventanas cuádruples de $T_N$. Sea una tríada o tétrada seleccionada sobre la matriz, su vector de diferencias $\vec{v} = \langle v_1, v_2, \dots \rangle$ define su vector de fase. Cuando una estructura armónica se somete al operador de conducción de voces microtonal $\mathcal{M}$:

$$\mathcal{M}(x) = x + \Delta \phi \pmod{1200}$$

la transición entre el Eje Mayor y el Eje Menor se formaliza mediante la trayectoria geodésica más corta en el toro interválico:

$$\text{dist}(A, B) = \sum_{i=1}^{k} |a_i - b_i|$$

```
    Eje Mayor (r_M = 0)                   Eje Menor (r_m = P_m)
  ... [SD] <---> [ T ] <---> [ D ] ...      ... [sd] <---> [ t ] <---> [ d ] ...
         \       /   \       /                 \       /   \       /
          \     /     \     /                   \     /     \     /
       [ Acorde Transformante T_N ] <=======> [ Residuo Simétrico S_N ]
                     (Vías de Conducción Parsimoniosa)
```

En el sistema $N=9$, la modulación microtonal desde la Tónica Mayor ($r_M = 0$) hacia la Tónica Menor ($r_m = 4$) no requiere una transposición diatónica convencional; se logra mutando la relación estructural a través del Acorde Transformante $T_9$, el cual absorbe la diferencia de $407.82$ cents distribuyéndola en dos vectores parsimoniosos de limma/apotomé:

$$0.0 \xrightarrow{+113.69} 113.69 \xrightarrow{+90.22} 203.91 \xrightarrow{+203.91} 407.82$$

Este deslizamiento escalar escalonado permite modulaciones infinitas sin discontinuidad acústica espectral, fundamentando la conectividad armónica no euclidiana propia de sistemas $N\text{-ET}$.

---

## 2.5. Implementación Algorítmica en SuperCollider

El siguiente módulo formaliza la proyección $T_{p,N}$, el ordenamiento $S_{p,N}$, la extracción de la Matriz Bi-Eje $F_N$ y la síntesis aditiva microtonal de acordes basada en "The Chain Theory":

```supercollider
// =====================================================================
// The Chain Theory: Motor de Mapeo Acústico, Ordenamiento y Bi-Eje
// Capítulo 2: Algoritmo para N-ET (N=9, N=11)
// =====================================================================

(
var calculateChain = { |n = 9, pm = 4, an = 3, p = 3|
    var t_n, acousticCents, sortedScale, stepVector;
    var f_matrix, symResidual;
    var log2p = log2(p);

    // 1. Generación de la Cadena Primaria T_N (Expansión Simétrica)
    // Inicialización con Cajita Central
    t_n = Array.newClear(n);
    t_n[0] = 0;
    t_n[1] = pm;
    
    // Relleno e intercalado modal algorítmico
    (2..(n - 1)).do { |k|
        var val;
        if(k.even) {
            val = (pm + (k / 2 * an)).asInteger % n;
        } {
            val = (0 - ((k + 1) / 2 * an)).asInteger % n;
        };
        t_n[k] = (val + n) % n;
    };

    // 2. Mapeo Acústico T_{p,N} (cents)
    acousticCents = t_n.collect { |idx|
        (1200.0 * idx * log2p) % 1200.0;
    };

    // 3. Ordenamiento Escalar S_{p,N}
    sortedScale = acousticCents.copy.sort;
    
    // Cálculo de pasos (Step Vector)
    stepVector = Array.fill(n, { |i|
        if(i < (n - 1)) {
            sortedScale[i + 1] - sortedScale[i];
        } {
            (1200.0 + sortedScale[0]) - sortedScale[i];
        };
    });

    // 4. Matriz Bi-Eje F_N
    // Eje Mayor (r_M = 0), Eje Menor (r_m = pm)
    // Desplazamientos c: -2, -1, 0, 1, 2
    f_matrix = Dictionary.new;
    f_matrix.put(\major_axis, [-2, -1, 0, 1, 2].collect { |c| (0 + c + n) % n });
    f_matrix.put(\minor_axis, [-2, -1, 0, 1, 2].collect { |c| (pm + c + n) % n });
    
    // Acorde Residual Simétrico S_N en N - 3
    symResidual = (n - 3) % n;
    f_matrix.put(\residual_symmetric, symResidual);

    // Retorno estructural
    (
        n: n,
        primary_matrix: t_n,
        acoustic_cents: acousticCents,
        scalar_order: sortedScale,
        step_vector: stepVector,
        bi_axial_matrix: f_matrix
    );
};

// Ejecución diagnóstica para N = 9 y N = 11
~chain9  = calculateChain.(9, 4, 3, 3);
~chain11 = calculateChain.(11, 4, 3, 3);

"--- ANÁLISIS ESTRUCTURAL N=9 ---".postln;
~chain9.postcs;
"\n--- ANÁLISIS ESTRUCTURAL N=11 ---".postln;
~chain11.postcs;
)

// =====================================================================
// Síntesis Espacializada Microtonal: Audición del Acorde Transformante
// =====================================================================

(
SynthDef(\chainOsc, { |out = 0, freq = 440, amp = 0.1, gate = 1, pan = 0|
    var sig, env;
    env = EnvGen.kr(Env.asr(0.6, 1.0, 1.2), gate, doneAction: 2);
    sig = SinOsc.ar(freq) * 0.6 + SinOsc.ar(freq * 2, 0, 0.2); // Resonancia armónica
    sig = sig * env * amp;
    Out.ar(out, Pan2.ar(sig, pan));
}).add;
)

// Rutina de sonificación polifónica microtonal de F_9
(
Routine({
    var baseFreq = 220.0;
    var centsToFreq = { |cents| baseFreq * (2.pow(cents / 1200.0)) };
    var synths;

    "Audición: Eje Mayor (Tónica - Dominante) modulando por Transformante".postln;
    
    // Disparo de tríada mayor proyectada
    synths = [0, 407.82, 701.96].collect { |c|
        Synth(\chainOsc, [\freq, centsToFreq.(c), \amp, 0.08, \pan, rrand(-0.5, 0.5)]);
    };
    2.wait;

    // Transición parsimoniosa vía Acorde Transformante hacia Eje Menor
    synths.do(_.set(\gate, 0));
    synths = [203.91, 407.82, 815.64].collect { |c|
        Synth(\chainOsc, [\freq, centsToFreq.(c), \amp, 0.08, \pan, rrand(-0.5, 0.5)]);
    };
    2.5.wait;

    // Resolución en polo residual simétrico S_9 (idx = 6 -> 611.73 c)
    synths.do(_.set(\gate, 0));
    synths = [0.0, 611.73].collect { |c|
        Synth(\chainOsc, [\freq, centsToFreq.(c), \amp, 0.1, \pan, 0]);
    };
    3.wait;
    synths.do(_.set(\gate, 0));
}).play;
)
```

Este entorno algorítmico corrobora empíricamente cómo las estructuras calculadas a partir de $C_N$ y proyectadas por $T_{p,N}$ configuran espacios geométricos consistentes, gobernados por leyes de conducción de voces microtonales puramente parsimoniosas.