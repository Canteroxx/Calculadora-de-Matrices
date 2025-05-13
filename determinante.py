# Usa el método de los cofactores para calcular el determinante de una matriz de hasta 4x4

def mostrar_matriz(matriz):
    """
    Función auxiliar que imprime cada fila de la matriz con indentación visual.
    Útil para mostrar las submatrices durante el proceso de cálculo.
    """
    for fila in matriz:
        print("    ", fila)

def obtener_menor(matriz, fila, columna):
    """
    Obtiene el menor (submatriz) al eliminar la fila y la columna especificadas.
    Este menor se usa para calcular el cofactor correspondiente.
    """
    return [
        [matriz[i][j] for j in range(len(matriz)) if j != columna]  # Elimina la columna
        for i in range(len(matriz)) if i != fila                    # Elimina la fila
    ]

def determinante(matriz, nivel=0):
    """
    Calcula recursivamente el determinante de una matriz cuadrada usando cofactores.
    El parámetro `nivel` sirve para manejar la indentación visual durante el proceso recursivo.
    """

    indent = "    " * nivel  # Crea un margen visual para mostrar los niveles recursivos
    n = len(matriz)          # Número de filas (o columnas) de la matriz

    # Validación: Verifica que todas las filas tengan la misma longitud (matriz cuadrada)
    if any(len(fila) != n for fila in matriz):
        print("Error: La matriz no es cuadrada.")
        return None

    # Límite: Solo se permiten matrices de hasta 4x4 para evitar llamadas recursivas muy profundas
    if n > 4:
        print("Error: Solo se permiten matrices de hasta 4x4.")
        return None

    # Caso base: matriz 1x1 → el determinante es simplemente el único valor presente
    if n == 1:
        print(f"{indent}Determinante de matriz 1x1: {matriz[0][0]}")
        return matriz[0][0]

    # Caso base: matriz 2x2 → aplicar fórmula directa ad - bc
    if n == 2:
        a, b = matriz[0]
        c, d = matriz[1]
        det = a * d - b * c
        print(f"{indent}Determinante 2x2: ({a}*{d}) - ({b}*{c}) = {det}")
        return det

    # Caso general: matriz 3x3 o 4x4 → usar cofactores por la primera fila
    print(f"{indent}Calculando determinante de matriz {n}x{n} usando la primera fila:")
    total = 0  # Inicializa el acumulador del determinante

    # Recorremos cada columna de la primera fila para aplicar el desarrollo por cofactores
    for col in range(n):
        signo = (-1) ** col         # Alternancia de signos: +, -, +, ... según la columna
        coef = matriz[0][col]       # Elemento actual de la primera fila
        menor = obtener_menor(matriz, 0, col)  # Submatriz (menor) correspondiente

        # Mostrar información del proceso para que sea entendible
        print(f"{indent}→ Tomando elemento en fila 0, columna {col}: {coef}")
        print(f"{indent}  Submatriz eliminando fila 0 y columna {col} (para el cofactor):")
        mostrar_matriz(menor)  # Imprimir la submatriz

        # Llamada recursiva: calcular el determinante del menor
        det_menor = determinante(menor, nivel + 1)

        # Calcular el cofactor usando el signo, el elemento y el determinante del menor
        cofactor = signo * coef * det_menor

        # Mostrar el cálculo del cofactor
        print(f"{indent}  Cofactor = ({signo}) * ({coef}) * ({det_menor}) = {cofactor}\n")

        total += cofactor  # Sumar el cofactor al total del determinante

    # Al final del nivel recursivo, mostrar el resultado parcial del determinante
    print(f"{indent}→ Determinante parcial en nivel {nivel} = {total}")
    return total  # Devolver el valor calculado del determinante
