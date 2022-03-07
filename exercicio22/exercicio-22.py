#Receba 3 valores obrigatoriamente em ordem crescente e um 4° valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.
print("{}NUMEROS EM ORDEM CRESCENTE{}".format('-'*20, '-'*20))
n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))
n3 = int(input('Digite um terceiro numero:'))

if n1>n2:
  maior = n1
  print('Os numero em ordem crescente são: ',n2, maior)

elif n2>n1:
  maior = n2
  print('Os numero em ordem crescente são: ',n1, maior)

else:
  print('Os numeros sao iguais, fim do programa.')