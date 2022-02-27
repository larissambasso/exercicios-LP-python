#Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:
#Se a mÉdia for >= 6,0 exibir 'APROVADO';
#Se a média for >= 3,0 ou < 6,0 exibir 'EXAME';
#Se a média for < 3,0 exibir 'RETIDO'.
print("{}MÉDIA ARITIMÉTICA{}".format('-'*20, '-'*20))
p1 = float(input('Qual o valor da primeira nota: '))
p2 = float(input('Qual o valor da segunda nota: '))
p3 = float(input('Qual o valor da terceira nota: '))
p4 = float(input('Qual o valor da quarta nota: '))

media = (p1+p2+p3+p4)/4

if media >=6:
  print('Sua media foi de {}, e você está aprovado'.format(media))

elif media >=3 and media<6:
  print('Sua media foi de {}, e você está de exame'.format(media))

else:
  print('Sua media foi de {}, e você está reprovado'.format(media))