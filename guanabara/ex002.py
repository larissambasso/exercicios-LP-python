print("{}VALORES ÚNICOS{}".format('-'*20, '-'*20))

numeros=[]

while True:
    n = int(input("Digite um valor: "))
    if n not in numeros:
      numeros.append(n)
      print("Valor adicionado!")
    else:
      print("voce ja digitou este valor.")   
    r = str(input("Deseja adicionar mais? [1]SIM [2]NÃO"))
    if r in '2':
      print("Fim do programa!")
      break
print ("Sua lista é:", numeros)
