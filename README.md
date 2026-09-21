# TaskTracker

## Descrição

O TaskTracker é uma aplicação de linha de comando desenvolvida em Python para gerenciamento de tarefas.

O sistema permite cadastrar novas tarefas, visualizar as tarefas cadastradas e encerrar a aplicação por meio de um menu no terminal.

Cada tarefa possui:

- Título
- Descrição
- Prioridade
- Data limite
- Status

O status de uma nova tarefa é definido automaticamente como **Pendente**.

O sistema também realiza validações durante o cadastro. O título é obrigatório e não pode ficar vazio ou conter apenas espaços. A prioridade aceita somente as opções **Alta**, **Média/Media** ou **Baixa**.

Caso não existam tarefas cadastradas, o sistema informa ao usuário que não existem registros no momento.

## Funcionalidades

1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação

## Tecnologias utilizadas

- Python 3
- Git
- GitHub

## Estrutura do projeto

```text
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Instalação

É necessário possuir o Python 3 instalado no computador.

Clone o repositório:

```bash
git clone https://github.com/elterncamargos/tasktracker-projeto.git
```

Acesse a pasta do projeto:

```bash
cd tasktracker-projeto
```

## Execução

Execute a aplicação com:

```bash
py src/main.py
```

ou:

```bash
python src/main.py
```

Após a execução, será exibido o menu:

```text
============================
       TASKTRACKER
============================
1 - Cadastrar nova tarefa
2 - Visualizar tarefas cadastradas
3 - Sair da aplicação
```

## Autor

Eltern Camargos Vieira

Curso: Ciência de Dados e Machine Learning  
Bootcamp II
