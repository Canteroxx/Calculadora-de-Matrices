def mostrar_matriz(matriz):
    for fila in matriz:
        print("    ", ["{0:7.2f}".format(x) for x in fila])

def obtener_menor(matriz, fila, columna):
    return [
        [matriz[i][j] for j in range(len(matriz)) if j != columna]
        for i in range(len(matriz)) if i != fila
    ]

def determinante(matriz, nivel=0):
    indent = "    " * nivel
    n = len(matriz)

    if any(len(fila) != n for fila in matriz):
        print("Error: La matriz no es cuadrada.")
        return None

    if n > 4:
        print("Error: Solo se permiten matrices de hasta 4x4.")
        return None

    if n == 1:
        print(f"{indent}Determinante de matriz 1x1: {matriz[0][0]}")
        return round(matriz[0][0], 2)

    if n == 2:
        a, b = matriz[0]
        c, d = matriz[1]
        det = round(a * d - b * c, 2)
        print(f"{indent}Det 2x2 = {a}*{d} - {b}*{c} = {det}")
        return det

    print(f"{indent}Calculando determinante usando la primera fila:")
    total = 0
    for col in range(n):
        signo = (-1) ** col
        coef = matriz[0][col]
        menor = obtener_menor(matriz, 0, col)

        print(f"{indent}Elemento ({0},{col}) = {coef}")
        print(f"{indent}Cálculo de los cofactores {col}:")
        mostrar_matriz(menor)

        det_menor = determinante(menor, nivel + 1)
        cofactor = round(signo * coef * det_menor, 2)

        print(f"{indent}Cofactor = {signo} * {coef} * {det_menor} = {cofactor}\n")
        total += cofactor

    total = round(total, 2)
    print(f"{indent}Determinante total (nivel {nivel}) = {total}")
    return total
