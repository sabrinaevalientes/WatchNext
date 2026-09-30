import time
import random
from serie import Serie, Genero
from arbol import ArbolBusqueda

def generar_datos_prueba(n):
    genero_demo = Genero("Drama")
    catalogo_lista = []
    
    for i in range(n):
        s = Serie(i, f"Serie_{i}", genero_demo, rating=8.0)
        catalogo_lista.append(s)
    
    lista_para_arbol = list(catalogo_lista)
    random.shuffle(lista_para_arbol)
    
    arbol = ArbolBusqueda()
    for s in lista_para_arbol:
        arbol.insertar(s)
        
    return catalogo_lista, arbol

def busqueda_secuencial(catalogo_lista, titulo_buscado):
    titulo_buscado = titulo_buscado.lower()
    for serie in catalogo_lista:
        if serie.titulo.lower() == titulo_buscado:
            return serie
    return None

def ejecutar_experimentos():
    tamanos = [1000, 10000, 100000]
    
    print(f"\n{'N ELEMENTOS':<15} | {'BÚSQUEDA SECUENCIAL':<20} | {'BÚSQUEDA EN ÁRBOL':<20}")
    print("-" * 62)
    
    for n in tamanos:
        catalogo_lista, arbol = generar_datos_prueba(n)
        target_titulo = f"Serie_{n - 1}"
        
        # Medición Secuencial
        inicio = time.perf_counter()
        busqueda_secuencial(catalogo_lista, target_titulo)
        fin = time.perf_counter()
        tiempo_secuencial_ms = (fin - inicio) * 1000

        # Medición en Árbol Binario
        inicio = time.perf_counter()
        arbol.buscar_por_titulo(target_titulo)
        fin = time.perf_counter()
        tiempo_arbol_ms = (fin - inicio) * 1000

        print(f"{n:<15} | {tiempo_secuencial_ms:.4f} ms{'':<11} | {tiempo_arbol_ms:.4f} ms")

if __name__ == "__main__":
    ejecutar_experimentos()