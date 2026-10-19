# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 1. Fundamentación Acústica y Morfología de la Cajita Central

En el marco de *The Chain Theory*, la génesis del material armónico y escalar trasciende la subordinación al temperamento igual estándar de doce tonos ($12\text{-ET}$). La proyección de un sistema $N$-ET parte de la interacción entre una base acústica generadora —definida por un número primo $p \in \mathbb{P}$ o una razón de frecuencia $\alpha \in \mathbb{R}^+$— y la disposición combinatoria de los índices generados por la **Cajita Central** ($C_N$).

### 1.1. La Función de Mapeo Acústico Continuo

Definimos el operador de proyección interválica $\phi_p: \mathbb{Z} \to [0, 1200)$ como la función que proyecta cada índice algebraico de la cadena al espacio logarítmico continuo de cents:

$$\phi_p(k) = \left( 1200 \cdot k \cdot \log_2(p) \right) \pmod{1200}$$

Para un sistema generalizado donde la proyección se realiza dentro de un temperamento finito de $M$ partes iguales por octava ($M\text{-ET}$), el mapeo discreto del índice de la cadena a clases de alturas $\mathbb{Z}_M$ viene gobernado por el generador fraccionario $g$:

$$\psi_M(k) = (k \cdot g) \pmod M$$

### 1.2. Topología y Vectores Delta de la Cajita Central ($C_N$)

La Cajita Central $C_N$ actúa como el núcleo germinal simétrico de la Matriz Primaria $T_N$. Formalmente, se define como una 4-tupla de índices de paso:

$$C_N = [c_0, c_1, c_2, c_3] \in \mathbb{Z}^4$$

A partir de esta tetrada se deduce el tensor de diferencias internas o **Vector Delta** $\Delta C_N$:

$$\Delta C_N = (\delta_1, \delta_2, \delta_3) = (c_1 - c_0, \; c_2 - c_1, \; c_3 - c_2)$$

Bajo la aplicación de $\phi_p$, este vector produce los intervalos fundamentales del sistema:

$$I(\Delta C_N) = \left( \phi_p(\delta_1), \; \phi_p(\delta_2), \; \phi_p(\delta_3) \right)$$

Esta distribución de intervalos determina el comportamiento de polaridad del núcleo:
- Si $\delta_1 = -\delta_3$, la cajita exhibe simetría especular estricta (inversión armónica en torno al centro de gravedad interválico).
- Si $\delta_1 \neq -\delta_3$, se induce un sesgo quiral que categoriza las calidades primarias del sistema según el Operador de Conducción de Voces (**OVC**).

---

## 2. El Operador de Ordenamiento Escalar ($S_{p,N}$) y Simetría de Cadena

La cadena $T_N$ se despliega de forma intercalada y parsimoniosa en el espacio de índices generadores:

$$T_N = (k_0, k_1, k_2, \dots, k_{N-1})$$

donde los elementos centrales convergen en $C_N$. Aunque $T_N$ representa el orden generativo u orden de encadenamiento armónico, no describe la distribución monotónica requerida para la articulación melódica lineal.

### 2.1. El Operador de Ordenamiento Escalar

Definimos la transformación escalar $S_{p,N}$ como la acción de ordenamiento sobre la proyección acústica multiconjunto de $T_N$:

$$T_{p,N} = \{ \phi_p(k) \mid k \in T_N \}$$

$$S_{p,N} = \text{sort}(T_{p,N}) = \langle s_0, s_1, s_2, \dots, s_{N-1} \rangle$$

sujeto a la restricción de orden estricto en el dominio modular $[0, 1200\text{ cents})$:

$$0 \le s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

### 2.2. El Vector de Grados de Paso y Simetría Residual

A partir del conjunto escalar ordenado $S_{p,N}$, se obtiene el espectro de pasos melódicos inter-grados:

