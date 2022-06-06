# Criar e coletar em um vetor [30] real e calcular e exibir:
# A média do grupo;
# A quantidade de notas acima do grupo;
# As posições dos valores abaixo da média do grupo.

print("{}MEDIA DE NOTAS{}".format('-'*20, '-'*20))

notas = []*5
soma = 0
contador = 0
for c in range(1,31):
  n = int(input("Digite um numero: "))
  notas.append(n)
  soma += n
  resultado = soma/c

for d in notas:
  if d>resultado:
    contador += 1
  elif d<resultado:
    posicao = notas.index(d)
    print(f'A posiçao dos numeros abaixo da média é: {posicao}!')
print(f'A quantidade de valores acima da média nesta lista é de: {contador} números!')

print(notas)
print("A media destes numeros é de: ",resultado)



# lista = [1, 2, 10, 5, 20]
# valor = 10
# pos = -1
# for i in range(len(lista)-1,-1,-1):
#  if lista[i] == valor:
#   pos = i
# print(pos)