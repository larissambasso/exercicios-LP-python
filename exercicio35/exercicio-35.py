#Receba 2 números inteiros, verifique qual o maior entre eles. 
#Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.
def impar(n1,n2):
  if n1>n2:
    maior = n1
    print(maior)
    for c in range(n1, n2):
      print('os numeros entre esses dois numeros são: ', c)
  elif n1<n2:
    maior = n2
    print(maior)
    for c in range(n2-1, n1, -1):
      print('os numeros entre esses dois numeros são: ', c)
  else:
    print("Os numeros sao iguais, comece o programa novamente") 




print("{}SOMA DOS IMPARES{}".format('-'*20, '-'*20))
n1 = int(input("digite um numero: "))
n2 = int(input("digite outro numero: "))

impar(n1,n2)


# terminar