#Receba o valor de um deposito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m.
print("{}RENDIMENTO DE APLICAÇÃO{}".format('-'*20, '-'*20))
Deposito = float(input("Digite o valor do deposito na conta poupança:"))
Rendimento = (Deposito*1.013)
print("Após um mês de aplicação, este valor aumentará para:{:.2f}".format(Rendimento))