# -*- coding: utf-8 -*-
"""punto47

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E5LHW-p5l3H_GxN0nqdiyDFeUGY5j7ih
"""

factura = {}
recaudado = 0
pendiente = 0
opcion = ''
while opcion != 'T':
    if opcion == 'A':
        key = input('Ingrese el número de la factura: ')
        costo = float(input('Ingrese el costo de la factura: '))
        factura[key] = costo
        pendiente += costo
    if opcion == 'P':
        key = input('Ingrese el número de la factura a pagar: ')
        costo = factura.pop(key, 0)
        recaudado += costo
        pendiente -= costo
    print('Recaudado:', recaudado)
    print('Pendiente de cobro: ', pendiente)
    opcion = input('¿Quieres añadir una nueva factura A, pagarla P o terminar T? ')