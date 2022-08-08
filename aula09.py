'''
Analisador de textos

nome =str(input('Digite uma frase: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {} '.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
'''

'''
Separando dígitos de um número

num =int(input('Informe um número: '))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))
'''

'''
Verificando as primeiras letras de um texto

cid =str(input('Em que cidade voce nasceu? ')).strip()
print(cid[:5].upper()== 'Santo'
'''

'''
Procurando uma string dentro de outra

nome=str(input('Qual é o seu nome? ')).strip()
print('Seu nome tem Rodrigues? {}'.format('Rodrigues' in nome.upper()))
'''

'''
Primeira e última ocorrencia de uma string

frase =str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posicao {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posicao {}'.format(frase.rfind('A')+1))
'''

'''
Primeiro e último nome da pessoa

n=str(input('Escreva o seu nome completo: ')).strip()
nome =n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
'''