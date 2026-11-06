class MaxHeapSeries:
    def __init__(self):
        self.elementos = []  # Lista que almacena las series como un árbol binario completo

    def insertar(self, serie):
        """Inserta una serie y la hace flotar según su rating (mayor rating = mayor prioridad)."""
        self.elementos.append(serie)
        self._flotar(len(self.elementos) - 1)

    def _flotar(self, indice):
        """Mueve el elemento hacia arriba si su rating es mayor que el de su padre."""
        while indice > 0:
            padre = (indice - 1) // 2
            if self.elementos[indice].rating > self.elementos[padre].rating:
                self.elementos[indice], self.elementos[padre] = self.elementos[padre], self.elementos[indice]
                indice = padre
            else:
                break

    def obtener_top(self, k=5):
        """Devuelve las K series con mayor rating sin alterar la estructura del heap."""
        copia = list(self.elementos)
        resultado = []
        while copia and len(resultado) < k:
            max_idx = 0
            for i in range(1, len(copia)):
                if copia[i].rating > copia[max_idx].rating:
                    max_idx = i
            resultado.append(copia.pop(max_idx))
        return resultado