import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

from PIL import ImageTk
from PIL import Image

class AppEuler(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("EDO  Método Euler")
        self.geometry("1150x800")

        # Menú horizontal
        self.menuFrame = tk.Frame(self, bg="#1F3A93", height=50) 
        self.menuFrame.pack(side="top", fill="x")

        self.contenidoFrame = tk.Frame(self, bg="white")
        self.contenidoFrame.pack(fill="both", expand=True)

        for menu in ["Presentación", "Euler", "Ayuda", "Acerca de"]:
            btn = tk.Button(self.menuFrame, text=menu, bg="#3A539B", fg="white",
                            font=("Arial", 11, "bold"), bd=0, padx=15, pady=10,
                            command=lambda n=menu: self.mostrarSeccion(n))
            btn.pack(side="left", padx=5, pady=5)

        self.mostrarSeccion("Presentación")

    def borrarContenido(self):
        for widget in self.contenidoFrame.winfo_children():
            widget.destroy()

    def mostrarSeccion(self, menu):
        self.borrarContenido()
        if menu == "Presentación":
            tk.Label(self.contenidoFrame, text="", font=("Arial", 12, "bold"), fg="#00008B", bg="white").pack() 
            tk.Label(self.contenidoFrame, text="", font=("Arial", 12, "bold"), fg="#00008B", bg="white").pack() 
            tk.Label(self.contenidoFrame, text="BIENVENIDOS A LA APLICACIÓN",
                     font=("Comic Sans MS", 18, "bold"),  fg="#00008B", bg="white").pack()
            tk.Label(self.contenidoFrame, text="Solución numérica de una Ecuación Diferencial Ordinaria\n"
                     " Método Euler",
                     font=("Arial", 14, "bold"), fg="#00008B", bg="white").pack()
            tk.Label(self.contenidoFrame, text="", font=("Arial", 12, "bold"), fg="#00008B", bg="white").pack()
            tk.Label(self.contenidoFrame, text="", font=("Arial", 12, "bold"), fg="#00008B", bg="white").pack()

            try:
                image = Image.open("softEDOEuler.png")  
                image = image.resize((500,350))
                image_tk = ImageTk.PhotoImage(image)
                imageLabel = tk.Label(self.contenidoFrame, image=image_tk, bg="white")
                imageLabel.image = image_tk
                imageLabel.pack(pady=20)
            except Exception as e:
                print(f"Error al cargar la imagen: {e}")

            tk.Label(self.contenidoFrame, text="", font=("Arial", 12, "bold"), fg="#00008B", bg="white").pack()
            tk.Label(self.contenidoFrame, text="", font=("Arial", 12, "bold"), fg="#00008B", bg="white").pack()
            tk.Label(self.contenidoFrame, text="SoftEDOEuler v1.0", font=("Comic Sans MS", 20, "bold"),
                     fg="#00008B", bg="white").pack()


        elif menu == "Euler":
            self.mostrarEuler()

        elif menu == "Ayuda":
  
            tk.Label(self.contenidoFrame, text="\n\nINSTRUCCIONES DE USO", bg="white",
                     font=("Lucida Handwriting", 14,"bold"), fg="#00008B").pack(pady=20)
            tk.Label(self.contenidoFrame, text="Solución Numérica de Ecuaciones Diferenciales Ordinarias"
                     "\n SoftEDOEuler v1.0:\n\n", bg="white",
                     font=("Comic Sans MS", 14,"bold"), fg="#00008B").pack(pady=20)
            tk.Label(self.contenidoFrame, text="\n1. Hacer un click en el menu Euler"
                     f"\n2. Hacer un click en la ventana de f(x,y) luego ingrese la ecuación diferencial\n"
                     f"Ejemplo: x + y, y - x**2, np.cos(x).\n"
                     f"3.Hacer un clic en la ventana de x0 luego ingrese el valor inicial para x0        \n "
                     f"4.Hacer un clic en la ventana de y0 luego ingrese el valor inicial para y0        \n "
                     f"5.Hacer un clic en la ventana de h luego ingrese el valor del incremento en x\n "
                     f"6. Hacer un clic en la ventana de n luego ingrese el valor del indice del paso actual\n",
                     bg="white",
                     font=("Arial", 14)).pack(pady=20)

        elif menu == "Acerca de":
            tk.Label(self.contenidoFrame, text="\n\n\n\nSolución Numérica de Ecuaciones Diferenciales Ordinarias"
                     "\nSoftEDOEuler v1.0",
                     bg="white", font=("Comic Sans MS", 14, "bold"),
                     fg="#00008B").pack(pady=(0, 10))
            # Lista de autores
            autores = [
                            "\nDesarrollado por: Leonel Coyla Idme",
                            "Elqui Yeye Pari Condori",
                            "Juan Reynaldo Paredes Quispe",
                            "José Pánfilo Tito Lipa",      
            ]

            # Etiqueta por autor
            for autor in autores:
                tk.Label(self.contenidoFrame, text=autor, bg="white",
                         font=("Comic Sans MS", 14)).pack(pady=2)

            labelAcercade = tk.Label(self.contenidoFrame, text= "\n\nLanzamiento : agosto  2025",
                                      font=("Comic Sans MS", 14),fg="#003366",bg="white")
            labelAcercade.pack(pady=(1,10))
            labelAcercade = tk.Label(self.contenidoFrame, text= "Contacto: lcoyla@unap.edu.pe",
                                      font=("Comic Sans MSl", 14),fg="#003366",bg="white")
            labelAcercade.pack(pady=(1,10))

    def mostrarEuler(self):
        tk.Label(self.contenidoFrame, text="Solución Numérica de EDO\n  Método Euler y muestra el grafico",
                 font=("Arial", 16, "bold"), bg="white",fg="#00008B").pack(pady=10)

        form = tk.Frame(self.contenidoFrame, bg="white")
        form.pack(pady=10)

        # Ingreso de datos
        tk.Label(form, text="f(x,y) =", font=("Arial", 12, "italic"),bg="white").grid(row=0, column=0, sticky="e")
        ecuacion_entry = tk.Entry(form, width=20, font=("Arial", 12))
        ecuacion_entry.grid(row=0, column=1, padx=5, pady=5)
        ecuacion_entry.insert(0, "x + y")

        tk.Label(form, text="x0 =", font=("Arial", 12, "italic"), bg="white").grid(row=1, column=0, sticky="e")
        x0_entry = tk.Entry(form, width=10)
        x0_entry.grid(row=1, column=1, padx=5,pady=5)
        x0_entry.insert(0, "0")

        tk.Label(form, text="y0 =", font=("Arial", 12, "italic"), bg="white").grid(row=2, column=0, sticky="e")
        y0_entry = tk.Entry(form, width=10)
        y0_entry.grid(row=2, column=1, padx=5,pady=5)
        y0_entry.insert(0, "1")

        tk.Label(form, text="h =", font=("Arial", 12, "italic"), bg="white").grid(row=3, column=0, sticky="e")
        h_entry = tk.Entry(form, width=10)
        h_entry.grid(row=3, column=1, padx=5,pady=5)
        h_entry.insert(0, "0.1")

        tk.Label(form, text="n =", font=("Arial", 12, "italic"), bg="white").grid(row=4, column=0, sticky="e")
        n_entry = tk.Entry(form, width=10)
        n_entry.grid(row=4, column=1, padx=5,pady=5)
        n_entry.insert(0, "20")

        resultadoFrame = tk.Frame(self.contenidoFrame, bg="white")
        resultadoFrame.pack(fill="both", expand=True, pady=10)

        def calcular():
            try:
                funcionCadena = ecuacion_entry.get()
                x0 = float(x0_entry.get())
                y0 = float(y0_entry.get())
                h = float(h_entry.get())
                n = int(n_entry.get())


                def funcion(x, y):
                    variablesOperacion = {
                        "x": x,
                        "y": y,
                        "np": np,
                        "math": math
                    }
                    return eval(funcionCadena, variablesOperacion)

                # Método de Euler
                xsgte = [x0]
                ysgte = [y0]
                for _ in range(n):
                    ynuevo = ysgte[-1] + h * funcion(xsgte[-1], ysgte[-1])
                    xnuevo = xsgte[-1] + h
                    xsgte.append(xnuevo)
                    ysgte.append(ynuevo)

                for w in resultadoFrame.winfo_children():
                    w.destroy()

                # Mostrar tabla
                columnas = ("i", "x", "y")
                tree = ttk.Treeview(resultadoFrame, columns=columnas, show="headings", height=15) 

                # Configura el encabezado
                for col in columnas:
                    tree.heading(col, text=col)

                # Ajuste de ancho de columna   (persona)
                tree.column("i", width=70, anchor="center") 
                tree.column("x", width=140, anchor="w")
                tree.column("y", width=210, anchor="w")

    
                style = ttk.Style()
                style.theme_use("clam")  # boton estilizado

                # Encabezado de la tabla
                style.configure(
                    "Treeview.Heading",
                    font=("Arial", 11, "bold"),
                    background="#3A539B",   # azul oscuro medio
                    foreground="white", #Color de texto
                    relief="flat"
                )

                # Filas de la tabla
                style.configure(
                    "Treeview",
                    background="#F5F5F5", 
                    foreground="black",
                    rowheight=25,
                    fieldbackground="#F5F5F5"
                )

                # Efecto hover puntero en barra o en filas
                style.map(
                    "Treeview",
                    background=[("selected", "#81C784")]
                )

                # Definir colores como variables
                colorFilaImpar = "#f2f2f2" #Color gris claro
                colorFilaPar = "white"
                colorSeleccion = "#FFB347" #Color naranja de la barra

                # Aplicar estilos
                style.map("Treeview", background=[("selected", colorSeleccion)])
                tree.tag_configure("oddrow", background=colorFilaImpar)
                tree.tag_configure("evenrow", background=colorFilaPar)

                # Encabezados
                for col in columnas:
                    tree.heading(col, text=col)
   
                for i in range(len(xsgte)):
                    xx = xsgte[i]
                    yy = ysgte[i]

                    if i % 2 == 0:
                        tag = "oddrow" # Fila impar
                    else:
                        tag = "evenrow"

                    valores = (i, f"{xx:.4f}", f"{yy:.10f}")
                    tree.insert("", "end", values=valores, tags=(tag,))

                tree.pack(side="left", padx=10, pady=5)


                # Gráfica con matplotlib
                figura = Figure(figsize=(5, 4), dpi=100)
                eje = figura.add_subplot(111)
                eje.plot(xsgte, ysgte, marker='o', color="red", label="Euler")
                eje.set_title("EDO método Euler - Solución aproximada")
                eje.set_xlabel("x")
                eje.set_ylabel("y")
                eje.grid(
                    True,  
                    which='major',      
                    color='#B0C4DE',    # Color azul suave
                    linestyle='--',
                    linewidth=0.7,
                    alpha=0.8   
                )
                eje.legend()

                canvas = FigureCanvasTkAgg(figura, master=resultadoFrame)
                canvas.draw()
                canvas.get_tk_widget().pack(side="right", fill="both", expand=True)

            except Exception as e:
                for w in resultadoFrame.winfo_children():
                    w.destroy()
                tk.Label(resultadoFrame, text=f"Error: {e}", fg="red", bg="white").pack()

        tk.Button(form, text="Resolver y graficar", command=calcular,
                  bg="#3A539B", fg="white", font=("Arial", 11, "bold")).grid(row=5, column=0,
                                                                             columnspan=2, pady=8)

def main():
    app = AppEuler()
    app.mainloop()
if __name__ == "__main__":
    main()
