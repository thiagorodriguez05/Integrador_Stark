from funciones_extra import*

# A. Analizar detenidamente el set de datos
#-------------------------------------------------------------------------------------------->

# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
def mostrar_heroes(lista:list)->None:
    """mostrar datos de todos los personajes

    Args:
        lista (list): contiene la informacion de los personajes
    """
    for heroe in lista:
        print("------------------------------------------")
        for key, value in heroe.items():
            print(f"{key :12}  ----> \t {value}")

#-------------------------------------------------------------------------------------------->

# C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
# la altura del mismo
def mostrar_nombre_altura(lista: list)->None:
    """muestra el nombre del heore con su respectiva altura

    Args:
        lista (list): contiene la informacion de los personajes
    """
    for heroe in lista:
        nombre = heroe["nombre"]
        altura = heroe["altura"]
        print(f" nombre: {nombre} \n \t altura: {altura} \n")

#-------------------------------------------------------------------------------------------->

# D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def mostrar_heroe_mas_alto(lista: list)->None:
    """muestra la altura del heroe mas alto

    Args:
        lista (list): contiene la informacion de los personajes

    Returns:
        _type_: retorna el maximo valor de altura
    """
    maxima_altura = calcular_maximo("altura", lista)
    return maxima_altura

#-------------------------------------------------------------------------------------------->

# E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def mostrar_heroe_menos_alto(lista: list)->None:
    """muestra la altura del heroe menos alto

    Args:
        lista (list): contiene la informacion de los personajes
    
    Returns:
        _type_: retorna el menor valor de altura
    """
    minima_altura = calcular_minimo("altura", lista)
    return minima_altura

#-------------------------------------------------------------------------------------------->

# F. Recorrer la lista y determinar la altura promedio de los superhéroes
# (PROMEDIO)
def mostrar_promedio_atura(lista: list)->None:
    """muestra la altura promedio de los heroes

    Args:
        lista (list): contiene la informacion de los personajes
    """
    for heroe in lista:
        if heroe["altura"]:
            promedio = calcular_promedio(0, 0, "altura", lista)
    print(f"la altura promedio de los heores es: {promedio}")

#-------------------------------------------------------------------------------------------->

# G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (MÁXIMO, MÍNIMO)
def mostra_nombre_del_max_y_min(lista: list)->None:
    """muestra los nombres del heroe mas alto y del menos alto

    Args:
        lista (list): contiene la informacion de los personajes
    """
    heroe_mas_alto = mostrar_heroe_mas_alto(lista)
    heroe_menos_alto = mostrar_heroe_menos_alto(lista)

    for heroe in lista:
        altura = float(heroe["altura"])
        if altura == heroe_menos_alto:
            heroe_menos_alto = heroe["nombre"]
        
        elif altura == heroe_mas_alto:
            heroe_mas_alto = heroe["nombre"]
    
    print(f"el nombre del heore mas bajo es: {heroe_menos_alto} y del mas alto es {heroe_mas_alto}")

#-------------------------------------------------------------------------------------------->

# H. Calcular e informar cual es el superhéroe más y menos pesado.
def mostrar_heroe_mas_y_menos_pesado(lista: list):
    """muestra los heroes con mayor y menor peso

    Args:
        lista (list): contiene la informacion de los personajes
    """
    minimo_peso = calcular_minimo("peso", lista)
    maximo_peso = calcular_maximo("peso", lista)
    
    for heroe in lista:
        altura = float(heroe["peso"])
        if altura == minimo_peso:
            minimo_peso = heroe["nombre"]
        
        elif altura == maximo_peso:
            maximo_peso = heroe["nombre"]
    
    print(f"el nombre del heore mas bajo es: {minimo_peso} y del mas alto es {maximo_peso}")

# I. Ordenar el código implementando una función para cada uno de los valores
# informados.

#-------------------------------------------------------------------------------------------->

