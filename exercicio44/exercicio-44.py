#Receba o número da base e do expoente. Calcule e mostre o valor da potência.
print("{}EXPOENTE E POTENCIAS{}".format('-'*20, '-'*20))
base = int(input('Digite o valor da base que deseja calcular a potencia: '))
expoente = int(input('Digite o valor do expoente que deseja calcular a potencia: '))
potencia = 0
for c in range(1, expoente):
  if c == 1:
    potencia += base*base

  if c>1:
    potencia*=base

print('O calculo desta potencia é de: ',potencia)
