# -*- coding: utf-8 -*-
"""punto25

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E5LHW-p5l3H_GxN0nqdiyDFeUGY5j7ih
"""

def LeyAckerman(m,n):
  if(m==0):
    return n+1
  elif(n==0):
    return LeyAckerman(m-1,1)
  else:
    return LeyAckerman(m-1,LeyAckerman(m,n-1))
  
m=int(input("Ingrese el primer valor: "))
n=int(input("Ingrese el segundo valor: "))
print("El valor Ackerman es : "+ str(LeyAckerman(m,n)))