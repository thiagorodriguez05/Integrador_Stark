def calcular_maximo (key:float, lista: list)->float:
    """buscar maximo valor de la clave pasada

    Args:
        key (float): contiene alguna key numerica
        lista (list): contiene la informacion de los personajes

    Returns:
        _type_: retorna el maximo valor de la key pasada
    """
    flag_maximo = True

    for i in lista:
        value = float(i[key])
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

    for i in lista:
        value = float(i[key])
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
    
    for i in lista:
        acumulador += float(i[key])
        contador += 1
    
    promedio = float(acumulador / contador)
    return promedio


def crear_diccionario_por_clave(key_ingresada, lista: list):
    """ crear diccionario con alguna clave

    Args:
        key_ingresada (_type_): clave pasada 
        lista (list): contiene la informacion de los personajes

    Returns:
        _type_: retorna un diccionario con una clave distinta y la cantidad
    """
    diccionario_creado = {}
    
    for i in lista:
        clave = i[key_ingresada].capitalize()
        if clave in diccionario_creado:
            diccionario_creado[clave] += 1
        else:
            diccionario_creado[clave] = 1
    for key, value in diccionario_creado.items():
        if key:
            print("{}: {}".format(key, value))
        else:
            print("sin", key_ingresada.replace("_", " "),"{} {}".format(key, value))
    return diccionario_creado


def listar_diccionarios_por_clave(lista: list, key_ingresada, listar_por_clave):
    """_summary_

    Args:
        lista (list): contiene la informacion de los personajes
        key_ingresada (_type_): clave pasada por el diccionario
        listar_por_clave (_type_): clave que se va a mostrar en cada diccionario

    Returns:
        _type_: retorna una lista mostrando una clave para cada diccionario 
    """
    diccionario = crear_diccionario_por_clave(key_ingresada, lista)
        
    for key, value in diccionario.items():
        listar = []
        for heroe in lista:
            if heroe[key_ingresada] == key:
                listar.append(heroe[listar_por_clave])
                key_seteada = key_ingresada.replace("_", " ")
        print("\n")
        print(f"{key_seteada}: {key} \n cantidad: {value}")
        print(f"Superhéroes: {', '.join(listar)}")
        print("--------------------------------------------------------")
    return listar