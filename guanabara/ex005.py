print("{}LISTA PAR E LISTA IMPAR{}".format('-'*20, '-'*20))
lista = [];
impar = [];
par = [];
for c in range(1,11):
  n = int(input("Digite um numero: "))
  lista.append(n)
  if n%2==0:
    par.append(n)
  if n%2!=0:
    impar.append(n)
print("A lista digitada foi: ", lista)
print("Os numeros impares digitados foram: ", impar)
print("Os numeros pares digitados foram: ", par)

# if lista[1] == lista[2]:
#   print(lista[1])