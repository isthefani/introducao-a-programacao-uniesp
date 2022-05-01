''' Faça um algoritmo para ler 20 números e armazenar em um vetor.
Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa. '''

lista = []
while len(lista) < 20:
  num = int(input('> Digite um número inteiro: '))
  lista.append(num)
print('Sua lista ficou da seguinte forma: ', lista)
lista.reverse()
print(f'A ordem inversa da lista é: {lista}.')
