def mostrarMenu():
    print("Menu")
    print("1. Descargar Video")
    print("2. Descargar Formato Podcast")
    print("3. Transcribir Video")
    print("4. Salir")

def opcion1():
    from scripts import descargarVideos
    descargarVideos()

def opcion2():
    from scripts import descargarPodcast
    descargarPodcast()

def opcion3():
    from scripts import transcribirVideos
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
            opcion3()
        elif(opcion =="4"):
            print("Saliendo")
            break
        else:
            print("Opcion no valida")


if __name__ == "__main__":
    main()