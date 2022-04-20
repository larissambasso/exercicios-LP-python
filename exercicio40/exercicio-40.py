#Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles.
print("{}NUMEROS PRIMOS{}".format('-'*20, '-'*20))
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

maior = n1 if n1>n2 else n2 
menor = n1 if n1<n2 else n2
divisivel = 0

for c in range (menor, maior):
  for r in range(2,c-1):
    if c%r==0 and c>2 and c%2==0:
      resultado = 1
    else:
      print(c)
if n1==n2:
  print('os numeros sao iguais, nao existe nenhum numero entre eles!')


#codigo funciona mas da forma mais longa, tentar fazer com a variavel "divisivel";