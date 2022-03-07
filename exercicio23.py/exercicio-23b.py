#Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.
print("{}DIVISÍVEL POR 2 e 3{}".format('-'*20, '-'*20))
n = int(input('Digite um numero inteiro: '))

if n%2==0 and n%3==0:
  print('este numero é divisivel por 2 e 3!')

elif n%2==0 and n%3!=0:
  print('Este numero é divisivel apenas por 2!')

elif n%2!=0 and n%3==0:
  print('este numero NÃO é divisivel por 2 mas é por 3!')

else:
  print('este numero nao é divisivel nem por 2 nem 3.')