from ArbolBinario.arbol import Arbol

arbol = Arbol("Martin")
arbol.agregar("Fernando")
arbol.agregar("Shimizu")
arbol.agregar("Messi")
arbol.agregar("Cristiano")
arbol.agregar("Montserrat")
arbol.agregar("Gilberto")
arbol.agregar("Jesus Vega")
arbol.agregar("Edward")
arbol.agregar("Cesar")

nombre = input("Ingresa algo para agregar al árbol: ")
arbol.agregar(nombre)
print("Recorrido Preorden:")
arbol.preorden()
print("Recorrido Inorden:")
arbol.inorden()
print("Recorrido Postorden:")
arbol.postorden()

busqueda = input("Busca algo en el árbol: ")
nodo = arbol.buscar(busqueda)
if nodo is None:
    print("No se encontró el elemento", busqueda)
else:
    print("Sí existe", busqueda)

arbol_numeros = Arbol(5)
arbol_numeros.agregar(1900)
arbol_numeros.agregar(60)
arbol_numeros.agregar(10)
arbol_numeros.agregar(20)
arbol_numeros.agregar(30)
arbol_numeros.agregar(40)
arbol_numeros.agregar(50)
arbol_numeros.agregar(60)
arbol_numeros.agregar(70)
arbol_numeros.agregar(80)
arbol_numeros.agregar(90)
arbol_numeros.agregar(23)
arbol_numeros.agregar(18)
print("Recorrido Preorden:")
arbol_numeros.preorden()
print("Recorrido Inorden:")
arbol_numeros.inorden()
print("Recorrido Postorden:")
arbol_numeros.postorden()

try:
    busqueda = int(input("Ingresa un número para buscar en el árbol: "))
    n = arbol_numeros.buscar(busqueda)
    if n is None:
        print(busqueda, "No existe")
    else:
        print(busqueda, "Sí existe")
except ValueError:
    print("Entrada inválida. Debe ser un número entero.")
