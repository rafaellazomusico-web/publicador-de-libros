# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 2.1 Fundamentación del Mapeo Acústico y la Morfología Interválica de la Cajita Central ($C_N$)

En el marco de *The Chain Theory*, la génesis del espacio armónico no proviene de una división arbitraria y regular del continuo frecuencial, sino de la proyección vectorial de un núcleo simétrico primario denominado **Cajita Central** ($C_N$). Dicho núcleo actúa como el centro de masa de la matriz generatriz $T_N$, conteniendo en estado latente las polaridades funcionales y los vectores de tensión que gobernarán el temperamento igual de $N$ tonos ($N$-ET).

### 2.1.1 El Operador de Mapeo Acústico $\Phi_{p}$

La transformación de índices abstractos $k \in \mathbb{Z}$ pertenecientes a la cadena tonal hacia magnitudes psicoacústicas medibles en *cents* se formaliza mediante el homomorfismo $\Phi_{p}$:

$$\Phi_{p}(k) = \left( 1200 \cdot k \cdot \log_2(p) \right) \pmod{1200}$$

donde:
- $k$ representa el índice posicional o grado relativo asignado por la matriz primaria.
- $p \in \mathbb{R}^+$ corresponde al generador acústico primordial (comúnmente $p = 3/2$ para cadenas de quintas pitagóricas, o bien las aproximaciones racionales correspondientes al generador interválico fundamental en sistemas $N$-ET: $p = 2^{m/N}$).
- $\Phi_{p}(k) \in [0, 1200)$ define la posición angular del pitch dentro del toroide de octava.

Cuando operamos directamente sobre un sistema temperado de $N$ divisiones iguales ($N$-ET), el generador unitario de paso microtonal primario está cuantizado en pasos discretos de tamaño $\delta = \frac{1200}{N}\text{ cents}$. En tales contextos, el índice $k$ se evalúa mediante la reducción módulo $N$:

$$\phi_N(k) = (k \cdot \delta) \pmod{1200} = \left( \frac{1200}{N} \cdot (k \bmod N) \right)$$

### 2.1.2 Topología Interválica de la Cajita Central

La Cajita Central $C_N$ es una tétrada orientada definida en su forma canónica por el cuarteto de índices:

$$C_N = [c_0, c_1, c_2, c_3]$$

Para los órdenes impares evaluados por el motor matemático, los deltas internos directos $\Delta C_N = (\Delta_1, \Delta_2, \Delta_3)$ determinan la huella microtonal basal del sistema:

$$\Delta_1 = c_1 - c_0, \quad \Delta_2 = c_2 - c_1, \quad \Delta_3 = c_3 - c_2$$

La proyección en cents de estos deltas revela los intervalos microtonales generadores:

$$\text{cents}(\Delta_i) = \Delta_i \cdot \frac{1200}{N} \pmod{1200}$$

Esta estructura cuádruple contiene simultáneamente la tercera mayor microtonal, la tercera menor neutra o infra-menor, y la quinta aproximada del sistema, codificando la semilla que la expansión simétrica propagará hacia los extremos de la cadena.

---

## 2.2 La Expansión Simétrica Intercalada y el Ordenamiento Escalar ($S_{p,N}$)

La matriz primaria $T_N$ no se despliega de manera lineal aditiva, sino mediante una **expansión simétrica intercalada**. A partir de los cuatro polos de $C_N$, el algoritmo anexa sistemáticamente polos agudos y graves alternados hasta agotar la cardinalidad del sistema $N$.

### 2.2.1 Algoritmo de Expansión de la Cadena

Dada la cajita central $C_N$, los elementos restantes de la cadena tonal $T_N = \{t_0, t_1, \dots, t_{N-1}\}$ se calculan iterativamente alrededor de los pivotes de tónica mayor ($r_M = 0$) y tónica menor ($r_m = P_m$ con $P_m = \lfloor N/2 \rfloor$), expandiéndose mediante un factor de salto o apertura $A_N$:

