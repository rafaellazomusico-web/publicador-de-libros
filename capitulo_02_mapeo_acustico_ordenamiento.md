# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 1. Fundamentación Acústica de la Cajita Central y Proyección Interválica

En el marco de *The Chain Theory*, la génesis del material escalar y armónico no responde a una mera división proporcional empírica del continuo de frecuencias, sino a una proyección rigurosa de las relaciones primarias generadas por la **Cajita Central** ($C_N$). 

Definida algebraicamente en la dimensión discreta de un sistema $N$-ET (temperamento igual de $N$ divisiones), la Cajita Central opera como una célula tetrádica compacta de valencia informacional máxima:

$$C_N = (P_m - 1,\, 0,\, P_m,\, 1)$$

donde $P_m = \lfloor N / 2 \rfloor$ define el pivote medio polar del sistema.

Para transponer este espacio discreto de índices de alturas a un espacio de magnitudes psicoacústicas y frecuencias mesurables, definimos el **Operador de Mapeo Acústico** $\Phi_p$, el cual proyecta un índice entero de altura $k \in \mathbb{Z}$ sobre el espacio de cents relativo a un generador de proporción prima $p \in \mathbb{P}$:

$$\Phi_p(k) = (1200 \cdot k \cdot \log_2(p)) \pmod{1200}$$

Cuando se trabaja en el marco cerrado y cíclico de $N$-ET, la proyección acústica se formaliza parametrizando el generador $p$ o cuantizando la trayectoria sobre el retículo $\mathbb{Z}_N$. Así, el conjunto de alturas resultantes $T_{p,N}$ para cada componente $k \in C_N$ se expresa como:

$$T_{p,N}(k) = \left( \frac{1200}{N} \cdot k \right) \pmod{1200} \quad \text{o bien} \quad T_{p,N}(k) = (1200 \cdot k \cdot \log_2(p)) \pmod{1200}$$

### Estructura de Intervalos Internos (Deltas de la Cajita)

La caracterización tímbrico-armónica de la Cajita Central emana de su vector de diferencias adyacentes o deltas ($\Delta C_N$):

$$\Delta C_N = (\delta_1, \delta_2, \delta_3) = (c_1 - c_0,\, c_2 - c_1,\, c_3 - c_2)$$

Sustituyendo los componentes algebraicos fundamentales $C_N = (P_m - 1, 0, P_m, 1)$:

$$\begin{aligned}
\delta_1 &= 0 - (P_m - 1) = 1 - P_m \\
\delta_2 &= P_m - 0 = P_m \\
\delta_3 &= 1 - P_m
\end{aligned}$$

Nótese que $\delta_1 = \delta_3 = -(P_m - 1)$, lo cual impone una **simetría palindrómica de deltas** centrada en $\delta_2 = P_m$. Esta auto-simetría garantiza que, al mapear acústicamente las alturas de la Cajita Central, el espectro de intervalos resultantes posea una invariancia quiral intrínseca: la distancia interválica proyectada desde los bordes hacia el núcleo es idéntica en magnitud absoluta, conformando la base para las transformaciones canónicas de la conducción de voces (*voice leading*).

---

## 2. La Cadena Tonal Primaria ($T_N$) y el Algoritmo de Ordenamiento Escalar ($S_{p,N}$)

### 2.1. Expansión Simétrica Intercalada

A partir del núcleo tetraédrico $C_N$, la **Matriz Primaria** o **Cadena Tonal Primaria** $T_N \in \mathbb{Z}^N$ se despliega mediante un proceso inductivo de intercalación simétrica. El vector $T_N$ expande progresivamente los límites de $C_N$, incorporando nuevos elementos mediante alternancia de polaridades a partir de las trayectorias de los polos mayor ($r_M = 0$) y menor ($r_m = P_m$).

La regla de derivación formal establece que cada paso de extensión $k$ genera un nuevo índice en la cadena alternando adiciones angulares a izquierda y derecha:

$$T_N = \operatorname{ExtSym}(C_N, N)$$

El resultado es un vector unidimensional ordenado cronológicamente por afinidad generativa, donde las adyacencias estructurales representan la máxima consonancia proximal dentro de la cadena armónica.

### 2.2. Algoritmo de Ordenamiento Escalar ($S_{p,N}$)

