#Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria 
#sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 m e cresce 2 cm ao ano.
print("{}ALTURA DE ANA E MARIA{}".format('-'*20, '-'*20))
ana = 110
maria = 150
anos = 0
while ana<=maria:
  ana += 3
  maria += 2
  anos += 1
if ana > maria:
  print('Levara {} anos para que ana seja maior que maria.'.format(anos))
  print('A altura de Ana é: ', ana)
  print('Enquanto a altura de maria é: ', maria)
