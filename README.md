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

## Execução com Docker

O TaskTracker também pode ser executado em um contêiner Docker, utilizando uma imagem baseada no Python 3.11.

O projeto utiliza Docker e Docker Compose para facilitar a execução da aplicação em ambientes compatíveis, sem a necessidade de instalar o Python diretamente no computador.

### Pré-requisitos

- Docker instalado e funcionando.
- Docker Compose disponível.
- Acesso aos arquivos do projeto.

A execução também pode ser realizada pelo GitHub Codespaces, utilizando o terminal disponibilizado no navegador.

### Construir a imagem Docker

No terminal, dentro da pasta principal do projeto, execute:

```bash
docker build -t tasktracker .
```

Esse comando utiliza o Dockerfile para construir uma imagem denominada `tasktracker`.

### Executar a aplicação com Docker

Após construir a imagem, execute:

```bash
docker run -it --rm tasktracker
```

O comando inicia o TaskTracker em modo interativo, permitindo utilizar o menu, cadastrar tarefas e visualizar os registros.

### Executar com Docker Compose

Para executar a aplicação utilizando o arquivo `docker-compose.yml`, digite:

```bash
docker compose run --rm tasktracker-app
```

O Docker Compose utiliza as configurações do projeto para construir a imagem, caso necessário, e iniciar a aplicação com entrada de dados e terminal interativo habilitados.

### Funcionamento da aplicação

Após iniciar o TaskTracker, será apresentado o seguinte menu:

```text
============================
       TASKTRACKER
============================
1 - Cadastrar nova tarefa
2 - Visualizar tarefas cadastradas
3 - Sair da aplicação
```

O sistema permite cadastrar tarefas informando título, descrição, prioridade e data limite.

O status inicial de cada tarefa é definido automaticamente como **Pendente**.

Durante o cadastro, o sistema verifica se o título foi preenchido e se a prioridade corresponde a uma das opções permitidas: Alta, Média/Media ou Baixa.

### Armazenamento das tarefas

Na versão atual, as tarefas são armazenadas temporariamente na memória durante a execução do programa.

Ao encerrar a aplicação, os registros não são preservados. Uma nova execução começa com uma lista vazia.

### Arquivos de configuração

**Dockerfile:** contém as instruções para construir a imagem Docker, configurar o ambiente Python e iniciar a aplicação.

**docker-compose.yml:** define o serviço `tasktracker-app` e habilita a interação do usuário pelo terminal.

### Testes de execução

A aplicação foi executada e testada no GitHub Codespaces utilizando Docker e Docker Compose.

Foram realizados testes de construção da imagem, inicialização do programa, cadastro de tarefas e visualização dos registros.
