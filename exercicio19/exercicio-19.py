#Receba 2 valores reais. Calcule e mostre o maior deles.
print("{}QUAL O MAIOR NUMERO?{}".format('-'*20, '-'*20))
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))

if n1>n2:
  maior = n1
  print('O maior numero é: ',maior)

elif n2>n1:
  maior = n2
  print('O maior numero é: ',maior)

else:
  print('Os numeros sao iguais, nao existe um maior.')