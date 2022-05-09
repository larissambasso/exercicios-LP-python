#Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.
def partes(n):
  resultado = 0
      
  msg = ''
      
  for contador in range(1, n+1):
    
    resultado = resultado + 1/contador
    
    if contador==1:
      msg += str(contador)
    
    if contador!=1:
      msg +=  ' + ' + '1/' + str(contador)
    
    if contador==n:
      msg += ' = '+ str('{:.2f}'.format(resultado))

  print(msg)

print("{}SOMA DAS PARTES{}".format('-'*20, '-'*20))  
n = int(input('digite um numero: '))

partes(n)