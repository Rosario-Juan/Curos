import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

lista = ['hola', 'palabara', 'clase', 'linux', 'Os/2']
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=10, listvariable=lista_items)
listbox.grid(column=0, row=0, sticky=tkinter.W)

label = ttk.Label(window)
label =ttk.Label(window,  text='Esta es mi lista')
label.grid(column=0, row=0, sticky=tkinter.W, padx=100,pady=100)

window.mainloop()