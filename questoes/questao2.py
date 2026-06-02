class Portal_dimensional:
    def __init__(self, nome, destino, energia_necessaria, energia_disponivel):
        self.nome=nome
        self.destino=destino
        self.energia_necessaria=energia_necessaria
        self.energia_disponivel=energia_disponivel
    def pode_abrir(self):
        if self.energia_necessaria<= self.energia_disponivel:
            print("O portal pode ser aberto")
        else:
            print("O portal não pode ser aberto. motivo: falta de energia")
    def calcular_falta_energia(self):
        if self.energia_disponivel<self.energia_necessaria:
            energia_falta=self.energia_necessaria-self.energia_disponivel
            print(f"Para acessar o portal é necessário +{energia_falta} de energia.")
        else:
            return 0        
    def classificar_estabilidade(self):
        energia_falta=self.energia_necessaria-self.energia_disponivel
        if self.energia_necessaria<= self.energia_disponivel:
            return "portal estável"
        elif energia_falta>=0 and energia_falta<=20:
            return"Portal quase estável"
        else:
            return "Portal instável"
    def exibir_resumo(self):
        print(f"O portal: {self.nome} com o destino: {self.destino}, tem como energia necessária: {self.energia_necessaria}.")
        print(f"Você tem:{self.energia_disponivel} de energia disponivel e a situação para você acessar o portal é: {self.classificar_estabilidade()}")
portal1=Portal_dimensional("Nedder", "minecraft", 50, 40)

portal1.calcular_falta_energia()
portal1.classificar_estabilidade()
portal1.pode_abrir()
portal1.exibir_resumo()

portal2=Portal_dimensional("Metropo", "metrópolis", 30, 40)
portal2.calcular_falta_energia()
portal2.classificar_estabilidade()
portal2.pode_abrir()
portal2.exibir_resumo()