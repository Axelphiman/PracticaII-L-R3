import tkinter
from tkinter import *
from tkinter import messagebox
from ArbolBinario import ArbolBinario

class VentanaArbol:
    def __init__(self):

        def informacionNodo():
            charNodo.set(text_nodo.get())
            flag = arbol.buscarNodo(arbol.root, charNodo)
            hijos = arbol.buscarHijos(arbol.root, charNodo)
            papa = arbol.buscarPapa(arbol.root, charNodo)
            hermano = arbol.buscarHermano(arbol.root, charNodo)
            ancestros = arbol.buscarAncestros(arbol.root, charNodo)[:-1]
            abuelo = arbol.buscarAbuelo(arbol.root,charNodo)
            tio = arbol.buscarTio(arbol.root, charNodo)
            posicion = arbol.buscarDerechoIzquierdo(arbol.root, charNodo)
            nodoPosicion = 'No es izquierdo ni derecho'
            if posicion == 1:
                nodoPosicion = 'derecho'
            if posicion == 0:
                nodoPosicion = 'izquierdo'


            if flag:
                messagebox._show(title="Información del Nodo " + charNodo.get(),
                                    message= "La información del Nodo " + charNodo.get()+" es: "+
                                             "\n\nNúmero de hijos: "+str(len(hijos))+" | Hijos: "+','.join(hijos)+
                                             "\nPapá: "+ str(papa)+"\nHermano:  " + str(hermano)+
                                             "\nAncestros: "+','.join(ancestros)+"\nAbuelos: "+','.join(abuelo)+
                                             "\nTio: "+ str(tio) +
                                              "\n Posición nodo: " + nodoPosicion)

            else:
                messagebox.showinfo(title="Manual de Usuario", message="No se encontro el nodo")

        def addTree():
            cadenaArbol.set(text_box.get())
            arbol.buildTree(cadenaArbol)
            iniciarComponentesAB()

        def iniciarComponentesAB():
            # Propiedades sección de Resultados
            result_box = Label(windowBinaryTree, font=("Consolas", 18), bg="#005e35", fg="#ffffff", width="63",
                               height="7")
            result_box.config(text="PreOrder: "+','.join(arbol.PreOrder(arbol.root))+"\nInOrder: "+','.join(arbol.InOrder(arbol.root))+
                                   "\nPostOrder: "+','.join(arbol.PosOrder(arbol.root))+"\nAltura: "+str(arbol.hallarAltura())+
                                   "\nHojas: "+','.join(arbol.encontrarHoja(arbol.root))+"\nGrado: "+str(arbol.grado(arbol.root)))
            result_box.place(x=13, y=145)
            # Propiedades de la caja de texto para nodo
            text_nodo.place(x=14, y=370)

            # Propiedades botón enviar nodo
            button_nodo = Button(windowBinaryTree, text="Enviar", font=("Consolas", 10),
                                 bg="#005e35", fg="#ffffff", width="14", height="2", command = informacionNodo)
            button_nodo.place(x=12, y=400)

        # Propiedades de la ventana
        windowBinaryTree = Tk()
        cadenaArbol = StringVar()
        charNodo = StringVar()
        arbol = ArbolBinario()
        windowBinaryTree.resizable(False, False)
        windowBinaryTree.geometry("850x450")
        windowBinaryTree.title("Ingreso de Árbol Binario")
        windowBinaryTree.config(background="#757574")
        # Propiedades del Label
        label = Label(windowBinaryTree, text="Escribe el árbol binario en forma de hilera y separe los nodos con comas",
                      font=("Consolas", 10), bg="#005e35", fg="#ffffff", width="117", height="2")
        label.place(x=12, y=10)
        # Propiedades de la caja de texto
        text_box = Entry(windowBinaryTree, font=("Consolas", 12), textvariable=cadenaArbol, width="30", justify=tkinter.CENTER)
        text_box.place(x=300, y=60)
        # Propiedades de los botones
        button_send = Button(windowBinaryTree, text="Crear", command= addTree, font=("Consolas", 10),
                             bg="#005e35", fg="#ffffff", width="14", height="2")
        button_send.place(x=380, y=95)
        button_end = Button(windowBinaryTree, text="Cerrar", font=("Consolas", 10),command=windowBinaryTree.destroy,
                            bg="#005e35", fg="#ffffff", width="14", height="2")
        button_end.place(x=730, y=400)
        text_nodo = Entry(windowBinaryTree, font=("Consolas", 12), width="11", justify=tkinter.CENTER,
                          textvariable=charNodo)


        windowBinaryTree.mainloop()