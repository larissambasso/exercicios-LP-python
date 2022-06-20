# Criar e coletar em um vetor [30] real e calcular e exibir:
# A média do grupo;
# A quantidade de notas acima do grupo;
# As posições dos valores abaixo da média do grupo.

print("{}MEDIA DE NOTAS{}".format('-'*20, '-'*20))
posicaoAbaixo = []
notas = []*5
soma = 0
contador = 0
for c in range(1,5):
  n = int(input("Digite um numero: "))
  notas.append(n)
  soma += n
  resultado = soma/c

for d in notas:
  if d>resultado:
    contador += 1
  elif d<resultado:
    posicao = notas.index(d)
    posicaoAbaixo.append(posicao)

print("A media destes numeros é de: ",resultado)

semColchete = str(posicaoAbaixo)[1:-1]#faz printar sem colchete
print("As posiçõs dos numeros abaixo da média são:" + semColchete)#faz printar sem colchete

print(f'A quantidade de valores acima da média nesta lista é de: {contador} números!')