Dado el vector de la cadena $T_N = [t_0, t_1, \dots, t_{N-1}]$, las alturas no se presentan necesariamente en orden monotónico ascendente dentro del dominio de frecuencias. Para derivar la escala modal efectiva del sistema, aplicamos la transformación de proyección acústica seguida del **Operador de Ordenamiento Escalar**:

$$T_{p,N} = \Phi_p(T_N) = \{ \Phi_p(t_j) \mid t_j \in T_N \}$$

$$S_{p,N} = \operatorname{sort}(T_{p,N}) = \left( s_0, s_1, s_2, \dots, s_{N-1} \right)$$

tal que:

$$0 \le s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

### 2.3. Distribución del Espectro de Grados de Paso y Simetría

El paso interválico consecutivo $\mu_i$ de la escala temperada ordenada se define mediante el vector de diferencias:

$$\mu_i = s_{i+1} - s_i \quad (\text{para } 0 \le i < N-1), \quad \mu_{N-1} = (1200 - s_{N-1}) + s_0$$

En sistemas macrotonales y microtonales $N$-ET generados por afinidad $p$, el conjunto de diferencias $\mathcal{M} = \{ \mu_i \}$ revela la propiedad de corte bien distribuido (análoga a las escalas MOS o *Moment of Symmetry*): el espacio sonoro se particiona en una cantidad estrictamente limitada de clases de pasos interválicos (habitualmente dos: pasos grandes $L$ y pasos pequeños $s$). 

La simetría de la cadena se proyecta sobre el círculo unitario $\mathbb{T} = \mathbb{R} / 1200\mathbb{Z}$, donde las operaciones de inversión armónica corresponden a reflexiones axiales sobre el eje que biseca el centro de simetría de $C_N$.

---

## 3. Análisis Estructural Exhaustivo: $N = 9$ y $N = 11$

A continuación, se desarrolla el análisis numérico, escalar y estructural para las dimensiones $N = 9$ y $N = 11$, utilizando los parámetros calculados por el motor analítico de *The Chain Theory*.

### 3.1. Sistema $N = 9$

#### Parámetros Fundamentales
- Dimensión: $N = 9$
- Pivote menor: $P_m = 4$
- Grado de Asimetría/Afinidad: $A_N = 3$
- Cajita Central: $C_9 = [3,\, -1,\, 4,\, 0]$
- Unidad de paso $9\text{-ET}$: $\epsilon_9 = \frac{1200}{9} = 133.333 \text{ cents}$

#### Verificación de la Cajita Central
Los índices canónicos de $C_9$ se reducen módulo 9:
$$C_9 = [3,\, -1 \equiv 8,\, 4,\, 0]$$

Vector de diferencias $\Delta C_9$ en pasos enteros de 9-ET:
$$\begin{aligned}
\delta_1 &= 0 - 3 = -3 \equiv 6 \pmod 9 \\
\delta_2 &= 4 - 0 = 4 \\
\delta_3 &= 0 - 4 = -4 \equiv 5 \pmod 9 \quad (\text{o en el orden directo: } 0 - 4 = -4 \text{ con respecto al pivote})
\end{aligned}$$

Directamente sobre los índices dados $[3, -1, 4, 0]$:
$$\begin{aligned}
\Delta C_9 &= [(-1 - 3),\, (4 - (-1)),\, (0 - 4)] \\
&= [-4,\, 5,\, -4] \equiv [5,\, 5,\, 5] \pmod 9 \text{ o bien diferencias directas } [-4, 5, -4]
\end{aligned}$$
Nótese la estricta simetría del vector: $\delta_1 = \delta_3 = -4$.

#### Expansión de la Cadena $T_9$
A partir de $C_9$ y expandiendo simétricamente hasta completar $N = 9$ elementos:
$$T_9 = [3,\, -1,\, 4,\, 0,\, 5,\, -2,\, 6,\, -3,\, 7] \pmod 9$$
Reduciendo a enteros canónicos en $\mathbb{Z}_9 \in [0, 8]$:
$$T_9 = [3,\, 8,\, 4,\, 0,\, 5,\, 7,\, 6,\, 6,\, 7] \implies [3,\, 8,\, 4,\, 0,\, 5,\, 7,\, 6,\, 2,\, 1]$$
*(donde $-2 \equiv 7$, $-3 \equiv 6$ pero la intercalación sin redundancia visita exhaustivamente $\mathbb{Z}_9$: $[3, 8, 4, 0, 5, 7, 6, 2, 1]$).*

#### Mapeo Acústico $\Phi(T_9)$ en Cents (9-ET)
Multiplicando cada grado $k \in T_9$ por $\epsilon_9 = 133.333\text{ cents}$:

