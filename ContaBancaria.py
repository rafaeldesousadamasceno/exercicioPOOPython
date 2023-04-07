"""
Problema: Crie uma classe "ContaBancaria" que represente uma conta bancária, com os atributos "saldo" e "titular".

Classe a ser criada: ContaBancaria

Métodos a serem criados: construtor (init) que recebe o titular como parâmetro e
atribui ao atributo da classe, inicializando o saldo com zero; método "depositar" que
recebe um valor como parâmetro e adiciona ao saldo da conta; método "sacar" que
recebe um valor como parâmetro e subtrai do saldo da conta, se o saldo for
suficiente; método "consultarSaldo" que retorna o saldo da conta.

Instruções: Crie um objeto da classe "ContaBancaria" com titular "Maria". Deposite
100 reais na conta e depois faça um saque de 50 reais. Imprima o saldo da conta
usando o método "consultarSaldo".
"""
class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return self.saldo
    
    def sacar(self, valor):
        if (valor > self.saldo):
            return print("Saldo insuficiente para realizar a transação!")
        else:
            self.saldo = self.saldo - valor
            return self.saldo
    
    def consultarSaldo(self):
        return print("Saldo:", self.saldo)
    

conta1 = ContaBancaria("Rafael Damasceno")
conta1.consultarSaldo() #Saldo: 0
conta1.depositar(1500) #Saldo: 1500
conta1.sacar(2000) #SALDO INSUFICIENTE
conta1.sacar(500) #1500 - 500 = 1000
conta1.consultarSaldo() #Saldo: 1000
conta1.depositar(399) #1000 + 399 = 1399
conta1.consultarSaldo() #Saldo: 1399