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