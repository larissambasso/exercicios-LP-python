#Criar e carregar uma matriz [4][3] inteiro com quantidade de produtos vendidos em 4 semanas. 
# Calcular e exibir:
# A quantidade de cada produto vendido no mês;
# A quantidade de produtos vendidos por semana;
# O total de produtos vendidos no mês.
print("{}MATRIZ [4][3]{}".format('-'*20, '-'*20))


produto = 1
media = 0
total = 0
soma = 0
soma2 = 0
soma3 = 0
selecao = False

print("Digite a quantidade de cada produto.")
matriz = [0,0,0,0],[0,0,0,0],[0,0,0,0]
for l in range(0,3):
    for c in range(0,4):
        matriz[l][c] = int(input(f'Produto {produto} : '))
        if l==0:
            soma += matriz[l][c]
            mediaM1 = soma/4
        if l==1:
            soma2 += matriz[l][c]
            mediaM2 = soma2/4
        if l==2:
            soma3 += matriz[l][c]
            mediaM3 = soma3/4
        produto += 1
print(soma)
print(matriz)


while selecao is False:
    mes = int(input("Digite um mes para visualizar: Mês 1, 2 ou 3:  "))
    if mes==1:
        print(matriz[0])
        print("A média de produtos vendidos por semana neste mes foi de: ", mediaM1)
        print("O total de produtos vendidos neste neste mes foi de: ", soma)
        selecao = True
    elif mes==2:
        print(matriz[1])
        print("A média de produtos vendidos por semana neste mes foi de: ", mediaM2)
        print("O total de produtos vendidos neste neste mes foi de: ", soma2)
        selecao = True
    elif mes==3:
        print(matriz[2])
        print("A média de produtos vendidos por semana neste mes foi de: ", mediaM3)
        print("O total de produtos vendidos neste neste mes foi de: ", soma3)
        selecao = True
    if not selecao:
        print("Mes invalido")

