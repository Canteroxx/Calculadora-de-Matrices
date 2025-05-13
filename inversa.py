# Usa el método de Gauss-Jordan para calcular la inversa de una matriz cuadrada

def mostrar_matriz(matriz):
    """
    Imprime la matriz en pantalla con formato fijo de 3 decimales.
    Esto ayuda a ver de forma clara cada paso del procedimiento.
    """
    for fila in matriz:
        # Se usa formato para alinear los números y mantener 3 decimales
        print("    ", ["{0:7.3f}".format(x) for x in fila])
    print()

def identidad(n):
    """
    Devuelve una matriz identidad de tamaño n x n.
    Es utilizada para formar la matriz aumentada (A | I).
    """
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def inversa(matriz):
    """
    Calcula la matriz inversa utilizando el método de Gauss-Jordan.
    """

    n = len(matriz)  # Número de filas (y columnas) de la matriz

    # Validación: todas las filas deben tener longitud igual a n (matriz cuadrada)
    if any(len(fila) != n for fila in matriz):
        print("Error: la matriz no es cuadrada.")
        return None

    # Clonamos la matriz original A y creamos la identidad I
    A = [fila[:] for fila in matriz]  # Copia de la matriz original
    I = identidad(n)                  # Matriz identidad del mismo tamaño

    # Unimos A e I horizontalmente para formar la matriz aumentada (A | I)
    for i in range(n):
        A[i] += I[i]

    print("Matriz aumentada inicial (A | I):")
    mostrar_matriz(A)  # Mostramos la matriz inicial antes de aplicar Gauss-Jordan

    # Aplicamos el método de Gauss-Jordan para transformar A en la identidad
    for i in range(n):
        # Si el pivote es cero, buscamos una fila inferior para intercambiar
        if A[i][i] == 0:
            for j in range(i + 1, n):
                if A[j][i] != 0:
                    # Intercambio de filas si se encuentra una con un pivote no nulo
                    A[i], A[j] = A[j], A[i]
                    print(f"Intercambio fila {i} con fila {j} para evitar pivote cero")
                    mostrar_matriz(A)
                    break
            else:
                # Si no se encuentra una fila válida, la matriz no es invertible
                print("No se puede invertir: hay un pivote que no se puede hacer distinto de cero.")
                return None

        # Escalamos la fila i para que el pivote (A[i][i]) sea 1
        pivote = A[i][i]
        A[i] = [x / pivote for x in A[i]]  # Divide toda la fila entre el pivote
        print(f"Fila {i} dividida por {pivote} para hacer el pivote igual a 1:")
        mostrar_matriz(A)

        # Eliminamos los demás elementos en la columna del pivote (hacemos ceros)
        for j in range(n):
            if j != i:
                factor = A[j][i]  # Elemento que queremos eliminar
                # Restamos: fila_j = fila_j - factor * fila_i
                A[j] = [a - factor * b for a, b in zip(A[j], A[i])]
                print(f"Fila {j} menos {factor} * fila {i}:")
                mostrar_matriz(A)

    # Extraemos la parte derecha de la matriz aumentada, que ahora es la inversa
    inversa = [fila[n:] for fila in A]
    print("Matriz inversa calculada:")
    mostrar_matriz(inversa)

    return inversa  # Devolvemos la matriz inversa resultante
