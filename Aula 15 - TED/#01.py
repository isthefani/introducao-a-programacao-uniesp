from time import sleep
funcionarios = []

def cadastrar():

    while True:
    
        print('\n\033[33m> FORNEÇA AS INFORMAÇÕES DOS FUNCIONÁRIOS <\033[m\n')
        info = {}
        info['nome'] = input('Nome: ')
        while (info['nome'] == ''):
            info['nome'] = input('Forneça um nome: ')

        info['codigo'] = input('Código: ')
        while (info['codigo'] == ''):
            info['codigo'] = input('Forneça um código: ')
        lista = {i['codigo']: i for i in funcionarios}
        while info['codigo'] in lista:
            print('\n\033[31mEste código já está cadastrado!\033[m\n')
            sleep(1)
            info['codigo'] = input('Use um código novo: ')

        info['email'] = input('E-mail: ')
        while (info['email'] == ''):
            info['email'] = input('Forneça um e-mail: ')
        lista = {i['email']: i for i in funcionarios}
        while info['email'] in lista:
            print('\n\033[31mEste e-mail já está cadastrado!\033[m\n')
            sleep(1)
            info['email'] = input('Use um e-mail novo: ')

        info['data'] = input('Data de admissão: ')
        while (info['data'] == ''):
            info['data'] = input('Forneça uma data: ')

        info['salario'] = input('Salário: R$')
        while (info['salario'] == ''):
            info['salario'] = input('Forneça um salário: ')

        funcionarios.append(info)
        sleep(0.5)
        print('\n\033[32mCADASTRO CONCLUÍDO!\033[m\n')
        sleep(1)
        opcao = input('Deseja cadastrar outro funcionário? (S/N): ').strip().upper()
        sleep(0.5)
        if (opcao == 'N'):
          menu()
          break
        if (opcao == 's'):
          cadastrar()
          break

def alterar():
    while True:
        lista = {i['codigo']: i for i in funcionarios}
        busca = input('\nCódigo do funcionário: ')

        if busca in lista:
            novoNome = input('Digite o novo nome: ')
            for i in funcionarios:
                i['nome'] = novoNome

            print('\n\033[32mALTERAÇÃO CONCLUÍDA!\033[m\n')
            opcao = input('Deseja alterar outro funcionário? ').strip().upper()
            if (opcao == 'N'):
                menu()
                break

        else:
            print('\n\033[31mCódigo não localizado!\033[m\n')
            sleep(1)
            while True:
                novoCod = input('Deseja tentar outro código: (S/N) ').strip().upper()
                if (novoCod == 'S'):
                    alterar()
                    break
                if (novoCod == 'N'):
                    menu()
                    break
        break

def listar():
    while True:
        print('\n\033[33m> LISTA DOS FUNCIONÁRIOS CADASTRADOS <\033[m\n')
        for i in funcionarios:
            print('Nome:', i['nome'], '| Código:', i['codigo'])

        if len(funcionarios) == 0:
            print('\033[1;30;47mA lista está vazia!\033[m\n')

        opcao = input('\nDeseja ver lista novamente? (S/N): ').strip().upper()
        sleep(1)
        if(opcao == 'N'):
            menu()
            break

def excluir():

    while True:
        lista = {i['codigo']: i for i in funcionarios}
        busca = input('\nCódigo do funcionário: ')
        sleep(1)
        for i in funcionarios:
            print('\nFuncionário(a):', i['nome'])
        sleep(1)

        if busca in lista:
            opcao = input('\nTem certeza que deseja excluir este funcionário(a)? (S/N): ').strip().upper()
            if (opcao == 'S'):
                del funcionarios[0]
                print('\n\033[32mFUNCIONÁRIO EXCLUÍDO!\033[m\n')
                menu()
            if (opcao == 'N'):
                print('OK! Operação cancelada.')
                menu()
                break

        else:
            print('\n\033[31mCódigo não localizado!\033[m\n')
            sleep(1)
            while True:
                novoCod = input('Deseja tentar outro código: (S/N) ').strip().upper()
                if (novoCod == 'S'):
                    excluir()
                    break
                if (novoCod == 'N'):
                    menu()
                    break
        break

def salario():
    while True:
        lista = {i['codigo']: i for i in funcionarios}
        busca = input('\nCódigo do funcionário: ')
        sleep(1)
        for i in funcionarios:
            print('\nFuncionário(a):', i['nome'], '| Salário: R$', i['salario'])
        sleep(1)

        if busca in lista:
            novoSalario = input('\nDigite o novo salário: R$')
            for i in funcionarios:
                i['salario'] = novoSalario

            print('\n\033[32mAUMENTO DE SALÁRIO REALIZADO!\033[m\n')
            sleep(1)
            print('A partir de hoje,',i['nome'],'passará a receber R${}.\n'.format(i['salario']))
            sleep(1)
            opcao = input('Deseja realizar outro aumento? (S/N): ').strip().upper()
            if (opcao == 'N'):
                menu()
                break

        else:
            print('\n\033[31mCódigo não localizado!\033[m\n')
            sleep(1)
            while True:
                novoCod = input('Deseja tentar outro código: (S/N) ').strip().upper()
                if (novoCod == 'S'):
                    alterar()
                    break
                if (novoCod == 'N'):
                    menu()
                    break
        break

def menu():
    print('\n\033[0;33m>> CADASTRO DE FUNCIONÁRIOS <<\033[m\n')
    print('[1] Cadastrar funcionário')
    print('[2] Alterar funcionário')
    print('[3] Exibir lista dos funcionários cadastrados')
    print('[4] Excluir um funcionário')
    print('[5] Adicionar um aumento de salário')
    print('[0] Encerrar programa')

menu()

while True:
    esc = int(input('\nEscolha a opção desejada > '))
    sleep(1)

    while esc > 5 or esc < 0:
        esc = int(input('Digite uma opcão válida! > '))

    if esc == 1:
        cadastrar()
    elif esc == 2:
        alterar()
    elif esc == 3:
        listar()
    elif esc == 4:
        excluir()
    elif esc == 5:
        salario()
    else:
        print('\n\033[1;96m-- PROGRAMA ENCERRADO --\033[m\n')
        break