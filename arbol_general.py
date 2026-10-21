class NodoArbolGeneral:
    def __init__(self, nombre, es_categoria=True):
        self.nombre = nombre
        self.es_categoria = es_categoria  # True si es Categoria/Subcategoria, False si es Serie
        self.hijos = []                   # Lista de nodos hijos (N-arios)

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)


class ArbolGeneralCategorias:
    def __init__(self, nombre_raiz="Series"):
        self.raiz = NodoArbolGeneral(nombre_raiz, es_categoria=True)

    def buscar_nodo(self, nombre, actual=None):
        """Busca un nodo dentro de la jerarquía (búsqueda recursiva)."""
        if actual is None:
            actual = self.raiz

        if actual.nombre.lower() == nombre.lower():
            return actual

        for hijo in actual.hijos:
            resultado = self.buscar_nodo(nombre, hijo)
            if resultado:
                return resultado
        return None

    def agregar_categoria(self, nombre_categoria, padre_nombre=None):
        """Agrega una categoría o subcategoría al árbol."""
        padre = self.buscar_nodo(padre_nombre) if padre_nombre else self.raiz
        if padre and padre.es_categoria:
            nuevo_nodo = NodoArbolGeneral(nombre_categoria, es_categoria=True)
            padre.agregar_hijo(nuevo_nodo)
            return True
        return False

    def agregar_serie(self, titulo_serie, categoria_nombre):
        """Agrega una serie a una categoría específica."""
        categoria = self.buscar_nodo(categoria_nombre)
        if categoria and categoria.es_categoria:
            nodo_serie = NodoArbolGeneral(titulo_serie, es_categoria=False)
            categoria.agregar_hijo(nodo_serie)
            return True
        return False

    def mostrar_jerarquia(self, actual=None, nivel=0):
        """Muestra el árbol jerárquico visualmente en la consola."""
        if actual is None:
            actual = self.raiz

        indentacion = "│   " * nivel
        prefijo = "├── " if nivel > 0 else ""
        icono = "📁 " if actual.es_categoria else "🎬 "
        print(f"{indentacion}{prefijo}{icono}{actual.nombre}")

        for hijo in actual.hijos:
            self.mostrar_jerarquia(hijo, nivel + 1)


def inicializar_jerarquia_ejemplo():
    """Construye la jerarquía inicial del dominio WatchNext."""
    arbol = ArbolGeneralCategorias("Series")

    # Categorías principales
    arbol.agregar_categoria("Ciencia Ficción", "Series")
    arbol.agregar_categoria("Acción", "Series")
    arbol.agregar_categoria("Comedia", "Series")

    # Subcategorías de Ciencia Ficción
    arbol.agregar_categoria("Cyberpunk", "Ciencia Ficción")
    arbol.agregar_categoria("Viajes temporales", "Ciencia Ficción")
    arbol.agregar_categoria("Inteligencia artificial", "Ciencia Ficción")

    # Cargar series de ejemplo
    arbol.agregar_serie("Dark", "Viajes temporales")
    arbol.agregar_serie("Stranger Things", "Ciencia Ficción")
    arbol.agregar_serie("Arcane", "Cyberpunk")
    arbol.agregar_serie("Westworld", "Inteligencia artificial")
    arbol.agregar_serie("The Office", "Comedia")

    return arbol