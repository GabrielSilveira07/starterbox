from models.usuario import Usuario  ##importando a classe Usuario
from models.tarefa import Tarefas   ##importando a classe Tarefas
from models.projeto import Projeto  ##importando a classe Projeto

usuario = Usuario("Gabriel", "gabriel@email.com")   ##define o usuario como Gabriel e seu email 

projeto = Projeto("StarterBox", usuario)    ##define o projeto como StarterBox para o usuario Gabriel

tarefa1 = Tarefas("Criar projeto", "criando o projeto starterbox em python")    ##define que a tarefa é Criar Projeto junto da descrição

projeto.adicionarTarefa(tarefa1)    ##agrega a tarefa1 ao projeto

tarefa1.concluir()  ##conclui a tarefa1

usuario.exibirDados1()  ##exibe os dados do usuario

projeto.listarTarefas() ##lista as tarefas do projeto