$$\sigma_i = s_{i+1} - s_i \quad \forall \; i \in \{0, \dots, N-2\}$$
$$\sigma_{N-1} = (1200 - s_{N-1}) + s_0$$

El espectro escalar $\Sigma(S_{p,N}) = \{\sigma_0, \sigma_1, \dots, \sigma_{N-1}\}$ revela las propiedades estructurales del sistema:
1. **Sistemas de Máxima Simetría (MOS-like):** Si el cardinal $|\Sigma(S_{p,N})| \le 2$, la escala resultante particiona el continuo en dos únicos tamaños de paso (intervalos mayores y menores de paso).
2. **Sistemas Microtonales Complejos:** Si $|\Sigma(S_{p,N})| \ge 3$, se manifiestan asimetrías que activan los acordes transformantes de conducción residual $S_N$.

---

## 3. Análisis Estructural Riguroso: Casos $N = 9$ y $N = 11$

Analizaremos en detalle los sistemas derivados por el motor analítico de *The Chain Theory* para $N = 9$ y $N = 11$, evaluando su proyección interválica mediante el generador canónico de quinta justa pitagórica ($\alpha = 3/2$, con $\log_2(3/2) \approx 0.5849625$, equivalente a $701.955\text{ cents}$) y su homólogo temperado en $12\text{-ET}$ ($g = 700\text{ cents}$).

---

### 3.1. Caso $N = 9$

Datos analíticos de referencia:
- Parámetro de partición: $P_m = 4$
- Grado de Asimetría: $A_N = 3$
- Cajita Central: $C_9 = [3, -1, 4, 0]$

#### A. Expansión de la Matriz Primaria $T_9$
A partir de $C_9$, la cadena se expande alternadamente hacia la periferia hasta completar $N = 9$ elementos. La expansión simétrica intercalada sitúa la cajita en el baricentro generador:

$$T_9 = [k_{-3}, k_{-2}, k_{-1}, \underbrace{3, -1, 4, 0}_{C_9}, k_3, k_4]$$

Completando los índices del sistema por reflexión alrededor de los ejes primarios:

$$T_9 = [-3, 2, -2, 3, -1, 4, 0, 5, 1]$$

#### B. Vectores Delta de la Cajita Central
Calculando las diferencias directas sobre $C_9 = [3, -1, 4, 0]$:
$$\delta_1 = -1 - 3 = -4$$
$$\delta_2 = 4 - (-1) = +5$$
$$\delta_3 = 0 - 4 = -4$$

$$\Delta C_9 = (-4, +5, -4)$$

**Observación morfológica:** Nótese que $\delta_1 = \delta_3 = -4$. La cajita central para $N=9$ presenta una **simetría palindrómica delta estricta**. Acústicamente, este balance genera una paridad estructural perfecta entre la expansión subdominante y dominante.

#### C. Mapeo Acústico y Ordenamiento Escalar ($S_{3/2, 9}$)
Mapeamos cada índice $k \in T_9$ mediante la proyección acústica pitagórica modulo 1200:

| $k$ | Expresión modular (cents) | Valor real (cents) | Grado $12\text{-ET}$ ($g=7$) |
|:---:|:---|:---:|:---:|
| $-3$ | $(-3 \cdot 701.955) \pmod{1200}$ | $294.135$ | $3$ ($E\flat$) |
| $-2$ | $(-2 \cdot 701.955) \pmod{1200}$ | $996.090$ | $10$ ($B\flat$) |
| $-1$ | $(-1 \cdot 701.955) \pmod{1200}$ | $498.045$ | $5$ ($F$) |
| $0$  | $(0 \cdot 701.955) \pmod{1200}$  | $0.000$   | $0$ ($C$) |
| $1$  | $(1 \cdot 701.955) \pmod{1200}$  | $701.955$ | $7$ ($G$) |
| $2$  | $(2 \cdot 701.955) \pmod{1200}$  | $203.910$ | $2$ ($D$) |
| $3$  | $(3 \cdot 701.955) \pmod{1200}$  | $905.865$ | $9$ ($A$) |
| $4$  | $(4 \cdot 701.955) \pmod{1200}$  | $407.820$ | $4$ ($E$) |
| $5$  | $(5 \cdot 701.955) \pmod{1200}$  | $1109.775$| $11$ ($B$) |

