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
    grafo_series.agregar_arista(s2, s6, 0.95)  # Dark <-> Interstellar
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
        print("         WATCHNEXT — TERMINAL           ")
        print("========================================")
        print("1. Buscar serie")
        print("2. Listar catálogo ordenado")
        print("3. Explorar categorías")
        print("4. Ver Top de series")
        print("5. Ver red de recomendaciones")
        print("6. Buscar conexión más cercana")
        print("7. Explorar red en profundidad")
        print("0. Salir")
        print("----------------------------------------")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            titulo = input("\nIngrese título a buscar: ").strip()
            res = arbol_series.buscar(titulo)
            if res:
                print(f"\n✅ Encontrado (Estructura: Árbol BST): {res}")
            else:
                print(f"\n❌ No se encontró '{titulo}'.")

        elif opcion == "2":
            print("\n📂 Catálogo Ordenado (Recorrido In-Order):")
            for s in arbol_series.recorrer_inorder():
                print(f" - {s}")

        elif opcion == "3":
            print("\n🌳 Jerarquía de Categorías (Árbol General):")
            arbol_cat.mostrar_jerarquia()

        elif opcion == "4":
            print("\n🏆 Top de Series con Mayor Rating (Estructura Max-Heap):")
            top = heap_series.obtener_top(5)
            for idx, s in enumerate(top, 1):
                print(f" {idx}. {s.titulo} — ⭐ {s.rating}")

        elif opcion == "5":
            print("\n🕸️ Red de Conexiones y Recomendaciones (Grafo):")
            grafo_series.mostrar_red()

        elif opcion == "6":
            print("\n🔍 BÚSQUEDA DE CAMINO MÁS CORTO [Algoritmo BFS]")
            titulo_inicio = input("Ingrese el título de la serie de partida: ").strip()
            titulo_buscado = input("Ingrese el título de la serie que desea encontrar: ").strip()
            
            serie_inicio_obj = None
            for s in grafo_series.adyacencias.keys():
                if s.titulo.lower() == titulo_inicio.lower():
                    serie_inicio_obj = s
                    break
                    
            if serie_inicio_obj:
                camino = grafo_series.bfs_camino_mas_cercano(serie_inicio_obj, titulo_buscado)
                if camino:
                    print("\n✨ ¡Camino encontrado (BFS):")
                    print(" -> ".join([s.titulo for s in camino]))
                else:
                    print("\n❌ No se encontró una conexión hacia esa serie.")
            else:
                print(f"\n❌ No se encontró la serie de partida '{titulo_inicio}' en el grafo.")

        elif opcion == "7":
            print("\n🌐 EXPLORACIÓN DE RED EN PROFUNDIDAD [Algoritmo DFS]")
            titulo_inicio = input("Ingrese el título de la serie para explorar: ").strip()
            
            serie_inicio_obj = None
            for s in grafo_series.adyacencias.keys():
                if s.titulo.lower() == titulo_inicio.lower():
                    serie_inicio_obj = s
                    break
                    
            if serie_inicio_obj:
                exploracion = grafo_series.dfs_explorar_red(serie_inicio_obj)
                print("\n🚀 Red explorada en profundidad (DFS):")
                for s in exploracion:
                    print(f" - {s.titulo} ({s.genero})")
            else:
                print(f"\n❌ No se encontró la serie '{titulo_inicio}' en el grafo.")

        elif opcion == "0":
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("\n⚠️ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()