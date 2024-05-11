import heapq

class FilaDePrioridades:
    def __init__(self):
        self.fila = []
        self.prioridades = {1: "Prioridade Crítica", 
                            2: "Prioridade Alta", 
                            3: "Prioridade Média", 
                            4: "Prioridade Baixa"}

    def enfileirar(self, dado, prioridade):
        heapq.heappush(self.fila, (prioridade, dado))

    def desenfileirar(self):
        if self.fila:
            return heapq.heappop(self.fila)[1]
        else:
            return None

    def desenfileirar_prioridade(self, prioridade):
        tarefas_restantes = []
        tarefa_removida = None
        for p, dado in self.fila:
            if p == prioridade and tarefa_removida is None:
                tarefa_removida = dado
            else:
                tarefas_restantes.append((p, dado))
        self.fila = tarefas_restantes
        return tarefa_removida

    def listar_tarefas(self, prioridade_desejada):
        return [(dado) 
            for prioridade, dado in self.fila 
                if prioridade == prioridade_desejada]

    def imprimir_tarefas(self, tarefas):
        for dado in tarefas:
            print(dado)

fila_prioridades = FilaDePrioridades()
fila_prioridades.enfileirar("Jogar CS", 1)  # Prioridade Crítica
fila_prioridades.enfileirar("Jogar LOL", 2) # Prioridade Alta
fila_prioridades.enfileirar("Jogar VAVA", 2) # Prioridade Alta
fila_prioridades.enfileirar("Jogar FIFA", 1) # Prioridade Crítica

print("Tarefas com Prioridade Crítica (1):")
tarefas_criticas = fila_prioridades.listar_tarefas(1)
fila_prioridades.imprimir_tarefas(tarefas_criticas)

tarefa_removida = fila_prioridades.desenfileirar_prioridade(1)
print("Tarefa removida:", tarefa_removida)

print("\nTarefas restantes:")
tarefas_restantes = fila_prioridades.listar_tarefas(1)
fila_prioridades.imprimir_tarefas(tarefas_restantes)


print("\nTarefas com Prioridade Alta (2):")
tarefas_altas = fila_prioridades.listar_tarefas(2)
fila_prioridades.imprimir_tarefas(tarefas_altas)


