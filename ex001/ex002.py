# Criar e coletar um vetor [100] inteiro e exibir:
# O maior e o menor valor;
# A média dos valores.

print("{}MAIOR, MENOR E MÉDIA{}".format('-'*20, '-'*20))
lista = []
maior = 0
soma = 0
for c in range(1,101):
    n = int(input("Digite um numero: "))
    lista.insert(c,n)
    soma += n
    if c==1:
        menor = n
    if n>maior:
        maior = n
    if n<menor:
        menor = n
    print(c)
    resultadoMedia = soma/c

        
print(menor)
print(maior)
print(resultadoMedia)
print(lista)