import math
'''
valor=float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(valor, math.trunc(valor)))
'''
'''
co=float(input('O valor do cateto oposto: '))
ca=float(input('O valor do cateto adjascente: '))
hi=math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''
'''
an =float(input('Digite o angulo que voce deseja: '))
sen=math.sin(math.radians(an))
print('O angulo {} tem o seno de {:.2f}'.format(an, sen))
cos=math.cos(math.radians(an))
print('O angulo {} tem o cosseno de {:.2f}'.format(an, cos))
tan=math.tan(math.radians(an))
print('O angulo {} tem a tangente de {:.2f}'.format(an, tan))
'''
import random
'''
n1 =str(input('Primeiro aluno: '))
n2 =str(input('Segundo aluno: '))
n3 =str(input('Terceiro aluno: '))
n4 =str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]
escolhido=random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
'''
'''
n1 =str(input('Primeiro aluno: '))
n2 =str(input('Segundo aluno: '))
n3 =str(input('Terceiro aluno: '))
n4 =str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem da apresentacao será ')
print(lista)
'''
'''
TOCANDO MÚSICA
import pygame
pygame.init()
pygame.mixer.music.load('arquivo com musica')
pygame.mixer.music.play()
pygame.event.wait()
'''