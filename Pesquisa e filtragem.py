class Tarefa:
    def __init__(self, titulo, descricao, prioridade):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade

class FilaDePrioridades:
    def __init__(self):
        self.fila = []

    def enfileirar(self, item, prioridade):
        for i, t in enumerate(self.fila):
            if t[1].prioridade > prioridade:
                self.fila.insert(i, (prioridade, item))
                return
        self.fila.append((prioridade, item))

    def adicionar_tarefa(self, tarefa):
        self.enfileirar(tarefa, tarefa.prioridade)

    def pesquisar_tarefas(self):
        consulta = input("Digite o nome da tarefa que deseja pesquisar: ")
        resultados = []
        for _, tarefa in self.fila:
            if consulta in tarefa.titulo or consulta in tarefa.descricao:
                resultados.append(tarefa)
        return resultados


fila_prioridades = FilaDePrioridades()
fila_prioridades.adicionar_tarefa(Tarefa("Jogar CS", "Jogo", 1))
fila_prioridades.adicionar_tarefa(Tarefa("Jogar LOL", "Jogo de Pc", 2))
fila_prioridades.adicionar_tarefa(Tarefa("Jogar VAVA", "Jogo de esportes", 2))
fila_prioridades.adicionar_tarefa(Tarefa("Jogar FIFA", "Jogo de futebol", 1))

resultados_pesquisa = fila_prioridades.pesquisar_tarefas()
for tarefa in resultados_pesquisa:
    print(f"Tarefa: {tarefa.titulo}, Prioridade: {tarefa.prioridade}")