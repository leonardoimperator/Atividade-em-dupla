class CapsulaDoTempo:
    def __init__(self, autor, mensagem, ano_abertura, ano_atual):
        self.autor = autor
        self.mensagem = mensagem
        self.ano_abertura = ano_abertura
        self.ano_atual = ano_atual

    def pode_abrir(self):
        if self.ano_abertura == self.ano_abertura:
            return "Pode abrir a capsula"
        
        else:
            return "Não pode abrir a capsula"
        
    def calcular_espera(self):
        calculo = self.ano_abertura - self.ano_atual
        return f"vai demorar {calculo} ano"

    def classificar_espera(self):
        if self.calcular_espera == 0:
            return "Pode abrir agora"
        
        elif (self.calcular_espera > 1) and (self.calcular_espera < 3):
            return "Espera curta"
        
        else:
            return "Espera longa"
        
    def exibir_resumo(self):
        return f"O autor: {self.autor} colocou a mensagem '{self.mensagem}' para ser aberta {self.ano_abertura} entretando ainda é {self.ano_atual}"
    
capsula = CapsulaDoTempo("Leonardo", "Mude enquanto tem tempo", 2027, 2026)

print(capsula.calcular_espera())
print(capsula.classificar_espera)
print(capsula.pode_abrir())
print(capsula.exibir_resumo())