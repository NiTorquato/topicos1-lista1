# Questão 2
# Faça um programa em Python para ler uma tabela contendo os nomes dos alunos de uma turma de 5 alunos.
# O programa deve solicitar ao usuário os nomes do aluno, sempre perguntando se ele deseja inserir mais um nome na lista.
# Uma vez lidos todos os alunos, o usuário irá indicar um nome que ele deseja verificar se está presente na lista.
# O programa deve procurar pelo nome (ou parte deste nome) e, se encontrar, deve exibir na tela o nome completo e o índice do vetor onde está guardado este nome.

alunos = []  # Lista para armazenar os nomes dos alunos

print('Cadastro de Alunos da Turma')

while True:
    nome = str(input('Digite o nome do aluno: ')).strip()
    alunos.append(nome)

    if len(alunos) == 5:
        print('Limite de 5 alunos atingido.')
        break

    continuar = str(input('Deseja adicionar mais um nome? [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).strip().upper()
    if continuar != 'S':
        break

print('-=' * 20)
print('Lista de alunos cadastrados:')
for i, aluno in enumerate(alunos, start=1):     # Começa a contar do 1
    print('{} - {}'.format(i, aluno))
print('-=' * 20)

busca = str(input('Digite um nome (ou parte do nome) que deseja buscar: ')).strip().upper()
encontrado = False

for i, aluno in enumerate(alunos, start=1):     # Começa a contar do 1
    if busca in aluno.upper():
        print('Nome encontrado: "\033[1;34m{}\033[m" está na posição \033[1;33m{}\033[m da lista.'.format(aluno, i))
        encontrado = True

if not encontrado:
    print('\nNome "{}" não foi encontrado na lista.'.format(busca))
