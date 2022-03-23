#Receba um número inteiro. Calcule e mostre o seu fatorial.
'''
from time import sleep

print("{}FATORIAL NUMERO INTEIRO{}".format('-'*20, '-'*20))
n = int(input('Digite um numero: '))
contador = n

while contador>0:
  sleep(1)
  contador -= 1
  print('asfassa',contador)
'''
  #CONTINUAR
print("{}FATORIAL NUMERO INTEIRO{}".format('-'*20, '-'*20))  
s = 0
n = int(input('digite um numero: '))
for c in range(0, n):
  s = (s+c)*c*s
  print(s)