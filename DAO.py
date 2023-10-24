import random


def adicionar_tarefa(tarefa):
    with open("To-do.txt", "r") as arquivo:
        tarefas = arquivo.readlines()
        indice = len(tarefas)
        id = random.randint(1000, 9999)
        if id in tarefas:
            id = random.randint(1000, 9999)
        else:
            with open("To-do.txt", "a") as arquivo:
                arquivo.write(f"\n {id}    {tarefa}")


def listar_tarefas():
    with open("To-do.txt", "r") as arquivo:
        tarefas = arquivo.readlines()
        for tarefa in tarefas:
            print(tarefa.strip())
