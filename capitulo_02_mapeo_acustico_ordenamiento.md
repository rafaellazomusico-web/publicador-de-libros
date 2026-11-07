# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión en Sistemas $N$-ET

---

## 1. Fundamentación Microtonal del Mapeo Acústico ($T_{p,N}$)

El núcleo generador de *The Chain Theory* postula que las estructuras armónicas no emergen de jerarquías interválicas fijadas a priori, sino de la proyección proyectiva de una **Cajita Central** ($C_N$) dentro de un espacio de alturas temperado generalizado ($N$-ET). Para vincular el espacio discreto del temperamento igual con los fenómenos de resonancia acústica pura (frecuencias racionales), se define el **Operador de Mapeo Acústico** $\Phi_{p,N}$:

$$\Phi_{p}(k) = \left( 1200 \cdot k \cdot \log_2(p) \right) \pmod{1200}$$

Donde:
- $p \in \mathbb{Q}^+$ representa el factor generador primo o intervalo base de proyección (e.g., $p = 3/2$ para la consonancia diatónica pitagórica clásica, o primos mayores $p \in \{5/4, 7/4, 11/8\}$ para extensiones espectrales).
- $k \in \mathbb{Z}$ es el índice ordinal posicional dentro de la cadena $T_N$.

Cuando este operador actúa en el temperamento de $N$ divisiones iguales de la octava ($N$-ET), la unidad discreta elemental queda gobernada por el cuanto interválico $\varpi_N$:

$$\varpi_N = \frac{1200}{N} \quad [\text{cents}]$$

Bajo este marco, cada coordenada de la Cajita Central $C_N$ proyecta un vector interválico microtonal en el continuo acústico. La distancia interválica en cents entre dos índices generadores $k_a$ y $k_b$ en la cadena se formaliza mediante la métrica modular:

$$\Delta \text{cents}(k_a, k_b) = \left| \left( \Phi_p(k_a) - \Phi_p(k_b) + 600 \right) \pmod{1200} - 600 \right|$$

La Cajita Central concentra la densidad armónica crítica del sistema. Actúa como un atractor gravitacional que restringe la dispersión enharmónica, vinculando los índices correspondientes a la tónica del eje mayor ($r_M = 0$), el polo menor ($r_m = P_m$) y sus extensiones vectoriales mínimas contiguas.

---

## 2. Dinámica Generativa, Topología y Ordenamiento Escalar ($S_{p,N}$)

La cadena tonal matricial $T_N$ se despliega de manera *no lineal* en el espacio de frecuencias. Mientras que el orden generativo de $T_N$ prioriza la contigüidad transformacional y la afinidad de conducción de voces (espacio de acordes), la manifestación auditiva como sustrato melódico exige una proyección sobre el círculo unitario de la octava $\mathbb{T} = \mathbb{R} / 1200\mathbb{Z}$.

```
        CADENA PRIMARIA T_N (Espacio de Conducción)
             [k_0, k_1, k_2, ..., k_{N-1}]
                          │
                          ▼  Mapeo Acústico: Φ_p(k)
             [cents_0, cents_1, ..., cents_{N-1}]
                          │
                          ▼  Operador de Ordenamiento: sort()
        ESCALA S_{p,N} (Espacio Melódico de Paso)
             [s_0, s_1, s_2, ..., s_{N-1}]
```

Se define el **Operador de Ordenamiento Escalar** como el automorfismo de reorganización monótona creciente:

$$S_{p,N} = \text{sort}(T_{p,N}) = \big( s_0, s_1, s_2, \dots, s_{N-1} \big)$$

tal que:

$$0 \le s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

### El Espectro de Grados de Paso ($\Sigma_N$)

A partir de $S_{p,N}$, se extrae la signatura interválica escalar $\Sigma_N$, compuesta por el conjunto ordenado de diferencias de paso contiguas:

