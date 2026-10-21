import time
from serie import Serie
from arbol import ArbolBinarioBusqueda
from arbol_avl import ArbolAVL

def calcular_altura_bst(nodo):
    if not nodo:
        return 0
    return 1 + max(calcular_altura_bst(nodo.izq), calcular_altura_bst(nodo.der))

def experimento_desbalance():
    print("========================================")
    print(" 🧪 EXPERIMENTO TP4: BST vs. AVL ")
    print("========================================")

    # Caso de prueba: Datos insertados en ORDEN ALFABÉTICO (peor caso para BST)
    titulos_ordenados = [f"Serie_{i:04d}" for i in range(1, 1001)] # 1000 series ordenadas
    
    bst = ArbolBinarioBusqueda()
    avl = ArbolAVL()

    # Carga de datos
    for t in titulos_ordenados:
        s = Serie(t, "Drama", 8.0, 2020)
        bst.insertar(s)
        avl.insertar(s)

    altura_bst = calcular_altura_bst(bst.raiz)
    altura_avl = avl.obtener_altura_total()

    print(f"📊 Total de elementos insertados: {len(titulos_ordenados)}")
    print(f"🌲 Altura del árbol BST común: {altura_bst} (degenerado a O(n))")
    print(f"⚖️ Altura del árbol AVL:        {altura_avl} (garantizado en O(log n))")

    # Medición de búsqueda en el peor caso (último elemento)
    elemento_buscar = "Serie_1000"

    inicio = time.perf_counter()
    res_bst = bst.buscar(elemento_buscar)
    tiempo_bst = (time.perf_counter() - inicio) * 1000

    inicio = time.perf_counter()
    res_avl = avl.buscar(elemento_buscar)
    tiempo_avl = (time.perf_counter() - inicio) * 1000

    print("\n⏱️ RESULTADOS DE BÚSQUEDA:")
    print(f"  - Tiempo BST: {tiempo_bst:.4f} ms")
    print(f"  - Tiempo AVL: {tiempo_avl:.4f} ms")

if __name__ == "__main__":
    experimento_desbalance()