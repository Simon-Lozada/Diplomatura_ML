#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 12:28:27 2022

@author: monky
"""
import random
import matplotlib.pyplot as plt 

import numpy as np

# EJERCICIO 5.10 CREAR ALBUM
def crear_album(figus_total):
    album = np.zeros(figus_total)
    
    return album

# EJERCICIO 5.11 INCOMPLETO O NO?
def album_incompleto(A):
    
    esta_incompleto = False
    if 0 in A:     
        esta_incompleto = True
      
    return esta_incompleto

# EJERCICIO 5.12 COMPRAR FIGUS
def comprar_figu(figus_total):
    num = random.randint(1,figus_total)
    
    return num

#  EJERCICIO 5.13 CANTIDAD DE COMPRAS
def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    
    compras = 0
    
    while album_incompleto(album) == True:
        figu_comprada = comprar_figu(figus_total)
        compras = compras + 1
        album[figu_comprada - 1] += 1    
     
    return compras

# EJERCICIO 5.14 CUÁNTAS FIGUS HAY QUE COMPRAR PARA LLENAR UN ALBUM DE 6 FIGUS?
n_repeticiones = 1000
compra_toal = []
for i in range(n_repeticiones):
    compras = cuantas_figus(6)
    compra_toal.append(compras)

print("media de figuritas a comprar para un album de 6: --->",np.mean(compras))    

# EJERCICIO 5.15 
def experimento_figus(n_repeticiones, figus_total):
    compra_toal = []
    for i in range(n_repeticiones):
        compras = cuantas_figus(6)
        compra_toal.append(compras)

    return np.mean(compras)
 
# EJERCICIO 5.16
pack = []
for i in range(5):
    figus = comprar_figu(670)
    pack.append(figus)
print(pack)

   
# EJERCICIO 5.17
def comprar_paquete(figus_total, figus_paquete):
    pack = []
    for i in range(figus_paquete):
        figus = comprar_figu(figus_total)
        pack.append(figus)
    
    return pack


# EJERCICIO 5.18
def cuantos_paquetes(figus_total, figus_paquete):
    album=crear_album(figus_total)
    compras_pack = 0
    while album_incompleto(album) == True:
        pack_comprado = comprar_paquete(figus_total, figus_paquete)
        compras_pack = compras_pack + 1
        for figu in pack_comprado:
            album[figu - 1] += 1    
     
    return compras_pack
    

# EJERCICIO 5.19
n_repeticiones = 1000
compra_total = []
for i in range(n_repeticiones):
    i = i+1
    compra_toal_pack = cuantos_paquetes(670, 5)
    compra_total.append(compra_toal_pack)

print("media de paquetes a comprar para un album de 670: --->",np.mean(compra_toal_pack))

# EJERCICIO 5.20
count = 0
for i in compra_total:
    if i <= 850:
        count = count + 1
    else:
        continue
print("probabilidad de completar el album comprando menos de 850 paquetes",count/n_repeticiones)
    
# EJERCICIO 5.21
paquetes = compra_total
plt.figure()
plt.hist(paquetes, bins = 50, color = 'magenta')
plt.xlabel('Paquetes de Figuritas ')
plt.ylabel('Cantidad de sucesos')
plt.title('Distribución de paquetes para llenar el Álbum (n = 1000 sucesos)', loc = 'center')
plt.show()
plt.close()
# EJERCICIO 5.22
prob_90 = np.percentile(compra_total, 90)
print("para tener un 90% de probabilidad se nesesitan comprar --->",prob_90, "paquetes")
# EJERCICIO 5.23

compras = 0
album = crear_album(670)
figus = [i+1 for i in range(670)]

while album_incompleto(album) == True:
    figus_compradas = random.sample(figus, k = 5)      
    
    compras = compras + 1
    for figu in figus_compradas:
        album[figu -1] += 1
print("media de paquetes a comprar para un album de 670(sin repetir): --->",np.mean(compras))

def crear_album_cinco(figus_total):
    
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

'''
RESULTADO OBTENIDO
En el caso en que cinco amigos cooperen para llenar el album de 670 figus:
Haciendo 100 repeticiones, para llenar un album de 670 figus, 
hay que comprar un promedio de 403 de paquetes de figuritas X PERSONA     
'''
paquetes = [cooperacion_cinco(670, 5) for i in range(n_repeticiones)] 
compras = np.array(paquetes)
promedio_compras_persona = np.mean(compras)/5

print(promedio_compras_persona)
    
    
    
    
    