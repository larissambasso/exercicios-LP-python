# Criar e coletar valores inteiros nos vetores VT1[3] e VT2[3]. 
# Concatenar esses valores em um 3º vetor (VT3[6]) e mostrar os seus dados. 
# P. ex: # VT1|	1|	2|	3|	
#          VT2|	4|	5|	6|	
#          VT3|	1|	2|	3|	4|	5|	6
print("{}CONCATENANDO DOIS VETORES{}".format('-'*20, '-'*20))


lista1 = []*3
lista2 = []*3

for c in range(1,4):
  n = int(input("Digite um valor: "))
  lista1.append(n)
for d in range(1,4):
  n2 = int(input("Digite um numero: "))
  lista2.append(n2)
lista3 = [lista1 + lista2]
print(lista3)
