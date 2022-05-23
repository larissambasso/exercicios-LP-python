# Criar e coletar um vetor [100] inteiro e exibir:
# O maior e o menor valor;
# A média dos valores.

print("{}MAIOR, MENOR E MÉDIA{}".format('-'*20, '-'*20))
lista = []
maior = 0
soma = 0
for c in range(1,6):
    n = int(input("Digite um numero: "))
    lista.insert(c,n)
    soma += n
    if c==1:
        menor = n
    if n>maior:
        maior = n
    if n<menor:
        menor = n
    resultadoMedia = soma/c

print("Você digitou: ",lista) 
print("O menor numero da lista é: ", menor)
print("O maior numero da lista é: ", maior)
print("A media destes números é: ", resultadoMedia)