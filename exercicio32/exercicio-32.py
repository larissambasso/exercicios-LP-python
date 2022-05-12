#Receba um número inteiro. Calcule e mostre o seu fatorial.
def calcularFatorial(n):
  f = 1
  msg = ""

  for c in range(n,0,-1):
    if c!=1:
      msg += str(c) + "x"
    else:
      msg += str(c) + " = "
    f*=(c)

  return (msg + str(f))



print("{}FATORIAL NUMERO INTEIRO{}".format('-'*20, '-'*20))  

n = int(input('Digite um numero: '))
print(calcularFatorial(n));