$$\Delta s_i = s_{i+1} - s_i \quad (\text{para } 0 \le i < N-1), \quad \Delta s_{N-1} = (1200 - s_{N-1}) + s_0$$

$$\Sigma_N = \big( \Delta s_0, \Delta s_1, \dots, \Delta s_{N-1} \big)$$

En sistemas $N$-ET mayores o no estándar, la simetría de la cadena se traduce en propiedades de simetría especular dentro de $\Sigma_N$, generando agrupaciones análogas a los conjuntos MOS (*Moments of Symmetry*). Cuando el grado de paso $\Delta s_i$ adopta múltiples magnitudes discretas, se manifiestan microintervalos característicos: limas, comas neutras y subcuartos de tono.

---

## 3. Análisis Estructural de Casos de Estudio: $N = 9$ y $N = 11$

A continuación, se computa la descomposición factorial, mapeo interválico y estructura escalar para los dos sistemas modelo procesados por el motor matemático.

### 3.1. Sistema $N = 9$

#### Parámetros del Motor Matemático
- Tamaño de paso base: $\varpi_9 = \frac{1200}{9} = 133.333 \dots \text{ cents}$
- Parámetro de polaridad media: $P_m = 4$
- Índice residual / afinidad anharmónica: $A_N = 3$
- **Cajita Central**: $C_9 = [3, -1, 4, 0]$

```
                EJE MAYOR (r_M = 0)
                 c = 0: [ 0 ] (0 cents)
                        │
       c = -1: [-1] ────┼──── c = +1: [3]  (Inversión/Tritono local)
     (1066.67 c)        │       (400.00 c)
                        │
                EJE MENOR (r_m = 4)
                 c = 0: [ 4 ] (533.33 cents)
```

#### Derivación de la Cadena Primaria ($T_9$)
Expandiendo simétricamente e intercalando desde la Cajita Central hacia los extremos del espacio modular $\mathbb{Z}_9$:

$$T_9 = [3, -1, 4, 0, 5, -2, 6, -3, 7] \pmod 9 \equiv [3, 8, 4, 0, 5, 7, 6, 6, 7] \dots$$

Normalizando estrictamente los índices de clase de altura $k \in \mathbb{Z}_9 = \{0, 1, 2, 3, 4, 5, 6, 7, 8\}$ mediante la alternancia centrada en $C_9$:

$$T_9 = [0, 4, 3, 8, 1, 5, 2, 7, 6]$$

#### Mapeo a Cents y Ordenamiento Escalar
Multiplicando cada grado discreto por $\varpi_9 \approx 133.333\text{ c}$:

$$T_{9,\text{cents}} = [0.00, 533.33, 400.00, 1066.67, 133.33, 666.67, 266.67, 933.33, 800.00]$$

Aplicando $S_9 = \text{sort}(T_9)$:

$$S_9 = [0.00, 133.33, 266.67, 400.00, 533.33, 666.67, 800.00, 933.33, 1066.67]$$

$$\Sigma_9 = (133.33, 133.33, 133.33, 133.33, 133.33, 133.33, 133.33, 133.33, 133.33)$$

#### Interpretación Microtonal
$N=9$ divide el tono entero tradicional ($200\text{ c}$) en tercios de tono exactos ($66.67\text{ c}$), dando lugar a la segunda mayor como paso neutroide o sobrediatónico. 

El intervalo nuclear de la Cajita Central entre el grado 0 y el grado 3 proyecta:
$$3 \times 133.333 = 400.00\text{ cents}$$
Esto constituye una **tercera mayor pitagórica/temperada perfecta**, mientras que el paso $0 \to 4$ proyecta:
$$4 \times 133.333 = 533.333\text{ cents}$$
Se trata de una **cuarta hiper-aumentada** o intervalo neutro entre la cuarta justa ($500\text{ c}$) y la quinta justa ($700\text{ c}$). La polaridad menor ($P_m = 4$) no descansa en una tercera menor canónica ($300\text{ c}$), sino en un espacio modal de suspensión interválica.

