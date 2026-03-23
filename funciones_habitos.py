# repo-colaborativo-reflexlab


# --------------------------MIRANDA-----------------------------------------

def registrar_habitos():
    """
    registra los habitos diarios de una persona
    Parameters
    ---------
    
    return
    --------
    lista
    Una lista con las actividades diarias de el usuario
    """
    lista_habitos=[]
    actividad=int(input("ingrese la activdad que usted realizo hoy en el dia, para temrinar ingrese stop: "))
    while actividad=="stop":
        break
    lista_habitos.append(actividad)
    return(lista_habitos)

#-----------------------MATILDE--------------------------------------------

def analizar_habitos(lista):
    """
    La funcion recibe una lista de actividades y devuelve un diccionario con la cantidad de veces que aparece cada una. 
    
    Parameters
    ----------
    lista : lista de actividades
    
    Returns 
    -------
    diccionario : diccionario en donde las claves son las actividades y el valor es la cantidad de veces que aparecen. 

    """
    diccionario={}
    
    for i in lista:
        if i not in diccionario:
            diccionario[i]=1
            
        else:
            diccionario[i]+=1
    return diccionario
    