$$t_{\text{ext}} = f_{\text{intercalada}}(C_N, A_N, N)$$

El conjunto resultante $T_{p,N}$ corresponde al conjunto no ordenado de alturas en el dominio temporal/funcional:

$$T_{p,N} = \{ \Phi_p(t) \mid t \in T_N \}$$

### 2.2.2 Proyección Monotónica y Espectro de Pasos ($S_{p,N}$)

Para que la cadena adquiera coherencia como marco de referencia melódico y modal, el conjunto $T_{p,N}$ debe someterse a un ordenamiento escalar estricto mediante la función $\text{sort}$:

$$S_{p,N} = \text{sort}(T_{p,N}) = \langle s_0, s_1, s_2, \dots, s_{N-1} \rangle$$

tal que:

$$0 \le s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

El **Espectro de Pasos** (Step-Size Spectrum) queda determinado por las diferencias adyacentes cíclicas:

$$\sigma_j = \begin{cases} 
s_{j+1} - s_j & \text{para } 0 \le j < N-1 \\ 
(s_0 + 1200) - s_{N-1} & \text{para } j = N-1 
\end{cases}$$

En un sistema $N$-ET puro, cada paso escalar individual colapsa idénticamente a:

$$\sigma_j = \frac{1200}{N}\text{ cents} \quad \forall j \in \{0, \dots, N-1\}$$

Sin embargo, el orden de aparición escalar y su correspondencia biunívoca con los índices de la cadena funcional $T_N$ revela la asimetría intrínseca entre la *proximidad sintáctica* (distancia en la cadena $T_N$) y la *proximidad física* (distancia en la escala $S_{p,N}$).

---

## 2.3 Aplicación Práctica y Análisis Estructural: Casos $N = 9$ y $N = 11$

Se analizan a continuación las matrices generadas para los sistemas no convencionales $9$-ET y $11$-ET según los parámetros fijados por el motor matemático.

```
       Cajita Central (C_N)        Pivote Menor (P_m)   Apertura (A_N)
N=9    [ 3, -1,  4,  0 ]           4                    3
N=11   [ 3, -2,  4, -1 ]           4                    3
```

---

### 2.3.1 Caso I: Sistema 9-ET ($N = 9$)

#### Constantes y Cajita Central
- División elemental: $\delta_9 = \frac{1200}{9} = 133.333\text{ cents}$.
- Pivote menor: $P_m = \lfloor 9/2 \rfloor = 4$.
- Factor de apertura: $A_N = 3$.
- Cajita Central: $C_9 = [3, -1, 4, 0]$.

#### Reducción Módulo 9 de la Cajita Central
Normalizando los índices negativos a la clase residual $\mathbb{Z}_9$:
- $c_0 = 3 \equiv 3$
- $c_1 = -1 \equiv 8$
- $c_2 = 4 \equiv 4$
- $c_3 = 0 \equiv 0$

$$C_9 \pmod 9 = [3, 8, 4, 0]$$

#### Vector de Deltas Internos
Calculando en el dominio no reducido:
$$\Delta_1 = -1 - 3 = -4 \equiv 5 \pmod 9$$
$$\Delta_2 = 4 - (-1) = 5 \equiv 5 \pmod 9$$
$$\Delta_3 = 0 - 4 = -4 \equiv 5 \pmod 9$$

Se aprecia una perfecta periodicidad oscilatoria en la Cajita Central, alternando saltos netos de $4$ y $5$ grados cromáticos de 9-ET.

#### Mapeo Acústico de la Cajita $C_9$

| Índice ($k$) | $k \pmod 9$ | Cálculo en Cents ($\Phi_9$) | Intervalo Nominal Microtonal |
| :---: | :---: | :---: | :--- |
| **0** | $0$ | $0 \times 133.33 = \mathbf{0.00\text{ c}}$ | Tónica ($1/1$) |
| **3** | $3$ | $3 \times 133.33 = \mathbf{400.00\text{ c}}$ | Tercera Mayor Pura ($5/4$ exacto de 9-ET) |
| **-1** | $8$ | $8 \times 133.33 = \mathbf{1066.67\text{ c}}$ | Séptima Mayor Sub-armónica |
| **4** | $4$ | $4 \times 133.33 = \mathbf{533.33\text{ c}}$ | Cuarta Aumentada / Tritono Neutro |

