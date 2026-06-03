class CofreDoDragao:
    def __init__(self, nome_dragao, tesouros):
        self.nome_dragao = nome_dragao
        self.tesouros = tesouros

    def adicionar_item(self, nome, valor):
        if nome != "" and valor > 0:
            tesouro_novo = {
                "nome": nome,
                "valor": valor
            }
            self.tesouros.append(tesouro_novo) 
            return "Adicionado!!!"
        
        else:
            return "Não foi possível"
        
    def listar_itens(self):
        i = 1
        for item in self.tesouros:
            print(f"{i} - {item['nome']}: {item['valor']} moedas")
            i += 1   

    def encontrar_item_mais_valioso(self):
        if not self.tesouros:
            return "O cofre está vazio."

        maior_tesouro = self.tesouros[0]
        for item in self.tesouros:
            if item["valor"] > maior_tesouro["valor"]:
                maior_tesouro = item

        return f"O maior tesouro é {maior_tesouro['nome']} valendo {maior_tesouro['valor']}" 

    def classificar_colecao(self):
        total = 0
        for item in self.tesouros:
            total += item["valor"]

        if total < 500:
            return "coleção pequena"
        
        elif total <= 1500:
            return "coleção respeitável"
        
        else:
            return "coleção lendária"

    def exibir_relatorio(self):
        total = 0
        for item in self.tesouros:
            total += item["valor"]
            
        print(f"Dragão: {self.nome_dragao}")
        print(f"Total Acumulado: {total}")
        print(self.encontrar_item_mais_valioso())
        print(f"Classificação: {self.classificar_colecao()}")