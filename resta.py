import time 
def resta(matrizA, matrizB):
    print("\nAhora vamos a restar las matrices")

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
    print("\nA - B =")
    for i in range(len(matrizA)):
        ops = [f"{matrizA[i][j]} - {matrizB[i][j]}" for j in range(len(matrizA[i]))]
        print(f"[{', '.join(ops)}]")
        time.sleep(1)

    # calcular la resta numérica
    resultado = []
    for i in range(len(matrizA)):
        fila_res = []
        for j in range(len(matrizA[i])):
            valor = round(matrizA[i][j] - matrizB[i][j], 2)
            fila_res.append(valor)
        resultado.append(fila_res)

    print("\nEl resultado de la resta es:")
    for fila in resultado:
        print(fila)
        time.sleep(1)