#### Expansión de la Cadena Completa ($T_9$) y Ordenamiento Escalar ($S_{9}$)
A partir de $C_9$, la intercalación expande los polos restantes aplicando el paso $A_N = 3$ y la simetría axial respecto a $r_M = 0$ y $r_m = 4$. La cadena completa resultante en clases de altura es:

$$T_9 = \{0, 3, 6, 8, 2, 5, 7, 1, 4\}$$

Ordenando monotónicamente para derivar la escala $S_{9}$:

$$S_{9} = \langle 0, 1, 2, 3, 4, 5, 6, 7, 8 \rangle$$

Cuya proyección acústica directa en cents es:

$$S_{p,9} = \langle 0.00, 133.33, 266.67, 400.00, 533.33, 666.67, 800.00, 933.33, 1066.67 \rangle$$

```
   0.00 c      266.67 c     533.33 c     800.00 c    1066.67 c
     |------------|------------|------------|------------|
   [s_0]        [s_2]        [s_4]        [s_6]        [s_8]
        \      /     \      /     \      /     \      /
         [s_1]        [s_3]        [s_5]        [s_7]
       133.33 c     400.00 c     666.67 c     933.33 c
```

---

### 2.3.2 Caso II: Sistema 11-ET ($N = 11$)

#### Constantes y Cajita Central
- División elemental: $\delta_{11} = \frac{1200}{11} = 109.091\text{ cents}$.
- Pivote menor: $P_m = 4$ (según calibración estructural del motor).
- Factor de apertura: $A_N = 3$.
- Cajita Central: $C_{11} = [3, -2, 4, -1]$.

#### Reducción Módulo 11 de la Cajita Central
- $c_0 = 3 \equiv 3$
- $c_1 = -2 \equiv 9$
- $c_2 = 4 \equiv 4$
- $c_3 = -1 \equiv 10$

$$C_{11} \pmod{11} = [3, 9, 4, 10]$$

#### Vector de Deltas Internos
$$\Delta_1 = -2 - 3 = -5 \equiv 6 \pmod{11}$$
$$\Delta_2 = 4 - (-2) = 6 \equiv 6 \pmod{11}$$
$$\Delta_3 = -1 - 4 = -5 \equiv 6 \pmod{11}$$

El motor de la teoría revela una invariante: el delta acústico es unívoco en el espacio modular ($\Delta \equiv 6 \pmod{11}$), lo que genera una isotropía de conducción en el núcleo del sistema de 11 notas.

#### Mapeo Acústico de la Cajita $C_{11}$

| Índice ($k$) | $k \pmod{11}$ | Cálculo en Cents ($\Phi_{11}$) | Intervalo Nominal Microtonal |
| :---: | :---: | :---: | :--- |
| **-1** | $10$ | $10 \times 109.09 = \mathbf{1090.91\text{ c}}$ | Séptima Mayor Neutra |
| **3** | $3$ | $3 \times 109.09 = \mathbf{327.27\text{ c}}$ | Tercera Neutra Clásica ($11/9$) |
| **-2** | $9$ | $9 \times 109.09 = \mathbf{981.82\text{ c}}$ | Séptima Menor / Armónica ($7/4$) |
| **4** | $4$ | $4 \times 109.09 = \mathbf{436.36\text{ c}}$ | Tercera Mayor Larga / Cuarta Sub-neutra |

#### Expansión de la Cadena Completa ($T_{11}$) y Ordenamiento Escalar ($S_{11}$)
Expandiendo con simetría intercalada y apertura $A_{11} = 3$:

