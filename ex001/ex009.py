# Criar e carregar uma matriz [4][4] com valores aleatórios, sendo que 
# a diagonal principal terá seus dados carregados no programa segundo: 1 4 16 64
import random
print("{}MATRIZ [4][4]{}".format('-'*20, '-'*20))

matriz = [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]
for c in range(0,4):
    for l in range(0,4):
      matriz[l][c] = random.randint(0,9)
      for i in range(0,4):
        if l == c:
          matriz[l][c] = 1

print(matriz)


#CONTINUAR