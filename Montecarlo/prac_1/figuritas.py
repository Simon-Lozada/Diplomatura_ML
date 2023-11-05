#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 07:38:24 2021

@author: anahi
"""
#  EJERCICIO EL ALBUM DE FIGURITAS

'''
EL ALBUM CONTIENE 640 FIGUS.
CADA FIGU TIENE LA MISMA PROBABILIDAD DE SALIR
CADA PAQUETE TRAE 5 FIGUS
'''
import random
import numpy as np
import matplotlib.pyplot as plt



# EJERCICIO 5.10 CREAR ALBUM

def crear_album(figus_total):
    '''     
    Creo el album de figuritas
    Crea un np array del tamaño del album lleno de ceros 
    '''
    album = np.zeros(figus_total)
    
    return album

# EJERCICIO 5.11 INCOMPLETO O NO?
    
def album_incompleto(A): 
    '''
     Mira si el album está incompleto.
     Si hay ceros en A, dará True
     '''
    esta_incompleto = False
    if 0 in A:     
        esta_incompleto = True
      
    return esta_incompleto

# EJERCICIO 5.12 COMPRAR FIGUS
    
def comprar_figu(figus_total):
    '''
    Compro figuritas de a 1.
    Para eso, genero un número entero (seudo) aleatorio de entre los 670 posibles.    
    '''
    figu_comprada = random.randint(1, figus_total)
     
    return figu_comprada
        
# EJERCICIO 5.13 CANTIDAD DE COMPRAS

def cuantas_figus(figus_total):
    '''
    Dado el tamaño del álbum (figus_total), genere un álbum nuevo, simule su 
    llenado y devuelva la cantidad de figuritas que se debieron comprar para 
    completarlo.
    '''
    compras = 0
    album = crear_album(figus_total)
    
    while album_incompleto(album) == True:
        figu_comprada = comprar_figu(figus_total)
        compras += 1
        album[figu_comprada - 1] += 1    
     
    return compras
    
# EJERCICIO 5.14 CUÁNTAS FIGUS HAY QUE COMPRAR PARA LLENAR UN ALBUM DE 6 FIGUS?
'''
print(f'Haciendo 1000 repeticiones, para llenar un album de 6 figus, hay que 
comprar un promedio de {round(album_de_seis())} figuritas')
Da que hay que comprar 15 figus, o sea, 2.5 veces el tamaño del album    
'''

# EJERCICIO 5.15 

def experimento_figus(n_repeticiones, figus_total):
    '''
    Va comprando figuritas y poniéndolas en el álbum que tiene lugar para 
    figus_total . Mientras el álbum esté incompleto, el proceso se repite.
    La cantidad de compras hasta que se completa el álbum se guarda en una lista, 
    esto se repite n_repeticiones. Sobre esa lista de n_repeticiones elementos se 
    calcula el promedio y ese valor es el que se retorna.
    '''
    cuantas_compras = [cuantas_figus(figus_total) for i in range(n_repeticiones)] 
    promedio_compras = np.mean(cuantas_compras)
    
    return promedio_compras
    
# EJERCICIO 5.16/17 paquete de figuritas
    
def comprar_paquete(figus_total, figus_paquete):
    '''
    Tomo una muestra de k figuritas (k es el tamaño del paquete) de la cantidad
    total de figuritas, que es figus, una lista con 670 elementos numerados.
    La muestra que tomo es CON REPOSICIÓN, porque pueden venir repetidas en el 
    mismo paquete.
    Por eso uso random.choices, en vez de random.sample
    K es 5, la cantidad de figus x paquete.
    '''
    figus = [i+1 for i in range(figus_total)]
    figus_compradas = random.choices(figus, k = figus_paquete)
    
    return figus_compradas
       
 # EJERCICIO 5.18 LLenar album con paquetes 

def cuantos_paquetes(figus_total, figus_paquete):
    '''
    Dado el tamaño del álbum (figus_total), genere un álbum nuevo, simule su 
    llenado y devuelva la cantidad de PAQUETES de figuritas que se debieron 
    comprar para completarlo.
    '''
    compras = 0
    album = crear_album(figus_total)
    
    while album_incompleto(album) == True:
        paquete_comprado = comprar_paquete(figus_total, figus_paquete)
        compras += 1
        for figu in paquete_comprado:
            album[figu -1] += 1    
     
    return compras
    
# EJERCICIO 5.19  CUÁNTOS PAQUETES DE 5 HAY QUE COMPRAR PARA LLENAR EL ALBUM DE 670 FIGUS?

def experimento_figus_670(n_repeticiones, figus_total, figus_paquete):
    '''
    RESULTADO OBTENIDO
    Haciendo 100 repeticiones, para llenar un album de 670 figus, 
    hay que comprar un promedio de 959 de paquetes de figuritas
    Haciendo 1000 repeticiones, para llenar un album de 670 figus, 
    hay que comprar un promedio de 954 de paquetes de figuritas
    '''
    paquetes = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)] 
    compras = np.array(paquetes)
    promedio_compras = np.mean(compras)
    
    return promedio_compras

# GRAFICAR CÓMO SE VA LLENANDO EL ALBUM
    
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()-1] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    
    return historia_figus_pegadas

def graficar_historia(figus_total, figus_paquete):
    '''
    Grafica cómo se va completando el álbum de figuritas.
    '''
    plt.figure()
    plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
    plt.xlabel("Cantidad de paquetes comprados.")
    plt.ylabel("Cantidad de figuritas pegadas.")
    plt.title("La curva de llenado se desacelera al final")
    plt.show()
    plt.close()
    
    return

# EJERCICIO 5.20 PROBABILIDAD DE COMPLETAR EL ALBUM CON 850 PAQUETES

def prob_completar_album(n_repeticiones, figus_total, figus_paquete, paq_lim):
    '''
    ESTIMA LA PROBABILIDAD DE COMPLETAR EL ALBUM CON HASTA UN NÚMERO LÍMITE DE PAQUETES
    DA ENTRE 20 Y 35%
    '''
    paquetes = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)] 
    n_paquetes_hasta_llenar = np.array(paquetes)
    np.save('../Data/paquetes.npy', n_paquetes_hasta_llenar)
    # SUMA LA CANTIDAD DE VECES QUE APARECEN NÚMEROS MENORES O = QUE EL PAQ_LIM PROPUESTO
    prob = (n_paquetes_hasta_llenar <= paq_lim).sum ()/n_repeticiones   
    prob_90 = np.percentile(n_paquetes_hasta_llenar, 90)   # calcula el percentil 90, o sea, la probabilidad del 90%
    
    
    return prob, prob_90
    
# EJERCICIO 5.21 PLOTEAR HISTOGRAMA DE LLENADO DE ALBUM

def plotear_paquetes_para_completar_album():
    '''
    Dibuja un histograma con la frecuencia en que aparece la cantidad de paquetes
    para completar el álbum de figuritas.
    '''
    paquetes = np.load('../Data/paquetes.npy')
    plt.figure()
    plt.hist(paquetes, bins = 50, color = 'magenta')
    plt.xlabel('Paquetes de Figuritas ')
    plt.ylabel('Cantidad de sucesos')
    plt.title('Distribución de paquetes para llenar el Álbum (n = 1000 sucesos)', loc = 'center')
    plt.savefig('../Data/paquetes.png', dpi = 300)
    plt.show()
    plt.close()
    
    return
     
# EJERCICIO 5.23 sUPONER QUE NO HAY FIGUS REPETIDAS EN LOS PAQUETES
    
def comprar_paquete_sin_repes(figus_total, figus_paquete):
    '''
    Tomo una muestra de k figuritas (k es el tamaño del paquete) de la cantidad
    total de figuritas, que es figus, una lista con 670 elementos numerados.
    La muestra que tomo es SIN REPOSICIÓN, para no tener figuritas repetidas en 
    los paquetes.
    Por eso uso random.sample
    K es 5, la cantidad de figus x paquete.
    '''
    figus = [i+1 for i in range(figus_total)]
    figus_compradas = random.sample(figus, k = figus_paquete)
    
    return figus_compradas

def cuantos_paquetes_sin_repes(figus_total, figus_paquete):
    '''
    Dado el tamaño del álbum (figus_total), genere un álbum nuevo, simule su 
    llenado y devuelva la cantidad de PAQUETES de figuritas que se debieron 
    comprar para completarlo.
    '''
    compras = 0
    album = crear_album(figus_total)
    
    while album_incompleto(album) == True:
        paquete_comprado = comprar_paquete_sin_repes(figus_total, figus_paquete)
        compras += 1
        for figu in paquete_comprado:
            album[figu -1] += 1    
     
    return compras
    
def experimento_figus_sin_repes(n_repeticiones, figus_total, figus_paquete):
    '''
    RESULTADO OBTENIDO
    Haciendo 100 repeticiones, para llenar un album de 670 figus, 
    hay que comprar un promedio de 959 de paquetes de figuritas
    Haciendo 1000 repeticiones, para llenar un album de 670 figus, 
    hay que comprar un promedio de 954 de paquetes de figuritas
    '''
    paquetes = [cuantos_paquetes_sin_repes(figus_total, figus_paquete) for i in range(n_repeticiones)] 
    promedio_paquetes = np.mean(paquetes)
    
    return promedio_paquetes

def prob_completar_album_sin_rep(n_repeticiones, figus_total, figus_paquete, paq_lim):
    '''
    ESTIMA LA PROBABILIDAD DE COMPLETAR EL ALBUM CON HASTA UN NÚMERO LÍMITE DE PAQUETES
    DA ENTRE 20 Y 35%
    '''
    paquetes = [cuantos_paquetes_sin_repes(figus_total, figus_paquete) for i in range(n_repeticiones)] 
    n_paquetes_hasta_llenar_sin_rep = np.array(paquetes)
    np.save('../Data/paquetes_sin_rep.npy', n_paquetes_hasta_llenar_sin_rep)
    # SUMA LA CANTIDAD DE VECES QUE APARECEN NÚMEROS MENORES O = QUE EL PAQ_LIM PROPUESTO
    prob = (n_paquetes_hasta_llenar_sin_rep <= paq_lim).sum ()/n_repeticiones   
    prob_90 = np.percentile(n_paquetes_hasta_llenar_sin_rep, 90)   # calcula el percentil 90, o sea, la probabilidad del 90%
    
    return prob, prob_90


# EJERCICIO 5.24 COOPERAR VS COMPETIR

def crear_album_cinco(figus_total):
    '''     
    Creo el album de figuritas para los cinco amigos
    Crea un np array del tamaño del album lleno de ceros 
    '''
    album_de_1 = [0 for i in range(figus_total)]
    album = np.array(album_de_1)
    
    return album

def album_incompleto_cinco(A): 
    '''
     Mira si el album está incompleto.
     Si todos los números no son mayores o iguales que 5, dará True
     '''
    esta_incompleto = False
    five_up = (A[A>=5])
    #print(len(A))
    #print(len(five_up))
    if not (len(five_up) == len(A)):     
        esta_incompleto = True
      
    return esta_incompleto


def cooperacion_cinco(figus_total, figus_paquete):
    '''
    Dado el tamaño del álbum (figus_total), genere un álbum nuevo, simule su 
    llenado y devuelva la cantidad de PAQUETES de figuritas que se debieron 
    comprar para completarlo.
    AHORA SON CINCO ALBUMES, PORQUE LOS 5 AMIGOS COOPERAN ENTRE SÍ
    '''
    compras = 0
    album = crear_album_cinco(figus_total)
    
    while album_incompleto_cinco(album) == True:
        paquete_comprado = comprar_paquete(figus_total, figus_paquete)
        compras += 1
        for figu in paquete_comprado:
            album[figu -1] += 1    
     
    return compras   

def experimento_cinco(n_repeticiones, figus_total, figus_paquete):
    '''
    RESULTADO OBTENIDO
    En el caso en que cinco amigos cooperen para llenar el album de 670 figus:
    Haciendo 100 repeticiones, para llenar un album de 670 figus, 
    hay que comprar un promedio de 403 de paquetes de figuritas X PERSONA
       
    '''
    paquetes = [cooperacion_cinco(figus_total, figus_paquete) for i in range(n_repeticiones)] 
    compras = np.array(paquetes)
    promedio_compras_persona = np.mean(compras)/5
    
    return promedio_compras_persona


if __name__ == "__main__": 
    
    n_repeticiones = 100
    figus_total = 670
    figus_paquete = 5
    paq_lim = 850
    
    promedio_cooperacion = experimento_cinco(n_repeticiones, figus_total, figus_paquete)
    print(f'En el caso en que cinco amigos cooperen para llenar el album de 670 figus:')
    print(f'Haciendo {n_repeticiones} repeticiones, para llenar un album de {figus_total} figus, ')
    print(f'hay que comprar un promedio de {round(promedio_cooperacion)} de paquetes de figuritas X PERSONA')
    
    
    promedio = experimento_figus_670(n_repeticiones, figus_total, figus_paquete)  
    prob_llenar_850 = prob_completar_album(n_repeticiones, figus_total, figus_paquete, paq_lim)[0]
    plotear_paquetes_para_completar_album()
    graficar_historia(figus_total, figus_paquete)
    
    print(f'Haciendo {n_repeticiones} repeticiones, para llenar un album de {figus_total} figus, ')
    print(f'hay que comprar un promedio de {round(promedio)} de paquetes de figuritas')
    print(f'La probabilidad de completar el album comprando hasta {paq_lim} paquetes de figus es de {round(100 * prob_llenar_850,2)}%')

    # EJERCICIO 5.22 ESTIMAR CUÁNTOS PAQUETES PARA TENER 90% DE PROBABILIDAD DE LLENAR EL ÁLBUM
    # Para tener 90% probabilidad de llenar el álbum hay que comprar 1164 paquetes
    prob_90 = prob_completar_album(n_repeticiones, figus_total, figus_paquete, paq_lim)[1]
    print(f'Para tener 90% probabilidad de llenar el álbum hay que comprar {round(prob_90)} paquetes')
        
    # EJERCICIO 5.23 SIN FIGUS REPETIDAS EN LOS PAQUETES
    # LAS PROBABILIDADES NO MEJORAN SIGNIFICATIVAMENTE
    ''' 
    Haciendo 100 repeticiones, para llenar un album de 670 figus SIN REPES,
    hay que comprar un promedio de 980 de paquetes de figuritas
    La probabilidad de completar el album comprando hasta 850 paquetes de figus SIN REPES es de 29.0%
    '''
    
    promedio_sin_repes = experimento_figus_sin_repes(n_repeticiones, figus_total, figus_paquete)
    prob_llenar_850_sin_rep = prob_completar_album_sin_rep(n_repeticiones, figus_total, figus_paquete, paq_lim)[0]
    
    print(f'Haciendo {n_repeticiones} repeticiones, para llenar un album de {figus_total} figus SIN REPES,')
    print(f'hay que comprar un promedio de {round(promedio_sin_repes)} de paquetes de figuritas')
    print(f'La probabilidad de completar el album comprando hasta {paq_lim} paquetes de figus SIN REPES es de {round(100 * prob_llenar_850_sin_rep,2)}%')
    