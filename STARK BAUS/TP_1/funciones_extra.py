def calcular_maximo (key:float, lista: list)->float:
    """buscar maximo valor de la clave pasada

    Args:
        key (float): contiene alguna key numerica
        lista (list): contiene la informacion de los personajes

    Returns:
        _type_: retorna el maximo valor de la key pasada
    """
    flag_maximo = True

    for heroe in lista:
        value = float(heroe[key])
        if flag_maximo == True or (value > valor_maximo):
            valor_maximo = value
            flag_maximo = False
        
    
    return valor_maximo

#---------------------------------------------------------------------

def calcular_minimo (key:float, lista: list)->float:
    """buscar minimo valor de la clave pasada

    Args:
        clave (float): contiene alguna key numerica
        lista (list): contiene la informacion de los personajes

    Returns:
        _type_: retorna el minimo valor de la key pasada
    """
    flag_minimo = True

    for heroe in lista:
        value = float(heroe[key])
        if flag_minimo == True or (value < valor_minimo):
            valor_minimo = value
            flag_minimo = False
        
    
    return valor_minimo

#---------------------------------------------------------------------

def calcular_promedio(acumulador: int, contador: int, key: float, lista: list) -> float:
    """_summary_

    Args:
        acumulador (int): acumula los valores ingresados por la clave
        contador (int): cuenta cuanttos personajes cumplen cierta clave o condicion
        key (float): clave pasada
        lista (list): contiene la informacion de los personajes

    Returns:
        float: retorna un valor promediado 
    """

    acumulador
    contador
    
    for heroe in lista:
        acumulador += float(heroe[key])
        contador += 1
    
    promedio = float(acumulador / contador)
    return promedio





