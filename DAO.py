def adicionar_tarefa(tarefa):
    with open("To-do.txt", "r") as arquivo:
        tarefas = arquivo.readlines()
        indice = len(tarefas)
    with open("To-do.txt", "a") as arquivo:
        arquivo.write(f"\n {indice}    {tarefa}\n")


def listar_tarefas():
    with open("To-do.txt", "r") as arquivo:
        tarefas = arquivo.readlines()
        for tarefa in tarefas:
            print(tarefa.strip())
