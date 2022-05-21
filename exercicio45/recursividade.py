def contador(numero):
    print(numero)
    if numero<10:
        contador(numero+1)
    print('fim', numero)

contador(1)

