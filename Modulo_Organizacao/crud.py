class Tarefa():
    def __init__(self):
        self.lista_tarefa = []
        
    def adicionar_tarefa(self):
        nome_tarefa = input('Digite o nome da tarefa: ')
        self.lista_tarefa.append(nome_tarefa)

    def renomear_tarefa(self):
        renome = input('Qual tarefa deseja renomear? ')
        if renome in self.lista_tarefa:
            indice = self.lista_tarefa.index(renome)
            novo_nome = input('Digite o novo nome da tarefa: ')
            self.lista_tarefa[indice] = novo_nome
            print(f'Tarefa "{renome}" renomeada para "{novo_nome}"')
        else:
            print(f'Tarefa "{renome}" não encontrada.')

    def excluir_tarefa(self):
        excluir = input('Qual tarefa deseja excluir? ')
        if excluir in self.lista_tarefa:
            self.lista_tarefa.remove(excluir)
            print(f'Tarefa "{excluir}" excluída com sucesso.')

    def listar_tarefa(self):
        if not self.lista_tarefa:
            print('Lista de tarefas vazia.')
        else:
            print('Lista de Tarefas:')
            for indice, tarefa in enumerate(self.lista_tarefa):
                print(f'{indice + 1}. {tarefa}')


tarefa = Tarefa()

tarefa.adicionar_tarefa()
tarefa.adicionar_tarefa()
tarefa.adicionar_tarefa()

tarefa.renomear_tarefa()
tarefa.excluir_tarefa()

tarefa.listar_tarefa()
            
