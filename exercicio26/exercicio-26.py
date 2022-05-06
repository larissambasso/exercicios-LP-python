#Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.
def multiplo(n1,n2):
  if n1>n2:
    if n1%n2==0:
      print('o maior É um multiplo do menor')

  elif n2>n1:
    if n2%n1==0:
      print('o maior É um multiplo do menor')
  
  elif n1==n2:
    print('os numeros sao iguais.fim do programa')

  else:
    print('o maior nao é um multiplo do menor')



print("{}MULTIPLOS{}".format('-'*20, '-'*20))
n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))

(multiplo(n1,n2))