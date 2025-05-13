def factorizacion_LU(matriz):
    from copy import deepcopy
    import sys
    import io

    n = len(matriz)
    
    # Inicializamos L como matriz identidad y U como copia de la matriz original
    L = [[0.0 if i != j else 1.0 for j in range(n)] for i in range(n)]
    U = deepcopy(matriz)

    print("Factorización LU paso a paso:\n")
    print("Matriz original A:")
    for fila in matriz:
        print(fila)
    print()

    # Proceso de factorización
    for i in range(n):
        print(f"--- Paso {i + 1} ---")

        # Para cada fila debajo de la diagonal
        for j in range(i + 1, n):
            if U[i][i] == 0:
                print(f"No se puede continuar, pivote U[{i}][{i}] es cero.")
                return None, None

            # Calculamos el multiplicador
            multiplicador = U[j][i] / U[i][i]
            L[j][i] = multiplicador  # Se guarda en L

            # Restamos la fila i multiplicada por el multiplicador
            for k in range(i, n):
                U[j][k] -= multiplicador * U[i][k]

            print(f"\nMultiplicador para fila {j} = U[{j}][{i}] / U[{i}][{i}] = {multiplicador:.4f}")
            print(f"Actualizando fila {j} de U...")

        # Mostramos las matrices L y U hasta este paso
        print("\nMatriz L hasta ahora:")
        for fila in L:
            print(["{:.2f}".format(x) for x in fila])
        print("\nMatriz U hasta ahora:")
        for fila in U:
            print(["{:.2f}".format(x) for x in fila])
        print()

    print("Factorización completada.")
    return L, U
