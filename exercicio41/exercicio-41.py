#Mostre todas as possibilidades de 2 dados de forma que a soma tenha como resultado 7.

print("{}PROBABILIDADE COM DADOS{}".format('-'*20, '-'*20))
# possibilidades = 0
# dado2 = 0
# resultado = 0
# while dado2<=6:
#   for dado in range(1,7):

#     if dado == 6:
#       dado2 += 1
#     if dado2 != 0 and dado2!=7:
#       print(dado2, '+',dado ,'= ', end='')
#       resultado = dado2+dado
#       print(resultado)

#     if resultado==7:
#       possibilidades += 1

# print('O numero de possibilidades que possuem o resultado =7, é de: ',possibilidades)

#oooou

for dado in range(1,7):
  for dado2 in range(1,7):
    if dado+dado2==7:
      print(dado,'+',dado2,'=',dado+dado2)
    