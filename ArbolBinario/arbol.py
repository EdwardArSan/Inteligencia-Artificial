from ArbolBinario.nodo import Nodo

class Arbol:
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def _agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self._agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self._agregar_recursivo(nodo.derecha, dato)

    def _inorden_recursivo(self, nodo):
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end=", ")
            self._inorden_recursivo(nodo.derecha)

    def _preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self._preorden_recursivo(nodo.izquierda)
            self._preorden_recursivo(nodo.derecha)

    def _postorden_recursivo(self, nodo):
        if nodo is not None:
            self._postorden_recursivo(nodo.izquierda)
            self._postorden_recursivo(nodo.derecha)
            print(nodo.dato, end=", ")

    def _buscar(self, nodo, busqueda):
        if nodo is not None:
            if nodo.dato == busqueda:
                return nodo
            if busqueda < nodo.dato:
                return self._buscar(nodo.izquierda, busqueda)
            else:
                return self._buscar(nodo.derecha, busqueda)
        return None

    def agregar(self, dato):
        self._agregar_recursivo(self.raiz, dato)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self._inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self._preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self._postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self._buscar(self.raiz, busqueda)
        
    def vacio(self):
        return self.raiz is None