import json
from serie import Serie, Genero, Usuario

def cargar_series(ruta_archivo):
    catalogo = []
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for item in datos:
                s = Serie(item["id"], item["titulo"], item["genero"], item["rating"])
                catalogo.append(s)
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo: {ruta_archivo}")
    return catalogo

def main():
    catalogo = cargar_series("series.json")
    usuario_actual = Usuario("Invitado")

    while True:
        print("\n=========================================")
        print(f"   📺 WATCHNEXT — Usuario: {usuario_actual.nombre}")
        print("=========================================")
        print("1. Listar catálogo completo")
        print("2. Buscar por título")
        print("3. Filtrar por género")
        print("4. Calificar una serie (Usuario)")
        print("0. Salir")
        print("-----------------------------------------")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- CATÁLOGO COMPLETO ---")
            for serie in catalogo:
                print(serie)

        elif opcion == "2":
            busqueda = input("\nIngrese el título a buscar: ").strip().lower()
            print(f"\n--- RESULTADOS PARA '{busqueda}' ---")
            encontrados = False
            for serie in catalogo:
                if busqueda in serie.titulo.lower():
                    print(serie)
                    encontrados = True
            if not encontrados:
                print("❌ No se encontraron coincidencias.")

        elif opcion == "3":
            genero_buscado = input("\nIngrese el género (ej. Comedia, Drama): ").strip().lower()
            print(f"\n--- SERIES DE GÉNERO: '{genero_buscado}' ---")
            encontrados = False
            for serie in catalogo:
                if serie.genero == genero_buscado:  # Compara usando la clase Genero
                    print(serie)
                    encontrados = True
            if not encontrados:
                print("❌ No hay series en ese género.")

        elif opcion == "4":
            try:
                id_serie = int(input("\nIngrese el ID de la serie a calificar: "))
                serie_encontrada = next((s for s in catalogo if s.id == id_serie), None)
                if serie_encontrada:
                    nuevo_rating = float(input(f"Ingrese el nuevo rating para '{serie_encontrada.titulo}' (0-10): "))
                    usuario_actual.calificar_serie(serie_encontrada, nuevo_rating)
                else:
                    print("❌ No se encontró ninguna serie con ese ID.")
            except ValueError as e:
                print(f"❌ Error de entrada: {e}")

        elif opcion == "0":
            print("\n¡Gracias por usar WatchNext! 👋")
            break

if __name__ == "__main__":
    main()