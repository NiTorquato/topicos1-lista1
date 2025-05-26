# Questão 9

"""  Escreva uma função “inva” em Python que recebe um dicionário d e retorna um
dicionário “inverso” do dicionário dado, onde, a cada valor v de d está associada a
lista das chaves de d que levam a v. """

def inva(d):

    inverso = {}
    for chave, valor in d.items():
        if valor in inverso:
            inverso[valor].append(chave)
        else:
            inverso[valor] = [chave]
    return inverso

# Testes
teste1 = {1: 2, 3: 1, 4: 2}
teste2 = {}
teste3 = {2: 1, 1: 2}

print('\033[1;33mDicionário original:\033[m {}'.format(teste1))
print('\033[1;32mDicionário invertido:\033[m {}'.format(inva(teste1)))

print('\n\033[1;33mDicionário original:\033[m {}'.format(teste2))
print('\033[1;32mDicionário invertido:\033[m {}'.format(inva(teste2)))

print('\n\033[1;33mDicionário original:\033[m {}'.format(teste3))
print('\033[1;32mDicionário invertido:\033[m {}'.format(inva(teste3)))

