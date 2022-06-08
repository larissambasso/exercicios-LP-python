import random

v1 = []
n = int(input("Digite um numero: "))
m = int(input("Digite um numero: "))
v1 = [n,m]


v2 = [random.randint(1,3)]


print(v1)
print(v2)

for c in range(0, len(v1)):
    if v2[0] == v1[c]:
      print(c)




# trocando variaveis
# maior = 0

# if v1[0]>v1[1]:
#     maior = v1[0]
#     v1[0] = v1[1]
#     v1[1] = maior