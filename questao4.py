# Questão 4
# contaVoigais
def contaVogais(texto):
    texto = texto.upper()  # deixa tudo maiusculo para facilitar a contagem
    vogais = {'A':0, 'E':0, 'I':0, 'O':0, 'U':0}
    for letra in texto:
        if letra in vogais:
            vogais[letra] += 1
    return vogais

# Programa principal
frase = str(input('Digite um texto: '))
resultado = contaVogais(frase)

print('Quantidade de vogais no texto:')
for vogal, quantidade in resultado.items():
    print('\033[1;32m{}\033[m: \033[1;34m{}\033[m'.format(vogal.upper(), quantidade))

