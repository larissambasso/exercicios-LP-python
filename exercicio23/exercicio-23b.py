#Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.
def divisivel(n):
  if n%2==0 and n%3==0:
    return('este numero é divisivel por 2 e 3!')

  elif n%2==0 and n%3!=0:
    return('Este numero é divisivel apenas por 2!')

  elif n%2!=0 and n%3==0:
    return('Este número é divisível apenas 3!')

  else:
    return('este numero nao é divisivel nem por 2 nem 3.')


print("{}DIVISÍVEL POR 2 e 3{}".format('-'*20, '-'*20))
n = int(input('Digite um numero inteiro: '))

print(divisivel(n))