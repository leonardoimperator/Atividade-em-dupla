class RoboColetor:
    def __init__(self, nome, amostras, capacidade_maxima):
        self.nome = nome
        self.amostras = amostras
        self.capacidade_maxima = capacidade_maxima

    def adicionar_amostra(self, amostra):
        if len(self.amostras) < self.capacidade_maxima:
            self.amostras.append(amostra)   
            return ("Coletado") 

        else:  
            return ("Não coletado")
        
    def listar_amostras(self):
        if len(self.amostras) >= self.capacidade_maxima:
            return "Impossível"
        
        else:    
            i = 1
            for amostra in self.amostras:
                print(f"{i} - {amostra}")
                i += 1

    def contar_amostras(self):
        return f"{len(self.amostras)} amostras"
    
    def verificar_armazenamento(self):
        if self.amostras >= self.capacidade_maxima:
            return "Cheio"
        
        else:
            return "Possui espaço"
        
    def exibir_relatorio(self):
        return f"O robô {self.nome} coletou {self.amostras} tendo a capacidade máxima de {self.capacidade_maxima} amostras" 

robo = RoboColetor("Bob", [], 10) 

print(robo.adicionar_amostra("cebola"))
print(robo.adicionar_amostra("boletim cheio de notas zerada do leo"))
robo.listar_amostras()
print(robo.contar_amostras())
print(robo.exibir_relatorio())