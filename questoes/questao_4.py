class Mochila_de_missao:
    def __init__(self, agente, equipamentos, capacidade_maxima):
        self.agente=agente
        self.capacidade_maxima=capacidade_maxima
        self.equipamentos=equipamentos
    def adicionar_equipamento(self, equipamentos):
        quantidade_equipamento=len(self.equipamentos)
        if  quantidade_equipamento>0 and self.equipamentos<self.capacidade_maxima:
           self.equipamentos.append(equipamentos)
        else:
            print("Adicione um equipamento")
    def listar_equipamentos(self):
        for equipamento in self.equipamentos:
            print(equipamento)
        
    def verificar_espaco(self):
        if len(self.equipamentos)<self.capacidade_maxima:
            return "A mochila ainda possui espaço"
        else:
            return "A mochila não possui mais espaço"
    def exibir_relatorio(self):
        print(f"O agente: {self.agente}, possui em sua mochila: {len(self.equipamentos)} equipamentos.")
        print(f"Sua mochila tem capacidade maxima de: {self.capacidade_maxima} equipamentos e está: {self.verificar_espaco()}")
#----------------------------main------------------------------------

mochila1=Mochila_de_missao("Sérgio",  ["escova", "casaco", "tesoura", "anel", "marmita"], 5)

mochila1.listar_equipamentos()
mochila1.verificar_espaco()
mochila1.exibir_relatorio()

mochila2=Mochila_de_missao("Marcos",  ["escova", "casaco","pente"], 5)

mochila2.listar_equipamentos()
mochila2.verificar_espaco()
mochila2.exibir_relatorio()


