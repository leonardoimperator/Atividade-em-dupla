class ExpedicaoTemplo:
    def __init__(self, nome_expedicao, desafios, energia_inicial):
        self.nome_expedicao = nome_expedicao
        self.desafios = desafios
        self.energia = energia_inicial
        self.pontos = 0
        self.desafios_concluidos = []

    def listar_desafios(self):
        i = 1
        for desafio in self.desafios:
            print(f"{i} - {desafio['nome']} | Custo: {desafio['custo']} | Recompensa: {desafio['energia']}")
            i += 1

    def tentar_desafio(self, numero_desafio):
        indice = numero_desafio - 1

        if indice < 0 or indice >= len(self.desafios):
            return "Número de desafio inválido."

        desafio_escolhido = self.desafios[indice]

        if desafio_escolhido in self.desafios_concluidos:
            return "Este desafio já foi concluído."

        if self.energia >= desafio_escolhido["custo"]:
            self.energia -= desafio_escolhido["custo"]
            self.pontos += desafio_escolhido["energia"]
            self.desafios_concluidos.append(desafio_escolhido)
            return "Desafio superado!"
        else:
            return "Energia insuficiente."

    def calcular_progresso(self):
        return len(self.desafios_concluidos)

    def verificar_situacao(self):
        if len(self.desafios_concluidos) == len(self.desafios):
            return "expedição concluída"
        elif self.energia == 0:
            return "expedição encerrada sem energia"
        else:
            return "expedição em andamento"

    def exibir_relatorio(self):
        print(f"Expedição: {self.nome_expedicao}")
        print(f"Energia restante: {self.energia}")
        print(f"Pontos acumulados: {self.pontos}")
        print(f"Desafios concluídos: {self.calcular_progresso()}")
        print(f"Situação final: {self.verificar_situacao()}")