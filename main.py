from models.usuario import Usuario
from models.tarefa import Tarefas
from models.projeto import Projeto


print("\n=== STARTERBOX ===")


usuario = Usuario("Gabriel", "gabriel@email.com")

projeto = Projeto("StarterBox", usuario)


tarefa1 = Tarefas(
    "Criar projeto",
    "Criando o projeto StarterBox em Python",
    "Alta",
    "25/05/2026"
)

tarefa2 = Tarefas(
    "Implementar banco",
    "Criar conexão com SQLite",
    "Média",
    "30/05/2026"
)


projeto.adicionarTarefa(tarefa1)
projeto.adicionarTarefa(tarefa2)


tarefa1.concluir()


usuario.exibirDados1()

projeto.listarTarefas()