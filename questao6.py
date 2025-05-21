# Questão 6

""" Armazenar uma agenda de telefones em um dicionário. """
def incluirNovoNome(agenda, nome, telefones):
    nome = nome.upper()
    agenda[nome] = telefones
    telefones_coloridos = ', '.join(f'\033[1;92m{tel}\033[m' for tel in telefones)
    print(f'Nome \033[1;34m"{nome}"\033[m incluído com telefones: [{telefones_coloridos}]')

def incluirTelefone(agenda, nome, telefone):
    nome = nome.upper()
    if nome in agenda:
        agenda[nome].append(telefone)
        print(f'Telefone \033[1;92m{telefone}\033[m adicionado para \033[1;34m{nome}\033[m.')
    else:
        resp = input(f'O nome \033[1;34m"{nome}"\033[m não está na agenda. Deseja incluí-lo? [\033[1;32mS\033[m/\033[1;31mN\033[m] ').strip().upper()
        if resp == 'S':
            incluirNovoNome(agenda, nome, [telefone])
        else:
            print('Nome não incluído.')

def excluirTelefone(agenda, nome, telefone):
    nome = nome.upper()
    if nome in agenda:
        if telefone in agenda[nome]:
            agenda[nome].remove(telefone)
            if len(agenda[nome]) == 0:
                del agenda[nome]
                print(f'Telefone removido e nome \033[1;34m"{nome}"\033[m excluído por não ter mais telefones.')
            else:
                print(f'Telefone \033[1;92m{telefone}\033[m removido de \033[1;34m{nome}\033[m.')
        else:
            print(f'Telefone \033[1;92m{telefone}\033[m não encontrado para \033[1;34m{nome}\033[m.')
    else:
        print(f'O nome \033[1;34m"{nome}"\033[m não está na agenda.')

def excluirNome(agenda, nome):
    nome = nome.upper()
    if nome in agenda:
        del agenda[nome]
        print(f'Nome \033[1;34m"{nome}"\033[m excluído da agenda.')
    else:
        print(f'O nome \033[1;34m"{nome}"\033[m não está na agenda.')

def consultarTelefone(agenda, nome):
    nome = nome.upper()
    if nome in agenda:
        telefones_coloridos = ', '.join(f'\033[1;92m{tel}\033[m' for tel in agenda[nome])
        print(f'Telefones de \033[1;34m{nome}\033[m: [{telefones_coloridos}]')
    else:
        print(f'O nome \033[1;34m"{nome}"\033[m não está na agenda.')

# Programa principal para testar as funções
agenda_telefonica = {}

while True:
    print('\nAgenda Telefônica')
    print('1 - Incluir novo nome')
    print('2 - Incluir telefone em nome existente')
    print('3 - Excluir telefone')
    print('4 - Excluir nome')
    print('5 - Consultar telefones')
    print('6 - Mostrar agenda')
    print('0 - Sair')
    escolha = input('Escolha uma opção: ').strip()

    if escolha == '1':
        nome = input('Nome: ').strip().upper()
        telefones = input('Telefones (separe por vírgula): ').strip().split(',')
        telefones = [tel.strip() for tel in telefones]
        incluirNovoNome(agenda_telefonica, nome, telefones)

    elif escolha == '2':
        nome = input('Nome: ').strip().upper()
        telefone = input('Telefone a adicionar: ').strip()
        incluirTelefone(agenda_telefonica, nome, telefone)

    elif escolha == '3':
        nome = input('Nome: ').strip().upper()
        telefone = input('Telefone a remover: ').strip()
        excluirTelefone(agenda_telefonica, nome, telefone)

    elif escolha == '4':
        nome = input('Nome: ').strip().upper()
        excluirNome(agenda_telefonica, nome)

    elif escolha == '5':
        nome = input('Nome para consultar: ').strip().upper()
        consultarTelefone(agenda_telefonica, nome)

    elif escolha == '6':
        print('\nAgenda Completa:')
        if not agenda_telefonica:
            print('Agenda vazia.')
        else:
            for nome, telefones in agenda_telefonica.items():
                telefones_coloridos = ', '.join(f'\033[1;92m{tel}\033[m' for tel in telefones)
                print(f'\033[1;34m{nome}\033[m: [{telefones_coloridos}]')

    elif escolha == '0':
        print('Saindo da agenda...')
        break

    else:
        print('Opção inválida! Tente novamente.')
