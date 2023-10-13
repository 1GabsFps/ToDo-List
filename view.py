from controller import *
from model import *

sair = True

while True:
    print("Software de gerenciamento de tarefas")
    print("1 -> Adicionar tarefa")
    print("2 -> Excluir tarefa")
    print("3 -> Listar tarefas")
    print("4 -> Sair")
    print("")

    opcao = obter_opcao()

    match opcao:
        case 1:
            limpar()
            print("--|Adicionar Tarefas |--")
            tarefa = input("Digite a tarefa: ")
            adicionartarefa = ControllerAdicionarTarefa(tarefa)
            parar()
            limpar()

        case 2:
            limpar()
            print("--|Lista de Tarefas |--")
            listarTarefa = ControllerListarTarefa()
            excluir = input("Digite o número da tarefa que deseja excluir: ")
            excluirTarefa = ControllerExcluirTarefa(excluir)
            limpar()
            print("--| Nova Lista de Tarefas |--")
            print("")
            listarTarefa = ControllerListarTarefa()
            parar()
            limpar()
        case 3:
            limpar()
            print("--|Lista de Tarefas |--")
            print("")
            listarTarefa = ControllerListarTarefa()
            parar()
            limpar()

        case 4:
            exit()

        case _:
            limpar()
            print("Opção inválida")
            parar()
            limpar()
