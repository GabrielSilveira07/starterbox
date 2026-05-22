class Usuario:

    def __init__(self, nome, email):
        self.nome = nome 
        self.email = email

    def exibirDados1(self): ##função exibir dados
        print(f"Usuario: {self.nome}")
        print(f"Email: {self.email}")