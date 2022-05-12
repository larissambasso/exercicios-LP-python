#Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, 
#sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.
print("{}TEMPO DE JOGO{}".format('-'*20, '-'*20))
import datetime
inicio = int(input('qual o horario do inicio do jogo:(separe hora e minuto com uma virgula) '))
final = int(input('qual o horario do inicio do jogo:(separe hora e minuto com uma virgula) '))
inicio = time.mktime(inicio)
print time.strftime("%H:%M",time.gmtime(inicio))

#continuar