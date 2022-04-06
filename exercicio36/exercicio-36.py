#Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!
print("{}FATORIAL DA SOMA DAS PARTES{}".format('-'*20, '-'*20))  
from cmath import pi, sqrt
import math
from unittest import result
n = int(input('Digite um numero: '))
msg = ''
resultado=1

for c in range(1, n+1):
  resultado = resultado*1*c

  if c == 1:
    msg = str(c) + '+ 1/1!'


  if c!=1:
    msg = ' + 1/' + str(c) + '!'
     

  if c==n+1:
    msg += ' = '
  print(msg, end='')

print(resultado)