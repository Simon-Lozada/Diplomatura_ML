#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 03:03:36 2021

@author: anahi
"""
# EL 11.15 PESO ESPECÍFICO (Unidades de g/cm3)
# barras de base 1 cm2 y largo 'l'
# R peso específico -> hay qu estimar
# se pesan las barras con una balanza con errores (pequeños pero desconocidos)
# barra largo 'm' -> volumen m cm3 y peso = R*m
# Peso = R * m, Peso se mide con errores,m se concoe

import requests
import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

def coef_corr(x, y):
    '''Dados, dos np.arrays 'x' e 'y', calcula el coeficiente de correlación
    para un ajuste lineal calculado por mínimos cuadrados. Es el coefifiente de
    correlación de Pearson, que indica que tan buena es la relación lineal entre
    dos variables, siendo 1 ó -1 correlación perfecta y 0 nula correlación'''
    arriba = sum(((x - x.mean())*(y-y.mean()))) 
    abajo = sum(((x-x.mean())**2)) * sum(((y -y.mean())**2))
    corr = arriba / np.sqrt(abajo)
    
    return corr
    
enlace = 'https://raw.githubusercontent.com/python-unsam/Programacion_en_Python_UNSAM/master/Notas/11_Recursion/longitudes_y_pesos.csv'
r = requests.get(enlace).content
data_lyp = pd.read_csv(io.StringIO(r.decode('utf-8')))
data_lyp.columns = ['longitud', 'peso']  # pd.dataframe
peso = data_lyp['peso']  # pd.serie
longitud = data_lyp['longitud'] # pd.serie

lyp = linear_model.LinearRegression(fit_intercept = False)
# poniendo doble corchete se vuelve a 'ver' como pd.DataFrame
lyp.fit(data_lyp[['longitud']], data_lyp['peso'])
R = float(lyp.coef_ ) # R = 7.202372690217998

errores = peso - (lyp.predict(data_lyp[['longitud']]))
ecm = (errores**2).mean()  # ecm = 0.9291181822605168

minlong = 0.    # límite inf para ver el ajuste
maxlong = 30.   # lím superior
grilla_longitud = np.linspace(start = minlong, stop = maxlong, num = 1000)
grilla_peso = grilla_longitud * R   # recta de ajuste x mínimos cuadrados
    
fig = plt.scatter(longitud, peso, c ='purple', marker = 'x') # x violetas
  # acomoda los elementos del gráfico
# Agrego la ecuación de la recta fiteada al título, valores redondeados con  
# 3 decim como cifra significativa, pues los precios estaban en miles de $
plt.title(f'Ajuste lineal: Peso vs. Longitud \n '
          f'Peso= {round(R, 3)} * Longitud \n'
          f'ECM = {round(ecm, 3)} | Coef de Correlación = '
          f'{round(coef_corr(longitud, peso), 3)}')
plt.plot(grilla_longitud, grilla_peso, c = 'magenta') # magenta p/ recta fitted
plt.xlabel('Longitud')
plt.ylabel('Peso')
plt.tight_layout() 
plt.show()

