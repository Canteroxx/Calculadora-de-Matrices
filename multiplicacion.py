import time

def multiplicacion(matrizA, matrizB):
    print("\nAhora vamos a multiplicar las matrices")

    # muestra la matriz A
    print("Matriz A:")
    for fila in matrizA:
        print(fila)
        time.sleep(1)

    # muestra la matriz B
    print("Matriz B:")
    for fila in matrizB:
        print(fila)
        time.sleep(1)

    # muestra la operación
    print("\nA x B =")
    for i in range(len(matrizA)):
        temp = []
        for j in range(len(matrizB[0])):
            ops = [f"{matrizA[i][k]} x {matrizB[k][j]}" for k in range(len(matrizA[0]))]
            temp.append(' + '.join(ops))
        print(f"[{'  '.join(temp)}]")
        time.sleep(1)

    # calcula la multiplicación
    resultado = []
    for i in range(len(matrizA)):
        temp2 = []
        for j in range(len(matrizB[0])):
            suma = 0
            for n in range(len(matrizA[0])):
                suma += matrizA[i][n] * matrizB[n][j]
            temp2.append(round(suma, 2))
        resultado.append(temp2)

    print("Resultado Final")
    for fila in resultado:
        print(fila)
        time.sleep(1)
