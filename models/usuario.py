class Usuario:

    def __init__(self, nome, email):
        self.__nome = nome 
        self.__email = email

    def getNome(self):  ##faz o get de nome
        return self.__nome
    
    def getEmail(self):     ##faz o get de email
        return self.__email 
    
    def setEmail(self, email):      ##faz a validação do email
        if "@" in email:
            self.__email = email    ##se o email conter @, OK
        else:
            print (f"Email inválido")   ##sem @, ERRO

    def exibirDados1(self): ##função exibir dados
        print(f"Usuario: {self.__nome}")
        print(f"Email: {self.__email}")

        