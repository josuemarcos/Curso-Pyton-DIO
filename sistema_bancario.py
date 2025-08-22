from datetime import datetime, date
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova Conta
[lc] Listar Contas
[nu] Novo Usuário
[q] Sair

=> """




def deposito(valor, saldo, extrato, /):  
    if valor.isdigit() and float(valor) > 0:
        valor_numerico = float(valor)
        saldo += valor_numerico
        extrato.append(f'Operação - Depósito; Valor - {valor_numerico}; Realizada em {datetime.now()}') 
        print('--Depósito realizado com sucesso!--')
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
                print('--Saque realizado com sucesso!--') 
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

def verifica_extrato(saldo, /, *, extrato):
    print('Histórico de operações:')
    for transacao in extrato:
        print(transacao)
    print(f'Saldo atual: R$ {saldo:.2f}')
    
def verifica_usuario_cadastrado(cpf, lista_usuarios):
    usuario_encontrado = {}
    for usuario in lista_usuarios:
        if cpf == usuario.get('cpf'):
            usuario_encontrado = usuario
    return usuario_encontrado

def filtrar_contas_por_cpf(cpf, lista_de_contas):
    contas_encontradas = []
    for conta in lista_de_contas:
        if cpf == conta.get('cpf'):
            contas_encontradas.append(conta)
    return contas_encontradas

def solicita_endereco():
    print('---ENDEREÇO---')
    logradouro = input('Digite o Logradouro do usuário: ')
    numero = input('Digite o Numero da casa do usuário: ')
    bairro = input('Digite o bairro do usuário: ')
    cidade = input('Digite a cidade do usuário: ')
    estado = input('Digite a sigla do estado do usuário: ')
    endereco = f'{logradouro}, {numero} - {bairro} - {cidade}/{estado}'
    return endereco

def cria_numero_conta(lista_contas):
    numero_conta = len(lista_contas) + 1
    return numero_conta

def criar_conta(lista_de_contas, lista_de_usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = verifica_usuario_cadastrado(cpf, lista_de_usuarios)
    if usuario:
        numero_conta = cria_numero_conta(contas)
        conta = {
            'agencia': '0001',
            'numero_conta': numero_conta,
            'usuario': usuario['nome'],
            'cpf': usuario['cpf']
        }
        lista_de_contas.append(conta)
        print('Conta criada com sucesso!')
    else:
        print("Usuário não cadastrado na base de dados!")
    return lista_de_contas
        
def criar_usuario(lista):
    cpf = input('Digite o CPF do usuário: ')
    if not cpf.isdigit():
        print("CPF inválido!")
    elif verifica_usuario_cadastrado(cpf, lista):
        print('Usuário já cadastrado!')
    else:
        nome = input('Digite o nome do usuário: ')
        data_nascimento = input('Digite a data de nascimento do usuário: ')
        endereco = solicita_endereco()
        novo_usuario = {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'cpf': cpf,
            'endereco': endereco
        }
        lista.append(novo_usuario)
        print('Usuário Cadastrado com Sucesso!')
    return lista

def listar_contas(lista_de_contas, lista_de_usuarios):
    cpf = input('Digite o CPF do usuário: ')
    if verifica_usuario_cadastrado(cpf, lista_de_usuarios):
        contas = filtrar_contas_por_cpf(cpf, lista_de_contas)
        if contas:
            for conta in contas:
                print(f"Agência: {conta['agencia']} - Número da conta: {conta['numero_conta']} - Titular: {conta['usuario']}")
        else:
            print('Este usuário não possui contas cadastradas!')
    else:
        print('Usuário não cadastrado na base de dados!')
    

def main():
    saldo = 300
    quantia_maxima_saque = 500
    extrato = []
    usuarios = []
    contas = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    LIMITE_OPERACOES = 10    
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
        elif opcao == 'nu':
            usuarios = criar_usuario(usuarios)
        elif opcao == 'nc':
            contas = criar_conta(contas, usuarios)
        elif opcao == 'lc':
            listar_contas(contas, usuarios)
        elif opcao == 'q':
            break
        else:
            print('Operação inválida, por favor selecione novamente a operação desejada')


main()