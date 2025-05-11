import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
import sys
import io

from creacion_de_matriz import Creacion_de_matriz
from suma import suma
from resta import resta
from multiplicacion import multiplicacion
from creacion_de_matriz import unica
from determinante import determinante
from inversa import inversa
from creditos import creditos

class MatrixCalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Matrices")
        master.geometry("300x400")

        tk.Label(master, text="Calculadora de Matrices", font=("Arial", 16, "bold")).pack(pady=10)

        buttons = [
            ("Sumar", self.sum_matrices),
            ("Restar", self.subtract_matrices),
            ("Multiplicar", self.multiply_matrices),
            ("Determinante", self.determinant_matrix),
            ("Inversa", self.inverse_matrix),
            ("Créditos", self.show_credits),
            ("Salir", master.quit)
        ]

        for (text, command) in buttons:
            tk.Button(master, text=text, width=20, command=command).pack(pady=5)

    def get_size(self, title):
        rows = simpledialog.askinteger(title, "Número de filas:")
        cols = simpledialog.askinteger(title, "Número de columnas:")
        if rows is None or cols is None:
            raise ValueError("Operación cancelada")
        return rows, cols

    def open_matrix_window(self, title, rows, cols, count=1):
        window = tk.Toplevel(self.master)
        window.title(f"{title} M{count}")
        entries = []
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                e = tk.Entry(window, width=5)
                e.grid(row=i, column=j, padx=2, pady=2)
                row_entries.append(e)
            entries.append(row_entries)
        return window, entries

    def capture_and_display(self, func, *args):
        old_stdout = sys.stdout
        buffer = io.StringIO()
        sys.stdout = buffer
        try:
            func(*args)
        except Exception as e:
            buffer.write(str(e))
        sys.stdout = old_stdout

        out_window = tk.Toplevel(self.master)
        out_window.title("Resultado")
        text_area = scrolledtext.ScrolledText(out_window, wrap=tk.WORD, width=60, height=20)
        text_area.pack(padx=10, pady=10)
        text_area.insert(tk.END, buffer.getvalue())
        text_area.configure(state='disabled')

    def sum_matrices(self):
        try:
            rows, cols = self.get_size("Sumar")
        except ValueError:
            return
        winA, entriesA = self.open_matrix_window("Matriz A", rows, cols, 1)
        winB, entriesB = self.open_matrix_window("Matriz B", rows, cols, 2)
        def compute():
            A = [[float(entriesA[i][j].get()) for j in range(cols)] for i in range(rows)]
            B = [[float(entriesB[i][j].get()) for j in range(cols)] for i in range(rows)]
            winA.destroy(); winB.destroy()
            self.capture_and_display(suma, A, B)
        tk.Button(winB, text="Calcular", command=compute).grid(row=rows, columnspan=cols, pady=10)

    def subtract_matrices(self):
        try:
            rows, cols = self.get_size("Restar")
        except ValueError:
            return
        winA, entriesA = self.open_matrix_window("Matriz A", rows, cols, 1)
        winB, entriesB = self.open_matrix_window("Matriz B", rows, cols, 2)
        def compute():
            A = [[float(entriesA[i][j].get()) for j in range(cols)] for i in range(rows)]
            B = [[float(entriesB[i][j].get()) for j in range(cols)] for i in range(rows)]
            winA.destroy(); winB.destroy()
            self.capture_and_display(resta, A, B)
        tk.Button(winB, text="Calcular", command=compute).grid(row=rows, columnspan=cols, pady=10)

    def multiply_matrices(self):
        try:
            r1, c1 = simpledialog.askinteger("Multiplicar", "Filas Matriz A:"), simpledialog.askinteger("Multiplicar", "Columnas Matriz A y Filas Matriz B:")
            c2 = simpledialog.askinteger("Multiplicar", "Columnas Matriz B:")
            if None in (r1, c1, c2): raise ValueError
        except ValueError:
            return
        winA, entriesA = self.open_matrix_window("Matriz A", r1, c1, 1)
        winB, entriesB = self.open_matrix_window("Matriz B", c1, c2, 2)
        def compute():
            A = [[float(entriesA[i][j].get()) for j in range(c1)] for i in range(r1)]
            B = [[float(entriesB[i][j].get()) for j in range(c2)] for i in range(c1)]
            winA.destroy(); winB.destroy()
            self.capture_and_display(multiplicacion, A, B)
        tk.Button(winB, text="Calcular", command=compute).grid(row=c1, columnspan=c2, pady=10)

    def determinant_matrix(self):
        try:
            n = simpledialog.askinteger("Determinante", "Tamaño de la matriz (n x n):")
            if n is None: raise ValueError
        except ValueError:
            return
        win, entries = self.open_matrix_window("Matriz", n, n)
        def compute():
            M = [[float(entries[i][j].get()) for j in range(n)] for i in range(n)]
            win.destroy()
            self.capture_and_display(determinante, M)
        tk.Button(win, text="Calcular", command=compute).grid(row=n, columnspan=n, pady=10)

    def inverse_matrix(self):
        try:
            n = simpledialog.askinteger("Inversa", "Tamaño de la matriz (n x n):")
            if n is None: raise ValueError
        except ValueError:
            return
        win, entries = self.open_matrix_window("Matriz", n, n)
        def compute():
            M = [[float(entries[i][j].get()) for j in range(n)] for i in range(n)]
            win.destroy()
            self.capture_and_display(inversa, M)
        tk.Button(win, text="Calcular", command=compute).grid(row=n, columnspan=n, pady=10)

    def show_credits(self):
        self.capture_and_display(creditos)

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixCalculatorGUI(root)
    root.mainloop()
