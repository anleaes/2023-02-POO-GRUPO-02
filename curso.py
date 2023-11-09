class Curso:
    def __init__(self,curso,capacidade,local):
        self.curso = curso
        self.capacidade = capacidade
        self.local = local
        self.alunos = []

    def inscrever(self,aluno):
        if len(self.alunos) < self.capacidade:
            self.alunos.append(aluno)
            print(f"Parabéns {aluno.nome}, você foi inscrito no curso {self.curso}")
        else:
            print(f"Desculpe {aluno.nome} mas já estão esgotadas as vagas")
    
    def printAlunos(self):
        print(f"Alunos inscritos no curso {self.curso}:")
        for aluno in self.alunos:
            print("-"+aluno.nome)
            


        
    