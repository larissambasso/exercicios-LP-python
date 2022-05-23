print("{}QUANTIDADE, ORDEM E PRESENÇA DE NÚMEROS{}".format('-'*20, '-'*20))
lista = [];
continuar = 1
contador = 0
while continuar==1:
  n = int(input("Digite um numero: "))
  continuar = int(input("Deseja adicionar mais um numero: [1]SIM [2]NÃO"))
  lista.append(n)
  contador +=1
lista.sort(reverse=True)
print(lista)
print("A quantidade de numeros digitados foi:", contador)
if 5 in lista:
  print("O numero 5 esta na sua lista!")
else:
  print("Voce nao digitou o numero 5.")