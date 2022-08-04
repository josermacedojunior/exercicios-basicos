'''
Tabuada

print('-'*12)
num=int(input('Digite um número para ver sua tabuada: '))
print('{} x {:2} = {} '.format(num, 1, num*1))
print('{} x {:2} = {}' .format(num, 2, num*2))
print('{} x {:2} = {}' .format(num, 3, num*3))
print('{} x {:2} = {}' .format(num, 4, num*4))
print('{} x {:2} = {}' .format(num, 5, num*5))
print('{} x {:2} = {}' .format(num, 6, num*6))
print('{} x {:2} = {}' .format(num, 7, num*7))
print('{} x {:2} = {}' .format(num, 8, num*8))
print('{} x {:2} = {}' .format(num, 9, num*9))
print('{} x {:2} = {}' .format(num, 10, num*10))
print('-'*12)
'''

'''
Conversor de moedas

real=float(input('Quanto de dinheiro voce tem na carteira? R$ '))
dolar= real/5.21
print('Com R${:.2f} voce pode comprar U${:.2f} .'.format(real, dolar))
'''

'''
Pintando parede
2m**2 precisa de 1l de tinta para ser pintado

largura=float(input('Largura da parede: '))
altura=float(input('Altura da parede: '))
area=largura*altura
tinta= area*0.5
print('Sua parede tem a dimensao de {}x{} e a sua área é de {}m**2.'.format(largura,altura,area))
print('Para pintar essa parede voce precisará de {}l de tinta.'.format(tinta))
'''

'''
Calculando descontos

preco=float(input('Qual é o preco do produto? R$ '))
pdesconto=preco*0.95
print('O produto que custava R${:.2f}, na promocao com desconto de 5% vai custar R${:.2f}'.format(preco,pdesconto))
'''

'''
Calculando reajuste salarial

salario=float(input('Qual é o salário do funcionário? R$ '))
reajuste=salario+(salario*15/100)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${}. '.format(salario,reajuste))
'''

'''
Conversor de temperatura

C=float(input('A temperatura em graus C é: '))
F=(C*9/5)+32
print('A temperatura de {}C corresponde a {}F'.format(C,F))
'''

'''
Aluguel de carros
60 reais/dia
0.15 reais/km

dias=int(input('Quantos dias o carro ficou alugado? '))
km=float(input('Quantos km rodados? '))
vdias=dias*60
vkm=km*0.15
vtotal=vdias+vkm
print('O total a pagar e de R${:.2f}'.format(vtotal))
'''