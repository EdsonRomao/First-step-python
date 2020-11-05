from random import randint
from time import sleep
lista = list()
jogos = list()
jogo_milionario = ('16', '23', '28', '32', '39', '48')

print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0)
while jogos != jogo_milionario:
    if jogos == jogo_milionario:
        break


print('-=' * 5, '< BOA SORTE! > ', '-=' * 5)
''''def compare():
    lista1 = set(jogos)
    jogo_m = set(jogo_milionario)
    intersection = lista1.intersection(jogo_m)
    print(intersection)


def compare2():
    intersection = []
    for numero in jogos:
        if numero in jogo_milionario:
            intersection.append(numero)
    print(len(intersection))'''