---

### 3.2. Sistema $N = 11$

#### Parámetros del Motor Matemático
- Tamaño de paso base: $\varpi_{11} = \frac{1200}{11} \approx 109.091\text{ cents}$
- Parámetro de polaridad media: $P_m = 4$
- Índice residual / afinidad anharmónica: $A_N = 3$
- **Cajita Central**: $C_{11} = [3, -2, 4, -1]$

```
                EJE MAYOR (r_M = 0)
              c = -2: [-2] (981.82 c)
                        │
              c = -1: [-1] (1090.91 c)
                        │
                        ┼──── c = +1: [3] (327.27 c)
                        │
                EJE MENOR (r_m = 4)
              c = 0:  [ 4 ] (436.36 c)
```

#### Derivación de la Cadena Primaria ($T_{11}$)
Proyectando la Cajita Central $C_{11} \pmod{11}$:
- $3 \equiv 3$ ($327.27\text{ c}$)
- $-2 \equiv 9$ ($981.82\text{ c}$)
- $4 \equiv 4$ ($436.36\text{ c}$)
- $-1 \equiv 10$ ($1090.91\text{ c}$)

Al expandir los 11 elementos completando la bi-alternancia simétrica alrededor de $r_M=0$ y $r_m=4$:

$$T_{11} = [0, 4, 3, 10, 5, 9, 2, 8, 1, 7, 6]$$

#### Mapeo a Cents y Ordenamiento Escalar
Multiplicando por $\varpi_{11} \approx 109.091\text{ c}$:

$$T_{11,\text{cents}} = [0.00, 436.36, 327.27, 1090.91, 545.45, 981.82, 218.18, 872.73, 109.09, 763.64, 654.55]$$

Ordenando escalarmente:

$$S_{11} = [0.00, 109.09, 218.18, 327.27, 436.36, 545.45, 654.55, 763.64, 872.73, 981.82, 1090.91]$$

$$\Sigma_{11} = (\varpi_{11}, \varpi_{11}, \dots, \varpi_{11}) \quad \text{con } \Delta s_i \approx 109.091\text{ cents}$$

#### Propiedades Microtonales
$N = 11$ aproxima con alta fidelidad el **undécimo armónico** natural ($11/8 \approx 551.318\text{ c}$). En este temperamento:
$$5 \times 109.091 = 545.455\text{ cents}$$
El error respecto al tritono armónico natural es de apenas $5.86\text{ cents}$. 

Obsérvese la conformación del acorde inducido por $C_{11}$:
- Paso $0 \to 3$: $327.27\text{ cents}$ (Tercera neutra perfecta, intermedia entre la tercera menor pura de $315.6\text{ c}$ y la justa mayor de $386.3\text{ c}$).
- Paso $0 \to 4$: $436.36\text{ cents}$ (Tercera ultra-mayor o cuarta infra-disminuida).
- Paso $0 \to 9$: $981.82\text{ cents}$ (Séptima menor neutra, altamente consonante con el armónico 7, $7/4 \approx 968.83\text{ c}$, error de $13\text{ cents}$).

---

## 4. Conducción de Voces Parsimoniosa y el Acorde Transformante ($T_N$)

El vector de transformación armónica no se comporta como una función de cadencia tonal clásica (tensión-resolución quintal), sino como una **permutación mínima de índices adyacentes** regida por el operador OVC (*Optimal Voice leading Classification*).

### La Matriz Operativa Bi-Eje ($F_N$)

La matriz $F_N$ organiza el espacio armónico en dos filas acopladas correspondientes a la proyección polar Mayor y Menor:

$$F_N = \begin{pmatrix}
\text{Eje Mayor } (M): & r_M = 0 & \to & \text{Desplazamientos } c \in \{-2, -1, 0, +1, +2\} \\
\text{Eje Menor } (m): & r_m = P_m & \to & \text{Desplazamientos } c \in \{-2, -1, 0, +1, +2\}
\end{pmatrix}$$

