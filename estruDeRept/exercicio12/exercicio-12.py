#Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos tera daqui a 17 anos.
print("{}IDADE DEPOIS DE 17 ANOS{}".format('-'*20, '-'*20))
Atual = int(input('Determine o ano atual:'))
Nasc = int(input('Determine o ano de nascimento:'))
if Atual<Nasc:
    print("A data de nascimento é maior que a data atual. Fim do programa")
elif Atual==Nasc:
    print("A datas são equivalentes, daqui a 17 anos voce terá 17 anos!")
else:
    Futuro = (Atual-Nasc)+17
    print('Daqui 17 anos você terá:',Futuro)