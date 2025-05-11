import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
import sys
import io

# Importar operaciones de matrices existentes
from creacion_de_matriz import Creacion_de_matriz
from suma import suma
from resta import resta
from multiplicacion import multiplicacion
from creacion_de_matriz import unica
from determinante import determinante
from inversa import inversa
from creditos import creditos

class CalculadoraMatricesGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Matrices")
        master.geometry("300x400")

        # Etiqueta de encabezado
        tk.Label(master, text="Calculadora de Matrices", font=("Arial", 16, "bold")).pack(pady=10)

        # Definir botones y sus comandos
        botones = [
            ("Sumar", self.sumar_matrices),
            ("Restar", self.restar_matrices),
            ("Multiplicar", self.multiplicar_matrices),
            ("Determinante", self.determinante_matriz),
            ("Inversa", self.inversa_matriz),
            ("Creditos", self.mostrar_creditos),
            ("Salir", master.quit)
        ]

        # Crear botones en la ventana principal
        for (texto, comando) in botones:
            tk.Button(master, text=texto, width=20, command=comando).pack(pady=5)

    def solicitar_tamano(self, titulo):
        # Pedir numero de filas y columnas
        filas = simpledialog.askinteger(titulo, "Numero de filas:")
        columnas = simpledialog.askinteger(titulo, "Numero de columnas:")
        if filas is None or columnas is None:
            raise ValueError("Operacion cancelada")
        return filas, columnas

    def crear_ventana_matriz(self, titulo, filas, columnas, indice=1):
        # Crear ventana para ingresar elementos de la matriz
        ventana = tk.Toplevel(self.master)
        ventana.title(f"{titulo} M{indice}")
        entradas = []
        for i in range(filas):
            fila_entradas = []
            for j in range(columnas):
                e = tk.Entry(ventana, width=5)
                e.grid(row=i, column=j, padx=2, pady=2)
                fila_entradas.append(e)
            entradas.append(fila_entradas)
        return ventana, entradas

    def mostrar_salida(self, funcion, *args):
        # Redirigir stdout a un buffer
        salida_antigua = sys.stdout
        buffer = io.StringIO()
        sys.stdout = buffer
        try:
            funcion(*args)
        except Exception as e:
            buffer.write(str(e))
        # Restaurar stdout
        sys.stdout = salida_antigua

        # Mostrar resultado en ventana con texto desplazable
        ventana_out = tk.Toplevel(self.master)
        ventana_out.title("Resultado")
        texto = scrolledtext.ScrolledText(ventana_out, wrap=tk.WORD, width=60, height=20)
        texto.pack(padx=10, pady=10)
        texto.insert(tk.END, buffer.getvalue())
        texto.configure(state='disabled')

    def sumar_matrices(self):
        try:
            filas, columnas = self.solicitar_tamano("Sumar")
        except ValueError:
            return
        ventanaA, entradasA = self.crear_ventana_matriz("Matriz A", filas, columnas, 1)
        ventanaB, entradasB = self.crear_ventana_matriz("Matriz B", filas, columnas, 2)
        def calcular():
            A = [[float(entradasA[i][j].get()) for j in range(columnas)] for i in range(filas)]
            B = [[float(entradasB[i][j].get()) for j in range(columnas)] for i in range(filas)]
            ventanaA.destroy()
            ventanaB.destroy()
            self.mostrar_salida(suma, A, B)
        tk.Button(ventanaB, text="Calcular", command=calcular).grid(row=filas, columnspan=columnas, pady=10)

    def restar_matrices(self):
        try:
            filas, columnas = self.solicitar_tamano("Restar")
        except ValueError:
            return
        ventanaA, entradasA = self.crear_ventana_matriz("Matriz A", filas, columnas, 1)
        ventanaB, entradasB = self.crear_ventana_matriz("Matriz B", filas, columnas, 2)
        def calcular():
            A = [[float(entradasA[i][j].get()) for j in range(columnas)] for i in range(filas)]
            B = [[float(entradasB[i][j].get()) for j in range(columnas)] for i in range(filas)]
            ventanaA.destroy()
            ventanaB.destroy()
            self.mostrar_salida(resta, A, B)
        tk.Button(ventanaB, text="Calcular", command=calcular).grid(row=filas, columnspan=columnas, pady=10)

    def multiplicar_matrices(self):
        try:
            f1 = simpledialog.askinteger("Multiplicar", "Filas Matriz A:")
            c1 = simpledialog.askinteger("Multiplicar", "Columnas Matriz A y Filas Matriz B:")
            c2 = simpledialog.askinteger("Multiplicar", "Columnas Matriz B:")
            if None in (f1, c1, c2):
                raise ValueError
        except ValueError:
            return
        ventanaA, entradasA = self.crear_ventana_matriz("Matriz A", f1, c1, 1)
        ventanaB, entradasB = self.crear_ventana_matriz("Matriz B", c1, c2, 2)
        def calcular():
            A = [[float(entradasA[i][j].get()) for j in range(c1)] for i in range(f1)]
            B = [[float(entradasB[i][j].get()) for j in range(c2)] for i in range(c1)]
            ventanaA.destroy()
            ventanaB.destroy()
            self.mostrar_salida(multiplicacion, A, B)
        tk.Button(ventanaB, text="Calcular", command=calcular).grid(row=c1, columnspan=c2, pady=10)

    def determinante_matriz(self):
        try:
            n = simpledialog.askinteger("Determinante", "Tamano de la matriz (n x n):")
            if n is None:
                raise ValueError
        except ValueError:
            return
        ventana, entradas = self.crear_ventana_matriz("Matriz", n, n)
        def calcular():
            M = [[float(entradas[i][j].get()) for j in range(n)] for i in range(n)]
            ventana.destroy()
            self.mostrar_salida(determinante, M)
        tk.Button(ventana, text="Calcular", command=calcular).grid(row=n, columnspan=n, pady=10)

    def inversa_matriz(self):
        try:
            n = simpledialog.askinteger("Inversa", "Tamano de la matriz (n x n):")
            if n is None:
                raise ValueError
        except ValueError:
            return
        ventana, entradas = self.crear_ventana_matriz("Matriz", n, n)
        def calcular():
            M = [[float(entradas[i][j].get()) for j in range(n)] for i in range(n)]
            ventana.destroy()
            self.mostrar_salida(inversa, M)
        tk.Button(ventana, text="Calcular", command=calcular).grid(row=n, columnspan=n, pady=10)

    def mostrar_creditos(self):
        # Mostrar creditos del programa
        self.mostrar_salida(creditos)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraMatricesGUI(root)
    root.mainloop()
