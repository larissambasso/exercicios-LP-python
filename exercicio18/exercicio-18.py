#Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.
def diferenca(n1,n2):
  if n1>n2:
    return n1-n2
  elif n2>n1:
    return n2-n1
  

print("{}RESULTADO DA DIFERENÇA{}".format('-'*20, '-'*20))
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1>n2:
  print('A diferença do maior para o menor é de: ',diferenca(n1,n2))

elif n2>n1:
  print('A diferença do maior para o menor é de: ',diferenca(n1,n2))

else:
  print('Os numeros sao iguais, nao existe diferença')
