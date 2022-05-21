# Criar e coletar um vetor [50] inteiro. Calcular e exibir:
# A média dos valores entre 10 e 200;
# A soma dos números ímpares.
print("{}SOMA E MEDIA DE UM VETOR{}".format('-'*20, '-'*20))

numeros = []
somarMedia = 0
contador = 0
impares = 0
for c in range(1,51):
  n = int(input("Digite um numero: "))
  numeros.append(n)
  if n>=10 and n<=200:
    somarMedia += n
    contador+=1
  if n%2!=0:
    impares += n
resultado = somarMedia/contador
print("Seus numeros armazenados sao: ", numeros)
print("A média do numeros entre 10 e 200 é de: ",resultado)
print("Os numeros impares dentro desta lista tem a soma de: ",impares)