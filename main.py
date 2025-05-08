from creacion_de_matriz import Creacion_de_matriz
from creditos import creditos
from suma import suma
    
inicio = True

while inicio:
    
    print("""
Bienvenido al nuestra calculadora de matrices
          
    Que opcion deseas escojer?
          
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Determinante
    5. Inversa
    6. Creditos
    7. Salir
          """)
    alternativa = input("Escoge una opción: ")
    if alternativa == "1":
        matrizA, matrizB, fila, columna = Creacion_de_matriz()
        suma(matrizA,matrizB)
    elif alternativa == "2":
        matrizA, matrizB, fila, columna = Creacion_de_matriz()
        for j in range(len (matrizB)):
            for k in range(len(matrizB)):
                matrizB[j][k] = -1*matrizB[j][k]      
        suma(matrizA,matrizB)
    elif alternativa == "3":
        pass
    elif alternativa == "4":
        pass
    elif alternativa == "5":
        pass
    elif alternativa == "6":
        creditos()
    elif alternativa == "7":
        print("Gracias por usar nuestra calculadora de matrices")
        inicio = False
    else:
        print("Opción no válida, por favor intenta de nuevo.")
        continue