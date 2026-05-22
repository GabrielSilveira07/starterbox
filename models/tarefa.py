class Tarefas:
    def __init__(self, titulo, descricao, prioridade, prazo):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self.concluida = False

    def concluir(self): ##define tarefa concluída como True
        self.concluida = True

    def exibirTarefa(self):     
        ##exibe a tarefa com seus atributos

        status = "Concluída" if self.concluida else "Pendente"

        print(f"Tarefa: {self.titulo}")
        print(f"Descrição: {self.descricao}")
        print(f"Prioridade: {self.prioridade}")
        print(f"Prazo de conclusão: {self.prazo}")
        print(f"Status: {self.concluida}")