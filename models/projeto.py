class Projeto:
    
    def __init__(self, nome, usuario):
        self.nome = nome
        self.usuario = usuario
        self.tarefas = []   ##recebe as tarefas

    def adicionarTarefa(self, tarefa):  ##cria o dicionario de tarefas do projeto
        self.tarefas.append(tarefa)

    def listarTarefas(self):    ##printa as tarefas listadas do projeto
        print(f"\nProjeto: {self.nome}")

        for tarefa in self.tarefas: ##exibe todas as tarefas listas no projeto
            tarefa.exibirTarefa()
