#Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!
print("{}FATORIAL DA SOMA DAS PARTES{}".format('-'*20, '-'*20))  

n = int(input('Digite um numero: '))
msg = 1
print(msg, end=' ')
resultado = 0

for c in range(1, n+1):

  if c>=1:
    msg = '+ 1/' + str(c) + '! '

  if c==n:
    msg += ' = '
  print(msg, end='')
