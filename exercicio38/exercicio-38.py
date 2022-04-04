#Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. 
# Obs.: somente valores positivos.
print("{}100 NUMEROS{}".format('-'*20, '-'*20))
r = 's'
while r=='s':
  n = int(input("digite um numero:"))
  r = input("deseja continuar?{} (S/N)   ").lower()
print('Os numeros digitados foram: {}'.format(n))