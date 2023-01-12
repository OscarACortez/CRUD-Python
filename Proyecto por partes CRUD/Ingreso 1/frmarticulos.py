import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos

class FormArticulos:
    def __init__(self):
        self.articulo1=articulos.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.title("Administracion de artículos")
        self.pc1 = ttk.Notebook(self.ventana1)        
        self.ingresoArticulos()
        self.pc1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def ingresoArticulos(self):
        self.pagina1 = ttk.Frame(self.pc1)
        self.pc1.add(self.pagina1, text="Ingreso de artículos")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Artículo")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe1, text="Descripción:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        self.descripcionIngreso=tk.StringVar()
        self.entryDescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcionIngreso)
        self.entryDescripcion.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe1, text="Precio:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        self.precioIngreso=tk.StringVar()
        self.entryPrecio=ttk.Entry(self.labelframe1, textvariable=self.precioIngreso)
        self.entryPrecio.grid(column=1, row=1, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def agregar(self):
        datos=(self.descripcionIngreso.get(), self.precioIngreso.get())
        self.articulo1.ingreso(datos)
        mb.showinfo("Información", "Los datos fueron ingresados")
        self.descripcionIngreso.set("")
        self.precioIngreso.set("")

app1=FormArticulos()