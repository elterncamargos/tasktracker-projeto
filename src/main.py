# TaskTracker
# Bootcamp II - Fase 2

tarefas = []


def cadastrar_tarefa():
    print("\n--- CADASTRAR NOVA TAREFA ---")

    # Validação do título
    while True:
        titulo = input("Título: ").strip()

        if titulo:
            break

        print("Erro: o título não pode ficar vazio.")

    # Descrição
    descricao = input("Descrição: ").strip()

    # Validação da prioridade
    while True:
        prioridade = input(
            "Prioridade (Alta, Média ou Baixa): "
        ).strip().lower()

        if prioridade == "alta":
            prioridade = "Alta"
            break

        elif prioridade in ["média", "media"]:
            prioridade = "Média"
            break

        elif prioridade == "baixa":
            prioridade = "Baixa"
            break

        else:
            print("Erro: informe apenas Alta, Média ou Baixa.")

    # Data limite
    data_limite = input(
        "Data limite (DD/MM/AAAA): "
    ).strip()

    # Criação da tarefa
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }

    # Adiciona a tarefa na lista
    tarefas.append(tarefa)

    print("\nTarefa cadastrada com sucesso!")


def visualizar_tarefas():
    print("\n--- TAREFAS CADASTRADAS ---")

    # Verifica se existem tarefas
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    # Exibe todas as tarefas
    for numero, tarefa in enumerate(tarefas, start=1):
        print("\n----------------------------")
        print(f"Tarefa {numero}")
        print("----------------------------")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status: {tarefa['status']}")


def exibir_menu():
    while True:
        print("\n============================")
        print("       TASKTRACKER")
        print("============================")
        print("1 - Cadastrar nova tarefa")
        print("2 - Visualizar tarefas cadastradas")
        print("3 - Sair da aplicação")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa()

        elif opcao == "2":
            visualizar_tarefas()

        elif opcao == "3":
            print("\nAplicação encerrada.")
            break

        else:
            print("\nErro: opção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    exibir_menu()