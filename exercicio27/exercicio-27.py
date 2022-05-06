#Receba o número de voltas, a extensão do circuito (em metros) e o tempo de 
#duração (minutos). Calcule e mostre a velocidade média em km/h.
import math
print("{}VELOCIDADE MÉDIA{}".format('-'*20, '-'*20))
voltas = int(input('Qual foi o numero de voltas? '))
metros = float(input('Qual foi a distancia do circuito?(m) '))
tempo = int(input('Quantos minutos durou o circuito? '))


distancia = voltas*metros

km = distancia/tempo

print('A velocidade média foi de:{}'.format(math.trunc(km))) #trunc pega a parte inteira do numero


#ARRUMAR
