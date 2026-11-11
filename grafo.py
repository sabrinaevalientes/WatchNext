from collections import deque

class GrafoSeries:
    def __init__(self):
        # Diccionario de adyacencia: { serie: { vecino: peso, ... } }
        self.adyacencias = {}

    def agregar_vertice(self, serie):
        if serie not in self.adyacencias:
            self.adyacencias[serie] = {}

    def agregar_arista(self, serie1, serie2, peso=1.0):
        # Aseguramos que existan ambos vértices
        self.agregar_vertice(serie1)
        self.agregar_vertice(serie2)
        # Grafo no dirigido: la conexión va en ambas direcciones con el mismo peso
        self.adyacencias[serie1][serie2] = peso
        self.adyacencias[serie2][serie1] = peso

    def obtener_recomendaciones(self, serie):
        """Retorna una lista de tuplas (serie_vecina, peso) ordenadas por mayor similitud."""
        if serie in self.adyacencias:
            vecinos = self.adyacencias[serie].items()
            return sorted(vecinos, key=lambda x: x[1], reverse=True)
        return []

    def mostrar_red(self):
        """Muestra todas las conexiones del grafo en la terminal."""
        for serie, vecinos in self.adyacencias.items():
            print(f"  🎬 {serie.titulo} ({serie.genero}):")
            if vecinos:
                for vecino, peso in vecinos.items():
                    print(f"     ├── Conectada con: {vecino.titulo} [Similitud: {peso}]")
            else:
                print("     └── Sin conexiones registradas.")

    def bfs_camino_mas_cercano(self, serie_inicio, titulo_buscado):
        """Busca una serie objetivo usando BFS (Amplitud) por el camino más corto en aristas."""
        if serie_inicio not in self.adyacencias:
            return None

        visitados = {serie_inicio}
        # La cola guarda tuplas de: (nodo_actual, [camino_recorrido])
        cola = deque([(serie_inicio, [serie_inicio])])

        while cola:
            actual, camino = cola.popleft()

            if actual.titulo.lower() == titulo_buscado.lower():
                return camino

            for vecino in self.adyacencias[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append((vecino, camino + [vecino]))
        return None

    def dfs_explorar_red(self, serie_inicio):
        """Explora toda la red conectada en profundidad (DFS) a partir de una serie."""
        if serie_inicio not in self.adyacencias:
            return []

        visitados = set()
        resultado = []
        pila = [serie_inicio]

        while pila:
            actual = pila.pop()
            if actual not in visitados:
                visitados.add(actual)
                resultado.append(actual)
                # Agregamos los vecinos a la pila en orden inverso para mantener coherencia
                for vecino in list(self.adyacencias[actual].keys()):
                    if vecino not in visitados:
                        pila.append(vecino)
        return resultado