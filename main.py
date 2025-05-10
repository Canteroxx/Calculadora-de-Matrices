from creacion_de_matriz import Creacion_de_matriz
from creditos import creditos
from suma import suma
from resta import resta
from multiplicacion import multiplicacion
from creacion_de_matriz import unica
from determinante import determinante
from inversa import inversa
    
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
    try:
        alternativa = int(input("Escoge una opción: "))
        if alternativa == 1:
            matrizA, matrizB = Creacion_de_matriz(alternativa, "sumar")
            suma(matrizA,matrizB)
        elif alternativa == 2:
            matrizA, matrizB= Creacion_de_matriz(alternativa, "restar")
            resta(matrizA, matrizB)
        elif alternativa == 3:
            matrizA, matrizB= Creacion_de_matriz(alternativa, "multiplicar")
            multiplicacion(matrizA, matrizB)
        elif alternativa == 4:
            matriz = unica()
            print("\ncalculo del determinante paso por paso")
            determinante(matriz)
        elif alternativa == 5:
            matriz = unica()
            print("\ncalculo de la inversa de la matriz paso por paso")
            inversa(matriz)
        elif alternativa == 6:
            creditos()
        elif alternativa == 7:
            print("Gracias por usar nuestra calculadora de matrices")
            inicio = False
        else:
            print("Opción no válida, por favor intenta de nuevo.")
            continue
    except ValueError:
        print("Error: Debes ingresar un número entero válido.")