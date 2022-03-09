#Calcule e mostre o quadrado dos números entre 10 e 150.
from os import sep


print("{}QUADRADO DOS NÚMEROS SEQUENCIAIS{}".format('-'*20, '-'*20))

print('O quadrados dos numeros entre 10 e 150 é:')
for n in range(10, 150):
  print((int((n*n)/n)),n*n)


#tentar separar os numeros com string