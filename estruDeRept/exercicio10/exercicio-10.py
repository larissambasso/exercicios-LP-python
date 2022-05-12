#Receba 2 numeros reais. Calcule e mostre a diferença desses valores.
print("{}DIFERENÇA DE VALORES{}".format('-'*20, '-'*20))
n1 = float(input("Digite qualquer numero:"))
n2 = float(input("Digite outro numero:"))

if n1<n2:
    Diference = n2-n1
else:
    Diference = n1-n2

if n1==n2:
   print("Os valores sao iguais, distancia 0. FIM DO PROGRAMA")
else:
    print("A diferença entre estes valores é de:",Diference)