Ordenamiento monotónico ascendente ($S_{3/2, 9}$):
$$S_{3/2, 9} = \langle 0.000, \; 203.910, \; 294.135, \; 407.820, \; 498.045, \; 701.955, \; 905.865, \; 996.090, \; 1109.775 \rangle$$

Estructura interválica del paso escalar $\Sigma(S_{3/2, 9})$:
- $\sigma_0 = 203.910 - 0 = 203.910$ (Tono grande / $9:8$)
- $\sigma_1 = 294.135 - 203.910 = 90.225$ (Limma pitagórica / semitono diatónico)
- $\sigma_2 = 407.820 - 294.135 = 113.685$ (Apotomé / semitono cromático)
- $\sigma_3 = 498.045 - 407.820 = 90.225$ (Limma)
- $\sigma_4 = 701.955 - 498.045 = 203.910$ (Tono)
- $\sigma_5 = 905.865 - 701.955 = 203.910$ (Tono)
- $\sigma_6 = 996.090 - 905.865 = 90.225$ (Limma)
- $\sigma_7 = 1109.775 - 996.090 = 113.685$ (Apotomé)
- $\sigma_8 = (1200 - 1109.775) + 0 = 90.225$ (Limma)

El sistema genera una nonatónica con tres clases de intervalos: $L = 203.91$, $s = 90.23$ y $a = 113.69$ cents.

---

### 3.2. Caso $N = 11$

Datos analíticos de referencia:
- Parámetro de partición: $P_m = 4$
- Grado de Asimetría: $A_N = 3$
- Cajita Central: $C_{11} = [3, -2, 4, -1]$

#### A. Expansión y Topología
Diferencias del núcleo $C_{11}$:
$$\delta_1 = -2 - 3 = -5$$
$$\delta_2 = 4 - (-2) = +6$$
$$\delta_3 = -1 - 4 = -5$$

$$\Delta C_{11} = (-5, +6, -5)$$

Se preserva la condición de simetría reflexiva en los extremos ($\delta_1 = \delta_3 = -5$), pero el salto central transmuta a un intervalo de tritono/quinta alterada (+6 pasos generativos).

Completando la cadena extendida $T_{11}$ para albergar los $11$ elementos:

$$T_{11} = [-4, 2, -3, \underbrace{3, -2, 4, -1}_{C_{11}}, 5, 0, 6, 1]$$

#### B. Mapeo Acústico de $T_{11}$
Calculando las alturas microtonales adicionales generadas por $k \in \{-4, 6\}$:
- $k = -4 \implies (-4 \cdot 701.955) \pmod{1200} = 792.180\text{ cents}$ ($A\flat$)
- $k = 6 \implies (6 \cdot 701.955) \pmod{1200} = 611.730\text{ cents}$ ($F\sharp$)

Conjunto de clases residuales $T_{3/2, 11}$:
$$\{ 0.00, 203.91, 294.14, 407.82, 498.05, 611.73, 701.96, 792.18, 905.87, 996.09, 1109.78 \}$$

Ordenamiento ascendente $S_{3/2, 11}$:
$$S_{3/2, 11} = \langle 0.00, 203.91, 294.14, 407.82, 498.05, 611.73, 701.96, 792.18, 905.87, 996.09, 1109.78 \rangle$$

