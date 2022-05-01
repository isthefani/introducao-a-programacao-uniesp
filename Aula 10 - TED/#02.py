''' Faça um algoritmo para ler 50 números e armazenar em um vetor VET, verificar e escrever se existem
números repetidos no vetor VET e em que posições se encontram. '''

import numpy as np
from random import randint as ri

lista = []
for c in range(0, 50):
  lista.append(ri(1, 500))
print(f'A lista a seguir contém 50 valores:\n{lista}')
lista = np.array(lista)
nChecked = []

for i in lista:
    if(nChecked.count(i)):
        break;
    result = np.where(lista == i)
    if (np.size(result) > 1):
        print('VALOR REPETIDO!')
        print('O número', i, 'foi encontrado nas posições: ', result[0]+1)
    nChecked.append(i)
