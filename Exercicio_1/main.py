from pessoa_fisica import Pessoa_fisica
from pessoa_juridica import Pessoa_juridica
from curso import Curso

pessoa_1 = Pessoa_fisica("Fulano",20,"Voluntário da Pátria,300",123456789,"fulano@gmail.com")
pessoa_2 = Pessoa_fisica("Leonardo",30,"Av.Ipiranga,48",9033045830,"leonardo@gmail.com")

empresa_1 = Pessoa_juridica("Microsoft",10,"Av. California,1200",1000984350,"microsoft@microsoft.com")
empresa_2 = Pessoa_juridica("SpaceX",23,"Av. Universe,2300",23423905409,"spacex@spacex.com.")

curso_1 = Curso("Web",2,"Zona sul")
curso_2 = Curso("POO",2,"Fapa")

curso_1.inscrever(pessoa_1)
curso_1.inscrever(empresa_1)
curso_2.inscrever(pessoa_2)
curso_2.inscrever(empresa_2)
curso_2.inscrever(empresa_1)

curso_1.printAlunos()