#Criar e carregar uma matriz [4][3] inteiro com quantidade de produtos vendidos em 4 semanas. 
# Calcular e exibir:
# A quantidade de cada produto vendido no mês;
# A quantidade de produtos vendidos por semana;
# O total de produtos vendidos no mês.
print("{}MATRIZ [4][3]{}".format('-'*20, '-'*20))
produto = 1
print("Digite a quantidade de cada produto.")
matriz = [0,0,0,0],[0,0,0,0],[0,0,0,0]
for l in range(0,3):
    for c in range(0,4):
        matriz[l][c] = int(input(f'Produto {produto} : '))
        produto += 1
print(matriz)

selecao = False
while selecao is False:
    mes = int(input("Digite um mes para visualizar: Mês 1, 2 ou 3:  "))
    if mes==1:
        print(matriz[0])
        selecao = True
    elif mes==2:
        print(matriz[1])
        selecao = True
    elif mes==3:
        print(matriz[2])
        selecao = True
    if not selecao:
        print("Mes invalido")


# print(f'Os produtos vendidos neste mes foram os: {produto}',selecioneMes(mes)) TENTANDO PRINTAR A POSIÇAO DOS NUMEROS