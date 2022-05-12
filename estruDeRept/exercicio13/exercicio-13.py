#Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.
print ("{}KILOS DE ALIMENTO{}".format('-'*20, '-'*20))
Alimento = float(input('Digite a quantidade de alimento em Kilos: '))
Conversao = (Alimento*1000)/0.50
dias = Conversao/50
print('Comendo 50gramas por dia, {} de comida durarão: {:.1f} dias'.format(Alimento,dias))
