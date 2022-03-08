#Receba o preço atual e a média de venda mensal de um produto. 
#Calcule e mostre o novo preço sabendo que:
# Venda Mensal	          Preço Atual	          Preço Novo
#< 500	                     < 30	                 + 10%
#>= 500 e < 1000	        >= 30 e < 80	           +15%
#>= 1000	                   >= 80	               - 5%
#Obs.: para outras condições, preço novo será igual ao preço atual.

print("{}NOVO PREÇO PRODUTO{}".format('-'*20, '-'*20))
pa = float(input('Qual o preço atual: '))
lucromensal = float(input('Qual o lucro mensal deste produto: '))

if lucromensal<500 and pa<30:
  pn = pa*1.10
  print('O preço novo será de: ',pn)

if (lucromensal>=500 and lucromensal<1000) and (pa>=30 and pa<80):
  pn = pa*1.15
  print('O preço novo será de: ',pn)

if lucromensal>=1000 and pa>=80:
  desconto = pa*0.05
  pn = pa-desconto
  print('O preço novo será de: ',pn)

else:
  print('O preço deste produto nao alterará. O valor é de: ',pa)
