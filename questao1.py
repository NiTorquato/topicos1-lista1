# Questão 1
# Código de César com deslocamento de 3 posições usando alfabeto fixo

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mensagem = str(input('\033[1;33mDigite uma mensagem para criptografar:\033[m ')).upper()  #.upper transforma qualquer letra em maiuscula!
resultado = ''

for letra in mensagem:
    if letra in alfabeto:
        indice = alfabeto.find(letra)
        nova_pos = (indice + 3) % 26
        resultado += alfabeto[nova_pos]
    else:
        resultado += letra  # Mantém espaços e caracteres não alfabéticos

print('\033[1;32mMensagem original:\033[m {}'.format(mensagem))
print('\033[1;34mMensagem criptografada:\033[m {}'.format(resultado))
