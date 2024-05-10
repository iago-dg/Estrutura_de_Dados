class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class FilaDeTarefas:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enfileirar(self, dado):
        novo_nó = No(dado)
        if not self.inicio:
            self.inicio = novo_nó
            self.fim = novo_nó
        else:
            self.fim.proximo = novo_nó
            self.fim = novo_nó

    def desenfileirar(self):
        if not self.inicio:
            return None
        else:
            dado = self.inicio.dado
            self.inicio = self.inicio.proximo
            return dado

    def olhar(self):
        if not self.inicio:
            return None
        else:
            return self.inicio.dado

    def está_vazia(self):
        return self.inicio is None

    def listar_tarefas(self):
        tarefas = []
        atual = self.inicio
        while atual:
            tarefas.append(atual.dado)
            atual = atual.proximo
        return tarefas

Estudante = FilaDeTarefas()
Estudante.enfileirar("Jogar CS")
Estudante.enfileirar("Jogar LOL")
Estudante.enfileirar("Jogar FIFA")

print(Estudante.listar_tarefas())

Estudante.desenfileirar()
print(Estudante.listar_tarefas())
