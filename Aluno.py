"""
Problema: Crie uma classe "Aluno" que represente um aluno, com os atributos "nome", "matrícula" e "notas".

Classe a ser criada: Aluno

Métodos a serem criados: construtor (init) que recebe o nome e a matrícula como
parâmetros e atribui aos atributos da classe, inicializando a lista de notas com uma
lista vazia; método "adicionarNota" que recebe uma nota como parâmetro e adiciona
à lista de notas do aluno; método "calcularMedia" que calcula a média das notas do
aluno e retorna o resultado.

Instruções: Crie um objeto da classe "Aluno" com nome "Ana" e matrícula "12345".
Adicione notas 7, 8 e 9 ao objeto criado usando o método "adicionarNota". Calcule e
imprima a média das notas do aluno usando o método "calcularMedia".
"""
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionarNota(self, nota):
        self.notas.append(nota)

    def calcularMedia(self):
        soma = 0
        for nota in self.notas:
            soma += nota
        return print("Aluna: {}\nMédia: {:.2f}".format(self.nome, soma / len(self.notas)))
    
aluno1 = Aluno("Ana", "12345")
aluno1.adicionarNota(7)
aluno1.adicionarNota(8)
aluno1.adicionarNota(9)
aluno1.calcularMedia()