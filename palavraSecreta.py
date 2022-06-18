import random


def minhaSenha():
    adivinhacao = [0]*5
    for d in range(0,5):
        adv = int(input("Digite um numero: "))
        adivinhacao[d] = adv
    return(adivinhacao)


def tentativa(numeros, senhaSecreta):
    
    encontrou = False;
    numero = '';

    
    for d in range(0, len(numeros)):
        for e in range(0, len(senhaSecreta)):
            if senhaSecreta[e] == numeros[d]:
                encontrou = True;
                if d==e:
                    numero = "\033[1;32m" + str(numeros[d])
                    break;
                elif d!=e:
                    numero = "\033[1;33m" + str(numeros[d])
        
        if not encontrou:
            numero = "\033[1;31m" + str(numeros[d])
        
        print(numero);

        encontrou = False;


senhaSecreta = []

for c in range(1,6):
    s = random.randint(1,9)
    senhaSecreta.append(s)

# print(senhaSecreta)
numeros = minhaSenha()


while senhaSecreta!=numeros:
    tentativa(numeros, senhaSecreta)
    print("\033[1;97m Tente novamente!",numeros)
    numeros = minhaSenha()

print("\033[1;32m CORRETA",numeros)


#TERMINAR

