menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 300
quantia_maxima_saque = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3


def deposito(valor):
    global saldo
    global extrato
    
    if valor.isdigit() and float(valor) > 0:
        valor_numerico = float(valor)
        saldo += valor_numerico
        extrato+= f'Operação - Depósito; Valor - {valor_numerico}\n'
    else:
        print('Valor inválido!')
        
        
def saque(valor):
    global quantia_maxima_saque
    global saldo
    global extrato
    global numero_saques
    global LIMITE_SAQUES
    
    if valor.isdigit() and float(valor) > 0:
        valor_numerico = float(valor)
        if valor_numerico > quantia_maxima_saque:
            print('O Valor excede o saque máximo permitido!')
        elif valor_numerico > saldo:
            print('Saldo insuficiente!')
        else:
            saldo -= valor_numerico
            numero_saques += 1
            extrato+= f'\nOperação - Saque; Valor - R$ {valor_numerico:.2f}\n'
    else:
        print('Valor inválido!')
        

while True:
    opcao = input(menu)
    
    if opcao == 'd':
        valor_deposito = input('Digite o valor a ser depositado: ')
        deposito(valor_deposito)

    elif opcao == 's':
        if numero_saques >= LIMITE_SAQUES:
            print('Número de saques excedido!')
        else:
            valor_saque = input('Digite o valor a ser sacado: ')
            saque(valor_saque)
    elif opcao == 'e':
        
        print('Histórico de operações:')
        print(extrato)
        print(f'Saldo atual: R$ {saldo:.2f}')
    elif opcao == 'q':
        break
    
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada')
    