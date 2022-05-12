#Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99
print("{}SOMA DE DENOMINADORES IMPARES{}".format('-'*20, '-'*20))
numerador = 1
resultado = 0
print(numerador, end='')
for denominador in range(3,100, 2):
    numerador += 1
    print(' +',numerador, end='/')
    print(denominador, end='')
    
    if denominador==99:
        print(' =')
    resultado += numerador/denominador
print(resultado)