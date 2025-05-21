# Questão 7

""" A conta do cartão de crédito de uma pessoa pode ser modelada por um dicionário
com os campos saldo"""
def compra(conta, valor_compra):
    conta_atualizada = conta.copy()
    conta_atualizada['saldo'] += valor_compra
    conta_atualizada['transacoes'] += 1
    conta_atualizada['media'] = conta_atualizada['saldo'] / conta_atualizada['transacoes']
    return conta_atualizada

saldo = float(input('Digite o saldo devedor da conta: R$ '))
transacoes = int(input('Digite o número de transações realizadas: '))
media = float(input('Digite a média de gastos por transação: R$ '))

conta = {'saldo': saldo, 'transacoes': transacoes, 'media': media}

valor_compra = float(input('Digite o valor da compra: R$ '))

conta = compra(conta, valor_compra)

print('\nConta atualizada:')
print('Saldo devedor: \033[1;31mR$ {:.2f}\033[m'.format(conta['saldo']))
print('Total de transações: \033[1;34m{}\033[m'.format(conta['transacoes']))
print('Média de gastos por transação: \033[1;32mR$ {:.2f}\033[m'.format(conta['media']))
