# Questão:
# Usar cinco palavras aprendidas em aula como chaves em um glossário e armazenar seus significados como valores.
# Mostrar cada palavra e seu significado em uma saída.

glossario = {
    'codar' : 'programar',
    'algoritmo': 'sequência de instruções',
    'indentação' : 'espaçamento nas linhas de código',
    'git' : 'sistema de controle de versões',
    'commitar' : 'salvar as alterações'
}

for p, s in glossario.items():
    print(f'A palavra é: {p.capitalize()}\nSeu significado é: {s}.\n')
