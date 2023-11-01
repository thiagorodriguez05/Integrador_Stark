from data_stark import lista_personajes
from funciones_extra import*
# Desafío #01:
# Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos,
# utilizando un menú que permita acceder a cada uno de los puntos por separado.

# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género M
def mostrar_heroes_masculinos(lista: list):
    """mostrar heroes masculinos

    Args:
        lista (list): contiene la informacion de los personajes
    """
    for heroes in lista:
        if heroes["genero"] == "M":
            nombre = heroes["nombre"]
            print(nombre)


# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género F
def mostrar_heroes_femenino(lista: list):
    """mostrar heroes femeninos

    Args:
        lista (list): contiene la informacion de los personajes
    """
    for heroes in lista:
        if heroes["genero"] == "F":
            nombre = heroes["nombre"]
            print(nombre)


# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
def mostrar_masculino_mas_alto(lista: list):
    """mostrar masculino mas alto

    Args:
        lista (list): contiene la informacion de los personajes

    Returns:
        _type_: retorna el msaculino mas alto
    """
    for heroes in lista:
        if heroes["genero"] == "M":
            altura_mas_alto_masculino = calcular_maximo("altura", lista)
    return altura_mas_alto_masculino


# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
def mostrar_femenino_mas_alto(lista: list):
    """mostrar el femenino mas alto

    Args:
        lista (list): contiene la informacion de los personajes

    Returns:
        _type_: retorna el femenino mas alto
    """
    for heroes in lista:
        if heroes["genero"] == "F":
            altura_mas_alto_femenino = calcular_maximo("altura", lista)
    return altura_mas_alto_femenino


# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
def mostrar_masculino_menos_alto(lista: list):
    """mostrar el masculino menos alto

    Args:
        lista (list): contiene la informacion de los personajes

    Returns:
        _type_: retorna el masculino meno alto
    """
    for heroes in lista:
        if heroes["genero"] == "M":
            altura_menos_alto_masculino = calcular_minimo("altura", lista)
    return altura_menos_alto_masculino


# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
def mostrar_femenino_menos_alto(lista: list):
    """mostrar el femenino menos alto

    Args:
        lista (list): contiene la informacion de los personajes

    Returns:
        _type_: retorna el femenio menos alto
    """
    for heroes in lista:
        if heroes["genero"] == "F":
            altura_menos__alto_femenino = calcular_minimo("altura", lista)
    return altura_menos__alto_femenino


# G. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género M
def mostrar_altura_promedio_masculino(lista: list):
    """mostrar la altura promedio de los masculinos

    Args:
        lista (list): contiene la informacion de los personajes
    """
    for heroes in lista:
        if heroes["genero"] == "M":
            altura_masculino_promedio = calcular_promedio(0, 0, "altura", lista)
    print(altura_masculino_promedio)


# H. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género F
def mostrar_altura_promedio_femenino(lista: list):
    """mostrar la altura promedio de los femenino

    Args:
        lista (list): contiene la informacion de los personajes
    """
    for heroes in lista:
        if heroes["genero"] == "M":
            altura_femenino_promedio = calcular_promedio(0, 0, "altura", lista)
    print(altura_femenino_promedio)

# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (ítems C a F)
def mostrar_nombres_C_a_F(lista: list):
    masculino_mas_alto = mostrar_masculino_mas_alto(lista)
    femenino_mas_alto = mostrar_femenino_mas_alto(lista)
    femenino_menos_alto = mostrar_femenino_menos_alto(lista)
    masculino_menos_alto= mostrar_masculino_menos_alto(lista)
    
    for heroe in lista:
        nombre = heroe["nombre"]
        for key, value in masculino_mas_alto.items():
            print(nombre, key, value)
    
mostrar_nombres_C_a_F(lista_personajes)

# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
def mostrar_tipos_de_ojos(lista: list):
    """mostrar lista con los distintos tipos de ojos

    Args:
        lista (list): contiene la informacion de los personajes

    Returns:
        _type_: retorna un diccionario con distinto colores de ojos
    """
    listar_tipos_ojos = crear_diccionario_por_clave("color_ojos", lista)
    return listar_tipos_ojos


# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo
def mostrar_tipos_de_pelo(lista: list):
    """mostrar lista con los distintos tipos de ojos

    Args:
        lista (list): contiene la informacion de los personajes

    Returns:
        _type_: retorna un diccionario con distinto colores de pelo
    """
    listar_tipos_pelo = crear_diccionario_por_clave("color_pelo", lista)
    return listar_tipos_pelo



# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
# no tener, Inicializarlo con ‘No Tiene’).
def mostrar_tipos_de_inteligencia(lista: list):
    """mostrar lista con los distintos tipos de inteligencia

    Args:
        lista (list): contiene la informacion de los personajes

    Returns:
        _type_: retorna un diccionario con distinto tipos de inteligencia
    """
    listar_tipos_inteligencia = crear_diccionario_por_clave("inteligencia", lista)
    return listar_tipos_inteligencia


# M. Listar todos los superhéroes agrupados por color de ojos.
def mostrar_superheroes_por_color_ojos(lista: list):
    """_summary_

    Args:
        lista (list): contiene la informacion de los personajes

    Returns:
        _type_: _description_
    """
    listado_heores = listar_diccionarios_por_clave(lista, "color_ojos", "nombre")
    return listado_heores

# N. Listar todos los superhéroes agrupados por color de pelo.
def mostrar_superheroes_por_color_pelo(lista: list):
    listado_heores = listar_diccionarios_por_clave(lista, "color_pelo", "nombre")
    return listado_heores

# O. Listar todos los superhéroes agrupados por tipo de inteligencia
def mostrar_superheroes_por_inteligencia(lista: list):
    listado_heores = listar_diccionarios_por_clave(lista, "inteligencia", "nombre")
    return listado_heores