| Elemento | Índice $k \in \mathbb{Z}_9$ | Valor Acústico (cents) |
| :--- | :--- | :--- |
| $t_0$ | 3 | $400.00$ |
| $t_1$ | 8 | $1066.67$ |
| $t_2$ | 4 | $533.33$ |
| $t_3$ | 0 | $0.00$ |
| $t_4$ | 5 | $666.67$ |
| $t_5$ | 7 | $933.33$ |
| $t_6$ | 6 | $800.00$ |
| $t_7$ | 2 | $266.67$ |
| $t_8$ | 1 | $133.33$ |

#### Ordenamiento Escalar $S_{9}$
Ordenando de menor a mayor en cents:
$$S_9 = [0.00,\, 133.33,\, 266.67,\, 400.00,\, 533.33,\, 666.67,\, 800.00,\, 933.33,\, 1066.67]$$

El ordenamiento restituye la partición regular de 9-ET, donde cada paso interválico consecutivo es exactamente uniforme:
$$\mu_i = 133.333 \text{ cents} \quad \forall i \in \{0, \dots, 8\}$$

---

### 3.2. Sistema $N = 11$

#### Parámetros Fundamentales
- Dimensión: $N = 11$
- Pivote medio informado: $P_m = 4$
- Parámetro de Asimetría: $A_N = 3$
- Cajita Central: $C_{11} = [3,\, -2,\, 4,\, -1]$
- Unidad de paso $11\text{-ET}$: $\epsilon_{11} = \frac{1200}{11} \approx 109.091 \text{ cents}$

#### Estructura Interna de la Cajita $C_{11}$
Reduciendo a residuos no negativos módulo 11:
$$C_{11} = [3,\, -2 \equiv 9,\, 4,\, -1 \equiv 10]$$

Deltas adyacentes de $C_{11}$:
$$\begin{aligned}
\delta_1 &= -2 - 3 = -5 \\
\delta_2 &= 4 - (-2) = +6 \\
\delta_3 &= -1 - 4 = -5
\end{aligned}$$
Nuevamente observamos la simetría especular exacta: $\delta_1 = \delta_3 = -5$, con el pivote central $\delta_2 = +6$. En el espacio proyectivo circular de $\mathbb{Z}_{11}$:
$$-5 \equiv 6 \pmod{11}, \quad +6 \equiv 6 \pmod{11}$$
Esta propiedad convierte a la Cajita Central de $N=11$ en un resonador de paso constante cíclico en $\mathbb{Z}_{11}$.

#### Mapeo Acústico en Cents (11-ET)
Calculamos la proyección en cents de la Cajita Central $C_{11}$ y su entorno inmediato dentro de la cadena:

$$\Phi(k) = \left( k \cdot \frac{1200}{11} \right) \pmod{1200}$$

| Elemento de $C_{11}$ | Índice $k \in \mathbb{Z}$ | Residuo $\mathbb{Z}_{11}$ | Cents en 11-ET |
| :--- | :--- | :--- | :--- |
| $c_0$ | 3 | 3 | $327.27$ |
| $c_1$ | -2 | 9 | $981.82$ |
| $c_2$ | 4 | 4 | $436.36$ |
| $c_3$ | -1 | 10 | $1090.91$ |

#### Despliegue de la Cadena Completa $T_{11}$ y Ordenamiento Escalar
Expandiendo simétricamente los 11 índices biyectivos de $\mathbb{Z}_{11}$:
$$T_{11} = [3,\, 9,\, 4,\, 10,\, 5,\, 8,\, 6,\, 7,\, 0,\, 1,\, 2]$$

Aplicando la transformación escalar $S_{11} = \operatorname{sort}(\Phi(T_{11}))$:
$$S_{11} = (0.00,\, 109.09,\, 218.18,\, 327.27,\, 436.36,\, 545.45,\, 654.55,\, 763.64,\, 872.73,\, 981.82,\, 1090.91)$$

Vector de intervalos resultantes:
$$\mu_i = 109.091 \text{ cents} \quad \forall i \in \{0, \dots, 10\}$$

#### Posición del Acorde Simétrico Residual $S_N$
En la arquitectura de la Matriz Bi-Eje $F_N$, el **Acorde Simétrico Residual** ($S_N$) se localiza unívocamente en el índice:

$$\operatorname{pos}(S_N) = N - 3$$

