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