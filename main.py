from serie import Serie
from arbol import ArbolBinarioBusqueda

def cargar_datos_prueba(arbol):
    series = [
        Serie("Dark", "Ciencia Ficción", 8.7, 2017),
        Serie("Breaking Bad", "Drama", 9.5, 2008),
        Serie("Stranger Things", "Fantasía", 8.7, 2016),
        Serie("Arcane", "Animación", 9.0, 2021),
        Serie("The Office", "Comedia", 8.9, 2005)
    ]
    for s in series:
        arbol.insertar(s)

def main():
    arbol_series = ArbolBinarioBusqueda()
    cargar_datos_prueba(arbol_series)

    while True:
        print("\n========================================")
        print("          📺 WATCHNEXT — TERMINAL      ")
        print("========================================")
        print("1. Buscar serie en BST (O(log n))")
        print("2. Listar series ordenadas alfabéticamente (In-Order)")
        print("3. Ver estructura del árbol (Pre-Order / Post-Order)")
        print("4. Agregar nueva serie")
        print("0. Salir")
        print("----------------------------------------")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            titulo = input("\nIngrese título a buscar: ").strip()
            res = arbol_series.buscar(titulo)
            if res:
                print(f"\n✅ Serie encontrada: {res}")
            else:
                print(f"\n❌ No se encontró '{titulo}'.")

        elif opcion == "2":
            print("\n📋 Catálogo (In-Order / Orden alfabético):")
            for s in arbol_series.recorrer_inorder():
                print(f"  - {s}")

        elif opcion == "3":
            print("\n🔍 Pre-Order:")
            for s in arbol_series.recorrer_preorder():
                print(f"  - {s.titulo}")
            print("\n🔍 Post-Order:")
            for s in arbol_series.recorrer_postorder():
                print(f"  - {s.titulo}")

        elif opcion == "4":
            t = input("Título: ").strip()
            g = input("Género: ").strip()
            r = float(input("Rating: "))
            a = int(input("Año: "))
            arbol_series.insertar(Serie(t, g, r, a))
            print(f"\n✅ '{t}' agregada al BST.")

        elif opcion == "0":
            print("\n👋 ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()