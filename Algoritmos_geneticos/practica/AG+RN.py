#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 19:50:14 2022

@author: anahi

KerasGA https://pypi.org/project/KerasGA/
Fuente: https://anderfernandez.com/blog/algoritmo-genetico-en-python/#C%C3%B3mo-usar-un-algoritmo-gen%C3%A9tico-en-Python-con-PyGAD
AG en 5 minutos: https://www.youtube.com/watch?v=RBrXGyo0kIw&list=RDLV_ZxrvAi0Mk0&index=7
Colab: http://fcaglp.unlp.edu.ar/~gbaume/grupo/Publicaciones/Apuntes/GoogleColab.pdf
"""

import warnings
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Input
from keras.losses import BinaryCrossentropy
from pygad import kerasga
from pygad import GA
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

warnings.simplefilter('ignore')

#%%    cargar dataset de cáncer de mama

diabetes = load_breast_cancer(as_frame = True)
data = diabetes['data']
target = diabetes['target']
print(data.head())
print(f'Shape data: {data.shape}')
print(f'Shape target: {target.shape}')
#%%  separar dataset en train/test dejando el valor default de 25% para test

#seed = 15
x_train, x_test, y_train, y_test = train_test_split(data, target)

#%%   construir una red neuronal sencilla: capa de entrada, capa oculta 
#     c/8 neuronas - act Relu y capa de salida c/1 neurona - act sigmoidea

model = Sequential()
model.add(Input(x_train.shape[1]))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

#%% acá aparece la magia: integración entre red y AG!!! by Keras :)

keras_ga = kerasga.KerasGA(model = model, num_solutions = 15)

#%%   para optimizar los parámetros, creamos el AG: primero definir FITNESS

def fitness_func(solution, solution_idx ):
  global model

  # Get the weights from the model
  weights = kerasga.model_weights_as_matrix(model= model,
                                            weights_vector= solution)
  
  # Set the weights
  model.set_weights(weights = weights)

  # Make the prediction
  prediction = model.predict(x_train)

  # Calculate fitness
  entropy = BinaryCrossentropy()(y_train, prediction)
  fitness = 1/(entropy.numpy() + 0.0001)

  return fitness

#%%    agregamos un 'callback' para observar cómo va aprendiendo la red neuronal

fitness_evol = []

def callback_generation(ga_instance):
  global fitness_evol
  fitness_evol.append(ga_instance.best_solution()[1])
  generation = ga_instance.generations_completed
  
  if generation % 2 == 0:
    print(f"Generation {generation}. Fitness: {ga_instance.best_solution()[1]}")

#%%   ya podemos entrenar la red usando las soluciones del AG

num_generations = 10
num_parents_mating = 5
initial_population = keras_ga.population_weights

ga_optimizer = GA(num_generations=num_generations, 
    num_parents_mating=num_parents_mating, 
    initial_population=initial_population,
    fitness_func=fitness_func, on_generation=callback_generation)

ga_optimizer.run()

#%%   para cómo fue aprendiendo el modelo, graficamos su evolución

sns.lineplot(x = range(len(fitness_evol)),
             y = fitness_evol)

#%%   ahora pedimos a la RN q prediga sobre datos nuevos (usamos el cjto de test)
#     y vemos cómo le va

pred = model.predict(x_test)

#print(y_test)
#print(pred)

cm = confusion_matrix(y_test, pred)
ConfusionMatrixDisplay(cm).plot()
