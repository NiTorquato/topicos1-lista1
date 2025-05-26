# Questão 10

""" Escreva um programa em Python que:
 • lê duas notas de vários alunos e armazena tais notas em um dicionário, onde a chave é o nome do aluno. A entrada de dados deve terminar quando for lida uma string vazia como nome.
 • Escreva uma função que retorna a média do aluno, dado seu nome.
 • Escreva um programa que exiba o nome e a média do aluno de maior média """

def calcular_media(aluno, notas_dict):
    """Retorna a média das notas de um aluno dado seu nome."""
    notas = notas_dict.get(aluno)
    if notas:
        return sum(notas) / len(notas)
    return 0

# Dicionário para armazenar alunos e suas notas
notas_alunos = {}

# Leitura dos dados
while True:
    nome = input('\nDigite o nome do aluno (ou \033[1;92mEnter\033[m para encerrar): ').strip()

    if nome == '':
        break

    if not nome.replace(' ', '').isalpha():
        print('\033[1;31mErro: O nome deve conter apenas letras.\033[m')
        continue

    try:
        nota1 = float(input('Digite a primeira nota de \033[1;34m{}\033[m: '.format(nome)))
        nota2 = float(input('Digite a segunda nota de \033[1;34m{}\033[m: '.format(nome)))
        notas_alunos[nome.upper()] = [nota1, nota2]
    except ValueError:
        print('\033[1;31mEntrada inválida. Notas devem ser números.\033[m')

# Cálculo da maior média
maior_media = -1
melhores_alunos = []

for aluno in notas_alunos:
    media = calcular_media(aluno, notas_alunos)
    if media > maior_media:
        maior_media = media
        melhores_alunos = [aluno]  # novo aluno com maior média
    elif media == maior_media:
        melhores_alunos.append(aluno)  # empate, adiciona também

# Exibição do resultado
if melhores_alunos:
    print('\n\033[1;32mAluno(s) com a maior média:\033[m')
    for aluno in melhores_alunos:
        print('Nome: \033[1;34m{}\033[m | Média: \033[1;33m{:.1f}\033[m'.format(aluno, maior_media))
else:
    print('\n\033[1;31mNenhum aluno foi cadastrado.\033[m')