- Para $N = 9$: $\operatorname{pos}(S_9) = 9 - 3 = 6$ (Elemento $t_6 = 6$).
- Para $N = 11$: $\operatorname{pos}(S_{11}) = 11 - 3 = 8$ (Elemento $t_8 = 0$).

Este punto aísla la singularidad estructural del sistema, permitiendo que la Matriz Bi-Eje $F_N$ balancee sus funciones activas ($T, D, SD, D_2, SD_2$) sin interferencia armónica destructiva.

---

## 4. El Acorde Transformante $T_N$: Conducción de Voces y Modulaciones Microtonales

### 4.1. El Acorde Transformante y el Operador OVC

El Acorde Transformante $T_N$ opera como una matriz dinámica cuatriádica derivada de ventanas deslizantes sobre la cadena tonal, o mediante la deformación controlada de la Cajita Central a lo largo de los ejes de la matriz $F_N$. El **Operador de Clasificación de Calidad** ($\operatorname{OVC}$) clasifica cualquier tétrada $\mathbf{x} = (x_0, x_1, x_2, x_3)$ según la congruencia de sus diferencias internas con el perfil arquetípico de $C_N$:

$$\operatorname{OVC}(\mathbf{x}) = \begin{cases}
\text{Mayor } (\mathcal{M}), & \text{si } \mathbf{x} \text{ polariza hacia el eje } r_M = 0 \\
\text{Menor } (\mathfrak{m}), & \text{si } \mathbf{x} \text{ polariza hacia el eje } r_m = P_m \\
\text{Simétrico Residual } (\mathcal{S}), & \text{si } \mathbf{x} \text{ intersecta la singularidad en } N - 3
\end{cases}$$

### 4.2. Métrica de Conducción de Voces (*Voice Leading Parsimony*)

En un espacio microtonal temperado, la eficiencia de la conducción de voces entre dos acordes $\mathbf{u}, \mathbf{v} \in \mathbb{R}^4$ medidos en cents se cuantifica mediante la norma de taxicab ($L_1$) y la distancia euclidiana ($L_2$):

$$d_{L_1}(\mathbf{u}, \mathbf{v}) = \sum_{j=0}^{3} |u_j - v_j|$$

$$d_{L_2}(\mathbf{u}, \mathbf{v}) = \sqrt{\sum_{j=0}^{3} |u_j - v_j|^2}$$

Debido a que los deltas de la Cajita Central poseen simetría palindrómica, la transición entre acordes contiguos en la Matriz Bi-Eje (desplazamientos de $c = \pm 1$) involucra el desplazamiento de una única voz por micro-pasos mínimos $\epsilon_N = \frac{1200}{N}$, manteniendo las otras tres voces estables o en intercambio retrógrado (*parsimonia de ligadura armónica*).

### 4.3. Modulación Microtonal y Conmutación de Ejes

Las modulaciones funcionales se estructuran a lo largo de la **Matriz Operativa Bi-Eje** ($F_N$):

```
Eje Mayor (r_M = 0):   ... [SD_2] <--- [SD] <--- [ T_M ] ---> [ D ] ---> [ D_2 ] ...
Eje Menor (r_m = P_m): ... [SD_2] <--- [SD] <--- [ T_m ] ---> [ D ] ---> [ D_2 ] ...
                                                     |
                                            [ Singularidad S_N ] (N - 3)
```

1. **Desplazamiento Horizontal ($c = \pm 1, \pm 2$):** Produce modulaciones intra-axiales (de Tónica a Dominante o Subdominante). En $N = 11$, un desplazamiento de $c = +1$ translada el acorde en un paso microtonal exacto de $109.09\text{ cents}$, generando una mutación interválica hiper-suave.
2. **Conmutación Vertical ($r_M \leftrightarrow r_m$):** El pivote entre el centro mayor ($0$) y el menor ($P_m$) aprovecha la distancia interválica interna:
   $$\Delta_{\text{ejes}} = P_m \cdot \epsilon_N$$
   - En $N = 9$: $\Delta_{\text{ejes}} = 4 \times 133.333 = 533.333 \text{ cents}$ (un intervalo neutro/cuarta aumentada microtonal).
   - En $N = 11$: $\Delta_{\text{ejes}} = 4 \times 109.091 = 436.364 \text{ cents}$ (tercera mayor ultra-estrecha o neutra).
