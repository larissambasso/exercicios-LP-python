#Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde: 
# Casa: 	1	2	3	4	...	64 
# Qdte:	1	2	4	8	...	N
print("{}TABULEIRO DE XADREZ{}".format('-'*20, '-'*20))
graos = 1
resultado = 1

for casa in range (1,64+1):
  print('casa numero:',casa)
  resultado *= graos*graos+1
  print(resultado) 