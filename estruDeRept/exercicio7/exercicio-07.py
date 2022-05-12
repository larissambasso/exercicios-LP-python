#Receba os valores do comprimento, largura e altura de um paralelepipedo. Calcule e mostre seu volume.
print ("{}VOLUME PARALELEPIPEDO{}".format('-'*20, '-'*20))
Comprimento = float(input("Digite o valor do comprimento:"))
Largura = float(input("Digite o valor da largura:"))
Altura = float(input("Digite o valor da Altura:"))

Volume =Comprimento*Largura*Altura

print("O volume deste paralelepipedo é de:{:.2f}".format(Volume))