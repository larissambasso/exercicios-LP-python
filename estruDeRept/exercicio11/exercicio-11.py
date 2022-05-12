#Receba o raio de uma circunferência. Calcule e mostre o comprimento da circunferencia.
from cmath import pi
import math
print("{}RAIO E CIRCUNFERENCIA{}".format('-'*20, '-'*20))
R = float (input('Determine o valor do raio(R): '))
C = (2*pi*R)
print('O valor do comprimento dessa circunferencia é de:{:.2f}'.format (C))