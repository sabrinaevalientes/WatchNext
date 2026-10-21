from serie import Serie
from arbol import ArbolBinarioBusqueda
from arbol_general import inicializar_jerarquia_ejemplo

def main():
    arbol_series = ArbolBinarioBusqueda()
    arbol_categorias = inicializar_jerarquia_ejemplo()

    while True:
        print("\n========================================")
        print("          📺 WATCHNEXT — TERMINAL      ")
        print("========================================")
        print("1. Buscar serie en BST (O(log n))")
        print("2. Listar series ordenadas alfabéticamente (In-Order)")
        print("3. Explorar categorías (Árbol General N-ario)")
        print("4. Ver estructura del árbol BST (Pre-Order / Post-Order)")
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
            print("\n🌳 Jerarquía de Categorías de WatchNext:")
            arbol_categorias.mostrar_jerarquia()

        elif opcion == "4":
            print("\n🔍 Pre-Order:")
            for s in arbol_series.recorrer_preorder():
                print(f"  - {s.titulo}")

        elif opcion == "0":
            print("\n👋 ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()