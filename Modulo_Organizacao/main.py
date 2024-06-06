import tkinter as tk
from tkinter import messagebox
import heapq

class FilaDePrioridades:
    def __init__(self):
        self.fila = []
        self.tarefas_concluidas = []

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
        return [(dado, prioridade) 
            for prioridade, dado in self.fila 
                if prioridade == prioridade_desejada]

    def listar_todas_tarefas(self):
        return [(dado, prioridade) for prioridade, dado in sorted(self.fila)]

    def tarefa_concluida(self, tarefa):
        for i, (p, dados) in enumerate(self.fila):
            if dados == tarefa:
                del self.fila[i]
                self.tarefas_concluidas.append(tarefa)
                return "A tarefa foi concluída!"
        return "Tarefa não encontrada."

    def buscar_tarefa_por_nome(self, nome):
        return [(dado, prioridade) for prioridade, dado in self.fila if nome.lower() in dado.lower()]

class Tkapp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Tarefas")
        self.root.geometry("800x600")

        self.fila_prioridades = FilaDePrioridades()

        self.style()

    def style(self):
        # cores e fontes
        bg_color = "#f0f0f0"
        fg_color = "#333333"
        button_color = "#4caf50"
        button_fg_color = "#ffffff"
        entry_color = "#ffffff"
        font = ("Arial", 12)

        self.root.configure(bg=bg_color)

        # entrada de tarefas
        self.entrada = tk.Frame(self.root, bg=bg_color)
        self.entrada.pack(pady=10)

        self.tarefa = tk.Label(self.entrada, text="Tarefa:", bg=bg_color, fg=fg_color, font=font)
        self.tarefa.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.entrada_tarefa = tk.Entry(self.entrada, width=50, bg=entry_color, font=font)
        self.entrada_tarefa.grid(row=0, column=1, padx=5, pady=5)

        self.prioridade = tk.Label(self.entrada, text="Prioridade (1-4):", bg=bg_color, fg=fg_color, font=font)
        self.prioridade.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        self.entrada_prioridade = tk.Entry(self.entrada, width=10, bg=entry_color, font=font)
        self.entrada_prioridade.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.botao_tarefa = tk.Button(self.entrada, text="Adicionar Tarefa", command=self.add_task, bg=button_color, fg=button_fg_color, font=font)
        self.botao_tarefa.grid(row=0, column=2, rowspan=2, padx=10, pady=5, sticky=tk.EW)

        # legenda prioridade
        self.legenda = tk.Label(self.entrada, text="1 = Crítica, 2 = Alta, 3 = Média, 4 = Baixa", bg=bg_color, fg=fg_color, font=font)
        self.legenda.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

        # pesquisa de tarefas
        self.pesquisa = tk.Frame(self.root, bg=bg_color)
        self.pesquisa.pack(pady=10)

        self.nome_pesquisa = tk.Label(self.pesquisa, text="Pesquisar Tarefa:", bg=bg_color, fg=fg_color, font=font)
        self.nome_pesquisa.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.entrada_pesquisa = tk.Entry(self.pesquisa, width=30, bg=entry_color, font=font)
        self.entrada_pesquisa.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = tk.Button(self.pesquisa, text="Pesquisar", command=self.search_task, bg=button_color, fg=button_fg_color, font=font)
        self.search_button.grid(row=0, column=2, padx=10, pady=5, sticky=tk.EW)

        self.nome_resultados = tk.Label(self.pesquisa, text="Resultados da Pesquisa:", bg=bg_color, fg=fg_color, font=font)
        self.nome_resultados.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W)

        self.quadro_resultados = tk.Listbox(self.pesquisa, width=70, height=5, bg=entry_color, font=font)
        self.quadro_resultados.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        # quadros de tarefas conc. e pendentes
        self.listagem = tk.Frame(self.root, bg=bg_color)
        self.listagem.pack(pady=10)

        self.pendentes_nome = tk.Label(self.listagem, text="Tarefas Pendentes:", bg=bg_color, fg=fg_color, font=font)
        self.pendentes_nome.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.tarefas_pendentes = tk.Frame(self.listagem, bg=entry_color)
        self.tarefas_pendentes.grid(row=1, column=0, padx=5, pady=5)

        self.tarefas_concluidas = tk.Label(self.listagem, text="Tarefas Concluídas:", bg=bg_color, fg=fg_color, font=font)
        self.tarefas_concluidas.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.lista_tarefas_conc = tk.Listbox(self.listagem, width=50, height=10, bg=entry_color, font=font)
        self.lista_tarefas_conc.grid(row=1, column=1, padx=5, pady=5)

        # remover maior prioridade
        self.remover_maior = tk.Frame(self.root, bg=bg_color)
        self.remover_maior.pack(pady=10)

        self.remover_botao = tk.Button(self.remover_maior, text="Remover Tarefa de Maior Prioridade", command=self.remove_highest_priority_task, bg=button_color, fg=button_fg_color, font=font)
        self.remover_botao.grid(row=0, column=0, padx=10, pady=5)

        self.update_pending_tasks_listbox()

    def add_task(self):
        task = self.entrada_tarefa.get()
        try:
            priority = int(self.entrada_prioridade.get())
        except ValueError:
            messagebox.showwarning("Aviso", "A prioridade deve ser um número entre 1 e 4.")
            return
        
        if task and 1 <= priority <= 4:
            self.fila_prioridades.enfileirar(task, priority)
            self.update_pending_tasks_listbox()
            self.entrada_tarefa.delete(0, tk.END)
            self.entrada_prioridade.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Você deve inserir uma tarefa e uma prioridade válida.")

    def update_pending_tasks_listbox(self):
        for widget in self.tarefas_pendentes.winfo_children():
            widget.destroy()

        self.pending_tasks_checkbuttons = []
        for tarefa, prioridade in self.fila_prioridades.listar_todas_tarefas():
            var = tk.BooleanVar()
            cb = tk.Checkbutton(self.tarefas_pendentes, text=f"{tarefa} (Prioridade {prioridade})", bg="#ffffff", font=("Arial", 10), variable=var, command=lambda tarefa=tarefa, var=var: self.complete_task(tarefa, var))
            self.pending_tasks_checkbuttons.append((cb, var))
            cb.pack(anchor=tk.W)

        self.update_completed_tasks_listbox()

    def remove_highest_priority_task(self):
        task = self.fila_prioridades.desenfileirar()
        if task:
            messagebox.showinfo("Tarefa Removida", f"A tarefa '{task}' foi removida.")
            self.update_pending_tasks_listbox()
        else:
            messagebox.showinfo("Sem Tarefas", "Não há tarefas para remover.")

    def complete_task(self, tarefa, var):
        if var.get():
            message = self.fila_prioridades.tarefa_concluida(tarefa)
            self.update_pending_tasks_listbox()
            messagebox.showinfo("Tarefa Concluída", message)
        else:
            messagebox.showwarning("Aviso", "Você deve marcar a tarefa para concluir.")

    def update_completed_tasks_listbox(self):
        self.lista_tarefas_conc.delete(0, tk.END)
        for tarefa in self.fila_prioridades.tarefas_concluidas:
            self.lista_tarefas_conc.insert(tk.END, tarefa)

    def search_task(self):
        query = self.entrada_pesquisa.get()
        if query:
            results = self.fila_prioridades.buscar_tarefa_por_nome(query)
            self.quadro_resultados.delete(0, tk.END)
            for tarefa, prioridade in results:
                self.quadro_resultados.insert(tk.END, f"{tarefa} (Prioridade {prioridade})")
        else:
            messagebox.showwarning("Aviso", "Você deve inserir um termo para pesquisar.")

root = tk.Tk()
app = Tkapp(root)
root.mainloop()
