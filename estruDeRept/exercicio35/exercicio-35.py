#Receba 2 números inteiros, verifique qual o maior entre eles. 
#Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.
print("{}SOMA DOS IMPARES{}".format('-'*20, '-'*20))
n1 = int(input("digite um numero: "))
n2 = int(input("digite outro numero: "))
s = 0

if n1>n2:
  for numeros in range(n1-1, n2, -1): #o ultimo numero do parenteses esta indicando a contagem de forma decrescente.
    if numeros%2!=0:
      s = s+numeros
  print("A soma de todos os numeros impares é: ",s)

elif n2>n1:
  for numeros in range(n2-1, n1, -1):
    if numeros%2!=0:
      s = s+numeros
  print("A soma de todos os numeros impares é: ",s)

else:
  print("Os numeros sao iguais, comece o programa novamente") 
  
  #arrumar para negativos