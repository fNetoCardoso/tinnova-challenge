class Eleicao:
    
    def __init__(self, total_eleitores, validos, brancos, nulos):
        self.total_eleitores = total_eleitores
        self.validos = validos
        self.brancos = brancos
        self.nulos = nulos

    def percentual_validos(self):
        return (self.validos / self.total_eleitores) * 100

    def percentual_brancos(self):
        return (self.brancos / self.total_eleitores) * 100

    def percentual_nulos(self):
        return (self.nulos / self.total_eleitores) * 100


eleicao = Eleicao(total_eleitores=1000, validos=800, brancos=150, nulos=50)

print(f"Percentual de votos válidos: {eleicao.percentual_validos():.2f}%")
print(f"Percentual de votos brancos: {eleicao.percentual_brancos():.2f}%")
print(f"Percentual de votos nulos: {eleicao.percentual_nulos():.2f}%")
