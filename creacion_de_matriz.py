def Creacion_de_matriz(opcion, operacion):
    # Solicitamos al usuario el tamaño (filas y columnas) de la primera matriz
    fila1 = int(input("¿Cuántas filas tiene la matriz A? "))
    columna1 = int(input("¿Cuántas columnas tiene la matriz A? "))

    matrizA = []  # Lista vacía que almacenará la matriz A
    matrizB = []  # Lista vacía que almacenará la matriz B

    # Informamos al usuario del tamaño ingresado para matriz A
    print(f"Ahora que sabemos que la 1ra matriz es de {fila1}x{columna1}, vamos a agregar los datos")
    
    # Rellenamos la matriz A elemento por elemento
    for i in range(fila1):
        fila = []  # Lista que representa una fila de la matriz
        for j in range(columna1):
            v = int(input(f"Ingrese el elemento [{i}][{j}] de la primera matriz: "))
            fila.append(v)  # Se agrega el elemento a la fila actual
        matrizA.append(fila)  # Se agrega la fila completa a la matriz A

    # Mostramos la matriz A al usuario
    print("La matriz A es:")
    for fila in matrizA:
        print(fila)

    # Solicitamos el tamaño de la segunda matriz
    fila2 = int(input("¿Cuántas filas tiene la 2da matriz? "))
    columna2 = int(input("¿Cuántas columnas tiene la 2da matriz? "))

    # Validamos compatibilidad de dimensiones dependiendo del tipo de operación
    if opcion == 1 or opcion == 2:  # Suma o resta
        # Para sumar o restar, las matrices deben tener el mismo tamaño
        while fila1 != fila2 or columna1 != columna2:
            print(f"Las matrices no tienen el mismo tamaño, no se pueden {operacion}.")
            fila2 = int(input("¿Cuántas filas tiene la 2da matriz? "))
            columna2 = int(input("¿Cuántas columnas tiene la 2da matriz? "))
    elif opcion == 3:  # Multiplicación
        # Para multiplicar, el número de columnas de la primera debe ser igual al número de filas de la segunda
        while columna1 != fila2:
            print("Las matrices no tienen el mismo tamaño, no se pueden multiplicar")
            fila2 = int(input("¿Cuántas filas tiene la 2da matriz? "))
            columna2 = int(input("¿Cuántas columnas tiene la 2da matriz? "))

    # Informamos al usuario del tamaño válido para la matriz B
    print(f"Ahora que sabemos que es una matriz de {fila2}x{columna2}, vamos a agregar los datos")
    
    # Rellenamos la matriz B con los datos ingresados
    for i in range(fila2):
        fila = []
        for j in range(columna2):
            v = int(input(f"Ingrese el elemento [{i}][{j}] de la segunda matriz: "))
            fila.append(v)
        matrizB.append(fila)

    # Mostramos la matriz B al usuario
    print("La matriz B es:")
    for fila in matrizB:
        print(fila)

    # Retornamos ambas matrices para ser utilizadas en la operación correspondiente
    return matrizA, matrizB




def unica():
    # Pedimos al usuario que indique el tamaño de una matriz cuadrada (de 1x1 a 4x4)
    fila = int(input("¿de que tamano es la matriz cuadrada? (max 4): "))
    
    # Validamos que el tamaño esté dentro del rango permitido
    while fila > 4 or fila < 1:
        fila = int(input("debe ser entre 1 y 4, ingrese de nuevo: "))

    matriz = []  # Lista vacía para almacenar la matriz

    # Rellenamos la matriz cuadrada elemento por elemento
    for i in range(fila):
        fila_actual = []  # Lista temporal para cada fila
        for j in range(fila):  # Como es cuadrada, el número de columnas es igual al de filas
            valor = int(input(f"ingrese el elemento [{i}][{j}]: "))
            fila_actual.append(valor)
        matriz.append(fila_actual)  # Se agrega la fila completa a la matriz

    # Mostramos la matriz ingresada
    print("la matriz ingresada es: ")
    for f in matriz:
        print(f)

    # Retornamos la matriz para ser usada en otra función (determinante, inversa, etc.)
    return matriz
