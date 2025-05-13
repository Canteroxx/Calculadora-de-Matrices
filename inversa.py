def mostrar_matriz(matriz):
    for fila in matriz:
        print("    ", ["{0:7.2f}".format(x) for x in fila])
    print()

def identidad(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def inversa(matriz):
    n = len(matriz)
    
    if any(len(fila) != n for fila in matriz):
        print("Error: la matriz no es cuadrada.")
        return None

    A = [fila[:] for fila in matriz]
    I = identidad(n)
    for i in range(n):
        A[i] += I[i]

    print("Matriz aumentada inicial (A | I):")
    mostrar_matriz(A)

    for i in range(n):
        if A[i][i] == 0:
            for j in range(i + 1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    print(f"Intercambio fila {i} con fila {j}")
                    mostrar_matriz(A)
                    break
            else:
                print("No se puede invertir.")
                return None

        pivote = A[i][i]
        A[i] = [round(x / pivote, 2) for x in A[i]]
        print(f"Fila {i} dividida por {pivote} para hacer el pivote 1:")
        mostrar_matriz(A)

        for j in range(n):
            if j != i:
                factor = A[j][i]
                A[j] = [round(a - factor * b, 2) for a, b in zip(A[j], A[i])]
                print(f"Fila {j} menos {factor} * fila {i}:")
                mostrar_matriz(A)

    inversa = [fila[n:] for fila in A]
    print("Matriz inversa calculada:")
    mostrar_matriz(inversa)
    return inversa
