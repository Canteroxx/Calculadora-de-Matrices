import time

def creditos():
    mensajes = [
        "Creado por: ",
        "- Joaquin Cantero",
        "- Franco Oyarzo",
        "- Demian Quezada",
        "Gracias por usar nuestra calculadora de matrices"
    ]

    for mensaje in mensajes:
        print(mensaje)
        time.sleep(1)