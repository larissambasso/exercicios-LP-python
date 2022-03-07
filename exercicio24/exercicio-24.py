#Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos,
#sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.
import datetime
print("{}HORA DE UM JOGO{}".format('-'*20, '-'*20))

hora_string = input("Que horas começou o jogo? (hh:mm): ")

hora = int(input(hora_string.split(':')[0]))
minuto = int(input(hora_string.split(':')[1]))

#CONTINUAR
