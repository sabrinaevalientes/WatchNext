from serie import Serie
from arbol import ArbolBinarioBusqueda
from arbol_general import inicializar_jerarquia_ejemplo
from heap import MaxHeapSeries
from grafo import GrafoSeries

def cargar_datos_iniciales(arbol_bst, heap_series, grafo_series):
    # Instancias de series
    s1 = Serie("Breaking Bad", "Drama", 9.5, 2008)
    s2 = Serie("Dark", "Ciencia Ficción", 8.7, 2017)
    s3 = Serie("Stranger Things", "Fantasía", 8.7, 2016)
    s4 = Serie("The Office", "Comedia", 8.9, 2005)
    s5 = Serie("Arcane", "Animación", 9.0, 2021)
    s6 = Serie("Interstellar", "Ciencia Ficción", 8.6, 2014)

    series = [s1, s2, s3, s4, s5, s6]

    # Carga en BST y Max-Heap
    for s in series:
        arbol_bst.insertar(s)
        heap_series.insertar(s)
        grafo_series.agregar_vertice(s)

    # Configuración de conexiones (Aristas con peso de similitud)
    # Series de Ciencia Ficción conectadas
    grafo_series.agregar_arista(s2, s6, 0.95)  # Dark <-> Interstellar
    # Conexiones temáticas y de género cruzado
    grafo_series.agregar_arista(s1, s3, 0.75)  # Breaking Bad <-> Stranger Things
    grafo_series.agregar_arista(s3, s5, 0.80)  # Stranger Things <-> Arcane

def main():
    arbol_series = ArbolBinarioBusqueda()
    arbol_cat = inicializar_jerarquia_ejemplo()
    heap_series = MaxHeapSeries()
    grafo_series = GrafoSeries()
    
    cargar_datos_iniciales(arbol_series, heap_series, grafo_series)

    while True:
        print("\n========================================")
        print("    📺 WATCHNEXT — TERMINAL (v5)       ")
        print("========================================")
        print("1. Buscar serie (BST)")
        print("2. Listar catálogo ordenado (In-Order)")
        print("3. Explorar categorías (Árbol General)")
        print("4. Ver Top de series por rating (Max-Heap)")
        print("5. Ver Red de Recomendaciones (Grafo)")
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
                print(f"  {idx}. {s.titulo} — ⭐ {s.rating} ({str(s.genero)})")

        elif opcion == "5":
            print("\n🕸️ Red de Conexiones y Recomendaciones (Grafo):")
            grafo_series.mostrar_red()

        elif opcion == "0":
            print("\n👋 ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()