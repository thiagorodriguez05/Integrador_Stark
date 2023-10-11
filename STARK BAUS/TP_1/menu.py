import os
from funciones import*
from data_stark import*

seguir = True
while seguir:
    os.system("cls")
    
    print("  *** menu de opciones ***")
    print("1- mostrar heroes")
    print("2- mostrar heore con nombre y su altura")
    print("3- mostrar heroe con mayor altura")
    print("4- mostrar heroe menos alto")
    print("5- mostrar la altura promeido")
    print("6- mostrar nombres del heore mas alto y del menos alto")
    print("7- mostrar heroe mas y menos pesado")
    print("8- salir")
    
    opcion = input("ingrese opcion: ")
    
    match opcion: 
        case "1":
            datos_personajes = mostrar_heroes(lista_personajes)
            print(f"{datos_personajes} \n")
        case "2":
            mostrar_nombre_altura(lista_personajes)
        case "3":
            heroe_mas_alto = mostrar_heroe_mas_alto(lista_personajes)
            print(f"la altura del heroe mas alto es: {heroe_mas_alto}")
        case "4":
            heroe_menos_alto = mostrar_heroe_menos_alto(lista_personajes)
            print(f"la altura del heroe menos alto es: {heroe_menos_alto}")
        case "5":
            mostrar_promedio_atura(lista_personajes)
        case "6":
            mostra_nombre_del_max_y_min(lista_personajes)
        case "7":
            mostrar_heroe_mas_y_menos_pesado(lista_personajes)
        case "8":
            seguir = False
    os.system("pause")