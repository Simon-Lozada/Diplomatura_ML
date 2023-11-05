# -*- coding: utf-8 -*-
"""
ALGORITMOS GENÉTICOS
MAXIMIZAR UNA FUNCIÓN NO LINEAL... 'DIFÍCIL' ;) 
"""

#importo las bibliotecas necesarias
import matplotlib.pyplot as plt
import numpy as np
import math

#%%   DEFINIMOS LA FUNCIÓN A MAXIMIZAR
# Lo que queremos es encontrar el valor "x" que da el pico mas alto en nuestro eje "y"
def fx(x):
    # Esta es la formular del siguiente grafico.
    # Como vemos la unica varible es "x" la que queremos encontrar
    
    # usamos pi para usar la tendencia y coseno para crear las ondas
    return -(0.1+(1-x)**2-0.1*math.cos(6*math.pi*(1-x)))+2

y_axis = []
x_axis=np.arange(0,2,0.02)

# Vamos asignando el eje y con base a el eje x segun la formula 
for num in x_axis:
    y_axis.append(fx(num))
    
plt.plot(x_axis,y_axis)
plt.show()

#%%

#individuo de ejemplo 
x = 0.54
y = fx(x)

plt.plot(x_axis,y_axis)
plt.plot(x,y,'x')
plt.show()

#%% ELEGIMOS CÓMO REPRESENTAR NUESTROS INDIVIDUOS(decimales), COMO LISTAS

# en este caso la lista "z" seria 0.54
z = [0,5,4]

#esta función convertira la lista en un numero decimal
def listToDecimal(num):
    decimal=0
    for i in range(len(num)):
        decimal+=num[i]*10**(-i)
    return decimal

print(listToDecimal(z))
#%%   ELEGIMOS EL TAMAÑO DE LOS INDIVIDUOS, DEL DOMINIO DE LA FN
# VAN DE 0. A 1.99999999999
ind_size = 15

#Genetic pool
# la primera lista sera nuestro posible numero entero, la segunda sera los posibles numeros decimales
# nuestro posibles genes van en los enteros de 0 a 1 solamente
# porque como vimos en el grafico el eje x maximo es 2, y por tantanto 2.99 no se puede
genetic_pool=[[0,1],[0,1,2,3,4,5,6,7,8,9]]

# Creamos nuestro individuo usando los posibles genes de nuestro Genetic pool
individuo = []
individuo += [np.random.choice(genetic_pool[0])]
individuo += list(np.random.choice(genetic_pool[1],ind_size-1))

print(individuo)
#%%
print(listToDecimal(individuo))
#%%  DEFINIMOS LA POBLACIÓN INICIAL DE 100 INDIVIDUOS

def gen_poblacion(cantidad_individuos):
    poblacion = []
    
    for i in range(100):# cantidad de población
        
        # Creamos nuestro individuo usando los posibles genes de nuestro Genetic pool
        individuo = []
        individuo += [np.random.choice(genetic_pool[0])]
        individuo += list(np.random.choice(genetic_pool[1],ind_size-1))
        
        # añadimos nuestro individuao a la población
        poblacion.append(individuo)
    return poblacion # retornamos nuestra población
  
cantidad_individuos = 100
poblacion = gen_poblacion(100)
print(poblacion[:10])

#%% LA GRAFICAMOS...

# graficamos nuestra población a lo largo de nuestra función
def graficar(poblacion):
    for individuo in poblacion:
        x = listToDecimal(individuo)
        y = fx(x)
        plt.plot(x,y,'x')
    plt.plot(x_axis,y_axis)
    plt.show()

graficar(poblacion)
#%%    DEFINIR EL FITNESS

