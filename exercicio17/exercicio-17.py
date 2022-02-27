#Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.
print("{}QUANTIDADE DE LITROS{}".format('-'*20, '-'*20))

percurso = int(input('Quantas horas demorou o percurso: '))
velocidade = int(input('Qual foi a velocidade média durante o percurso: '))

distancia = percurso*velocidade
litros = distancia/12
print('A quantidade de litros gastos nessa viagem foi de: {:.2f} litros'.format(litros))