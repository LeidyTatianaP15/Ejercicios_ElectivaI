# -*- coding: utf-8 -*-
"""punto49

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E5LHW-p5l3H_GxN0nqdiyDFeUGY5j7ih
"""

nuevo_diccionario = {}
palabras = input("Ingrese la lista de palabras y traducciones en formato español:ingles separadas por comas: ")
for i in palabras.split(','):
    key, value = i.split(':')
    nuevo_diccionario[key] = value
frase = input('Ingrese una frase en español: ')
for i in frase.split():
    if i in nuevo_diccionario:
        print(nuevo_diccionario[i], end=' ')
    else:
        print(i, end=' ')