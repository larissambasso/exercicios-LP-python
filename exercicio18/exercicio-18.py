#Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.
print("{}RESULTADO DA DIFERENÇA{}".format('-'*20, '-'*20))
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1>n2:
  resultado = n1-n2
  print('A diferença do maior para o menor é de: ',resultado)

elif n2>n1:
  resultado = n2-n1
  print('A diferença do maior para o menor é de: ',resultado)

else:
  print('Os numeros sao iguais, nao existe diferença.')
