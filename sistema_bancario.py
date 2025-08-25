from datetime import datetime, date
from abc import ABC, abstractmethod
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova Conta
[lc] Listar Contas
[nu] Novo Usuário
[q] Sair

=> """

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor_saldo):
        self._saldo = valor_saldo
        
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        if valor > self._saldo:
            print('Saldo insucifiente!')
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        else:
            print('Valor inválido!')
        return False
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('Depósito realizado com sucesso!')
            return True
        else:
            print('Valor inválido!')
        return False
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        
    def sacar(self, valor):
        limite = self._limite
        limite_saques = self._limite_saques
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__])
        
        if valor > limite:
            print('O valor excede o limite por saque!')
        elif numero_saques >= limite_saques:
            print('Limite diário de saques excedido!')
        else:
            return super().sacar(valor)
        return False
    def __str__(self):
        return f'Agência: {self.agencia} \n C/C: {self.numero} \n Titular: {self.cliente.nome}'         
class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self._contas.append(conta)  
class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
    @property
    def cpf(self):
        return self._cpf
    @property
    def nome(self):
        return self._nome      
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass  
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)    
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)   
class Historico:
    def __init__(self):
        self._transacoes = []   
    @property
    def transacoes(self):
        return self._transacoes
    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor,
                'data': datetime.now()
            }
        )
def verifica_usuario_cadastrado(cpf, lista_usuarios):
    usuario_encontrado = {}
    for usuario in lista_usuarios:
        if cpf == usuario.cpf:
            usuario_encontrado = usuario
    return usuario_encontrado
def filtrar_contas_por_usuario(cpf, lista_contas):
    contas_do_usuario = [conta for conta in lista_contas if conta.cliente.cpf == cpf]
    if not contas_do_usuario:
        print('Este usuário ainda não possui contas cadastradas!')
    return contas_do_usuario
def selecionar_conta(numero_da_conta, lista_de_contas):
    for conta in lista_de_contas:
        if conta.numero == numero_da_conta:
            return conta
        
    
    

def main():
    usuarios = []
    contas = []
    while True:
        opcao = input(menu)
        if opcao == 'nu':
            cpf = input('digite seu cpf: ')
            if not cpf.isdigit():
                print("CPF inválido!")
            elif verifica_usuario_cadastrado(cpf, usuarios):
                print('Usuário já cadastrado!')
            else:
                nome = input('digite seu nome: ')
                endereco = input('digite seu endereço: ')
                data_nascimento = input('digite sua data de nascimento: ')
                usuarios.append(PessoaFisica(
                    endereco, cpf, nome, data_nascimento
                ))
        if opcao == 'nc':
            cpf = input('Informe o CPF do cliente: ')
            if verifica_usuario_cadastrado(cpf, usuarios):
                numero_conta = len(contas) + 1
                usuario = verifica_usuario_cadastrado(cpf, usuarios)
                nova_conta = ContaCorrente.nova_conta(numero_conta, usuario)
                contas.append(nova_conta)
            else:
                print('Usuário não cadastrado!')
        if opcao == 'lc':
            cpf = input('Inform o CPF do usuário ')
            if verifica_usuario_cadastrado(cpf, usuarios):
                contas_do_usuario = filtrar_contas_por_usuario(cpf, contas)
                if contas_do_usuario:
                    for conta in contas_do_usuario:
                        print(conta)
            else:
                print('Usuário não cadastrado!')
        if opcao == 'd':
            cpf = input('Informe o CPF do cliente: ')
            if verifica_usuario_cadastrado(cpf, usuarios):
                contas_do_usuario = filtrar_contas_por_usuario(cpf, contas)
                if len(contas_do_usuario) == 0:
                    print('Este usuário não possui nenhuma conta cadastrada!')
                else:
                    numero_da_conta = int(input('Digite o número da conta em que deseja fazer a operação: '))
                    conta_selecionada = selecionar_conta(numero_da_conta, contas)
                    if conta_selecionada:
                        valor_do_deposito = float(input('Deigite o valor que deseja depositar: '))
                        Deposito(valor_do_deposito).registrar(conta_selecionada)
                    else:
                        print('Número de conta inválido!')       
            else:
                print('Usuário não cadastrado')
        if opcao == 'e':
            cpf = input('Informe o CPF do cliente: ')
            if verifica_usuario_cadastrado(cpf, usuarios):
                contas_usuario = filtrar_contas_por_usuario(cpf, contas)
                for conta in contas_usuario:
                    print(f"Extrato da conta número {conta.numero}")
                    lista_de_transacoes = conta.historico.transacoes
                    for transacao in lista_de_transacoes:
                        print(f"Tipo: {transacao['tipo']}, Valor: {transacao['valor']}, Data: {transacao['data']} ")
                    print(f"Saldo: {conta.saldo}")
            else:
                print('Usuário não possui contas cadastradas')             
        if opcao == 's':
            cpf = input('Informe o CPF do cliente: ')
            if verifica_usuario_cadastrado(cpf, usuarios):
                contas_do_usuario = filtrar_contas_por_usuario(cpf, contas)
                if len(contas_do_usuario) == 0:
                    print('Este usuário não possui nenhuma conta cadastrada!')
                else:
                    numero_da_conta = int(input('Digite o número da conta em que deseja fazer a operação: '))
                    conta_selecionada = selecionar_conta(numero_da_conta, contas)
                    if conta_selecionada:
                        valor_do_saque = float(input('Deigite o valor que deseja sacar: '))
                        Saque(valor_do_saque).registrar(conta_selecionada)
                    else:
                        print('Número de conta inválido!')       
            else:
                print('Usuário não cadastrado')        
        if opcao == 'q':
            break    
        
main()
        
    




