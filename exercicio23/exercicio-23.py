#Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.
print("{}DIVISÍVEL POR 2 e 3{}".format('-'*20, '-'*20))
n = int(input('Digite um numero inteiro: '))
if n%2 == 0:
  print('Este numero é divisivel por 2!')
else:
  print('Este numero NÃO é divisivel por 2!')

if n%3 == 0:
  print('Este número é divisivel por 3!')
else:
  print('Este numero NAO é divisivel por 3.')


