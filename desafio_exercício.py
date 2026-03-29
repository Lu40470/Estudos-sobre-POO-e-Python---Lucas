from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import date

class conta:
    def __init__(self,saldo:float,numero:int,agencia:str,cliente:Cliente, historico:Histórico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico
    def saldo(self):
        return self._saldo
    @classmethod
    def nova_conta(conta,_cliente,_numero):
        return conta(_cliente,_numero)
    def depositar(self,valor):
        return 
        self._saldo +=valor
        print(f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${self._saldo}")
    def sacar(self,valor):
        return 
        if _saldo>=valor:
            self._saldo -=valor
            print(f"Saque de R$ {valor} realizado com sucesso. Saldo atual: R${self._saldo}")
class Cliente(conta):
    def __init__(self,nome,endereço:str,saldo,numero,agencia,cliente, historico,contas:list):   
        self._contas =contas.append(object)
        self._endereço = endereço
    def realizar_transacao(self,conta,transacao:transacao):
        while texto !="3":
            texto = input("Digite o tipo de transação (1 - Depósito, 2 - Saque, 3 - Sair): ")
            if texto == "1":
                valor = float(input("Digite o valor do depósito: "))
                transacao.Deposito(valor)
                continue
            elif texto == "2":
                valor = float(input("Digite o valor do saque:"))
                if valor > conta.saldo():
                    print("Saldo insuficiente para realizar o saque.")
                    continue
                else:
                    transacao.Sacar(valor)
                    continue
            elif texto == "3":
                print("Saindo do sistema de transações.")
                break
            else:
                print("Opção inválida. Por favor, digite 1, 2 ou 3.")
    def adicionar_conta(self,conta:conta):
        texto2 = input("Deseja adicionar uma nova conta? (s/n): ")
        if texto2.lower() == "s":
            transacao.registra_conta(conta)
class Histórico(conta):
    def adicionar_transacao(self, transacao:transacao):
        pass
class ContaCorrente(conta):
    def __init__(self,saldo,numero,agencia,cliente,historico, limite:float,limite_saque:int):
        self._limite = limite
        self._limite_saque = limite_saque
class PessoaFísica(Cliente):
    def __init__(self,nome:str,endereço,saldo,numero,agencia,cliente,Histórico,cpf:str,data_nascimento:date):
        self._cpf = cpf
        self._data_nascimento =data_nascimento
class transacao(ABC):
    @abstractmethod
    def registra_conta(self, conta:conta):
        texto3 = input("Digite os dados da sua conta: ")
        self._contas.append(conta)
    @abstractmethod
    def Deposito(self,valor:float):
        self._saldo.append(valor)
    @abstractmethod
    def Sacar(self,valor:float):
        self._saldo.append(-valor)