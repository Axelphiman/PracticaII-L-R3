from tkinter import *
import tkinter as tk
from tkinter import messagebox
from VentanaNuevoArbol import VentanaArbol
from VentanaArbolAle import VentanaArbolAle
from VentanaArbolRecorridos import VentanaRecorridos

#Función para generar los manuales
def openInfoUser():
    messagebox.showinfo(title="Manual de Usuario", message="Aquí el manual de usuario o tecnico")

#Propiedades de la ventana Principal
window = Tk()
window.resizable(False,False)
window.geometry("520x340")
window.title("Práctica #2 - LyR III")
window.config(background = "#757574")
back_Title = tk.Label(text="Segunda práctica de Lógica y Representanción III\n\n Hecho por: Diego Muñoz y Esteban Cossio",
                      font=("Consolas",14), bg="#005e35", fg="#ffffff", width="52",height="8")
back_Title.place(x = 0, y = 80)
button_end = Button(window, text="Cerrar", font=("Consolas", 10),command=window.destroy,
                            bg="#005e35", fg="#ffffff", width="14", height="2")
button_end.place(x=400, y=290)

#Creando la barra de Menú
barMenu = Menu(window)
mnuTree = Menu(barMenu)
mnuInformation = Menu(barMenu)
#Añadiendo los botones para Árboles Binarios en la barra de Menú
mnuTree.add_command(label="Nuevo Árbol", command=VentanaArbol)
mnuTree.add_command(label="Árbol aleatorio", command=VentanaArbolAle)
mnuTree.add_command(label="Árbol a partir de recorridos", command=VentanaRecorridos)
#Añadiendo los botones para Información del Programa
mnuInformation.add_command(label="Manual de Usuario", command=openInfoUser)
mnuInformation.add_command(label="Manual técnico")
#La barra de menú es tipo cascada
barMenu.add_cascade(label="Árboles",menu=mnuTree)
barMenu.add_cascade(label="Información",menu=mnuInformation)
window.config(menu=barMenu)

window.mainloop()