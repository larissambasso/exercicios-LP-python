#Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. 
#Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= salario Bruto - desconto). 
# A cada dependente será acrescido R$ 100 no salario Líquido. Exiba o salário a receber.
def calcular (horas, valorh, desconto, dependente):
    salario = horas*valorh
    acrescimo = dependente*100
    total = salario+acrescimo
    return total-desconto
    
print ("{}SALÁRIO LIQUIDO{}".format('-'*20, '-'*20))
horas = int(input('Digite a quantidade de horas trabalhadas: '))
valorh = float(input('Digite o valor da sua hora: '))
desconto = float(input('Digite o percentual de desconto: '))
dependente = int(input('Determine o numero de dependentes: '))


print('Seu salario liquido é igual a:',calcular(horas, valorh,desconto,dependente))



