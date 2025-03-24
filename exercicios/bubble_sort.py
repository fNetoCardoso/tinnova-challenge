class BubbleSort:
    def __init__(self, vetor):
        self.vetor = vetor

    def ordenar(self):
        n = len(self.vetor)
        for i in range(n - 1):
            trocou = False
            for j in range(n - 1 - i):
                if self.vetor[j] > self.vetor[j + 1]:
                    self.vetor[j], self.vetor[j + 1] = self.vetor[j + 1], self.vetor[j]
                    trocou = True 
            if not trocou:
                break

    def exibir(self):
        print(self.vetor)


valores = [5, 3, 2, 4, 7, 1, 0, 6]
bubble_sort = BubbleSort(valores)
print("Vetor antes da ordenação:", valores)
bubble_sort.ordenar()
print("Vetor após a ordenação:", valores)
