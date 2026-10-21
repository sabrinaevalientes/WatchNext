class NodoBST:
    def __init__(self, serie):
        self.serie = serie
        self.izq = None
        self.der = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    # 1. INSERCIÓN (por título alfabético)
    def insertar(self, serie):
        self.raiz = self._insertar_recursivo(self.raiz, serie)

    def _insertar_recursivo(self, actual, serie):
        if actual is None:
            return NodoBST(serie)

        if serie.titulo.lower() < actual.serie.titulo.lower():
            actual.izq = self._insertar_recursivo(actual.izq, serie)
        elif serie.titulo.lower() > actual.serie.titulo.lower():
            actual.der = self._insertar_recursivo(actual.der, serie)

        return actual

    # 2. BÚSQUEDA
    def buscar(self, titulo_buscado):
        return self._buscar_recursivo(self.raiz, titulo_buscado.lower())

    def _buscar_recursivo(self, actual, titulo_buscado):
        if actual is None or actual.serie.titulo.lower() == titulo_buscado:
            return actual.serie if actual else None

        if titulo_buscado < actual.serie.titulo.lower():
            return self._buscar_recursivo(actual.izq, titulo_buscado)
        return self._buscar_recursivo(actual.der, titulo_buscado)

    # 3. RECORRIDOS (Inorder, Preorder, Postorder)
    def recorrer_inorder(self):
        resultado = []
        self._inorder(self.raiz, resultado)
        return resultado

    def _inorder(self, actual, resultado):
        if actual:
            self._inorder(actual.izq, resultado)
            resultado.append(actual.serie)
            self._inorder(actual.der, resultado)

    def recorrer_preorder(self):
        resultado = []
        self._preorder(self.raiz, resultado)
        return resultado

    def _preorder(self, actual, resultado):
        if actual:
            resultado.append(actual.serie)
            self._preorder(actual.izq, resultado)
            self._preorder(actual.der, resultado)

    def recorrer_postorder(self):
        resultado = []
        self._postorder(self.raiz, resultado)
        return resultado

    def _postorder(self, actual, resultado):
        if actual:
            self._postorder(actual.izq, resultado)
            self._postorder(actual.der, resultado)
            resultado.append(actual.serie)