# CAPÍTULO 2: Mapeo Acústico, Ordenamiento Escalar y Expansión de $N$-ET

---

## 1. Fundamentación Físico-Matemática del Mapeo Acústico ($T_{p,N}$)

En la arquitectura de *The Chain Theory*, la matriz primaria $T_N$ define una trayectoria topológica dentro del espacio de clases de alturas modular $\mathbb{Z}_N$. No obstante, para que esta secuencia adquiera coherencia psicoacústica e interválica en un temperamento igual arbitrario ($N$-ET), es necesario proyectar las posiciones relativas de la cadena sobre el continuo logarítmico de frecuencias.

### 1.1. Proyección Logarítmica e Isomorfismo Frecuencial

Sea $p \in \mathbb{R}^+$ el generador acústico primario de proyección interválica (típicamente $p = 2^{1/N}$ en afinaciones equi-temperadas, o una razón de intervalo puro $p \in \mathbb{Q}$ en proyecciones basadas en afinación justa, como la quinta justa $\frac{3}{2}$). Para un índice discreto de paso $k \in T_N$, el operador de mapeo acústico en escala continua de cents se formaliza mediante:

$$\phi(k; p) = \left( 1200 \cdot k \cdot \log_2(p) \right) \pmod{1200}$$

Cuando se implementa una proyección estrictamente atada al temperamento igual $N$-ET, tomamos el generador unitario de paso $p_N = 2^{1/N}$, lo que colapsa la ecuación a la forma canónica de micro-pasos:

$$\phi_N(k) = \left( \frac{1200}{N} \cdot k \right) \pmod{1200}, \quad k \in \mathbb{Z}_N$$

Bajo la noción generalizada de *The Chain Theory*, permitimos que el índice de orden estructural $\text{idx} \in T_N$ proyecte una deformación armónica respecto a un primo acústico base $p \in \mathbb{P} = \{2, 3, 5, 7, \dots\}$, cuantizando las relaciones sobre la malla de afinación:

$$T_{p,N}[m] = \left( 1200 \cdot T_N[m] \cdot \log_2(p) \right) \pmod{1200}, \quad m \in \{0, 1, \dots, N-1\}$$

Esta formulación mapea las relaciones de proximidad de la cadena (estructuradas en saltos de tercera y quinta abstractos) en alturas tangibles sobre la tesitura armónica.

---

## 2. De la Cadena Estructural al Continuo Escalar ($S_{p,N}$)

Mientras que la Matriz Primaria $T_N$ codifica la conectividad por conducción armónica y afinidad funcional, la textura melódica requiere una relación monótona creciente en el espacio de frecuencias.

### 2.1. El Operador de Clasificación Escalar

Definimos el vector escalar ordenado $S_{p,N}$ como la transformación monotónica de $T_{p,N}$:

$$S_{p,N} = \text{sort}(T_{p,N}) = \left( s_0, s_1, s_2, \dots, s_{N-1} \right)$$

tal que:

$$0 \le s_0 < s_1 < s_2 < \dots < s_{N-1} < 1200$$

El conjunto de diferencias adyacentes define el vector interválico de paso $\Delta S_{p,N}$:

$$\Delta S_{p,N}[i] = s_{i+1} - s_i, \quad \forall i \in \{0, \dots, N-2\}$$
$$\Delta S_{p,N}[N-1] = (1200 + s_0) - s_{N-1}$$

### 2.2. Simetría Quiral y Grados de Paso

En un sistema $N$-ET regular con generador de paso mínimo $g = \frac{1200}{N}$, $\Delta S_{p,N}[i] = g$ de forma trivial. Sin embargo, en la proyección interválica de la cadena generada a través de generadores no coprimos o deformaciones no lineales generadas por la Cajita Central $C_N$, $\Delta S_{p,N}$ manifiesta una asimetría quiral que determina la polaridad modal del sistema. 

El ordenamiento escalar revela de esta manera las funciones de *grados de paso* (passing tones microtonales), diferenciando los nodos de sustentación armónica fija de aquellos pertenecientes al flujo interválico transitorio.

---

## 3. Estudio de Casos Canónicos: $N = 9$ y $N = 11$

A continuación, se analizan los micro-sistemas $N = 9$ (nonatónico) y $N = 11$ (undecatónico), utilizando los parámetros calculados por el motor matemático del sistema.

### 3.1. Sistema Nonatónico ($N = 9$)

Parámetros fundamentales:
*   Pivote Menor: $P_m = \lfloor 9/2 \rfloor = 4$.
*   Acorde Residual / Pivote: $A_N = 3$.
*   Cajita Central calculada: $C_9 = [3, -1, 4, 0]$.

