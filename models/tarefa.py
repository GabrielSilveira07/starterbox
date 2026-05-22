class Tarefas:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao

    def concluir(self): ##define tarefa concluída como True
        self.concluida = True

    def exibirTarefa(self):     ##exibe a tarefa com titulo e descrição
        print(f"Tarefa: {self.titulo}")
        print(f"Descrição: {self.descricao}")