def fitness(poblacion):
    ''' Definimos la función fitness para la población'''
    fitness =[]
    # extraigo los valores de y para medir su éxito
    for individuo in poblacion:
        # convertimos nuestro individuo(lista) a un decimal 
        x = listToDecimal(individuo)
        
        # buscamos cul seria el valor "y" para nuestro decimal "x"
        y = fx(x)
        
        # Guardamos el fitness en una lista
        fitness += [y]
    #convierto fitness en un vector de numpy para aprovechar las operaciones
    fitness = np.array(fitness)
    #divido todos los valores de 'y' para la suma total y así obtener valores entre 0 y 1
    fitness=fitness/fitness.sum()
    
    return fitness

fit = fitness(poblacion)
print(fit)

#%%  EJEMPLO DE FITNESS CON SÓLO 2 INDIVIDUOS
array = np.array([8,5])
array = array/array.sum()
print(array)

#%%  DEFINO LA OPERACIÓN DE CRIANZA X CROSSPOINT

def reproduction(poblacion, ind_size, fitness):
    size_poblacion = len(poblacion)
    #hijos
    offspring = []
    for i in range(size_poblacion//2):
        parents = np.random.choice(size_poblacion, 2, p=fitness)
        cross_point = np.random.randint(ind_size)
        offspring += [poblacion[parents[0]][:cross_point] + poblacion[parents[1]][cross_point:]]
        offspring += [poblacion[parents[1]][:cross_point] + poblacion[parents[0]][cross_point:]]
    
    return offspring

next_gen = reproduction(poblacion, ind_size, fit)
print(next_gen[:10])

#%%  VEMOS A LA SGTE GENERACIÓN
poblacion = next_gen
graficar(poblacion)

#%%   DEFINIMOS LA OPERACIÓN DE MUTACIÓN CON UNA PROBABILIDAD MUY BAJA

def mutate(individuals, prob, pool):
    for i in range(len(individuals)):
        mutate_individual=individuals[i]
        if np.random.random() < prob:
            mutation = np.random.choice(pool[0])
            mutate_individual = [mutation] + mutate_individual[1:]
        
        for j in range(1,len(mutate_individual)):
            if np.random.random() < prob:
                mutation = np.random.choice(pool[1])
                mutate_individual = mutate_individual[0:j] + [mutation] + mutate_individual[j+1:]
        individuals[i] = mutate_individual
        
    return individuals
        
pob = mutate(poblacion,0.001,genetic_pool)
print(pob[:10])

#%% GRAFICAMOS LA POBLACIÓN MUTADA (NO SE NOTA MUCHO QUE DIGAMOS)

graficar(pob)

#%%  AHORA JUNTAMOS TODO Y HACEMOS EVOLUCIONAR A LA POBLACIÓN DURANTE UNA 
#    CANTIDAD DE GENERACIONES
generaciones = 100

def evolucionar(poblacion, generaciones):
    ''' Hace evolucionar una población durante una cantidad de generaciones'''
    
    for _ in range(generaciones):
        fit = fitness(poblacion)
        # REPRODUCCIÓN
        offspring = reproduction(poblacion, ind_size, fit)           
        # MUTACIONES                
        poblacion = mutate(offspring,0.005,genetic_pool)
    
    return poblacion

#%%  VEMOS CÓMO EVOLUCIONÓ LA POBLACIÓN

graficar(evolucionar(poblacion, generaciones)) 

#%%  UBICAMOS EL MÁXIMO

print(np.where(fit == fit.max()))
maxi  = fit.argmax()
print(maxi)
#%%
print(listToDecimal(poblacion[maxi]))
#%%
print(fx(listToDecimal(poblacion[maxi])))
#%%   AHORA LO DEJO EVOLUCIONAR MÁS GENERACIONES

generaciones = 500
cantidad_individuos = 100
poblacion = gen_poblacion(cantidad_individuos)
solucion = evolucionar(poblacion, generaciones)
graficar(solucion)

print('x_max', listToDecimal(solucion[fit.argmax()]))
print('f(x_max) = ', fx(listToDecimal(solucion[fit.argmax()])))

