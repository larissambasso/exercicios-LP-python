# Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.
print ("{}TROCA DE VALORES{}".format('-'*20, '-'*20))

A = int(input("insira o valor de A:"))
B = int(input("insira o valor de B:"))
print(A,B)
C = A
A = B
B = C
print("Ao fazermos a inversão, A vale: {} e B vale {}".format(A,B))
