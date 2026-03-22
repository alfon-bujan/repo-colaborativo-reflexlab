# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:39:42 2026

@author: Invitade
"""

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

    
    
    
    