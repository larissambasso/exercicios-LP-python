#Receba 2 valores reais. Calcule e mostre o maior deles.
def bigger(n1,n2):
  
  if(n1 == n2): return "Os dois valores são iguais";
  
  if n1>n2:
    return n1
  elif n2>n1:
    return n2  

print("{}QUAL O MAIOR NUMERO?{}".format('-'*20, '-'*20))
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))

print('O maior numero é: ', bigger(n1,n2))
