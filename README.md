# 📺 WatchNext — Sistema de Gestión de Series

Proyecto desarrollado en Python para la materia Estructuras de Datos. Incluye arquitectura modular, persistencia JSON, modelos POO y análisis experimental de complejidad algorítmica.

---

## 📁 Estructura del Repositorio

- `serie.py`: Clases de dominio (`Serie`, `Genero`, `Usuario`), encapsulamiento y validaciones.
- `main.py`: Menú interactivo por consola y carga de datos.
- `series.json`: Persistencia de datos del catálogo.
- `arbol.py`: Implementación de Árbol Binario de Búsqueda (ABB) para búsqueda optimizada por título.
- `experimentos.py`: Script de benchmarking y medición de tiempos empíricos.

---

## ⚡ TP2: Análisis de Complejidad y Rendimiento

Se evaluó la operación crítica de **Búsqueda por Título** comparando dos estructuras de datos:
1. **Búsqueda Secuencial sobre Lista:** $\mathcal{O}(n)$
2. **Búsqueda sobre Árbol Binario de Búsqueda (ABB):** $\mathcal{O}(\log n)$

### Tabla de Resultados Medidos

| N Elementos | Búsqueda Secuencial ($\mathcal{O}(n)$) | Búsqueda en Árbol ($\mathcal{O}(\log n)$) |
| :--- | :--- | :--- |
| **1.000** | 0.1811 ms | 0.0096 ms |
| **10.000** | 1.2637 ms | 0.0105 ms |
| **100.000** | 53.6028 ms | 0.0133 ms |

### Conclusión Técnica
La búsqueda secuencial presenta un crecimiento de tiempo directamente proporcional a la cantidad de datos ($n$). En cambio, la estructura en Árbol Binario descarta la mitad de las ramas en cada comparación, logrando un rendimiento casi constante a gran escala. Para volúmenes de datos superiores a $1.000$ registros, el uso del ABB reduce drásticamente el tiempo de respuesta.

---

## 💻 Requisitos y Ejecución

- **Python 3.10+**

Ejecutar menú principal:
```bash
python main.py


## TP3: Árbol Binario de Búsqueda (BST)

En esta etapa incorporamos un Árbol Binario de Búsqueda (`ArbolBinarioBusqueda`) para gestionar el catálogo de series de **WatchNext**, utilizando como clave de ordenamiento el **título de la serie** (orden alfabético).

### Funcionalidades implementadas:
- **Inserción:** Inserta de forma recursiva manteniendo la propiedad del BST.
- **Búsqueda Eficiente:** Búsqueda recursiva con complejidad de tiempo $O(\log n)$ en promedio.
- **Recorridos:**
  - `In-Order`: Muestra el catálogo ordenado alfabéticamente.
  - `Pre-Order`: Permite visualizar/respaldar la estructura jerárquica desde la raíz.
  - `Post-Order`: Procesa primero las hojas.

### Comparación técnica: Búsqueda Secuencial (TP2) vs. BST (TP3)
| Estructura | Complejidad Promedio | Peor Caso |
| :--- | :--- | :--- |
| **Lista Lineal (TP2)** | $O(n)$ | $O(n)$ |
| **Árbol Binario (TP3)** | **$O(\log n)$** | $O(n)$ *(si el árbol se desbalancea)* |


## TP4: Árbol AVL (Auto-balanceado)

### 1. Experimento de Desbalance
Insertamos 1.000 series ordenadas alfabéticamente (`Serie_0001` a `Serie_1000`) para simular la degradación de la estructura.

### 2. Resultados Obtenidos
| Estructura | Altura del Árbol | Complejidad de Búsqueda |
| :--- | :--- | :--- |
| **BST Común (TP3)** | **1000** | $O(n)$ *(degeneró en lista enlazada)* |
| **Árbol AVL (TP4)** | **10** ($\approx \log_2(1000)$) | **$O(\log n)$** *(balance perfecto)* |

### 3. Conclusión Técnica
El balance importa porque evita que el árbol degeneren en una lista lineal cuando se insertan elementos ordenados. Las rotaciones automáticas del AVL garantizan una altura acotada por $O(\log n)$, manteniendo las búsquedas eficientes en el peor de los casos.