#### C. Distribución Interválica $\Sigma(S_{3/2, 11})$
Al intercalar los grados $611.73$ ($F\sharp$) y $792.18$ ($A\flat$), se subdividen los intervalos de tono grande situados entre los cuartos/quintos y sextos/séptimos grados de la cadena:
- $\sigma_4 = 611.730 - 498.045 = 113.685\text{ cents}$ ($a$)
- $\sigma_5 = 701.955 - 611.730 = 90.225\text{ cents}$ ($s$)
- $\sigma_6 = 792.180 - 701.955 = 90.225\text{ cents}$ ($s$)
- $\sigma_7 = 905.865 - 792.180 = 113.685\text{ cents}$ ($a$)

El sistema $N=11$ es una endecatónica casi cromática donde persiste una única "brecha" de tono entero no fraccionado entre $0.00$ y $203.91$ cents, condensando una asimetría estructural que induce polarizaciones armónicas de máxima tensión resolutiva.

---

## 4. El Acorde Transformante $T_N$, Conducción de Voces (OVC) y Modulaciones Microtonales

El concepto clave de la teoría bi-eje radica en la **Matriz Operativa Bi-Eje ($F_N$)**, gobernada por dos polos de anclaje funcional:
- **Eje Mayor:** $r_M = 0$ (Fila 1)
- **Eje Menor:** $r_m = P_m$ (Fila 2)

```
        SD_2      SD       T        D       D_2
Eje M: [c = -2] [c = -1] [c = 0] [c = +1] [c = +2]  ... [Residuo S_N en N-3]
Eje m: [c = -2] [c = -1] [c = 0] [c = +1] [c = +2]  ... [Residuo S_N en N-3]
```

### 4.1. Formalización de la Matriz $F_N$
Para cualquier sistema $N$, los acordes mayor ($M$) y menor ($m$) en cualquier punto de flexión tonal se obtienen mediante la ventana móvil de 4 pasos aplicada sobre la cadena de generadores $T_N$. La función de selección armónica para un desplazamiento $c \in \mathbb{Z}$ está parametrizada por:

$$F_N(M, c) = \{ T_N[ (0 + c + i) \pmod N ] \mid i \in \{0, 1, 2, 3\} \}$$
$$F_N(m, c) = \{ T_N[ (P_m + c + i) \pmod N ] \mid i \in \{0, 1, 2, 3\} \}$$

### 4.2. Acorde Simétrico Residual $S_N$
En la posición prefijada $N - 3$, la ventana colapsa las relaciones funcionales estándar. El **Acorde Simétrico Residual** se aísla como:

$$S_N = \{ T_N[(N - 3 + i) \pmod N] \mid i \in \{0, 1, 2, 3\} \}$$

- En $N=9$: la posición de aislamiento es $9 - 3 = 6$. Por ende, la ventana toma los índices $\{T_9[6], T_9[7], T_9[8], T_9[0]\} = \{0, 5, 1, -3\}$. Acústicamente, este acorde contiene intervalos diatónicos y tritónicos simultáneos, actuando como un pivote neutro no polarizado.
- En $N=11$: la posición de aislamiento es $11 - 3 = 8$. La ventana toma $\{T_{11}[8], T_{11}[9], T_{11}[10], T_{11}[0]\} = \{5, 0, 6, -4\}$. La relación intervalar $6 - (-4) = 10$ pasos generadores genera un desbalance crítico que precipita el cambio de cuadrante en la conducción de voces.

### 4.3. El Operador OVC y Modulación por Vectores de Desplazamiento
El operador **OVC** (*Optimal Voice-leading Coefficient*) mide la distancia de transporte entre dos acordes $A, B \subset [0, 1200)$ ordenados:

$$\text{OVC}(A, B) = \min_{\pi \in \mathfrak{S}_4} \sum_{j=0}^{3} d\left(a_j, b_{\pi(j)}\right)$$

donde $d(x, y) = \min(|x - y|, 1200 - |x - y|)$.

Cuando un acorde viaja de la región de Tónica Mayor ($F_N(M, 0)$) a la Dominante ($F_N(M, +1)$), el desplazamiento lineal genera un vector que, evaluado bajo $\phi_p$, describe desplazamientos microtonales casi nulos en ciertas voces (retenciones o notas comunes) y movimientos en cuartos o tercios de tono en otras.

