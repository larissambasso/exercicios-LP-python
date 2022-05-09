#Receba um número. Calcule e mostre os resultados da tabuada desse número.
def calculoTaboada(n):
  print("A taboada {} é:\n".format(n)) 
  for taboada in range(1, 11):
    print("{} x {} = {}".format(n, taboada, n*taboada))



print("{}TABOADA{}".format('-'*20, '-'*20))
n = int(input("digite um numero para ver a taboada: "))

calculoTaboada(n)