#Receba um número inteiro. Calcule e mostre o seu fatorial.
def inteiro(n):
  f = 1
  for c in range(n,0,-1):
    if c!=1:
      print(c, end='x')
    else:
      print(c, end='=')
    f*=(c)
  print(f, end='')


print("{}FATORIAL NUMERO INTEIRO{}".format('-'*20, '-'*20))  

n = int(input('Digite um numero: '))
inteiro(n)