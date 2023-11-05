#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 19:58:07 2022

@author: anahi
"""
# https://pygad.readthedocs.io/en/latest/
# pip install pygad
# https://pygad.readthedocs.io/en/latest/README_pygad_ReadTheDocs.html#pygad-ga-class

############## LIBRERIAS ##############

# Libreria para los algortimos geneticos
import pygad
# Manipulación de datos numericos
import numpy
#######################################


############## Problema ##############
# Estas son la varibles de entrada 
# Tendremos que ir multiplicando estos numeros con el objetivo de acercarnos a "desired_output"
# miralo como una ecución == 0.4X + 1B + 0C + 7D + 8E = "desired_output"
inputs = [0.4,1,0,7,8]

# Esta es la respuesta al que queremos aproximarnos
desired_output = 32
#######################################

############### Fitness ###############
# Hay dos formas principales para hacer nuestra función Fitness

# - Minimizar: con este enfoque mientras menor sea nuestro Fitness mejor sera nuestra solución
# Para este enfoque solo necesitamos calcular la diferencia entre  nuestra solocuión y el valor esperado.

# - Maximizar: con este enfoque mientras mayor sea nuestro Fitness mejor sera nuestra solución
# Para este enfoque solo necesitamos hacer la inversa  del enfoque de minimizar (x⁻¹)
# IMPORTANTE si usas este enfoque tenemos que evitar que se haga una división entre 0 pues dara infito
# para esto sumamos un pequeño numero que evite una solución "perfecta"

# Aqui usamos el enfoque de maximizar
def fitness_func(solution, solution_idx):
    # multiplicamos nuestra solución por nuestro input
    output = numpy.sum(solution*inputs)
    
    # caculamos la inversa de nuestra diferencia entre nuestra solución y el valor esperado.
    # y sumamos un muy pequeño numero (una millonesima)
    # por tanto el valor maximo que pueda dar "fitness" es 1/0.000001==1000000
    fitness = 1.0 / (numpy.abs(output - desired_output) + 0.000001)
    
    return fitness
#######################################

############## Población ##############
ga_instance = pygad.GA(num_generations=100,# Numero de generaciones
                       sol_per_pop=10,# Cantidad de respuestas por generación
                       num_genes=len(inputs),# Numero de genes (varibles de nuestra ecuacion solución)
                       num_parents_mating=2,# Número de padres
                       fitness_func=fitness_func, #Nuestra Función fitness
                       mutation_type="random", # Nuestro tipo de mutación
                       mutation_probability=0.6, # nuestro porcentaje de mutación
                       save_solutions = True) # Guardamos las mejores respuestas
#######################################

############## Graficos ##############
ga_instance.run()
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

# Movimientode nuestro fitness
ga_instance.plot_fitness()

# movimiento de los genes
ga_instance.plot_genes()

# canidad de nuevas posibles soluciones
ga_instance.plot_new_solution_rate()
ga_instance.plot_result
#######################################
