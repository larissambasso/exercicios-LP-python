print("{}5 VALORES ORDENADOS SEM SORT{}".format('-'*20, '-'*20))
list = [];

for c in range(0,5):
  n  = int(input("Digite um número: "))
  if c==0 or c>0 and n>list[-1]:
   list.append(n)
  else:
    posicao = 0
    while posicao<len(list):
      if n<=list[posicao]:
        list.insert(posicao,n)
        break
      posicao += 1
print(list)
