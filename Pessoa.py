"""
Problema: Crie uma classe "Pessoa" que represente uma pessoa, com os atributos "nome" e "idade".

Classe a ser criada: Pessoa

Métodos a serem criados: construtor (init) que recebe nome e idade como
parâmetros e atribui aos atributos da classe; método "getNome" que retorna o nome
da pessoa; método "getIdade" que retorna a idade da pessoa.

Instruções: Crie um objeto da classe "Pessoa" com nome "João" e idade "25".
Imprima o nome e idade da pessoa usando os métodos criados.
"""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade
    

pessoa1 = Pessoa("João", 25)
print("Nome: {}\nIdade: {}".format(pessoa1.getNome(),pessoa1.getIdade()))