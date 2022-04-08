#Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!
print("{}FATORIAL DA SOMA DAS PARTES{}".format('-'*20, '-'*20))  

n = int(input('Digite um numero: '))
resultado = 1
msg = 1
print(msg, '+ ',end='')

for c in range(1, n+1):
  print('1/', end='')
  print(c, end='')

  if c>1:
    resultado = (resultado*c)

  if c<n:
    print(end='! + ')
  if c==n:
    print('! =', end='')

  msg += 1/resultado 
  
print(msg)               