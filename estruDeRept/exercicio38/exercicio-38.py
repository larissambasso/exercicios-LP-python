#Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. 
# Obs.: somente valores positivos.
print("{}100 NUMEROS{}".format('-'*20, '-'*20))
contador = 0
menor = 0
maior = 0
while contador<5:
  n = int(input("digite um numero:"))
  
  if(contador == 0): 
    menor = n

  if n>0:
    if n>maior:
      maior = n
    if n<menor:
      menor = n

  contador+=1
  
  
print('o numero maior é: ',maior)
print('o menor numero é: ',menor)