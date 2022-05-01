'''Construir uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:
   a. Imprimir o resultado da soma de todos os valores da matriz no terminal;
   b. Criar uma nova matriz B, no qual cada item seja o valor da matriz A * 3.'''

from random import randint as ri

matriz = []
for x in range(10):
    aux = []
    for y in range(10):
        aux.append(ri(1, 99))
    matriz.append(aux)
print('=-' * 20)
print(' MATRIZ-A 10x10 COM VALORES ALEATÓRIOS')
print('=-' * 20)
for i in matriz:
    print(i)

soma = 0
for x in matriz:
    for y in x:
        soma += y
print(f'\n> A SOMA de todos os valores é igual a: {soma}\n')

matriz_b = []
for x in range(0, len(matriz)):
    aux = []
    for y in range(0, len(matriz[x])):
        mult = matriz[x][y] * 3
        aux.append(mult)
    matriz_b.append(aux)

print('=-' * 29)
print('MATRIZ-B 10x10 COM VALORES MULTIPLICADOS POR 3 DA MATRIZ-A')
print('=-' * 29)

for i in matriz_b:
    print(i)
    