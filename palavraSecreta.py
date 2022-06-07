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


adivinhacao = minhaSenha()
while senhaSecreta!=adivinhacao:
    print("SENHA INCORRETA. Tente novamente!",adivinhacao)
    adivinhacao = minhaSenha()

print("\033[1;32m CORRETA",adivinhacao)