$$T_{11} = \{0, 3, 6, 9, 1, 4, 7, 10, 2, 5, 8\}$$

Nótese que la cadena en $\mathbb{Z}_{11}$ corresponde a la proyección del ciclo del generador $g = 3$:

$$\{ (0 \cdot 3) \bmod 11, (1 \cdot 3) \bmod 11, (2 \cdot 3) \bmod 11, \dots \} = \{0, 3, 6, 9, 1, 4, 7, 10, 2, 5, 8\}$$

La escala monotónica ordenada $S_{11}$ queda:

$$S_{p,11} = \langle 0.00, 109.09, 218.18, 327.27, 436.36, 545.45, 654.55, 763.64, 872.73, 981.82, 1090.91 \rangle$$

---

## 2.4 El Acorde Transformante $T_N$, Conducción de Voces (OVC) y Dinámica Modulatoria

### 2.4.1 Operador OVC (Optimal Voice Leading Coefficient)

El operador OVC evalúa cuantitativamente la parsimonia en la conducción de voces entre cualquier tétrada o tríada generada en la cadena y la Cajita Central de referencia. Se define mediante la minimización de la métrica $L_1$ en el espacio toroidal:

$$\text{OVC}(X, Y) = \min_{\pi \in \mathfrak{S}_k} \sum_{i=1}^k \min\Big(|x_i - y_{\pi(i)}|,\, N - |x_i - y_{\pi(i)}|\Big)$$

La tipología armónica de un acorde en el sistema $N$-ET se deduce a partir de su desviación formal con respecto a los deltas canónicos de $C_N$:
- **Cualidad Mayor:** $\text{sgn}(\Delta_1) = -\text{sgn}(\Delta_3)$ con polaridad positiva en el pivote $r_M = 0$.
- **Cualidad Menor:** Inversión axial con centro de gravedad en el pivote $r_m = P_m$.
- **Cualidad Simétrica Residual ($S_N$):** Acordes generados en la posición $N - 3$, donde los vectores de desplazamiento colapsan en simetría especular neutra:

$$\Delta_1 \equiv \Delta_2 \equiv \Delta_3 \pmod N$$

### 2.4.2 Matriz Operativa Bi-Eje ($F_N$)

La arquitectura de navegación armónica se articula en una matriz bidimensional $F_N \in \mathcal{M}_{2 \times m}$, cuyos ejes polarizan la estabilidad funcional:

$$F_N = \begin{pmatrix} 
\text{Eje Mayor } (r_M = 0) \\ 
\text{Eje Menor } (r_m = P_m) 
\end{pmatrix}$$

El desplazamiento lateral $c \in \mathbb{Z}$ sobre las columnas de $F_N$ engendra las funciones tonales microtonales:

```
        c = -2         c = -1          c = 0          c = +1         c = +2
   +--------------+--------------+--------------+--------------+--------------+
Eje|     SD_2     |      SD      |   Tónica T   |      D       |     D_2      |
 M | Subdominante | Subdominante |    Mayor     |  Dominante   |  Dominante   |
   |  Secundaria  |              |   (r_M=0)    |              |  Secundaria  |
---+--------------+--------------+--------------+--------------+--------------+
Eje|    sd_2      |      sd      |   Tónica t   |      d       |     d_2      |
 m | Subdominante | Subdominante |    Menor     |  Dominante   |  Dominante   |
   |  Secundaria  |              |   (r_m=P_m)  |              |  Secundaria  |
   +--------------+--------------+--------------+--------------+--------------+
```

El **Acorde Simétrico Residual** ($S_N$), situado obligatoriamente en la coordenada $k = N - 3$, actúa como **pivote neutro**. Al carecer de polaridad modal (no pertenece estrictamente ni al Eje Mayor ni al Menor), opera como un conducto hiper-dimensional que permite modular entre armaduras microtonales distantes mediante una perturbación parsimoniosa mínima de un solo paso de escala ($\pm \delta$).

### 2.4.3 Modulación Microtonal Vectorial

