#Ler um vetor R de 5 elementos contendo o gabarito da LOTO. A seguir ler um vetor A de 10
# elementos contendo uma aposta. A seguir imprima quantos pontos fez o apostador.
import random

print("{}LOTOFÁCIL{}".format('-'*20, '-'*20))

minhaAposta = []
while len(minhaAposta)<15:
  meusNumeros = int(input("Digite um numero de 1 a 25:"))
  if meusNumeros not in minhaAposta and meusNumeros<=25:
    minhaAposta.append(meusNumeros)

  elif meusNumeros>25 or meusNumeros==0:
    print("Este numero não é permitido. Digite outro!")

  else:
    print("Este numero já foi digitado!")

print("Os numeros de sua aposta foram:", minhaAposta)

loteria = []

while len(loteria)<15:
    n = (random.randint(1,25))
    if n not in loteria:
      loteria.append(n)

print ("Os números sorteados foram:", loteria)


pontos = 0

for c in range(0, len(minhaAposta)):
    for d in range(0, len(loteria)):
      if minhaAposta[c] == loteria[d]:
        pontos+=1
print("Você fez um total de: ", pontos)