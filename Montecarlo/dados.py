#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 19:15:17 2022

@author: monky / https://towardsdatascience.com/how-to-create-a-monte-carlo-simulation-using-python-c24634a0978a
"""

"""
El juego consiste en sacar el mismo numero en dos dados de 6 caras al lazarlos.
Si el jugador gana obtine 4 veces lo apostado, si pierde le quitan lo apostado

6 caras * 6 caras = 36 caras 
- 30 combinaciones de caras perdedoras 
- 6 gandoras

En este caso el jugador va a intetarlo 1000 veces, apostando 1$
- si gana las 1000 tiradas = 1000$ apostado + 4000$ ganado = 5000$
- si pierde las 1000 tiradas = 0$
"""
# Importing Packages
import matplotlib.pyplot as plt
import random

# Funcion para lanzar los dados
def roll_dice():
    # Numero aleatorio entre 1 y 6 = Cara del primer dado
    die_1 = random.randint(1, 6)
    # Numero aleatorio entre 1 y 6 = Cara del segundo dado 
    die_2 = random.randint(1, 6)

    # Revisar si son iguales o no
    if die_1 == die_2:
        same_num = True
    else:
        same_num = False
    return same_num

# Inputs
# Numero de similaciones
num_simulations = 1000
# Numero de tiradas
max_num_rolls = 1000
# Dinero apostado 
bet = 1

# Tracking
#Probabilidad de tirada
win_probability = []
#Balance toltal
end_balance = []


# Creamos la figura = lienzo
fig = plt.figure()

# Le damos como titulo "Montecarlo juego del dado 1000 simulaciones"
plt.title("Montecarlo juego del dado [" + str(num_simulations) + " simulaciones]")

# Nombramos al eje de las "x" como ""
plt.xlabel("Numero de tiradas")

# Nombramos al eje de las "y" como ""
plt.ylabel("Dinero [$]")

# Especificamos el limite en el eje de las "x"
# El limite es igual a la cantidad de veces que lanzamos el dado
plt.xlim([0, max_num_rolls])


# Hacemos un bucle de por el numero de simulaciones
for i in range(num_simulations):
    # Configuramos nuestro cuenta/balance actual
    balance = [1000]
    # configuramos el numero de tiradas
    num_rolls = [0]
    # Guardamos el nuemro actual de tiradas ganadas 
    num_wins = 0
    # Tiramos los dados hasta que llegamos al maximo de tiradas
    while num_rolls[-1] < max_num_rolls:
        same = roll_dice()        # Revisamos si los dos dados son iguales
        # Si, si son iguales
        if same:
            # Guardamos en nuestra cuenta/balance lo apostado + lo ganado
            balance.append(balance[-1] + 4 * bet)
            # Sumamos uno al numero de tiradas ganadas
            num_wins += 1
        # Si los dados no son iguales restamos de nuestra cuenta/balance lo apostado
        else:
            balance.append(balance[-1] - bet)
        # Añadimos uno al numero de tiradas
        num_rolls.append(num_rolls[-1] + 1)
    #Guardamos la probabilidad de victoria
    win_probability.append(num_wins/num_rolls[-1])
    # Guardamos el estado final de la cuenta/balance
    end_balance.append(balance[-1])
    # Lo graficamos
    plt.plot(num_rolls, balance)
    

# Mostramos el grafico con el seguimiento de todas las simulaciones
plt.show()

# Averaging win probability and end balance
overall_win_probability = sum(win_probability)/len(win_probability)

overall_end_balance = sum(end_balance)/len(end_balance)# Displaying the averages

print("Average win probability after " + str(num_simulations) + " runs: " + str(overall_win_probability))

print("Average ending balance after " + str(num_simulations) + " runs: $" + str(overall_end_balance))