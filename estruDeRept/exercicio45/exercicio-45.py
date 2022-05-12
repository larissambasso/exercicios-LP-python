#Calcule e mostre a série 1 + 2/4 + 3/9 + 4/16 + 5/25 + ... + 15/225
print("{}DOBRO DO NUMERADOR{}".format('-'*20, '-'*20))
dobro = 2
resultado = 0
print(1, end='')
for c in range (2,16):
  dobro = c*c
  print(' +',c, end='/')
  print(dobro, end='')
  resultado += (c/dobro)
  if c == 15:

    print(' = ',resultado)