Una modulación microtonal entre dos centros $r_1, r_2 \in F_N$ se parametriza por el vector de transporte armónico $\vec{\mu}$:

$$\vec{\mu} = (r_2 - r_1) \cdot A_N \pmod N$$

En el sistema $11$-ET, una modulación desde la Tónica Mayor ($r_M = 0$) a la Dominante Menor ($d$, correspondiente a $c = +1$ en el eje $P_m = 4$, es decir, clase funcional $5$) produce:

$$\vec{\mu} = (5 - 0) \cdot 3 \equiv 15 \equiv 4 \pmod{11}$$

Desplazarse $\vec{\mu} = 4$ pasos cromáticos en 11-ET equivale a un cambio tonal acústico de:

$$4 \times 109.091 = 436.364\text{ cents}$$

El acorde transformante $T_{11}$ actúa redistribuyendo las voces mediante movimientos oblicuos donde tres voces se desplazan a un microtono ($\pm 109.1\text{ c}$) mientras la cuarta voz permanece estacionaria como polo de enlace armónico.

---

## 2.5 Implementación Algorítmica

El siguiente bloque formalizado en SuperCollider implementa el motor de cálculo acústico, la expansión simétrica y el ordenamiento escalar para los órdenes $N=9$ y $N=11$:

```supercollider
// =====================================================================
// The Chain Theory: Acoustic Engine & Scalic Ordering for N-ET
// =====================================================================

(
var calculateChain = { |n, c_box, pm, a_n|
    var delta = 1200.0 / n;
    var chain = Array.newClear(n);
    var acousticCents, sortedScale;

    // 1. Asignar Cajita Central en el núcleo
    c_box.do { |val, idx|
        chain[idx] = val % n;
    };

    // 2. Expansión Intercalada Simétrica
    for(4, n - 1, { |i|
        var prev = chain[i - 1];
        var step = if(i.isEven) { a_n } { n - a_n };
        chain[i] = (prev + step) % n;
    });

    // 3. Mapeo Acústico (Phi_N)
    acousticCents = chain.collect { |deg| (deg * delta).round(0.001) };

    // 4. Ordenamiento Escalar (S_{p, N})
    sortedScale = chain.asSet.asArray.sort.collect { |deg| (deg * delta).round(0.001) };

    // Salida Estructurada
    (
        \N: n,
        \delta_cents: delta.round(0.001),
        \cajita_normalizada: c_box % n,
        \cadena_TN: chain,
        \cents_TN: acousticCents,
        \escala_SpN: sortedScale,
        \acorde_simetrico_pos: n - 3
    );
};

// Ejecución para N = 9
~data9 = calculateChain.value(9, [3, -1, 4, 0], 4, 3);

// Ejecución para N = 11
~data11 = calculateChain.value(11, [3, -2, 4, -1], 4, 3);

"--- ANÁLISIS SISTEMA 9-ET ---".postln;
~data9.keysValuesDo { |k, v| (k.asString ++ ": " ++ v.asString).postln };

"\n--- ANÁLISIS SISTEMA 11-ET ---".postln;
~data11.keysValuesDo { |k, v| (k.asString ++ ": " ++ v.asString).postln };
)
```

### Síntesis Estructural

1. **Topología de red:** La Cajita Central $C_N$ encapsula las tensiones acústicas fundamentales que evitan la entropía en temperamentos no diatónicos.
2. **Homomorfismo Escalar:** El ordenamiento $S_{p,N}$ restituye la noción de proximidad lineal en el espacio microtonal continuo sin distorsionar los potenciales armónicos discretos contenidos en la matriz $T_N$.
3. **Mecánica Modulatoria:** Mediante la matriz bi-eje $F_N$ y el Acorde Simétrico Residual $S_N$, los sistemas microtonales adquieren la capacidad de modular funcionalmente manteniendo parsimonia de conducción interválica mínima ($L_1$), resolviendo la pérdida de jerarquías tonales en los órdenes impares de $N$-ET.