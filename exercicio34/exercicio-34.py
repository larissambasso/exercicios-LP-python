#Receba um número. Calcule e mostre os resultados da tabuada desse número.
def calculoTaboada(n):

  resultados = [0]*10;



  print("A taboada {} é:\n".format(n)) 
  
  for taboada in range(1, 11):
    resultados[taboada-1] = n * taboada
    # print("{} x {} = {}".format(n, taboada, n*taboada))

  return resultados




print("{}TABOADA{}".format('-'*20, '-'*20))
n = int(input("digite um numero para ver a taboada: "))

valores = calculoTaboada(n)

for i in range(0, 10):
  print(str(i+1) + " x "+ str(n) + " = " + str(valores[i]))