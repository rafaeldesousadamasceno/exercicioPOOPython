"""
Problema: Crie uma classe "Círculo" que represente um círculo, com o atributo "raio".

Classe a ser criada: Círculo

Métodos a serem criados: construtor (init) que recebe o raio como parâmetro e
atribui ao atributo da classe; método "calcularArea" que retorna a área do círculo;
método "calcularCircunferencia" que retorna a circunferência do círculo.

Instruções: Crie um objeto da classe "Círculo" com raio igual a 5. Calcule e imprima
a área e circunferência do círculo usando os métodos criados.
"""
class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.PI = 3.14159265358979323846

    def calcularArea(self):
        return (self.PI * (self.raio**2))
    
    def calcularCircunferencia(self):
        return (2 * self.PI) * self.raio
    
circulo1 = Circulo(5)
print("Área: {:.2f}\nCircunferência: {:.2f}"
      .format(circulo1.calcularArea(), circulo1.calcularCircunferencia()))