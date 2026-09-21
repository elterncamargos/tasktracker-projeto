tarefas = []


def cadastrar_tarefa():
    print("\n--- CADASTRAR NOVA TAREFA ---")

    titulo = input("Título: ")
    descricao = input("Descrição: ")
    prioridade = input("Prioridade: ")
    data_limite = input("Data limite: ")

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }

    tarefas.append(tarefa)

    print("\nTarefa cadastrada com sucesso!")


while True:
    print("\n============================")
    print("       TASKTRACKER")
    print("============================")
    print("1 - Cadastrar nova tarefa")
    print("2 - Visualizar tarefas cadastradas")
    print("3 - Sair da aplicação")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_tarefa()

    elif opcao == "3":
        print("\nAplicação encerrada.")
        break