print("{}LENDO VALORES{}".format('-'*20, '-'*20))

listaA = [];


for c in range(0,5):
  listaA.append(int(input("Digite um numero: ")))
  listaA.sort()
print(listaA)
print('O maior valor desta lista é o:', listaA[4])
print('O menor valor desta lista é o:', listaA[0])
