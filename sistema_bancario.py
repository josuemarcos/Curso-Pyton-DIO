from datetime import datetime, date
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Usuário
[q] Sair

=> """

saldo = 300
quantia_maxima_saque = 500
extrato = []
usuarios = []
numero_saques = 0
LIMITE_SAQUES = 2
LIMITE_OPERACOES = 3


def deposito(valor, saldo, extrato):  
    if valor.isdigit() and float(valor) > 0:
        valor_numerico = float(valor)
        saldo += valor_numerico
        extrato.append(f'Operação - Depósito; Valor - {valor_numerico}; Realizada em {datetime.now()}') 
    else:
        print('Valor inválido!') 
    return saldo, extrato
        
def saque(*,valor, quantia_maxima_saque, saldo, extrato, numero_saques, limite_de_saques):
    
    if numero_saques < limite_de_saques:
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
    else:
         print('Número de saques excedido!')
    return saldo, extrato, numero_saques
        
            
def verifica_limite_diario_de_operacoes(data, extrato):
    numero_operacoes = 0
    data_string = str(data)
    for registro in extrato:
        if data_string in registro:
            numero_operacoes+=1
    return numero_operacoes

def verifica_extrato(saldo, *, extrato):
    print('Histórico de operações:')
    for transacao in extrato:
        print(transacao)
    print(f'Saldo atual: R$ {saldo:.2f}')
    
def verifica_usuario_cadastrado(cpf, lista):
    checagem = False
    for registro in lista:
        if registro['cpf'] == cpf:
            checagem = True
    return checagem

def criar_usuario(lista):
    cpf = input('Digite o CPF do usuário: ')
    if verifica_usuario_cadastrado(cpf, lista):
        print('Usuário já cadastrado!')
        return None
    elif not cpf.isdigit:
        print("CPF inválido!")
        return None
    else:
        nome = input('Digite o nome do usuário: ')
        data_nascimento = input('Digite a data de nascimento do usuário: ')
        endereco = input('Digite o endereço do usuário: ')
        novo_usuario = {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'cpf': cpf,
            'endereco': endereco
        }
        lista.append(novo_usuario)
        return lista
        
while True:
    opcao = input(menu)
    
    if (opcao == 'd' or opcao == 's') and verifica_limite_diario_de_operacoes(date.today(), extrato) >= LIMITE_OPERACOES:
        print('Número de operações diárias excedido!')
        
    elif opcao == 'd':
        valor_deposito = input('Digite o valor a ser depositado: ')
        saldo, extrato = deposito(valor_deposito, saldo, extrato)

    elif opcao == 's':
        valor_saque = input('Digite o valor a ser sacado: ')
        saldo, extrato, numero_saques = saque(valor=valor_saque,
                                        quantia_maxima_saque=quantia_maxima_saque,
                                        saldo=saldo,
                                        extrato=extrato,
                                        numero_saques=numero_saques,
                                        limite_de_saques=LIMITE_SAQUES)
    elif opcao == 'e':
        verifica_extrato(saldo, extrato=extrato)
    elif opcao == 'c':
        criar_usuario(usuarios)
    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada')
