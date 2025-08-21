from datetime import datetime, date
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 300
quantia_maxima_saque = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_OPERACOES = 3


def deposito(valor):
    global saldo
    global extrato
    
    if valor.isdigit() and float(valor) > 0:
        valor_numerico = float(valor)
        saldo += valor_numerico
        extrato.append(f'Operação - Depósito; Valor - {valor_numerico}; Realizada em {datetime.now()}') 
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
            extrato.append(f'Operação - Saque; Valor - R$ {valor_numerico:.2f}; Realizada em {datetime.now()}') 
    else:
        print('Valor inválido!')
        
def verifica_limite_diario_de_operacoes(data):
    global extrato
    numero_operacoes = 0
    data_string = str(data)
    for registro in extrato:
        if data_string in registro:
            numero_operacoes+=1
    return numero_operacoes
    

        


while True:
    opcao = input(menu)
    
    if (opcao == 'd' or opcao == 's') and verifica_limite_diario_de_operacoes(date.today()) >= LIMITE_OPERACOES:
        print('Número de operações diárias excedido!')
        
    elif opcao == 'd':
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
        for transacao in extrato:
            print(transacao)
        print(f'Saldo atual: R$ {saldo:.2f}')
    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada')
