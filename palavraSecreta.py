import random


def minhaSenha():
    adivinhacao = [0]*5
    indice = 0
    while indice<5:
        adv = int(input("Digite um numero de 0 a 9: "))
        if adv<=15:
            adivinhacao[indice] = adv
            indice+=1
        else:
            print("Os numeros tem que ser ate 9!")
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


senhaSecreta = [0]*5
indice2 = 0
while indice2<5:
    s = random.randint(0,9)
    if s not in senhaSecreta:
        senhaSecreta[indice2] = s
        indice2+=1
print(senhaSecreta)
numeros = minhaSenha()

quantTentativa = 1

while senhaSecreta!=numeros:
    tentativa(numeros, senhaSecreta)
    print("\033[1;97m Tente novamente!",numeros)
    numeros = minhaSenha()
    quantTentativa += 1

print("\033[1;32m CORRETA",numeros)
print(f'-------------- Você acertou em {quantTentativa} tentativas. --------------')


