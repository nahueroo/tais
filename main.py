from scripts import *

def mostrarMenu():
    print("Menu")
    print("1. Descargar Video")
    print("2. Transcribir Video")
    print("3. Salir")

def opcion1():
    descargarVideos()

def opcion2():
    transcribirVideos()

def main():
    while True:
        mostrarMenu()
        opcion = input("¿Que desea hacer?")

        if(opcion == "1"):
            opcion1()
        elif(opcion =="2"):
            opcion2()
        elif(opcion =="3"):
            print("Saliendo")
            break
        else:
            print("Opcion no valida")


if __name__ == "__main__":
    main()