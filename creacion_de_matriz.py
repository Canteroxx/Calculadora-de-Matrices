def Creacion_de_matriz(opcion, operacion):
    # ingresamos el tamaño de la matriz
    fila1 = int(input("¿Cuántas filas tiene la matriz A? "))
    columna1 = int(input("¿Cuántas columnas tiene la matriz A? "))

    matrizA = []
    matrizB = []

    print(f"Ahora que sabemos que la 1ra matriz es de {fila1}x{columna1}, vamos a agregar los datos")
    for i in range(fila1):
        fila = []
        for j in range(columna1):
            v = int(input(f"Ingrese el elemento [{i}][{j}] de la primera matriz: "))
            fila.append(v)
        matrizA.append(fila)

    print("La matriz A es:")
    for fila in matrizA:
        print(fila)

    # dimensiones segunda matriz
    fila2 = int(input("¿Cuántas filas tiene la 2da matriz? "))
    columna2 = int(input("¿Cuántas columnas tiene la 2da matriz? "))

    if opcion == 1 or opcion == 2:
        while fila1 != fila2 or columna1 != columna2:
            print(f"Las matrices no tienen el mismo tamaño, no se pueden {operacion}.")
            fila2 = int(input("¿Cuántas filas tiene la 2da matriz? "))
            columna2 = int(input("¿Cuántas columnas tiene la 2da matriz? "))
    elif opcion == 3:
        while columna1 != fila2:
            print("Las matrices no tienen el mismo tamaño, no se pueden multiplicar")
            fila2 = int(input("¿Cuántas filas tiene la 2da matriz? "))
            columna2 = int(input("¿Cuántas columnas tiene la 2da matriz? "))
    
    print(f"Ahora que sabemos que es una matriz de {fila2}x{columna2}, vamos a agregar los datos")
    for i in range(fila2):
        fila = []
        for j in range(columna2):
            v = int(input(f"Ingrese el elemento [{i}][{j}] de la segunda matriz: "))
            fila.append(v)
        matrizB.append(fila)
    print("La matriz B es:")
    for fila in matrizB:
        print(fila)

    return matrizA, matrizB



def unica():
    fila = int(input("¿de que tamano es la matriz cuadrada? (max 4): "))
    while fila > 4 or fila < 1:
        fila = int(input("debe ser entre 1 y 4, ingrese de nuevo: "))

    matriz = []
    for i in range(fila):
        fila_actual = []
        for j in range(fila):
            valor = int(input(f"ingrese el elemento [{i}][{j}]: "))
            fila_actual.append(valor)
        matriz.append(fila_actual)

    print("la matriz ingresada es: ")
    for f in matriz:
        print(f)
    return matriz