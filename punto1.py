# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mzLG-vl6AI_GVf-wWPV-mAgnJO0yXZI0
"""

def obtenerLetra(numeroDNI):
	letras="TRWAGMYFPDXBNJZSQVHLCKEO"
	resto=int(dni/23)
	resto*=23
	resto=dni-resto;
	return letras[resto]
numeroDNI=int(input("Ingrese el número del DNI:" ))
print('La letra del DNI %s es: %s' % (numeroDNI,obtenerLetra(numeroDNI)))