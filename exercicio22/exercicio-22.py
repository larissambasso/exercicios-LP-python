#Receba 3 valores obrigatoriamente em ordem crescente e um 4° valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.
def ordem (n1,n2,n3):
    n4 = int(input('digite um 4 numero qualquer: '))

    if n4>n3:
      return('Os numeros em ordem crescente são: ',n1, n2, n3, n4)

    elif n4>n2 and n4<n3:
      return('Os numeros em ordem crescente são: ',n1, n2, n4, n3)

    elif n4>n1 and n4<n2:
      return('Os numeros em ordem crescente são: ',n1, n4, n2, n3)

    else:
      return('Os numeros em ordem crescente são: ',n4,n1,n2,n3)


print("{}NUMEROS EM ORDEM CRESCENTE{}".format('-'*20, '-'*20))
n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite um numero inteiro maior que o primeiro: '))

if n2<n1:
  print('O segundo valor é menor que o primeiro, comece novamente)')

else:
  n3 = int(input('Digite um numero inteiro maior que o segundo: '))
  if n3<n2:
    print('Este numero é menor que o anterior. Comece novamente')
  else:
    print('Os valores digitados são:',n1,n2,n3)

print(ordem(n1,n2,n3))

#sei que é possivel fazer com vetores.. refarei quando eu souber.
