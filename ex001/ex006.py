# Criar e coletar em um vetor [20] com números aleatórios. 
# Classificar este vetor em ordem crescente e mostre os dados.
print("{}20 NUMEROS EM ORDEM CRESCENTE{}".format('-'*20, '-'*20))

numeros = []
maior = 0
for c in range(0,5):
  n = int(input("Digite um numero: "))
  numeros.append(n)
  if numeros[1]<[0]:
    maior = numeros[1]
    numeros[0] = maior

print(numeros)

#TERMINAR