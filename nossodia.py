import time
def linha():
  print('-'*40)
def tempo():
  time.sleep(1)
  linha()
  print('CARREGANDO A PROXIMA PERGUNTA...')
  linha()
  time.sleep(2)
str(print('(1) Sobre o que foi o nosso primeiro assunto no tinder?'))
def opcoes(num,txt):
  print('[',num,']', txt)

opcoes('1','tenis')
opcoes('2','feriado')
opcoes('3','comida')

total = 0
r1 = int(input(''))
if r1==1 or r1==3:
  print('Resposta ERRADA, 0 pontos')
  print('Seu total de pontos é:',total)
else:
  print('Resposta CORRETA, você ganhou 1 ponto.')
  total += 1
  print('Seu total de pontos é:',total)


tempo()

str(print('(2) Que dia começamos a nos falar?'))
time.sleep(2)

opcoes('1','02/março')
opcoes('2','19/abril')
opcoes('3','21/abril')

r2 = int(input(''))

if r2==1 or r2==2:
  print('Resposta ERRADA, 0 pontos')
  print('Seu total de pontos é:',total)
else:
  print('Resposta CORRETA, você ganhou 1 ponto.')
  total += 1
  print('Seu total de pontos é:',total)

tempo()


str(print('(3) Qual foi o primeiro filme que assistimos juntos?'))
time.sleep(2)

opcoes('1','Guerra dos mundos')
opcoes('2','Harry Potter')
opcoes('3','Jogos Vorazes')

r3 = int(input(''))

if r3==2 or r3==3:
  print('Resposta ERRADA, 0 pontos')
  print('Seu total de pontos é:',total)
else:
  print('Resposta CORRETA, você ganhou 1 ponto.')
  total += 1
  print('Seu total de pontos é:',total)

tempo()

str(print('(4) Quantas kills eu tenho de AWP? '))
time.sleep(2)

opcoes('1','5.647 kills')
opcoes('2','8.700 kills')
opcoes('3','13.050 kills')

r4 = int(input(''))

if r4==1 or r4==2:
  print('Resposta ERRADA, 0 pontos')
  print('Seu total de pontos é:',total)
else:
  print('Resposta CORRETA, você ganhou 1 ponto.')
  total += 1
  print('Seu total de pontos é:',total)

tempo()

str(print('(5) Quantas vezes a gente já transou? '))
time.sleep(2)

opcoes('1','1200 vezes')
opcoes('2','847 vezes')
opcoes('3','376 vezes')

r5 = int(input(''))

print('Não sei, mas a gnt pode somar +1 daqui a pouco, que tal?')
opcoes('1','Chupadinha')
opcoes('2','Completão')

r52 = int(input(''))
print("(¬‿¬)   Hmmmmmmm   (¬‿¬) ")

tempo()

str(print('(6) Quais foram nossas viagens ate agora, na ordem: '))
time.sleep(2)

opcoes('1','Serra Negra / RJ / Ilha Bela')
opcoes('2','Ilha Bela, Serra negra, RJ')
opcoes('3','Serra Negra, Ilha Bela, RJ ')

r6 = int(input(''))
if r6==3:
  print('Resposta CORRETA, você ganhou 1 ponto.')
  total += 1
  print('Seu total de pontos é:',total)
  
else:
  print('Resposta ERRADA, 0 pontos')
  print('Seu total de pontos é:',total)

time.sleep(2)

print("VOCÊ GANHOU DIREITO A UM SUPER DESENHO! ")

time.sleep(2)


str(print('Preparado?'))
time.sleep(2)

opcoes('1','SIM')
opcoes('2','NÃO')

r7 = int(input(''))

while r7!=1:
  r7 = int(input('E agora?'))
  if r7==1:
    print('Então lá vai!')
time.sleep(2)


import turtle
t = turtle.Turtle()
t.width(10)
tela = turtle.Screen()
tela.screensize(520,580)
t.shape("turtle")
t.penup()
t.speed(2)
t.setpos(-400, 300)
t.pendown()
t.forward(100)
t.backward(100)
t.right(90)
t.forward(80)
t.left(90)
t.forward(100)
t.backward(100)
t.right(90)
t.forward(80)
t.left(90)
t.forward(100)
t.penup()
t.forward(80)
t.pendown()
t.left(90)
t.forward(160)
t.backward(160)
t.right(90)
t.forward(100)
t.left(90)
t.forward(160)
t.right(90)
t.penup()
t.forward(80)
t.pendown()
t.forward(150)
t.backward(75)
t.right(90)
t.forward(160)
t.left(90)
t.penup()
t.forward(60)
t.forward(100)
t.left(90)
t.pendown()
t.forward(160)
t.right(90)
t.forward(100)
t.backward(100)
t.right(90)
t.forward(80)
t.left(90)
t.forward(100)
t.backward(100)
t.right(90)
t.forward(90)
t.left(90)
t.forward(100)
t.penup()
t.speed(2)
t.setpos(-350, 50)
t.pendown()
t.left(70)
t.backward(180)
t.forward(180)
t.right(140)
t.forward(180)
t.backward(90)
t.left(70)
t.backward(63)
t.penup()
t.forward(170)
t.right(103)
t.pendown()
t.forward(89)
t.backward(175)
t.left(40)
t.forward(100)
t.right(60)
t.backward(100)
t.right(135)
t.backward(168)
t.penup()
t.forward(100)
t.right(130)
t.penup()
t.forward(150)
t.pendown()
t.circle(80)
t = turtle.Turtle()
t.width(10)
tela = turtle.Screen()
tela.bgcolor("firebrick")
t.shape("turtle")
t.penup()
t.right(35)
t.forward(350)
t.pendown()

def curve(): 
    for i in range(200): 
        t.right(1) 
        t.forward(1) 
def heart(): 
  
    
    t.fillcolor('red') 
  
    
    t.begin_fill() 
  
    
    t.left(140) 
    t.forward(113) 
  
    
    curve() 
    t.left(120) 
  
    
    curve() 
  
    
    t.forward(112) 
  
    
    t.end_fill() 
def txt(): 
  
    
    t.up() 
  
    
    t.setpos(-68, 95) 
  
    
    t.down()
  
  
heart() 
txt() 
t.ht()