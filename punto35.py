# -*- coding: utf-8 -*-
"""punto35

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E5LHW-p5l3H_GxN0nqdiyDFeUGY5j7ih
"""

choferes = []
continuar = "S"
while continuar == "S" :
  choferes.append(input("Ingrese el nombre del chofer: "))
  continuar = input("¿Desea continuar? S/N: ")
  
dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]  
km_diarios = []

for i in range (len(choferes)):
  sub_lista = []
  for j in range(len(dias)):
    km = int(input(f"Ingrese los kilometros recorridos por el trabajador {choferes[i]} el día {dias[j]}: "))
    sub_lista.append(km)
  km_diarios.append(sub_lista)

km_semanales = []
for i in range(len(choferes)):
  acum = 0
  for j in range(len(dias)):
    acum = acum + km_diarios[i][j]
  km_semanales.append(acum)


for i in range(len(choferes)):
    print("El chofer",choferes[i],"en el transcurso de la semana recorrió ",km_diarios[i])
    print("El chofer", choferes[i],"recorrio un total de",km_semanales[i],"kilometros por semana")

print("Las horas por cada trabajador trabajadas cada dia de la semana son: ",km_diarios)
print("Las horas semanales trabajadas por cada trabajador son: ",km_semanales)