import random


def adicionar_tarefa(tarefa):
    with open("To-do.txt", "r") as arquivo:
        tarefas = arquivo.readlines()
        id = random.randint(1000, 9999)
        listaids = []
        while id in tarefas:
            id = random.randint(1000, 9999)
        if id not in listaids:
            listaids.append(id)
        else:
            pass
        with open("To-do.txt", "a") as arquivo:
            arquivo.write(f"\n {id}    {tarefa}")


def listar_tarefas():
    with open("To-do.txt", "r") as arquivo:
        tarefas = arquivo.readlines()
        tarefas_sem_numero = []
        index = 0
        for item in tarefas:
            item_sem_numeros = ""
            for caractere in item:
                if not caractere.isdigit():
                    item_sem_numeros += caractere
            tarefas_sem_numero.append(item_sem_numeros)
        for item in tarefas_sem_numero:
            if index == 0:
                print(item.strip())
                index += 1
            else:
                print(index - 1, "   ", item.strip())
            index += 1
    return tarefas


def excluir_tarefas(tarefa):
    with open("To-do.txt", "r") as arquivo:
        tarefas = arquivo.readlines()
        tarefas.pop(tarefa)
        index = 0
        listaids = []
        for ids in tarefas:
            item_id = ""
            for caractere in ids:
                if caractere.isdigit():
                    item_id += caractere
            listaids.append(item_id)
        with open("To-do.txt", "w") as arquivo:
            for item in tarefas:
                arquivo.write(f"{item}")
                index += 1
