import os
from funciones import*
from data_stark import*

seguir = True
while seguir:
    os.system("cls")
    
    print("  *** menu de opciones ***")
    print("1- mostrar heroes masculinos")
    print("2- mostrar heroes femeninos")
    print("3- mostrar heroe masculino mas alto")
    print("4- mostrar heroe femenino mas alto")
    print("5-  mostrar heroe masculino menos alto")
    print("6- mostrar heroe femenino menos alto")
    print("7- mostrar altura promedio de los heroes masculinos")
    print("8- mostrar altura promedio de los heroes femenino")
    print("9- mostrar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)")
    print("10- mostrar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("11-  mostrar cuántos superhéroes tienen cada tipo de color de pelo")
    print("12-  mostrar cuántos superhéroes tienen cada tipo de inteligencia")
    print("13- Listar todos los superhéroes agrupados por color de ojos. ")
    print("14- Listar todos los superhéroes agrupados por color de pelo.")
    print("15- Listar todos los superhéroes agrupados por inteligencia.")
    print("16- salir")
    
    print("\n")
    opcion = input("ingrese opcion: ")
    print("\n")
    
    match opcion: 
        case "1":
            mostrar_heroes_masculinos(lista_personajes)
        case "2":
            mostrar_heroes_femenino(lista_personajes)
        case "3":
            masculino_mas_alto = mostrar_masculino_mas_alto(lista_personajes)
            print(f"el heroe masculino mas alto es: {masculino_mas_alto}")
        case "4":
            femenino_mas_alto = mostrar_femenino_mas_alto(lista_personajes)
            print(f"el heroe femenino mas alto es: {femenino_mas_alto}")
        case "5":
            masculino_menos_alto = mostrar_masculino_menos_alto(lista_personajes)
            print(f"el heroe masculino menos alto es: {masculino_menos_alto}")
        case "6":
            femenino_menos_alto = mostrar_femenino_menos_alto(lista_personajes)
            print(f"el heroe femenino mas alto es: {femenino_menos_alto}")
        case "7":
            mostrar_altura_promedio_masculino(lista_personajes)
        case "8":
            mostrar_altura_promedio_femenino(lista_personajes)
        case "9":
            mostrar_nombres_C_a_F(lista_personajes)
        case "10":
            mostrar_tipos_de_ojos(lista_personajes)
        case "11":
            mostrar_tipos_de_pelo(lista_personajes)
        case "12":
            mostrar_tipos_de_inteligencia(lista_personajes)
        case "13":
            mostrar_superheroes_por_color_ojos(lista_personajes)
        case "14":
            mostrar_superheroes_por_color_pelo(lista_personajes)
        case "15":
            mostrar_superheroes_por_inteligencia(lista_personajes)
        case "16":
            seguir = False
    os.system("pause")