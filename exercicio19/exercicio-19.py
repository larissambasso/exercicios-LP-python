#Receba 2 valores reais. Calcule e mostre o maior deles.
def bigger(n1,n2):
  if n1>n2:
    return n1
  elif n2>n1:
    return n2  

print("{}QUAL O MAIOR NUMERO?{}".format('-'*20, '-'*20))
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))

if n1>n2:
  print('O maior numero é: ', bigger(n1,n2))

elif n2>n1:
  print('O maior numero é: ', bigger(n1,n2))

else:
  print('Os numeros sao iguais, nao existe um maior.')