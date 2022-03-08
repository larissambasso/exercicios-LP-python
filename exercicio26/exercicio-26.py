#Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.
print("{}MULTIPLOS{}".format('-'*20, '-'*20))
n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))

if n1>n2:
  if n1%n2==0:
    print('sim')
  else:
    print('nao')


elif n2>n1:
  if n2%n1==0:
    print('sim')
  else:
    print('nao')


else:
  print('os numeros sao iguais.fim do programa')