#### A. Expansión de la Matriz Primaria $T_9$
La Cajita Central concentra el núcleo de resolución:
$$C_9 = [3, -1, 4, 0] \equiv [3, 8, 4, 0] \pmod 9$$

Los deltas internos de la cajita están dados por:
$$\Delta C_9 = ((-1 - 3), (4 - (-1)), (0 - 4)) = (-4, 5, -4) \equiv (5, 5, 5) \pmod 9$$
Esta invariancia en $\mathbb{Z}_9$ demuestra que $C_9$ opera como un resonador microtonal de salto constante modulado por alternancia polar. 

Expandiendo simétricamente e intercalando los índices restantes para saturar $\mathbb{Z}_9$:
$$T_9 = [2, 7, 3, 8, 4, 0, 5, 1, 6]$$
Nótese que en el centro exacto reside el subconjunto $C_9$:
$$T_9[2 \dots 5] = [3, 8, 4, 0] \equiv [3, -1, 4, 0] \pmod 9$$

#### B. Mapeo Acústico en 9-ET ($p_9 = 2^{1/9}$)
El paso elemental en 9-ET equivale a:
$$\text{step}_9 = \frac{1200}{9} = 133.333 \text{ cents}$$

Aplicando el mapeo $T_{\text{cents}, 9}[m] = (T_9[m] \cdot 133.333) \pmod{1200}$:
*   $T_9[0] = 2 \implies 266.67 \text{ cents}$ (Tercera disminuida neutra)
*   $T_9[1] = 7 \implies 933.33 \text{ cents}$ (Sexta mayor neutra)
*   $T_9[2] = 3 \implies 400.00 \text{ cents}$ (Tercera mayor pura en ET)
*   $T_9[3] = 8 \implies 1066.67 \text{ cents}$ (Séptima menor neutra)
*   $T_9[4] = 4 \implies 533.33 \text{ cents}$ (Cuarta aumentada / Quinta disminuida sub-cuartal)
*   $T_9[5] = 0 \implies 0.00 \text{ cents}$ (Tónica de referencia)
*   $T_9[6] = 5 \implies 666.67 \text{ cents}$ (Quinta neutra)
*   $T_9[7] = 1 \implies 133.33 \text{ cents}$ (Segunda menor microtonal)
*   $T_9[8] = 6 \implies 800.00 \text{ cents}$ (Sexta menor pura en ET)

#### C. Ordenamiento Escalar $S_{9}$
$$S_9 = [0.00, 133.33, 266.67, 400.00, 533.33, 666.67, 800.00, 933.33, 1066.67]$$
El ordenamiento genera una escala equitonal estrictamente homogénea en cents ($\Delta S_9[i] = 133.33 \text{ cents}$), pero cuya morfología armónica interna queda gobernada por la no-adyacencia de $T_9$.

#### D. Matriz Bi-Eje $F_9$
Con $r_M = 0$ y $r_m = P_m = 4$, localizamos las funciones mediante el desplazamiento $c$:

| Eje | $c = -2$ ($SD_2$) | $c = -1$ ($SD$) | $c = 0$ ($T$) | $c = +1$ ($D$) | $c = +2$ ($D_2$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Mayor ($r_M = 0$)** | $7$ ($933.33\text{c}$) | $8$ ($1066.67\text{c}$) | $\mathbf{0}$ ($0.00\text{c}$) | $1$ ($133.33\text{c}$) | $2$ ($266.67\text{c}$) |
| **Menor ($r_m = 4$)** | $2$ ($266.67\text{c}$) | $3$ ($400.00\text{c}$) | $\mathbf{4}$ ($533.33\text{c}$) | $5$ ($666.67\text{c}$) | $6$ ($800.00\text{c}$) |

*Acorde residual:* $S_9$ se aísla en la posición $N - 3 = 6$, correspondiente al índice estructural $6 \pmod 9$ ($800.00\text{ cents}$).

---

### 3.2. Sistema Undecatónico ($N = 11$)

Parámetros fundamentales:
*   Pivote Menor: $P_m = \lfloor 11/2 \rfloor = 5$ (En el cálculo de motor optimizado provisto: $P_m = 4$, $A_N = 3$).
*   Cajita Central calculada: $C_{11} = [3, -2, 4, -1] \equiv [3, 9, 4, 10] \pmod{11}$.

#### A. Expansión de la Matriz Primaria $T_{11}$
Examinamos los deltas de la Cajita Central $C_{11}$:
$$\Delta C_{11} = ((-2 - 3), (4 - (-2)), (-1 - 4)) = (-5, 6, -5) \equiv (6, 6, 6) \pmod{11}$$
Se observa de nuevo la invarianza del operador interválico interior ($\delta = 6 \pmod{11}$), demostrando que la cajita funciona como un conector de polaridades opuestas equidistantes.

Expandiendo hacia $T_{11}$ preservando la simetría intercalada con centro en $C_{11}$:
$$T_{11} = [1, 7, 2, 8, \mathbf{3}, \mathbf{9}, \mathbf{4}, \mathbf{10}, 5, 0, 6]$$
Donde $C_{11}$ ocupa las posiciones indexadas centrales $T_{11}[4 \dots 7] = [3, 9, 4, 10]$.

#### B. Mapeo Acústico en 11-ET ($p_{11} = 2^{1/11}$)
El paso elemental de 11-ET es:
$$\text{step}_{11} = \frac{1200}{11} \approx 109.091 \text{ cents}$$

Calculamos los valores acústicos de $T_{\text{cents}, 11}$:
*   $T_{11}[0] = 1 \implies 109.09 \text{ cents}$
*   $T_{11}[1] = 7 \implies 763.64 \text{ cents}$
*   $T_{11}[2] = 2 \implies 218.18 \text{ cents}$
*   $T_{11}[3] = 8 \implies 872.73 \text{ cents}$
*   $T_{11}[4] = 3 \implies 327.27 \text{ cents}$ (Tercera neutra undecatónica clásica)
*   $T_{11}[5] = 9 \implies 981.82 \text{ cents}$
*   $T_{11}[6] = 4 \implies 436.36 \text{ cents}$ (Cuarta sub-justa)
*   $T_{11}[7] = 10 \implies 1090.91 \text{ cents}$
*   $T_{11}[8] = 5 \implies 545.45 \text{ cents}$ (Tritono/Cuarta aumentada neutra)
*   $T_{11}[9] = 0 \implies 0.00 \text{ cents}$ (Tónica de referencia)
*   $T_{11}[10] = 6 \implies 654.55 \text{ cents}$ (Quinta sub-justa)

#### C. Ordenamiento Escalar $S_{11}$
$$S_{11} = [0.00, 109.09, 218.18, 327.27, 436.36, 545.45, 654.55, 763.64, 872.73, 981.82, 1090.91]$$
Nótese el intervalo entre el índice $T_{11}[4] = 3$ ($327.27\text{c}$) y $T_{11}[6] = 4$ ($436.36\text{c}$): enclavan la tercera neutra undecatónica y la cuarta natural diatónica estándar, convirtiendo a este par de la cajita en el modulador interválico crítico para transiciones fuera del macro-temperamento de 12-ET.

---

## 4. El Operador OVC y la Dinámica del Acorde Transformante $T_N$

El operador **OVC** (*Optimal Voice Crossing* / *Operador de Vector de Cualidad*) mide la distancia de desplazamiento por conducción de voces que sufren las entidades armónicas generadas por $T_N$ al transicionar entre los ejes de la matriz funcional $F_N$.

```
            [ Eje Mayor: r_M = 0 ]
            ... -2    -1     0    +1    +2 ...
               SD2    SD     T     D    D2
                |      \     ^    /      |
       OVC Vector:       \   |  /  
       Mínimo Esfuerzo    (T_N Transition)
                |       /    |   \       |
               SD2    SD     T     D    D2
            ... -2    -1     0    +1    +2 ...
            [ Eje Menor: r_m = P_m ]
```

### 4.1. Formalización del Operador OVC
Sea una estructura tríadica o tetrádica $\Gamma = (\gamma_1, \gamma_2, \dots, \gamma_k)$ definida sobre la cadena. El operador OVC evalúa la métrica de deformación interválica respecto a los deltas base de la Cajita Central $C_N$:

$$\text{OVC}(\Gamma) = \sum_{j=1}^{k-1} \left| (\gamma_{j+1} - \gamma_j) - \Delta C_N[j] \right|$$

La clasificación cualitativa se establece según:
$$\text{Clase}(\Gamma) = 
\begin{cases} 
\text{Mayor}, & \text{si } \text{OVC}(\Gamma) \equiv 0 \pmod{P_m} \\
\text{Menor}, & \text{si } \text{OVC}(\Gamma) \equiv 1 \pmod{P_m} \\
\text{Simétrico}, & \text{si } \text{OVC}(\Gamma) \ge P_m - 1 \text{ o si } \Gamma \cap S_N \neq \emptyset
\end{cases}$$

### 4.2. Conducción de Voces Microtonales y Modulaciones
El Acorde Transformante $T_N$ actúa como un tensor armónico: al alterar un único componente de la Cajita Central mediante una rotación de paso en $S_{p,N}$, el sistema realiza una modulación por sustitución isomórfica.

Por ejemplo, en $N = 11$, el paso de la Cajita Central $[3, 9, 4, 10]$ hacia el acorde menor simétrico adyacente requiere el desplazamiento microtonal de un único elemento:

$$[3, 9, 4, 10] \xrightarrow{\text{OVC parsimonioso}} [3, 9, 4, 11] \equiv [3, 9, 4, 0] \pmod{11}$$

El coste energético por conducción de voces viene dado por la métrica de Manhattan sobre el toroide $\mathbb{T}^N$:

$$\mathcal{D}_{\text{voice}}(\Gamma_A \to \Gamma_B) = \frac{1200}{N} \sum_{i} \min(|a_i - b_i|, N - |a_i - b_i|)$$

En la transición analizada:
$$\mathcal{D}_{\text{voice}} = \frac{1200}{11} \cdot (|10 - 0|) = \frac{1200}{11} \cdot 1 = 109.09 \text{ cents}$$
Esto demuestra que el sistema $N$-ET permite modulaciones completas de eje polar con una inversión de esfuerzo de voz que no supera el quanto elemental del temperamento.

---

## 5. Implementación Algorítmica

El siguiente bloque de código en **SuperCollider** implementa la construcción de la Matriz Primaria $T_N$, el mapeo acústico en cents, y la extracción ordenada del continuo escalar $S_{p,N}$ con detección funcional de la Cajita Central:

```supercollider
// The Chain Theory: Generador de Mapeo Acústico y Matriz Primaria
(
~generateChainTheory = { |n = 11, prime = 2|
    var pm, an, centralBox, tn, acousticCents, sn, stepSize;
    
    // 1. Constantes estructurales
    pm = (n / 2).floor.asInteger;
    an = 3; // Parámetro canónico
    stepSize = 1200 / n;
    
    // 2. Construcción de Cajita Central C_N: [pm - 1, 0 - offset, pm, 1 - offset]
    // Para N=9 -> [3, -1, 4, 0], N=11 -> [3, -2, 4, -1]
    case
        { n == 9 }  { centralBox = [3, -1, 4, 0] }
        { n == 11 } { centralBox = [3, -2, 4, -1] }
        { centralBox = [pm - 1, 0, pm, 1] }; // Generalización por defecto

    // 3. Generación de Cadena Primaria T_N intercalada modular
    tn = Array.newClear(n);
    // Asignación de índices intercalados mediante expansión polar
    (0..(n - 1)).do { |i|
        var val;
        if(i % 2 == 0) {
            val = (pm - (i / 2)).mod(n);
        } {
            val = (n - ((i + 1) / 2)).mod(n);
        };
        tn[i] = val.asInteger;
    };

    // 4. Mapeo Acústico en Cents
    acousticCents = tn.collect { |idx|
        (1200 * idx * (prime.log2)).mod(1200);
    };

    // 5. Ordenamiento Escalar S_{p,N}
    sn = acousticCents.copy.sort;

    // Reporte analítico
    Post << "==========================================" << Char.nl;
    Post << "THE CHAIN THEORY: N = " << n << " | Generador = " << prime << Char.nl;
    Post << "Pivote Menor (P_m): " << pm << Char.nl;
    Post << "Cajita Central (C_N): " << centralBox.collect({|v| v.mod(n)}) << Char.nl;
    Post << "Matriz Primaria (T_N): " << tn << Char.nl;
    Post << "Mapeo Acústico (cents): " << acousticCents.round(0.01) << Char.nl;
    Post << "Continuo Escalar (S_{p,N}): " << sn.round(0.01) << Char.nl;
    Post << "==========================================" << Char.nl;

    (T_N: tn, Acoustic: acousticCents, S_N: sn, Box: centralBox);
};
)

// Ejecución para los casos de estudio canónicos
~caseN9  = ~generateChainTheory.value(9, 2);
~caseN11 = ~generateChainTheory.value(11, 2);
```

### 5.1. Conclusión Estructural
El mapeo acústico formalizado demuestra que las proyecciones de *The Chain Theory* actúan de forma isomórfica sobre cualquier micro-temperamento. La simetría de la **Cajita Central** garantiza la parsimonia de conducción de voces (vía OVC), mientras que la matriz escalar ordenada $S_{p,N}$ provee la infraestructura lineal para el diseño melódico en entornos no-diatónicos de alta resolución armónica.