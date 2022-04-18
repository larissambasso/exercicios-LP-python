#Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles.
print("{}NUMEROS PRIMOS{}".format('-'*20, '-'*20))
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

divisivel = 0

if n2>n1:
  for c in range (n1+1, n2):
    if c%2==0 and c!=2 or c%3==0 and c!=3 or c%5==0 and c!=5 or c%7==0 and c!=7:
      divisivel += 1 #nao estou usando
    else:
      print(c)

  

if n1>n2:
  for c in range (n1-1, n2, -1):
    if c%2==0 and c!=2 or c%3==0 and c!=3 or c%5==0 and c!=5 or c%7==0 and c!=7:
      divisivel += 1
    else:
      print(c)

if n1==n2:
  print('os numeros sao iguais, nao existe nenhum numero entre eles!')


#codigo funciona mas da forma mais longa, tentar fazer com a variavel "divisivel";