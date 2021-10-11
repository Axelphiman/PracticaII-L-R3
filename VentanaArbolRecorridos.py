import tkinter
from tkinter import *
from ArbolBinario import  ArbolBinario
class VentanaRecorridos:
    def __init__(self):

        def buildTree():
            cadenaInOrder.set(text_Inorden.get())
            cadenaPosOrder.set(text_Postorden.get())
            cadenaPreOrder.set(text_Preorden.get())
            InOrder = cadenaInOrder.get().split(',')
            flag = False
            if cadenaPreOrder.get() != '' and cadenaInOrder.get() != '':
                PreOrder = cadenaPreOrder.get().split(',')
                arbol.ConstruirArbolPre(InOrder, PreOrder, len(InOrder))
                flag = True
            elif cadenaInOrder.get() != '' and cadenaPosOrder != '':
                PosOrder = cadenaPosOrder.get().split(',')
                arbol.ConstruirArbolPos(InOrder, PosOrder, len(InOrder))

            iniciarComponentesAR(flag)

        def iniciarComponentesAR(flag):
            text_nodo = Entry(windowRecTree, font=("Consolas", 12), width="8", justify=tkinter.CENTER)
            if flag:
                result_box.config(text="PreOrder: "+','.join(arbol.PreOrder(arbol.root))+"\nInOrder: "+','.join(arbol.InOrder(arbol.root))+
                                   "\nPostOrder: "+','.join(arbol.PosOrder(arbol.root))+"\nAltura: "+str(arbol.hallarAltura())+
                                   "\nHojas: "+','.join(arbol.encontrarHoja(arbol.root))+"\nGrado: "+str(arbol.grado(arbol.root)))
            else:
                result_box.config(text="PreOrder: "+','.join(arbol.PreOrder(arbol.root))+"\nInOrder: "+','.join(arbol.InOrder(arbol.root))+
                                   "\nPostOrder: "+','.join(arbol.PosOrder(arbol.root))+"\nAltura: "+str(arbol.hallarAltura())+
                                   "\nHojas: "+','.join(arbol.encontrarHoja(arbol.root))+"\nGrado: "+str(arbol.grado(arbol.root)))
            text_nodo.place(x=12, y=615)
            button_nodo = Button(windowRecTree, text="Enviar", font=("Consolas", 10),
                                 bg="#005e35", fg="#ffffff", width="14", height="2")
            button_nodo.place(x=90, y=600)

        def buildInPre():
            if (text_Postorden != "" or text_Preorden != "" or text_Inorden != ""):
                text_Postorden.delete("0","end")
                text_Inorden.delete("0","end")
                text_Preorden.delete("0", "end")
            text_Postorden.config(state=tkinter.DISABLED)
            text_Inorden.config(state=tkinter.NORMAL)
            text_Preorden.config(state=tkinter.NORMAL)
            button_Send.config(state=tkinter.NORMAL,command=buildTree)

        def buildInPos():
            if(text_Postorden != "" or text_Preorden != "" or text_Inorden != ""):
                text_Postorden.delete("0", "end")
                text_Inorden.delete("0", "end")
                text_Preorden.delete("0", "end")
            text_Postorden.config(state=tkinter.NORMAL)
            text_Inorden.config(state=tkinter.NORMAL)
            text_Preorden.config(state=tkinter.DISABLED)
            button_Send.config(state=tkinter.NORMAL,command=buildTree)

        # Propiedades de la ventana
        windowRecTree = Tk()
        arbol = ArbolBinario()
        cadenaInOrder = StringVar()
        cadenaPreOrder  = StringVar()
        cadenaPosOrder = StringVar()
        windowRecTree.resizable(False, False)
        windowRecTree.geometry("850x650")
        windowRecTree.title("Ingreso de Árbol por recorridos")
        windowRecTree.config(background="#757574")

        # Propiedades del Label
        label_title = Label(windowRecTree, text="Utilice los botones para seleccionar los recorridos que quiere ingresar",
                      font=("Consolas", 9), bg="#005e35", fg="#ffffff", width="117", height="3")
        label_title.place(x=12, y=10)
        label_Inorden = Label(windowRecTree, text="Recorrido Inorden",font=("Consolas", 8),
                              bg="#005e35", fg="#ffffff", width="20", height="1")
        label_Inorden.place(x=380, y=110)
        label_Preorden = Label(windowRecTree, text="Recorrido Preorden", font=("Consolas", 8),
                              bg="#005e35", fg="#ffffff", width="20", height="1")
        label_Preorden.place(x=380, y=170)
        label_Postorden = Label(windowRecTree, text="Recorrido Postorden", font=("Consolas", 8),
                              bg="#005e35", fg="#ffffff", width="20", height="1")
        label_Postorden.place(x=380, y=230)
        result_box = Label(windowRecTree, font=("Consolas", 18),bg="#005e35", fg="#ffffff", width="63", height="7")
        result_box.place(x=12, y=350)

        # Propiedades de la caja de texto
        text_Inorden = Entry(windowRecTree, font=("Consolas", 12) ,textvariable = cadenaInOrder, width="20",state=tkinter.DISABLED,justify=tkinter.CENTER)
        text_Inorden.place(x=350, y=140)
        text_Preorden = Entry(windowRecTree, font=("Consolas", 12), textvariable = cadenaPreOrder, width="20",state=tkinter.DISABLED, justify=tkinter.CENTER)
        text_Preorden.place(x=350, y=200)
        text_Postorden = Entry(windowRecTree, font=("Consolas", 12), textvariable = cadenaPosOrder, width="20",state=tkinter.DISABLED, justify=tkinter.CENTER)
        text_Postorden.place(x=350, y=260)

        # Propiedades de los botones
        button_InPre = Button(windowRecTree, text="In/Pre", command=buildInPre, font=("Consolas", 10),
                             bg="#005e35", fg="#ffffff", width="14", height="2")
        button_InPre.place(x=290, y=60)
        button_InPost = Button(windowRecTree, text="In/Post", command=buildInPos, font=("Consolas", 10),
                             bg="#005e35", fg="#ffffff", width="14", height="2")
        button_InPost.place(x=485, y=60)
        button_Send = Button(windowRecTree, text="Crear",command = buildTree ,font=("Consolas", 10),bg="#005e35", fg="#ffffff",
                             width="14", height="2",state=tkinter.DISABLED)
        button_Send.place(x=390, y=300)
        button_end = Button(windowRecTree, text="Cerrar", font=("Consolas", 10), command=windowRecTree.destroy,
                            bg="#005e35", fg="#ffffff", width="14", height="2")
        button_end.place(x=730, y=600)

        #text = J,K,B,I,H,G,A,C,E,D,F                    D,B,E,A,F,C
        #Postext = J,K,I,G,H,B,E,F,D,C,A                 A,B,D,E,C,F
        windowRecTree.mainloop()