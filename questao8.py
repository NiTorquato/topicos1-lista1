# QUestão 8

"""Um programa em Python que leia nomes de alunos e suas respectivas notas até que o nome ’oooo’ seja informado,
após o fim da leitura, imprima o nome do aluno que possui a maior nota."""

alunos = {}
while True:
    nome = input('Digite o nome do aluno (ou "oooo" para encerrar): ').strip()
    if nome.lower() == 'oooo':
        break
    nota = float(input('Digite a nota do aluno {}: '.format(nome)))
    alunos[nome.upper()] = nota

if alunos:
    melhor_aluno = max(alunos, key=alunos.get)
    print('\nAluno com a maior nota:')
    print('\033[1;34m{} \033[mcom nota \033[1;32m{:.2f}\033[m'.format(melhor_aluno, alunos[melhor_aluno]))
else:
    print('\n\033[1;31mNenhum aluno foi registrado.\033[m')
