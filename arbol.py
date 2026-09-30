class NodoArbol:
    def __init__(self, serie):
        self.serie = serie
        self.izquierda = None
        self.derecha = None


class ArbolBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, serie):
        if self.raiz is None:
            self.raiz = NodoArbol(serie)
        else:
            self._insertar_recursivo(self.raiz, serie)

    def _insertar_recursivo(self, nodo_actual, serie):
        titulo_nuevo = serie.titulo.lower()
        titulo_actual = nodo_actual.serie.titulo.lower()

        if titulo_nuevo < titulo_actual:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = NodoArbol(serie)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, serie)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = NodoArbol(serie)
            else:
                self._insertar_recursivo(nodo_actual.derecha, serie)

    def buscar_por_titulo(self, titulo_buscado):
        return self._buscar_recursivo(self.raiz, titulo_buscado.lower())

    def _buscar_recursivo(self, nodo_actual, titulo_buscado):
        if nodo_actual is None:
            return None
        
        titulo_actual = nodo_actual.serie.titulo.lower()

        if titulo_buscado == titulo_actual:
            return nodo_actual.serie
        elif titulo_buscado < titulo_actual:
            return self._buscar_recursivo(nodo_actual.izquierda, titulo_buscado)
        else:
            return self._buscar_recursivo(nodo_actual.derecha, titulo_buscado)