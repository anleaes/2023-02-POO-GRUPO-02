class Pessoa_fisica:
    def __init__(self,nome,idade,endereco,doc,email):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco 
        self.doc = doc
        self.email = email 
    
    #Getters
    def getNome(self):
        return self.nome
    def getIdade(self):
        return self.idade
    def getEndereco(self):
        return self.endereco
    def getCpf(self):
        return self.doc
    def getEmail(self):
        return self.email
    
    #Setters
    def setNome(self,nome):
        self.nome = nome
    def setIdade(self,idade):
        self.idade = idade
    def setEndereco(self,endereco):
        self.endereo = endereco
    def setCpf(self,doc):
        self.cpf = doc
    def setCpf(self,email):
        self.email = email
    
    #Print
    def printData(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Endereço: {self.endereco}")
        print(f"CPF: {self.doc}")
        print(f"Email: {self.email}")