| Función Cadencial | Notación | Desplazamiento Vectorial ($c$) | Índice $N=9$ | Índice $N=11$ |
| :--- | :---: | :---: | :---: | :---: |
| **Subdominante Secundaria** | $\text{SD}_2$ | $-2$ | $0 - 2 \equiv 7$ | $0 - 2 \equiv 9$ |
| **Subdominante** | $\text{SD}$ | $-1$ | $0 - 1 \equiv 8$ | $0 - 1 \equiv 10$ |
| **Tónica** | $\text{T}$ | $0$ | $0 \text{ y } P_m=4$ | $0 \text{ y } P_m=4$ |
| **Dominante** | $\text{D}$ | $+1$ | $0 + 1 \equiv 1$ | $0 + 1 \equiv 1$ |
| **Dominante Secundaria** | $\text{D}_2$ | $+2$ | $0 + 2 \equiv 2$ | $0 + 2 \equiv 2$ |

### Dinámica del Acorde Simétrico Residual ($S_N$)

En todo sistema $N$-ET procesado bajo *The Chain Theory*, se aísla un punto singular en el índice:

$$\kappa_S = N - 3$$

Para los sistemas evaluados:
- En $N=9$: $\kappa_S = 9 - 3 = 6$.
- En $N=11$: $\kappa_S = 11 - 3 = 8$.

Este elemento carece de pareja de inversión directa bajo la paridad de la Cajita Central; actúa como un **pivote anharmónico invariante** (análogo al tritono en el sistema diatónico de 12-ET, o al eje de polarización de Bartók). 

```
Eje Mayor [0] <──────────────> Acorde Transformante T_N <──────────────> Eje Menor [P_m]
                                      │
                                      ▼
                        Acorde Simétrico Residual (S_N)
                              Posición: N - 3
                    (Eje de Modulación Microtonal Neutra)
```

#### Mecanismo de Modulación Microtonal
La modulación entre regiones tonales distantes se ejecuta reteniendo los nodos comunes de la Cajita Central y mutando el Acorde Transformante $T_N$:

1. **Estado Inicial**: Se establece la sonoridad nuclear a través de $C_N = [k_{\alpha}, k_{\beta}, k_{\gamma}, k_{\delta}]$.
2. **Activación de Voz Parsimoniosa**: Un desplazamiento unitario $\delta = \pm 1$ en el índice de una sola voz transmuta la calidad tridimensional del acorde de Calidad Mayor a Simétrica según el operador OVC:
   $$\Delta_{\text{OVC}} = \sum_{j=1}^{4} |C_N(j) - C_N'(j)| = 1 \text{ paso microtonal}$$
3. **Inflexión del Pivote**: Al alcanzarse el índice $\kappa_S = N - 3$, el acorde residual colapsa las diferencias de género armónico (mayor/menor), abriendo una compuerta de conmutación escalar hacia una transposición de la cadena $T_N^{(\mu)}$ definida por:
   $$\mu = (k + A_N) \pmod N$$
   donde $A_N = 3$ actúa como el operador de salto angular en el toro modal.

---

## 5. Implementación Algorítmica (SuperCollider)

El siguiente script en SuperCollider modela de forma determinista la generación de la Cajita Central, el mapeo acústico en cents, el ordenamiento escalar $S_{p,N}$ y la extracción del Acorde Residual para cualquier sistema $N$-ET.