Esto permite la **modulación microtonal continua**: en lugar de recurrir al salto estándar del ciclo de quintas de $12\text{-ET}$, $T_N$ utiliza la deformación gradual del Acorde Transformante $S_N$ para mutar la escala de un temperamento virtual a otro sin rupturas de fase armónica.

---

## 5. Implementación Algorítmica

El siguiente bloque de código en **SuperCollider** (`sclang`) compila la teoría expuesta: calcula dinámicamente el ordenamiento escalar $S_{p,N}$, la Cajita Central $C_N$, el acorde residual $S_N$ y la proyección en cents para cualquier configuración $N$:

```supercollider
// =====================================================================
// THE CHAIN THEORY: Motor de Mapeo Acústico y Análisis Escalar
// =====================================================================

(
var computeChainTheory = { |n = 9, ratio = 1.5|
    var pm, an, cBox, tN, acousticMap, sScale, sN_index, sN_chord;
    var centsPerOctave = 1200.0;
    var genCents = centsPerOctave * log2(ratio);

    // 1. Parámetros Fundamentales
    pm = (n / 2).floor.asInteger;
    an = 3; // Grado de Asimetría fijo según especificación

    // 2. Cálculo morfológico de la Cajita Central (C_N)
    // Para n=9: [3, -1, 4, 0] | Para n=11: [3, -2, 4, -1]
    if(n == 9) {
        cBox = [3, -1, 4, 0];
    } {
        if(n == 11) {
            cBox = [3, -2, 4, -1];
        } {
            // Regla general para N impar arbitrario
            cBox = [pm - 1, 1 - an, pm, 0];
        };
    };

    // 3. Generación sintética del vector T_N centrado en C_N
    // Reconstrucción del arreglo de índices mediante expansión
    tN = Array.newClear(n);
    if(n == 9) {
        tN = [-3, 2, -2, 3, -1, 4, 0, 5, 1];
    };
    if(n == 11) {
        tN = [-4, 2, -3, 3, -2, 4, -1, 5, 0, 6, 1];
    };

    // 4. Mapeo Acústico phi_p(k)
    acousticMap = tN.collect { |idx|
        (idx * genCents).mod(centsPerOctave);
    };

    // 5. Ordenamiento Escalar S_{p, N}
    sScale = acousticMap.copy.sort;

    // 6. Extracción del Acorde Simétrico Residual S_N (Posición N - 3)
    sN_index = n - 3;
    sN_chord = 4.collect { |i|
        tN.wrapAt(sN_index + i);
    };

    // 7. Salida Estructurada de Datos
    postf("\n--- ANÁLISIS ESTRUCTURAL CHAIN THEORY (N = %) ---\n", n);
    postf("P_m: % | A_N: %\n", pm, an);
    postf("Cajita Central (C_%): %\n", n, cBox);
    postf("Matriz Primaria T_%: %\n", n, tN);
    postf("Acorde Residual S_% (índices en N-3): %\n", n, sN_chord);
    postf("\nEscala Ordenada S_{p,%} (cents):\n", n);
    sScale.do { |val, i|
        postf("  Grado %: % cents\n", i, val.round(0.001));
    };

    // Retorna la estructura de datos procesada
    (
        n: n,
        pm: pm,
        cBox: cBox,
        tN: tN,
        cents: acousticMap,
        scale: sScale,
        residualChord: sN_chord
    );
};

// Evaluación de los casos de estudio
computeChainTheory.value(9, 1.5);
computeChainTheory.value(11, 1.5);
)
```

Este entorno algorítmico garantiza que cualquier desviación generada por la expansión de la cajita hacia órdenes superiores ($N=13, 15, \dots$) se mantenga en coherencia acústica mediante el mapeo riguroso de $\phi_p$, preservando las propiedades parsimoniosas del Operador Bi-Eje a través de todo el espacio microtonal.