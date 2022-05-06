#Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N'nésimo termo.
print("{}FIBONACCI{}".format('-'*20, '-'*20))
n = int(input('Digite quantos termos voce quer mostrar: '))

n1=0
n2=1
print("A sequencia de fibonacci começa assim: {} -> {}".format(n1, n2), end=' -> ')
f=3
while f <= n:
  soma = n1+n2
  print(soma, end=' -> ')
  n1 = n2
  n2 = soma
  f = f+1
print('fim do programa')

#tentar fazer sem os dois primeiros