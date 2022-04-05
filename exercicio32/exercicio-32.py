#Receba um número inteiro. Calcule e mostre o seu fatorial.
print("{}FATORIAL NUMERO INTEIRO{}".format('-'*20, '-'*20))  
n = int(input('Digite um numero: '))
contador = n
fatorial=n
print(n)
while contador>1:
  contador-=1
  fatorial*=contador
  print(contador)
print(fatorial)
