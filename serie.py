class Genero:
    def __init__(self, nombre):
        # Nos aseguramos de que el nombre del género sea siempre un string limpio
        self.nombre = str(nombre)

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre


class Serie:
    def __init__(self, titulo, genero, rating, anio):
        self.titulo = str(titulo)
        self.genero = Genero(genero) if not isinstance(genero, Genero) else genero
        self.rating = float(rating)
        self.anio = int(anio)

    def __repr__(self):
        return f"{self.titulo} ({self.anio}) — Género: {self.genero} — ⭐ {self.rating}"