# 📺 WatchNext — Sistema de Gestión y Recomendación de Series

Proyecto desarrollado para la tecnicatura en programación, aplicando estructuras de datos avanzadas y algoritmos en Python para gestionar un catálogo de producciones audiovisuales.

---

## 🚀 Características Principales y Estructuras Utilizadas

* **1. Búsqueda de Series (Árbol Binario de Búsqueda - BST):**
  * Permite buscar de forma eficiente cualquier título dentro del catálogo utilizando las propiedades de un Árbol Binario de Búsqueda ordenado alfabéticamente.
* **2. Catálogo Ordenado (Recorrido In-Order):**
  * Despliega la totalidad de las series ordenadas alfabéticamente de manera automática mediante un recorrido `in-order` sobre el árbol.
* **3. Exploración de Categorías (Árbol General):**
  * Muestra la jerarquía de géneros y clasificaciones temáticas organizadas mediante nodos multinivel.
* **4. Top de Series por Rating (Max-Heap):**
  * Utiliza una estructura de montículo máximo para extraer y ordenar de forma inmediata las producciones mejor valoradas por los usuarios.
* **5. Red de Recomendaciones y Conexiones (Grafo):**
  * Modela las relaciones de similitud entre las distintas producciones mediante un grafo no dirigido con pesos en las aristas.

---

## 🌐 Módulo TP8: Recorridos de Grafos (BFS y DFS)

Se incorporaron dos algoritmos clave para la navegación y análisis de la red de series:

* **BFS (Breadth-First Search / En Amplitud):**
  * *Caso de uso:* **Búsqueda de conexión más cercana.** Permite hallar el camino mínimo en saltos (aristas) entre una serie de partida y otra dentro de la red de similitudes.
  * *Utilidad:* Responde de forma óptima a consultas del tipo *"¿Cuál es el camino de recomendaciones más corto para llegar de una serie a otra?"*.
* **DFS (Depth-First Search / En Profundidad):**
  * *Caso de uso:* **Exploración profunda de la red.** Recorre las ramas de recomendación de forma exhaustiva antes de retroceder.
  * *Utilidad:* Permite desplegar y mapear todas las derivaciones temáticas encadenadas a partir de una producción inicial.

### Análisis de Complejidad (BFS y DFS)
* **Complejidad Temporal:** $\mathcal{O}(V + E)$, donde $V$ representa los vértices (series) y $E$ las aristas (conexiones de similitud). Ambos algoritmos visitan cada nodo y arista adyacente un número acotado de veces.
* **Complejidad Espacial:** $\mathcal{O}(V)$, debido al almacenamiento en memoria de las estructuras auxiliares (cola para BFS / pila para DFS) y al conjunto de control de nodos visitados.

---

## 💻 Interfaz y Ejecución

La aplicación cuenta con una **interfaz de línea de comandos (CLI)** limpia y accesible:

```bash
python main.py