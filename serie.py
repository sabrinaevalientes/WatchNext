class Genero:
    def __init__(self, nombre: str):
        self._nombre = nombre.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    def __eq__(self, otro):
        # Permite comparar Genero("Drama") == "drama" o Genero("Drama") == Genero("drama")
        if isinstance(otro, Genero):
            return self._nombre.lower() == otro._nombre.lower()
        if isinstance(otro, str):
            return self._nombre.lower() == otro.lower()
        return False

    def __hash__(self):
        return hash(self._nombre.lower())

    def __repr__(self):
        return self._nombre


class Serie:
    def __init__(self, id_serie: int, titulo: str, genero: str, rating: float):
        self._id = id_serie
        self._titulo = titulo
        self._genero = Genero(genero) if isinstance(genero, str) else genero
        self._rating = float(rating)

    @property
    def id(self):
        return self._id

    @property
    def titulo(self):
        return self._titulo

    @property
    def genero(self):
        return self._genero

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, valor):
        if not (0 <= valor <= 10):
            raise ValueError("El rating debe estar entre 0 y 10")
        self._rating = float(valor)

    def __repr__(self):
        return f"📺 [{self._id}] {self._titulo} ({self._genero}) ⭐ {self._rating}"


class Usuario:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._historial = {}  # id_serie -> rating propio

    @property
    def nombre(self):
        return self._nombre

    @property
    def historial(self):
        return dict(self._historial)

    def calificar_serie(self, serie: Serie, nuevo_rating: float):
        # Utiliza el setter de Serie (con validación de 0 a 10)
        serie.rating = nuevo_rating
        self._historial[serie.id] = nuevo_rating
        print(f"✅ {self._nombre} actualizó la calificación de '{serie.titulo}' a {nuevo_rating} ⭐")