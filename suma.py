

def suma(matrizA, matrizB):
    print("\nAhora vamos a sumar las matrices")
    print("Matriz A:")
    for fila in matrizA:
        print(fila)
    print("Matriz B:")
    for fila in matrizB:
        print(fila)
    print("\nA + B =")
    # mostrar la operación
    for i in range(len(matrizA)):
        ops = [f"{matrizA[i][j]}+{matrizB[i][j]}" for j in range(len(matrizA[i]))]
        print(f"[{', '.join(ops)}]")

    # calcular la suma numérica
    resultado = []
    for i in range(len(matrizA)):
        fila_res = []
        for j in range(len(matrizA[i])):
            fila_res.append(matrizA[i][j] + matrizB[i][j])
        resultado.append(fila_res)

    print("\nEl resultado de la suma es:")
    for fila in resultado:
        print(fila)



    
