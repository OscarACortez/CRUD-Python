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
        self.consultaCodigo()
        self.modificar()
        self.pc1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def consultaCodigo(self):
        self.pagina2 = ttk.Frame(self.pc1)
        self.pc1.add(self.pagina2, text="Consulta x código")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        self.codigo=tk.StringVar()
        self.entryCodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entryCodigo.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe2, text="Descripción:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        self.descripcion=tk.StringVar()
        self.entryDescripcion=ttk.Entry(self.labelframe2, textvariable=self.descripcion, state="readonly")
        self.entryDescripcion.grid(column=1, row=1, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe2, text="Precio:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)

        self.precio=tk.StringVar()
        self.entryPrecio=ttk.Entry(self.labelframe2, textvariable=self.precio, state="readonly")
        self.entryPrecio.grid(column=1, row=2, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.descripcion.set('')
            self.precio.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def modificar(self):
        self.pagina5 = ttk.Frame(self.pc1)
        self.pc1.add(self.pagina5, text="Modificar artículo")
        self.labelframe5=ttk.LabelFrame(self.pagina5, text="Artículo")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe5, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        self.codigoModificar=tk.StringVar()
        self.entryCodigo=ttk.Entry(self.labelframe5, textvariable=self.codigoModificar)
        self.entryCodigo.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe5, text="Descripción:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        self.descripcionModificar=tk.StringVar()
        self.entryDescripcion=ttk.Entry(self.labelframe5, textvariable=self.descripcionModificar)
        self.entryDescripcion.grid(column=1, row=1, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe5, text="Precio:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)

        self.precioModificar=tk.StringVar()
        self.entryPrecio=ttk.Entry(self.labelframe5, textvariable=self.precioModificar)
        self.entryPrecio.grid(column=1, row=2, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe5, text="Consultar", command=self.consultaModificar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

        self.boton2=ttk.Button(self.labelframe5, text="Modificar", command=self.modificaArt)
        self.boton2.grid(column=1, row=4, padx=4, pady=4)

    def modificaArt(self):
        datos=(self.descripcionModificar.get(), self.precioModificar.get(), self.codigoModificar.get())
        cantidad=self.articulo1.modifica(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se modificó el artículo")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def consultaModificar(self):
        datos=(self.codigoModificar.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.descripcionModificar.set(respuesta[0][0])
            self.precioModificar.set(respuesta[0][1])
        else:
            self.descripcionModificar.set('')
            self.precioModificar.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")
    
app1=FormArticulos()