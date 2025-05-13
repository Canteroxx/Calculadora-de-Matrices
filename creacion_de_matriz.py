def ingresar_matriz(filas, columnas, nombre="matriz"):
    matriz = []
    print(f"Ingrese los elementos de la {nombre} ({filas}x{columnas}):")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Ingrese el elemento [{i}][{j}] de la {nombre}: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz


def Creacion_de_matriz(opcion, operacion):
    fila1 = int(input("¿Cuántas filas tiene la matriz A? "))
    columna1 = int(input("¿Cuántas columnas tiene la matriz A? "))
    matrizA = ingresar_matriz(fila1, columna1, "primera matriz")

    fila2 = int(input("¿Cuántas filas tiene la 2da matriz? "))
    columna2 = int(input("¿Cuántas columnas tiene la 2da matriz? "))

    if opcion in (1, 2):  # Suma o resta
        while fila1 != fila2 or columna1 != columna2:
            print(f"Las matrices no tienen el mismo tamaño, no se pueden {operacion}.")
            fila2 = int(input("¿Cuántas filas tiene la 2da matriz? "))
            columna2 = int(input("¿Cuántas columnas tiene la 2da matriz? "))
    elif opcion == 3:  # Multiplicación
        while columna1 != fila2:
            print("Las dimensiones no permiten multiplicar las matrices.")
            fila2 = int(input("¿Cuántas filas tiene la 2da matriz? "))
            columna2 = int(input("¿Cuántas columnas tiene la 2da matriz? "))

    matrizB = ingresar_matriz(fila2, columna2, "segunda matriz")

    print("Matriz A:")
    for fila in matrizA:
        print(fila)
    print("Matriz B:")
    for fila in matrizB:
        print(fila)

    return matrizA, matrizB


def unica():
    fila = int(input("¿De qué tamaño es la matriz cuadrada? (max 4): "))
    while fila > 4 or fila < 1:
        fila = int(input("Debe ser entre 1 y 4. Ingrese de nuevo: "))
    matriz = ingresar_matriz(fila, fila, "matriz cuadrada")
    print("La matriz ingresada es:")
    for f in matriz:
        print(f)
    return matriz
