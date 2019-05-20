# -*- coding: utf-8 -*-
"""punto43

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E5LHW-p5l3H_GxN0nqdiyDFeUGY5j7ih
"""

def plan(nota):
    if nota < 3:
        return 'Reprobo'
    else:
        return 'Aprobo'

def sexto_semestre(notas):

    return {materia.upper():plan(nota) for materia, nota in notas.items() if nota >= 3}

print(sexto_semestre({'Ingeniería de Sistemas':4.2, 'Sistemas de Comunicación':1, 'Modelamiento de Sistemas':3.4, 'Sistemas distribuidos':3, 'Democracia y Paz':2, 'Electiva Profesional I':4}))