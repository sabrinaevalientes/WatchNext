ESTRUCTURA DE DATOS 
COMISIÓN 2 
INTEGRANTES:
SABRINA VALIENTES  
FRANCISCO SEBASTIÁN CARDOZO
Nombre del proyecto: WatchNext 
Dominio elegido: Series de televisión y plataformas de streaming. 
Justificación: Elegimos series porque sus elementos tienen relaciones naturales (mismo 
creador, elenco compartido, géneros, plataformas o universos compartidos). Esto nos 
permite modelar estructuras de datos avanzadas a lo largo de la cursada: árboles generales 
para la jerarquía de géneros/subgéneros, heaps para rankings por puntuación, y grafos para 
representar la red de conexiones entre series, actores y directores. 
Problema que resuelve: 
Resuelve la "parálisis por elección" y la pérdida de tiempo que ocurre al finalizar una serie. 
En lugar de depender de algoritmos comerciales que priorizan contenido promocionado, 
WatchNext analiza coincidencias reales en la red de datos para ofrecer una recomendación 
precisa y rápida sin navegar a ciegas por catálogos masivos. 
Usuario objetivo: 
Mariana (22 años): Ve series los fines de semana. Cuando termina una temporada o serie 
que le gustó mucho, quiere encontrar inmediatamente otra opción de estilo y tono similar 
para seguir mirando, evitando perder 20 minutos scrolleando sin saber qué elegir. 
Cinco funcionalidades iniciales: 
1. Buscar serie: Búsqueda rápida de una serie por su título o identificador único. 
2. Explorar por categorías: Navegación jerárquica por géneros y subgéneros (ej. Drama → 
Suspenso → Policial). 
3. Ver Top 10: Consulta de las series mejor valoradas por la crítica y los usuarios. 
4. Recomendación directa: Algoritmo "Si te gustó X, te sugerimos Y" basado en 
características compartidas. 
5. Explorar red de conexiones: Visualizar relaciones directas entre series (mismo creador, 
actores en común o spin-offs). 
Primer boceto de la interfaz de terminal: 
 
================================================== 
                    WATCHNEXT  
================================================== 
 
1. Buscar serie por título 
2. Explorar categorías y géneros 
3. Ver Top 10 mejor valoradas 
4. Obtener recomendaciones ("Si te gustó X...") 
5. Explorar red de conexiones (Creadores / Actores) 
0. Salir 
 -------------------------------------------------- 
Seleccione una opción: 
 
Ejemplo de interacción (Input / Output tipo terminal): 
 
> Seleccione una opción: 4 
> Ingrese el título de la serie que acaba de ver: Stranger Things 
 
╔══════════════════════════════════════════════════╗ 
║       WATCHNEXTRECOMIENDA                                        ║ 
╠══════════════════════════════════════════════════╣ 
║   Si te gustó STRANGER THINGS, quizás te   interesen:                                         ║ 
║                                                                                                                     ║ 
║ 1. Dark           [Misterio/Sci-Fi] ⭐ 8.7
                                                   ║ 
║ 2. Super 8        [Sci-Fi/Aventura] ⭐ 8.2
                                                   ║ 
║ 3. Paper Girls    [Sci-Fi/Aventura] ⭐ 7.8
                                                   ║ 
╚══════════════════════════════════════════════════╝




# 📺 WatchNext — TP1

Proyecto en Python para la gestión y consulta de un catálogo de series, desarrollado con Programación Orientada a Objetos (POO), persistencia de datos en JSON y arquitectura modular.

## 🚀 Funcionalidades

- **Listar catálogo completo:** Visualización de todas las series registradas con su puntuación y género.
- **Búsqueda por título:** Búsqueda interactiva por coincidencias en el nombre.
- **Filtrado por género:** Filtrado dinámico de series según la categoría.
- **Calificación de series:** Sistema de calificación para usuarios con validación de rango (0 a 10).

## 📁 Estructura del Proyecto

- `serie.py`: Módulo con las clases de dominio (`Serie`, `Genero`, `Usuario`), encapsulamiento (`@property`) y validaciones.
- `main.py`: Lógica principal, lectura del archivo de datos y menú interactivo por consola.
- `series.json`: Archivo de datos para la persistencia del catálogo.

## 💻 Requisitos y Ejecución

- **Python 3.10+** (utiliza bibliotecas nativas como `json`).

Para ejecutar el proyecto localmente:
```bash
python main.py