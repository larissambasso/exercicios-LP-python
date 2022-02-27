#Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. 
#Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto - desconto). 
# A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber.
print ("{}SALÁRIO LIQUIDO{}".format('-'*20, '-'*20))
horas = int(input('Digite a quantidade de horas trabalhadas: '))
valorh = float(input('Digite o valor da sua hora: '))
desconto = float(input('Digite o percentual de desconto: '))
dependente = int(input('Determine o numero de dependentes: '))

Salário = horas*valorh

if dependente>0:
  acrescimo = dependente*100
  total = Salário+acrescimo
  SalarioL = total-desconto
  print('Seu salario liquido é igual a:',SalarioL)

else:
  SalarioL = Salário-desconto

  print('Seu salario liquido é igual a:',SalarioL)