from pessoa_fisica import Pessoa_fisica

class Pessoa_juridica(Pessoa_fisica):
    def __init__(self, nome, idade, endereco,doc,email):
        super().__init__(nome, idade, endereco,doc,email)
        self.doc = doc
        self.email = email
        self.funcionario = []
    
    def add_funcionario(self, funcionario):
        self.funcionario.append(funcionario)
        print(f"Você foi contratado {funcionario.nome}!")