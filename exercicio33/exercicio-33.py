#Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.
from unittest import result


print("{}SOMA DAS PARTES{}".format('-'*20, '-'*20))  
n = float(input('digite um numero: '))
c = 1
while c<=(n-1):
  c+=1
  resultado = 1/c
  print('1/',c)
  if c+1<=n:
    resultado += (1/(c+1))
    print(resultado)