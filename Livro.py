"""
Problema: Crie uma classe "Livro" que represente um livro, com os atributos "titulo", "autor" e "ano".

Classe a ser criada: Livro

Métodos a serem criados: construtor (init) que recebe o título, autor e ano como
parâmetros e atribui aos atributos da classe; método "getTitulo" que retorna o título
do livro; método "getAutor" que retorna o autor do livro; método "getAno" que
retorna o ano do livro.

Instruções: Crie um objeto da classe "Livro" com título "O Senhor dos Anéis", autor
"J.R.R. Tolkien" e ano "1954". Imprima o título, autor e ano do livro usando os
métodos criados.
"""
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def getTtulo(self):
        return print("Título:",self.titulo)
    
    def getAutor(self):
        return print("Autor:",self.autor)
    
    def getAno(self):
        return print("Ano:",self.ano)
    
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro1.getTtulo()
livro1.getAutor()
livro1.getAno()