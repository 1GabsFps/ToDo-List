def adicionar_tarefa(tarefa):
    with open('To-do.txt', 'r') as arquivo:
        tarefas = arquivo.readlines()
        indice = len(tarefas) + 1
    with open('To-do.txt', 'a') as arquivo:
        arquivo.write(f"{indice} -- {tarefa}\n")


def listar_tarefas():
    with open('To-do.txt', 'r') as arquivo:
        tarefas = arquivo.readlines()
        for tarefa in tarefas:
            print(tarefa.strip())
