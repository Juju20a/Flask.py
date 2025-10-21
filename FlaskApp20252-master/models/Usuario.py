class Usuario():
    def __init__(self, id, nome, cpf, nascimento):
        # Inicializa os atributos do usuário
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento

    def __repr__(self):
        # Representação do usuário para depuração
        return f'<Usuario {self.nome}, {self.cpf}, {self.nascimento}>'

    def to_json(self):
        # Converte os atributos principais para um dicionário JSON
        return {"id": self.id, "nome": self.nome, "cpf": self.cpf, "nascimento": self.nascimento}

    def get(self, key):
        # Retorna o valor de um atributo com base na chave fornecida
        return getattr(self, key, None)


print(__name__)
if __name__ == "__main__":
    # Teste básico da classe Usuario
    usuario = Usuario(1, "João", "00011122233", "2025-10-09")
    print(usuario)
