class pokemon:
    def __init__(self, nome, tipo, hp):
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.fora_de_combate = False

    #def atacar(self, oponente, miss, critico):