class MultiploSoma:
    def __init__(self, limite):
        self.limite = limite

    def calcular_soma(self):
        return sum(num for num in range(self.limite) if num % 3 == 0 or num % 5 == 0)

num = int(input("Digite um número: "))
soma = MultiploSoma(num)  
print(f"A soma dos multiplos de 3 ou 5 abaixo de {num} é {soma.calcular_soma()}")
