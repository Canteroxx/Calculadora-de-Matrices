import sys
import io
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

try:
    from ttkbootstrap import Style
except ImportError:
    Style = None

from suma import suma
from resta import resta
from multiplicacion import multiplicacion
from determinante import determinante
from inversa import inversa
from creditos import creditos
from factorizacion_lu import factorizacion_LU

class MatrixCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Matrices")
        self.geometry("900x650")
        if Style:
            Style(theme="flatly")
        self._build_widgets()

    def _build_widgets(self):
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        sidebar = ttk.Frame(container, width=200)
        sidebar.pack(side="left", fill="y", padx=10, pady=10)

        btn_opts = [
            ("Sumar", self.show_sum),
            ("Restar", self.show_subtract),
            ("Multiplicar", self.show_multiply),
            ("Determinante", self.show_determinant),
            ("Inversa", self.show_inverse),
            ("Factorizacion LU", self.show_lu),
            ("Créditos", self.show_credits),
            ("Salir", self.quit)
        ]
        for text, cmd in btn_opts:
            ttk.Button(sidebar, text=text, command=cmd).pack(fill="x", pady=5)

        self.content = ttk.Frame(container)
        self.content.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        self._show_welcome()

    def _clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def _show_welcome(self):
        self._clear_content()
        ttk.Label(self.content, text="¡Bienvenido a la Calculadora de Matrices!", font=(None, 16)).pack(pady=20)
        ttk.Label(self.content, text="Selecciona una operación desde la barra lateral.").pack()

    def _show_credits(self):
        self._clear_content()
        buf = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = buf
        try:
            creditos()
        finally:
            sys.stdout = old_stdout
        text = buf.getvalue()
        self._display_output(text)

    def _display_output(self, text):
        self._clear_content()
        txt = tk.Text(self.content, wrap="word")
        txt.insert("1.0", text)
        txt.config(state="disabled")
        txt.pack(fill="both", expand=True)

    def _setup_binary_inputs(self, operation, func):
        self._clear_content()
        ttk.Label(self.content, text=f"{operation} Matrices", font=(None, 14)).pack(pady=10)
        frame = ttk.Frame(self.content)
        frame.pack(pady=5)

        ttk.Label(frame, text="Filas A:").grid(row=0, column=0)
        rowsA = ttk.Entry(frame, width=5); rowsA.grid(row=0, column=1)
        ttk.Label(frame, text="Columnas A:").grid(row=0, column=2)
        colsA = ttk.Entry(frame, width=5); colsA.grid(row=0, column=3)
        ttk.Label(frame, text="Filas B:").grid(row=1, column=0)
        rowsB = ttk.Entry(frame, width=5); rowsB.grid(row=1, column=1)
        ttk.Label(frame, text="Columnas B:").grid(row=1, column=2)
        colsB = ttk.Entry(frame, width=5); colsB.grid(row=1, column=3)

        def create_tables():
            try:
                rA, cA = int(rowsA.get()), int(colsA.get())
                rB, cB = int(rowsB.get()), int(colsB.get())
                if func in (suma, resta) and (rA != rB or cA != cB):
                    raise ValueError("Dimensiones deben coincidir para suma/resta")
                if func is multiplicacion and cA != rB:
                    raise ValueError("Columnas A deben igual filas B para multiplicación")
            except Exception as e:
                messagebox.showerror("Error", str(e))
                return
            self._render_matrix_entries(rA, cA, rB, cB, func)

        ttk.Button(self.content, text="Confirmar dimensiones", command=create_tables).pack(pady=10)

    def _render_matrix_entries(self, rA, cA, rB, cB, func):
        self._clear_content()
        ttk.Label(self.content, text="Ingresa los valores de las matrices:", font=(None, 12)).pack(pady=5)

        canvas = tk.Canvas(self.content)
        scr = tk.Scrollbar(self.content, orient="vertical", command=canvas.yview)
        scroll_frame = ttk.Frame(canvas)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scr.set)

        canvas.pack(side="left", fill="both", expand=True)
        scr.pack(side="right", fill="y")

        entriesA = [[ttk.Entry(scroll_frame, width=5) for _ in range(cA)] for _ in range(rA)]
        entriesB = [[ttk.Entry(scroll_frame, width=5) for _ in range(cB)] for _ in range(rB)]

        ttk.Label(scroll_frame, text="Matriz A").grid(row=0, column=0, columnspan=cA)
        for i in range(rA):
            for j in range(cA):
                entriesA[i][j].grid(row=i+1, column=j, padx=2, pady=2)

        offset = rA + 2
        ttk.Label(scroll_frame, text="Matriz B").grid(row=offset, column=0, columnspan=cB)
        for i in range(rB):
            for j in range(cB):
                entriesB[i][j].grid(row=offset + i + 1, column=j, padx=2, pady=2)

        def calculate():
            try:
                A = [[float(entriesA[i][j].get()) for j in range(cA)] for i in range(rA)]
                B = [[float(entriesB[i][j].get()) for j in range(cB)] for i in range(rB)]
                buf = io.StringIO()
                old_stdout = sys.stdout
                sys.stdout = buf
                func(A, B)
                sys.stdout = old_stdout
                self._display_output(buf.getvalue())
            except Exception as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(self.content, text="Calcular", command=calculate).pack(pady=10)

    def _setup_unary_input(self, operation, func):
        self._clear_content()
        ttk.Label(self.content, text=f"{operation} de Matriz", font=(None, 14)).pack(pady=10)
        frame = ttk.Frame(self.content)
        frame.pack(pady=5)

        ttk.Label(frame, text="Tamaño (cuadrada máx 4):").grid(row=0, column=0)
        size = ttk.Entry(frame, width=5); size.grid(row=0, column=1)

        def create_table():
            try:
                n = int(size.get())
                if n < 1 or n > 4:
                    raise ValueError("Tamaño debe ser entre 1 y 4")
            except Exception as e:
                messagebox.showerror("Error", str(e))
                return
            self._render_unary_entries(n, func)

        ttk.Button(self.content, text="Confirmar tamaño", command=create_table).pack(pady=10)

    def _render_unary_entries(self, n, func):
        self._clear_content()
        ttk.Label(self.content, text="Ingresa los valores de la matriz:", font=(None, 12)).pack(pady=5)

        container = ttk.Frame(self.content)
        container.pack()

        entries = [[ttk.Entry(container, width=5) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                entries[i][j].grid(row=i, column=j, padx=2, pady=2)

        def calculate():
            try:
                M = [[float(entries[i][j].get()) for j in range(n)] for i in range(n)]
                buf = io.StringIO()
                old_stdout = sys.stdout
                sys.stdout = buf
                func(M)
                sys.stdout = old_stdout
                self._display_output(buf.getvalue())
            except Exception as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(self.content, text="Calcular", command=calculate).pack(pady=10)

    def show_sum(self):    self._setup_binary_inputs("Sumar", suma)
    def show_subtract(self): self._setup_binary_inputs("Restar", resta)
    def show_multiply(self): self._setup_binary_inputs("Multiplicar", multiplicacion)
    def show_determinant(self): self._setup_unary_input("Determinante", determinante)
    def show_inverse(self): self._setup_unary_input("Inversa", inversa)
    def show_lu(self):            self._setup_unary_input("Factorización LU", factorizacion_LU)
    def show_credits(self): self._show_credits()

if __name__ == "__main__":
    app = MatrixCalculatorApp()
    app.mainloop()
