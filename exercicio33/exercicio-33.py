#Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.
from unittest import result


print("{}SOMA DAS PARTES{}".format('-'*20, '-'*20))  
n = int(input('digite um numero: '))
# c = 1
resultado = 0

# while c<=(n-1):
#   c+=1
#   print('1/',c)
#   if c+1<=n:
#     resultado += (1/(c+1))
#     print(resultado)
#  resultado += 1/contador
    
msg = ''
    
for contador in range(1, n+1):
  
  resultado = resultado + 1/contador
  
  if contador==1:
    msg += str(contador)
  
  if contador!=1:
    msg +=  ' + ' + '1/' + str(contador)
  
  if contador==n:
    msg += ' = '+ str(resultado)

  
print(msg)
