#Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles.
print("{}NUMEROS PRIMOS{}".format('-'*20, '-'*20))
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n2>n1:
  for c in range (n1+1, n2):
    if c%2!=0 and c%1==0 and c%c==0:
      print(c)

if n1>n2:
  for c in range (n1-1, n2, -1):
    if c%2!=0:
      print(c)

if n1==n2:
  print('os numeros sao iguais, nao existe nenhum numero entre eles!')





#CONTINUAR