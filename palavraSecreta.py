import random


def minhaSenha():
    adivinhacao = [0]*5
    for d in range(0,5):
        adv = int(input("Digite um numero: "))
        adivinhacao[d] = adv
    return(adivinhacao)




senhaSecreta = []

for c in range(1,6):
    s = random.randint(1,9)
    senhaSecreta.append(s)
    
print(senhaSecreta)
numeros = minhaSenha()

for d in range(0, len(numeros)):
    for e in range(0, len(senhaSecreta)):
        if senhaSecreta[e] == numeros[d]:
            if d==e:
                print("\033[1;32m",numeros[d])
            else:
                print("\033[1;33m",numeros[d])
        else:
                print("\033[1;31m",numeros[d]) #ajustar

while senhaSecreta!=numeros:
    print("Tente novamente!",numeros)
    numeros = minhaSenha()

print("\033[1;32m CORRETA",numeros)
