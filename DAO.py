import random
import re


def adicionar_tarefa(tarefa):
    with open("To-do.txt", "r") as arquivo:
        tarefas = arquivo.readlines()
        indice = len(tarefas)
        listaid = []
        id = random.randint(1000, 9999)
        if id in tarefas:
            id = random.randint(1000, 9999)
        else:
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
                print(index, item.strip())
            index += 1