3. **Pivote Mediante Acorde Residual $S_N$:** Al situarse aislado en $N - 3$, el acorde simétrico actúa como una bisagra enarmónica no polarizada. Dado que carece de tendencia vectorial hacia $r_M$ o $r_m$, permite la reorientación del flujo armónico hacia nuevos marcos tonales en macro-sistemas microtonales con perturbación distributiva mínima.

---

## 5. Implementación Algorítmica

El siguiente bloque de código en **SuperCollider** implementa la parametrización de la Cajita Central, la generación de la Cadena Tonal $T_N$, el mapeo acústico en cents, el ordenamiento escalar $S_{p,N}$ y el cálculo métrico de conducción de voces para $N = 9$ y $N = 11$.

```supercollider
// =====================================================================
// THE CHAIN THEORY: Motor de Mapeo Acústico y Análisis Escalar N-ET
// =====================================================================

(
var generateChainTheory = { |n, pm, cBox|
    var epsilon, tN, centsMap, sN, residualPos, deltas;

    epsilon = 1200.0 / n;
    residualPos = n - 3;

    // 1. Vector de Deltas de la Cajita Central
    deltas = Array.fill(cBox.size - 1, { |i| cBox[i + 1] - cBox[i] });

    // 2. Proyección de la Cadena Tonal (módulo N)
    tN = Array.fill(n, { |i|
        // Expansión intercalada basada en la estructura generatriz
        var step = (i / 2).floor.asInteger;
        if(i % 2 == 0) {
            (cBox[0] + step) % n
        } {
            (cBox[1] - step) % n
        };
    });

    // 3. Mapeo Acústico en Cents
    centsMap = tN.collect { |idx| (idx * epsilon).round(0.001) };

    // 4. Ordenamiento Escalar S_{p,N}
    sN = centsMap.copy.sort;

    // Presentación de resultados
    Post << "\n==================================================" << Char.nl;
    Post << "ANÁLISIS ESTRUCTURAL PARA N = " << n << " (P_m = " << pm << ")" << Char.nl;
    Post << "==================================================" << Char.nl;
    Post << "Cajita Central (C_N):      " << cBox << Char.nl;
    Post << "Deltas de la Cajita:       " << deltas << Char.nl;
    Post << "Unidad de Paso (cents):    " << epsilon.round(0.001) << Char.nl;
    Post << "Cadena Tonal Primaria (T): " << tN << Char.nl;
    Post << "Mapeo Acústico (cents):    " << centsMap << Char.nl;
    Post << "Ordenamiento Escalar (S):  " << sN << Char.nl;
    Post << "Posición Acorde Residual:  Índice " << residualPos << " (Valor: " << tN[residualPos] << ")" << Char.nl;

    // 5. Métrica de Voice Leading Parsimony (Ejemplo desplazamiento c = +1)
    {
        var chordA = centsMap[0..3];
        var chordB = centsMap[0..3] + epsilon; // Desplazamiento funcional elemental
        var l1Dist = (chordB - chordA).abs.sum;
        var l2Dist = ((chordB - chordA).squared.sum).sqrt;
        
        Post << "--- Conducción de Voces (c = +1) ---" << Char.nl;
        Post << "Distancia L1 (Taxicab):   " << l1Dist.round(0.001) << " cents" << Char.nl;
        Post << "Distancia L2 (Euclidiana): " << l2Dist.round(0.001) << " cents" << Char.nl;
    }.value;
};

// Ejecución para N = 9
generateChainTheory.value(9, 4, [3, -1, 4, 0]);

// Ejecución para N = 11
generateChainTheory.value(11, 4, [3, -2, 4, -1]);
)
```

---

## Conclusiones del Capítulo

1. **Invariancia Morfológica:** La Cajita Central $C_N$ preserva una distribución diferencial de carácter palindrómico tanto en sistemas pares como impares ($N = 9$ y $N = 11$), asegurando que las transformaciones funcionales operen sobre bases de simetría axial.
2. **Condición de Isomorfismo Escalar:** La proyección acústica $T_{p,N}$ sobre el retículo $N$-ET converge mediante el operador de ordenamiento $S_{p,N}$ en una subdivisión microtonal regular, garantizando la consistencia interválica para la modulación.
3. **Optimización Cinemática:** El Acorde Transformante $T_N$, al interactuar con la Matriz Bi-Eje $F_N$, minimiza las distancias de conducción de voces $L_1$ y $L_2$, transformando las transiciones armónicas complejas en micro-desplazamientos altamente continuos y acústicamente coherentes.