'''
Jogo da adivinhacao

import random
from time import sleep
nc = random.randint(0,5)
print('-=-'*25)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-'*25)
n =int(input('Escolha um número entre 0 e 5: '))
print('Processando...')
sleep(3)
if n == nc:
    print('Voce ganhou!')
else:
    print('Voce errou, o número que eu pensei foi {} e nao {}'.format(nc, n))
'''

'''
Radar eletronico

vel=float(input('Qual é a velocidade atual do carro? '))
if vel>80:
    print('Voce foi multado, sua velocidade era de {}km/h, e o máximo permitido é de {}km/h, o valor da sua multa é de R${:.2f}'.format(vel,80,(vel-80)*7))
else:
    print('Sua velocidade é de {}, voce está dentro do permitido'.format(vel))
'''
'''
Par ou ímpar
numero=int(input('Escolha um número: '))
print('Processando...')
from time import sleep
sleep(1)
if numero%2==0:
    print('O número {} é par'.format(numero))
else:
    print('O número {} é ímpar'.format(numero))
'''

'''
Custo da viagem

#para viagens de até 200 km cobra 0,50 cents por km, acima de 200 km cobrar 0,45 cents por km
dist=float(input('Qual a distancia da viagem em km? '))
print('A distancia da viagem é de {}'.format(dist))
print('Vou calcular o preco da passagem para voce, aguarde um momento...')
from time import sleep
sleep(2)
if dist<=200:
    print('O valor da sua passagem é de R${:.2f}'.format(dist*0.50))
else:
    print('O valor da sua passagem é de R${:.2f}'.format(dist*0.45))
'''

'''
Ano bissexto

ano=int(input('Qual ano voce quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é um ano bissexto'.format(ano))
else:
    print('O ano {} nao é bissexto'.format(ano))
'''

'''
Maior e menor valor

primeiro=float(input('Primeiro valor: '))
segundo=float(input('Segundo Valor: '))
terceiro=float(input('Terceiro Valor: '))
lista= [primeiro,segundo,terceiro]
print('O maior valor entre eles é {}'.format(max(lista)))
print('O menor valor entre eles é {}'.format(min(lista)))
'''

'''
Aumentos múltiplos

salario = float(input('Qual o valor do seu salário? R$'))
if salario > 1250:
    aumento = salario + (salario * 0.1)
    print('O seu antigo salário era de R${} e o seu novo salário será de R${}'.format(salario,aumento))
else:
    aumento = salario + (salario * 0.15)
    print('O seu antigo salário era de R${} e o seu novo salário será de R${}'.format(salario,aumento))
'''

'''
analisando triangulos

a=int(input('Primeiro segmento: '))
b=int(input('Segundo segmento: '))
c=int(input('Terceiro segmento: '))
if a + b > c and b + c > a and c + a > b:
    print('Os segmentos {}, {} e {} podem formar um triangulo'.format(a,b,c))
else:
    print('Os segmentos {}, {} e {} nao podem formar um triangulo'.format(a,b,c))
'''