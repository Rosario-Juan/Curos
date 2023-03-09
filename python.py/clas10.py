import tkinter
from tkinter import ttk

window = tkinter.Tk()


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

seleccionado = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text='casa', value='1', variable=seleccionado)
r2 = ttk.Radiobutton(window, text='auto', value='2', variable=seleccionado)
r3 = ttk.Radiobutton(window, text='telefono', value='3', variable=seleccionado)
r4 = ttk.Radiobutton(window, text='caballo', value='4', variable=seleccionado)
r5 = ttk.Radiobutton(window, text='avion', value='5', variable=seleccionado)

r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)
r3.grid(column=0, row=3, pady=5, padx=5)
r4.grid(column=0, row=4, pady=5, padx=5)
r5.grid(column=0, row=5, pady=5, padx=5)

#todo lo que este dentro de la clase seleccionado, este boton hara la funcion de borrar la seleccion
def  reiniciar():
    seleccionado.set(None)

Button = tkinter.Button(window, text="Reiniciar", command=reiniciar)
Button.grid(column=0, row=6, sticky=tkinter.E, padx=5, pady=5)

window.mainloop()

