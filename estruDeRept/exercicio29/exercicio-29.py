#Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento.
#Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%.
#Demais tipos não serão considerados.
def renda(investimento):
  if investimento==1:
    valorInvestimento = float(input('Qual valor deseja investir? '))
    rendimento = valorInvestimento*1.03
    print('Seu rendimento daqui 30 dias será de: rendimento', rendimento)

  elif investimento==2:
    valorInvestimento = float(input('Qual valor deseja investir? '))
    rendimento = valorInvestimento*1.05
    print('Seu rendimento daqui 30 dias será de: rendimento', rendimento)


  else:
    print('Opção nao encontrada. Tente novamente.')


print("{}INVESTIMENTOS{}".format('-'*20, '-'*20))
print('''[1] poupança[2] renda fixa''')
investimento = int(input('selecione o tipo de investimento que deseja fazer: '))

renda(investimento)

