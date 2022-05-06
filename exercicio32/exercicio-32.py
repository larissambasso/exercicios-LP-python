#Receba um número inteiro. Calcule e mostre o seu fatorial.
print("{}FATORIAL NUMERO INTEIRO{}".format('-'*20, '-'*20))  
s = 1
n = int(input('digite um numero: '))
for c in range(1, n+1):
  s *= c
  print(c, end='')
  if c<n:
    print('x', end='')
  if c==n:
    print(' = ', end='')
    c*=c
print(s)
