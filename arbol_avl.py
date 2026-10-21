class NodoAVL:
    def __init__(self, serie):
        self.serie = serie
        self.izq = None
        self.der = None
        self.altura = 1


class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def _obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def _obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self._obtener_altura(nodo.izq) - self._obtener_altura(nodo.der)

    def _rotacion_derecha(self, z):
        y = z.izq
        T3 = y.der
        y.der = z
        z.izq = T3

        z.altura = 1 + max(self._obtener_altura(z.izq), self._obtener_altura(z.der))
        y.altura = 1 + max(self._obtener_altura(y.izq), self._obtener_altura(y.der))

        return y

    def _rotacion_izquierda(self, z):
        y = z.der
        T2 = y.izq
        y.izq = z
        z.der = T2

        z.altura = 1 + max(self._obtener_altura(z.izq), self._obtener_altura(z.der))
        y.altura = 1 + max(self._obtener_altura(y.izq), self._obtener_altura(y.der))

        return y

    def insertar(self, serie):
        self.raiz = self._insertar_recursivo(self.raiz, serie)

    def _insertar_recursivo(self, actual, serie):
        if not actual:
            return NodoAVL(serie)

        if serie.titulo.lower() < actual.serie.titulo.lower():
            actual.izq = self._insertar_recursivo(actual.izq, serie)
        elif serie.titulo.lower() > actual.serie.titulo.lower():
            actual.der = self._insertar_recursivo(actual.der, serie)
        else:
            return actual

        actual.altura = 1 + max(self._obtener_altura(actual.izq), self._obtener_altura(actual.der))
        balance = self._obtener_balance(actual)

        # Rotaciones
        if balance > 1 and serie.titulo.lower() < actual.izq.serie.titulo.lower():
            return self._rotacion_derecha(actual)

        if balance < -1 and serie.titulo.lower() > actual.der.serie.titulo.lower():
            return self._rotacion_izquierda(actual)

        if balance > 1 and serie.titulo.lower() > actual.izq.serie.titulo.lower():
            actual.izq = self._rotacion_izquierda(actual.izq)
            return self._rotacion_derecha(actual)

        if balance < -1 and serie.titulo.lower() < actual.der.serie.titulo.lower():
            actual.der = self._rotacion_derecha(actual.der)
            return self._rotacion_izquierda(actual)

        return actual

    def buscar(self, titulo_buscado):
        return self._buscar_recursivo(self.raiz, titulo_buscado.lower())

    def _buscar_recursivo(self, actual, titulo_buscado):
        if not actual or actual.serie.titulo.lower() == titulo_buscado:
            return actual.serie if actual else None

        if titulo_buscado < actual.serie.titulo.lower():
            return self._buscar_recursivo(actual.izq, titulo_buscado)
        return self._buscar_recursivo(actual.der, titulo_buscado)

    def obtener_altura_total(self):
        return self._obtener_altura(self.raiz)