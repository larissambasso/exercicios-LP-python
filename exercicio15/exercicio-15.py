#Receba os valores de 2 catetos de um triangulo retangulo. Calcule e mostre a hipotenusa.
print ("{}TEOREMA DE PITÁGORAS{}".format('-'*20, '-'*20))
C1 = int(input('Qual o valor do primeiro cateto: '))
C2 = int(input('Qual o valor do segundo cateto: '))

H = (C1**2+C2**2)**(1/2)
print('O valor da hipotenusa é de:{:.2f} '.format(H))


#ooou
#import math
#print ("{}TEOREMA DE PITÁGORAS{}".format('-'*20, '-'*20))
#C1 = int(input('Qual o valor do primeiro cateto: '))
#C2 = int(input('Qual o valor do segundo cateto: '))
#H = math.hypot(C1, C2)
#print('O valor da hipotenusa é de:{:.2f} '.format(H))