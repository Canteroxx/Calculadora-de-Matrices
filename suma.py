def suma():
    # ingresamos el tamaño de la matriz
    fila1 = int(input("¿Cuántas filas tiene la matriz A? "))
    columna1 = int(input("¿Cuántas columnas tiene la matriz A? "))

    matrizA = [] # matriz A
    matrizB = [] # matriz 2
    resultado = [] # resultado

    print(f"Ahora que sabemos que la 1ra matriz es de {fila1}x{columna1}, vamos a agregar los datos")

    for i in range(fila1):
        fila = [] # creamos una fila vacia 
        for j in range(columna1):
            valores1 = int(input(f"Ingrese el elemento [{i}][{j}] de la primera matriz: "))
            fila.append(valores1) # agregamos el valor a la fila vacia
        matrizA.append(fila) # agregamos la fila a la matriz A

    print("La matriz A es:")
    for elemento in matrizA:# mostramos la matriz A
        print(elemento)

    fila2 = int(input("¿Cuántas filas tiene la 2da matriz? "))
    columna2 = int(input("¿Cuántas columnas tiene la 2da matriz? "))

    while fila1 != fila2 or columna1 != columna2: # verificamos que las matrices tengan el mismo tamaño
        print("Las matrices no tienen el mismo tamaño, no se pueden sumar.")
        print("Por favor, ingrese las dimensiones de la segunda matriz nuevamente.")
        fila2 = int(input("¿Cuántas filas tiene la 2da matriz? "))
        columna2 = int(input("¿Cuántas columnas tiene la 2da matriz? "))

    print(f"Ahora que sabemos que es una matriz de {fila2}x{columna2}, vamos a agregar los datos")
    
    for i in range(fila2):
        fila = [] # creamos una fila vacia
        for j in range(columna2):
            valores2 = int(input(f"Ingrese el elemento [{i}][{j}] de la segunda matriz: "))
            fila.append(valores2)
        matrizB.append(fila)

    print("La matriz B es:")
    for elemento in matrizB: # mostramos la matriz B
        print(elemento)
    
    print("Ahora vamos a sumar las matrices")
    print("la operacion es la siguiente:")
    
    print("Matriz A:")
    for fila in matrizA:
        print(fila)
        
    print("Matriz B:")
    for fila in matrizB:
        print(fila)
    
    print("A + B =")

    for i in range(len(matrizA)):
        fila = []
        for j in range(len(matrizA[i])):  # recorrer las columnas
            fila.append(f"{matrizA[i][j]} + {matrizB[i][j]}")  # agregar la operación a la fila
        print(f"[{', '.join(fila)}]")

    for i in range(fila1):
        resultado.append([])  # inicializamos una nueva fila en el resultado
        for j in range(columna1):
            suma_matriz = matrizA[i][j] + matrizB[i][j]
            resultado[i].append(suma_matriz)

    print("El resultado de la suma es:")
    for elemento in resultado:
        print(elemento)
