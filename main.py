from serie import Serie
from arbol import ArbolBinarioBusqueda
from arbol_general import inicializar_jerarquia_ejemplo
from heap import MaxHeapSeries

def cargar_datos_iniciales(arbol_bst, heap_series):
    # Las series de siempre, coherentes con todo el proyecto
    series = [
        Serie("Breaking Bad", "Drama", 9.5, 2008),
        Serie("Dark", "Ciencia Ficción", 8.7, 2017),
        Serie("Stranger Things", "Fantasía", 8.7, 2016),
        Serie("The Office", "Comedia", 8.9, 2005),
        Serie("Arcane", "Animación", 9.0, 2021)
    ]
    for s in series:
        arbol_bst.insertar(s)
        heap_series.insertar(s)

def main():
    arbol_series = ArbolBinarioBusqueda()
    arbol_cat = inicializar_jerarquia_ejemplo()
    heap_series = MaxHeapSeries()
    
    cargar_datos_iniciales(arbol_series, heap_series)

    while True:
        print("\n========================================")
        print("          📺 WATCHNEXT — TERMINAL      ")
        print("========================================")
        print("1. Buscar serie (BST)")
        print("2. Listar catálogo ordenado (In-Order)")
        print("3. Explorar categorías (Árbol General)")
        print("4. Ver Top de series por rating (Max-Heap)")
        print("0. Salir")
        print("----------------------------------------")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            titulo = input("\nIngrese título a buscar: ").strip()
            res = arbol_series.buscar(titulo)
            if res:
                print(f"\n✅ Encontrado: {res}")
            else:
                print(f"\n❌ No se encontró '{titulo}'.")

        elif opcion == "2":
            print("\n📋 Catálogo Ordenado (In-Order):")
            for s in arbol_series.recorrer_inorder():
                print(f"  - {s}")

        elif opcion == "3":
            print("\n🌳 Jerarquía de Categorías:")
            arbol_cat.mostrar_jerarquia()

        elif opcion == "4":
            print("\n🏆 Top de Series con Mayor Rating (Max-Heap):")
            top = heap_series.obtener_top(5)
            for idx, s in enumerate(top, 1):
                print(f"  {idx}. {s.titulo} — ⭐ {s.rating} ({s.genero})")

        elif opcion == "0":
            print("\n👋 ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()