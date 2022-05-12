# Receba o salario de um funcionario e mostre o novo salario com reajuste de 15%.

print("{}REAJUSTE SALÁRIO{}".format('-'*20, '-'*20))
salario = float(input("qual o seu atual salario?"))
reajuste = salario * 1.15
print ('Seu salario ficará {:.2f} após o reajuste de 15%'.format(reajuste))