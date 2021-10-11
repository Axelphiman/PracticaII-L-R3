
from Nodo import Nodo
import random
from tkinter import *
class ArbolBinario:
    #Funciones privadas
    def __init__(self, dato = None):
        self.root = Nodo(dato)

    #Contruye el árbol
    def buildTree(self, cadenaTexto):
        #Variables
        aleatorio = random

        vectorCaracteres = cadenaTexto.get().split(',')
        vectorNodos = []

        #Creación vector de nodos
        for char in vectorCaracteres:
            vectorNodos.append(Nodo(char))

        arbol = [None]*(2**(len(vectorNodos))-1)
        espaciosDisponibles = [0]

#Creación de los espacios disponibles para la ubicación de los nodos
        for nodo in vectorNodos:
            numero = aleatorio.randint(0, len(espaciosDisponibles) - 1)
            arbol[espaciosDisponibles[numero]] = nodo
            espaciosDisponibles.append(espaciosDisponibles[numero]*2 + 1)
            espaciosDisponibles.append(espaciosDisponibles[numero] * 2 + 2)
            del espaciosDisponibles[numero]

#Posicionando los Nodos en el árbol con base en los espacios que salieron anteriormente
        for i in range(len(arbol)):
            if arbol[i] is not None and (i*2+2) < len(arbol):
                arbol[i].left = arbol[i*2 + 1]
                arbol[i].right = arbol[i*2 + 2]
        self.root = arbol[0]

    # Imprime el recorrido PreOrder del árbol
    def PreOrder(self, root):
        result = []
        if root is not None:
            result.append(str(root))
            result += self.PreOrder(root.left)
            result += self.PreOrder(root.right)
        return result

    # Imprime el recorrido InOrder del árbol
    def InOrder(self,root):
        result = []
        if root is not None:
            result += self.PreOrder(root.left)
            result.append(str(root))
            result += self.PreOrder(root.right)
        return result

    #Imprime el recorrido PosOrder del árbol
    def PosOrder(self, root):
        result = []
        if root is not None:
            result += self.PosOrder(root.left)
            result += self.PosOrder(root.right)
            result.append(str(root))
        return result

    def buildUtil(self,In, post, inStrt, inEnd, pIndex):
    # Caso base
        if (inStrt > inEnd):
            return None

        node = Nodo(post[pIndex[0]])
        pIndex[0] -= 1

        if (inStrt == inEnd):
            return node
        iIndex = self.search(In, inStrt, inEnd, node.dato)

        node.right = self.buildUtil(In, post, iIndex + 1,
                            inEnd, pIndex)
        node.left = self.buildUtil(In, post, inStrt,
                          iIndex - 1, pIndex)
        return node

    # construye arbol binario dados los arreglos inorden y postorden
    def ConstruirArbolPos(self,In, post, n):
        pIndex = [n - 1]
        self.root = self.buildUtil(In, post, 0, n - 1, pIndex)

    # busqueda de la raiz en la serie inorder
    def search(self,arr, strt, end, value):
        i = 0
        for i in range(strt, end + 1):
            if (arr[i] == value):
                break
        return i

    def auxiliarPre(self, In, pre, inStrt, inEnd, pIndex):
            # Caso base
            if (inStrt > inEnd):
                return None

            node = Nodo(pre[pIndex[0]])
            pIndex[0] += 1

            if (inStrt == inEnd):
                return node
            iIndex = self.search(In, inStrt, inEnd, node.dato)

            node.left = self.buildUtil(In, pre, inStrt,
                                       iIndex - 1, pIndex)
            node.right = self.buildUtil(In, pre, iIndex + 1,
                                        inEnd, pIndex)

            return node

    # construye arbol binario dados los arreglos inorden y postorden
    def ConstruirArbolPre(self, In, pre, n):
            pIndex = [0]
            self.root = self.buildUtil(In, pre, 0, n - 1, pIndex)

    #Encuentra la altura del árbol binario
    def hallarAltura(self):
        if self.root is None:
            return 0
        else:
            nodoEncolado = list()
            nodoEncolado.append(self.root)
            altura = 0
            while len(nodoEncolado):
                nodosAnteriores = len(nodoEncolado)
                while nodosAnteriores:
                    q = nodoEncolado.pop(0)
                    nodosAnteriores = nodosAnteriores - 1
                    if q.left is not None:
                        nodoEncolado.append(q.left)
                    if q.right is not None:
                        nodoEncolado.append(q.right)
                altura = altura + 1
            return altura

    #Encuentra las hojas del árbol binario, hay un problema con el retorno de la hoja
    def encontrarHoja(self,root):
        # Si la raíz es nula, retorna
        if (root is None):
            return "El árbol está vacío"
        Hojas = []
        # Si el nodo es una hoja escribe el dato del nodo #E,F,L,M,B
        if (root.left is None and root.right is None):
            Hojas.append(str(root))

        # Si tiene hijo izquierdo revisa los otros nodos recursivamente
        if root.left:
            Hojas += self.encontrarHoja(root.left)

        # Si el hijo derecho existe revisa otros nodos recursivamente
        if root.right:
            Hojas += self.encontrarHoja(root.right)
        return Hojas

    #Determinar grado del árbol binario
    def grado(self, root):
        #El mayor grado que puede tener un árbol binario es 2.
        g = 0
        if root is None:
            return 0
        if root.left is not None and root.right is not None:
            return 2
        if root.left is not None or root.right is not None:
            g = 1
        g = max(g, self.grado(root.left))
        if g == 2:
            return 2
        g = max(g, self.grado(root.right))
        return g

    #Verifica si el nodo existe o no
    def buscarNodo(self, root, dato):

        if root is None:
            return False
        if root.dato == dato.get():
            return True
        result1 = self.buscarNodo(root.left, dato)
        if result1:
            return True
        result2 = self.buscarNodo(root.right, dato)
        return result2

    #Busca el número y los hijos del dato enviado
    def buscarHijos(self,root, dato):
        hijos = []
        if root is None:
            return []
        if root.dato == dato.get():
            if root.left:
                hijos.append(str(root.left))
            if root.right:
                hijos.append(str(root.right))
            return hijos

        hijos += self.buscarHijos(root.left, dato)
        if hijos:
            return hijos
        hijos += self.buscarHijos(root.right, dato)
        return hijos

    #Busca el padre del dato enviado
    def buscarPapa(self,root, dato):
        papa = []
        if root is None:
            return []
        if root.left:
            if root.left.dato == dato.get():
                papa.append(root.dato)
                return papa
        if root.right:
            if root.right.dato == dato.get():
                papa.append(root.dato)
                return papa
        papa += self.buscarPapa(root.left, dato)
        if papa:
            return papa
        papa += self.buscarPapa(root.right, dato)
        return papa

    # Busca el Hermano del dato enviado
    def buscarHermano(self, root, dato):
        hermano = []
        if root is None:
            return []
        if root.left is not None and root.right is not None:
            if root.left.dato == dato.get():
                hermano.append(root.right.dato)
                return hermano
            if root.right.dato == dato.get():
                hermano.append(root.left.dato)
                return hermano
        hermano += self.buscarHermano(root.left, dato)
        if hermano:
            return hermano
        hermano += self.buscarHermano(root.right, dato)
        return hermano

    #Busca los ancestros del dato enviado
    def buscarAncestros(self, root, dato):
        ancestros = []
        if root is None:
            return []
        ancestros.append(root.dato)

        if root.dato == dato.get():
            return ancestros

        ancestros += self.buscarAncestros(root.left, dato)
        if ancestros[-1] == dato.get():
            return ancestros
        ancestros += self.buscarAncestros(root.right, dato)
        if ancestros[-1] == dato.get():
            return ancestros
        ancestros.pop()
        return ancestros

    def buscarTio(self,root, dato):
        papa = StringVar()
        try:
            papa.set(self.buscarPapa(root, dato)[0])
        except IndexError:
            papa.set('')
        return self.buscarHermano(root, papa)

    def buscarAbuelo(self, root, dato):
        papa = StringVar()
        try:
            papa.set(self.buscarPapa(root, dato)[0])
        except IndexError:
            papa.set('')
        return self.buscarPapa(root, papa)

    def buscarDerechoIzquierdo(self, root, dato):
        flag = -1
        if root is None:
            return -1
        if root.left:
            if root.left.dato == dato.get():
                return 0
        if root.right:
            if root.right.dato == dato.get():
                return 1

        flag = self.buscarDerechoIzquierdo(root.left, dato)
        if flag != -1:
            return flag
        flag = self.buscarDerechoIzquierdo(root.right, dato)

        return flag