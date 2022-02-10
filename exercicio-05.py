import math
print("{}EQUAÇÃO DE SEGUNDO GRAU{}".format('-'*20, '-'*20))

A = int(input("Digite o valor de A:"))

if A==0:
    print("Nao é uma equaçao do segundo grau!")

else:
    B = int(input("Digite o valor de B:"))
    C = int(input("Digite o valor de C:"))
    delta = (B*B)-(4*A*C)
    
    if delta<0:
        print("Fim do programa. Raizes imaginarias")
    elif delta==0:
        raiz = -B/(2*A)
        print("A equaçao só possui uma raiz:", raiz)
    else:
        raiz1 = (-B + math.sqrt(delta))/(2*A)
        print(raiz1)
        raiz2 = (-B - math.sqrt(delta))/(2*A)
    
        print("A raiz 1 desta equaçao é igual a:", raiz1)
        print("A raiz 2 desta equaçao é igual a :", raiz2)
