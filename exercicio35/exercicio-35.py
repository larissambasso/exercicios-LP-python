#Receba 2 números inteiros, verifique qual o maior entre eles. 
#Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.
n1 = int(input("digite um numero: "))
n2 = int(input("digite outro numero: "))

if n1>n2:
  maior = n1
  for numeros in range(maior, n2):
    print("oi",numeros)

elif n2>n1:
  maior = n2
  print("deu certo")
else:
  print("Os numeros sao iguais, comece o programa novamente") 