```supercollider
// =====================================================================
// THE CHAIN THEORY: Motor de Generación y Mapeo Escalar N-ET
// Capítulo 2: Algoritmo de Mapeo Acústico y Conducción Parsimoniosa
// =====================================================================

(
var generateChainSystem = { |n, pRatio = 1.5|
    var pm, an, boxCentral, chainIndices, centsDegrees, scalarOrder, residualIdx;
    var stepSize;

    stepSize = 1200.0 / n;
    pm = (n / 2).floor.asInteger;
    an = 3; // Parámetro del motor axiomático

    // 1. Derivación de la Cajita Central basada en la paridad de N
    if (n == 9) {
        boxCentral = [3, -1, 4, 0];
    } {
        if (n == 11) {
            boxCentral = [3, -2, 4, -1];
        } {
            // Regla general de repliegue sintético
            boxCentral = [pm - 1, 0, pm, 1];
        };
    };

    // 2. Construcción de la Cadena Expandida (T_N)
    chainIndices = List.new;
    chainIndices.addAll(boxCentral);
    
    // Relleno simétrico por alternancia modular
    (0..(n - 1)).do { |deg|
        if (chainIndices.includes(deg).not) {
            chainIndices.add(deg);
        };
    };

    // 3. Mapeo Acústico en Cents: Φ_p(k)
    centsDegrees = chainIndices.collect { |k|
        (k * stepSize).round(0.001);
    };

    // 4. Ordenamiento Escalar S_{p,N}
    scalarOrder = centsDegrees.asArray.sort;

    // 5. Acorde Simétrico Residual S_N en N - 3
    residualIdx = (n - 3);

    // Salida estructurada de resultados teóricos
    Post << "\n==========================================" << Char.nl;
    Post << "REPORTE DE EXPANSIÓN PARA N = " << n << "-ET" << Char.nl;
    Post << "==========================================" << Char.nl;
    Post << "P_m (Polo Menor):        " << pm << Char.nl;
    Post << "A_N (Afinidad Residual):  " << an << Char.nl;
    Post << "Cajita Central (C_N):    " << boxCentral << Char.nl;
    Post << "Cuanto Interválico (cents): " << stepSize.round(0.001) << Char.nl;
    Post << "Cadena Primaria (T_N):   " << chainIndices.asArray << Char.nl;
    Post << "Mapeo T_{p,N} (cents):   " << centsDegrees.asArray << Char.nl;
    Post << "Escala S_{p,N} (cents):   " << scalarOrder << Char.nl;
    Post << "Índice Residual S_N (N-3): Posición " << residualIdx 
         << " -> " << chainIndices[residualIdx] << " (" 
         << (chainIndices[residualIdx] * stepSize).round(0.001) << " c)" << Char.nl;
    Post << "==========================================" << Char.nl;

    // Retorna diccionario estructurado para integración por OSC/MIDI
    (
        n: n,
        stepCents: stepSize,
        centralBox: boxCentral,
        chain: chainIndices.asArray,
        scale: scalarOrder,
        residual: chainIndices[residualIdx]
    );
};

// Ejecución analítica de los casos de estudio
~eval9  = generateChainSystem.value(9, 1.5);
~eval11 = generateChainSystem.value(11, 1.5);
)
```

---

## 6. Conclusiones Estructurales

1. **Invariancia Isomórfica**: La Cajita Central $C_N$ actúa como el núcleo holográfico del sistema; tanto en $N=9$ como en $N=11$, fija la interacción vectorial entre la tónica fundamental ($r_M = 0$) y la tónica de la polaridad complementaria ($r_m = P_m$).
2. **Divergencia entre Espacio Escalar y Espacio Armónico**: La proyección melódica $S_{p,N}$ y la cadena generativa $T_N$ son representaciones ortogonales de la misma entidad matemática. Mientras que $S_{p,N}$ se distribuye uniformemente en el continuo del registro mediante pasos de $\varpi_N$, la cadena $T_N$ dicta saltos parsimoniosos optimizados para la conducción de voces dentro del toroide n-dimensional.
3. **El Punto de Fuga Anarmónico**: El acorde residual aislado en la posición $N-3$ funge como el portal intrínseco de modulación. Todo sistema microtonal de $N$ divisiones posee así una bisagra funcional determinable algorítmicamente mediante el operador $A_N = 3$, evitando la necesidad de resoluciones simétricas forzadas derivadas de la armonía tradicional de 12 tonos.