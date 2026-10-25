# TaskTracker

## Descrição

O TaskTracker é uma aplicação de linha de comando (CLI) desenvolvida em Python para gerenciamento de tarefas.

O sistema permite cadastrar novas tarefas, visualizar as tarefas cadastradas e encerrar a aplicação por meio de um menu interativo no terminal.

Cada tarefa possui as seguintes informações:

- Título
- Descrição
- Prioridade
- Data limite
- Status

O status de uma nova tarefa é definido automaticamente como **Pendente**.

O sistema também realiza validações durante o cadastro. O título é obrigatório e não pode ficar vazio ou conter apenas espaços em branco. A prioridade aceita somente as opções **Alta**, **Média/Media** ou **Baixa**.

Caso não existam tarefas cadastradas, o sistema informa ao usuário que não há registros no momento.

O projeto foi desenvolvido progressivamente durante o Bootcamp II, contemplando planejamento lógico, implementação em Python, versionamento com Git e GitHub e, na etapa final, conteinerização com Docker.

## Funcionalidades

1. Cadastrar nova tarefa.
2. Visualizar tarefas cadastradas.
3. Sair da aplicação.

Durante o cadastro, o usuário informa o título, a descrição, a prioridade e a data limite da tarefa.

O programa verifica os dados obrigatórios, apresenta mensagens em caso de entradas inválidas e permite visualizar as tarefas registradas durante a execução.

## Tecnologias utilizadas

- **Python 3:** linguagem de programação utilizada no desenvolvimento da aplicação.
- **Git:** ferramenta de controle de versões do projeto.
- **GitHub:** plataforma utilizada para armazenamento e versionamento do código-fonte.
- **Docker:** tecnologia utilizada para criar a imagem e executar a aplicação em um contêiner.
- **Docker Compose:** ferramenta utilizada para configurar e executar o serviço da aplicação.
- **GitHub Codespaces:** ambiente de desenvolvimento em nuvem utilizado para construir e testar os contêineres diretamente pelo navegador.

## Estrutura do projeto

```text
tasktracker-projeto/
├── README.md
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

### Descrição dos arquivos

| Arquivo ou pasta | Finalidade |
|---|---|
| `README.md` | Apresenta o projeto e contém as instruções de instalação e execução. |
| `.gitignore` | Define arquivos e diretórios que não devem ser versionados. |
| `Dockerfile` | Contém as instruções para construir a imagem Docker da aplicação. |
| `docker-compose.yml` | Configura o serviço Docker e habilita a interação pelo terminal. |
| `docs/` | Armazena a documentação do projeto. |
| `docs/planejamento_logico.pdf` | Contém o planejamento lógico desenvolvido na Etapa Inicial. |
| `src/` | Contém o código-fonte da aplicação. |
| `src/main.py` | Implementa o menu, o cadastro, a listagem e as validações das tarefas. |

## Instalação e execução com Python

O TaskTracker pode ser executado diretamente pelo Python, sem utilizar Docker.

### Pré-requisitos

É necessário possuir o Python 3 instalado no computador.

### Clonar o repositório

```bash
git clone https://github.com/elterncamargos/tasktracker-projeto.git
```

Acesse a pasta do projeto:

```bash
cd tasktracker-projeto
```

### Executar a aplicação

No Windows, execute:

```bash
py src/main.py
```

Ou, em ambientes que utilizam o comando `python`:

```bash
python src/main.py
```

Após a execução, será apresentado o menu:

```text
============================
       TASKTRACKER
============================
1 - Cadastrar nova tarefa
2 - Visualizar tarefas cadastradas
3 - Sair da aplicação
```

O usuário poderá selecionar uma opção digitando o número correspondente.

---

## Execução com Docker

Na Etapa Final do Bootcamp II, o TaskTracker foi configurado para execução em contêineres Docker.

A utilização do Docker permite executar a aplicação em um ambiente padronizado, baseado no Python 3.11, sem a necessidade de instalar o Python diretamente no computador utilizado para executar os contêineres.

### Pré-requisitos

Para executar o projeto utilizando Docker, é necessário:

- Possuir o Docker instalado e funcionando, localmente ou em um ambiente remoto.
- Possuir o Docker Compose disponível.
- Ter acesso aos arquivos do repositório TaskTracker.

A aplicação também pode ser executada por meio do **GitHub Codespaces**, utilizando o ambiente Linux e o terminal disponibilizados diretamente pelo navegador.

### 1. Construir a imagem Docker

No terminal, dentro da pasta principal do projeto, execute:

```bash
docker build -t tasktracker .
```

Esse comando utiliza as instruções do arquivo `Dockerfile` para construir uma imagem denominada `tasktracker`.

O Dockerfile utiliza a imagem base `python:3.11-slim`, define o diretório de trabalho `/app`, copia o código-fonte para o contêiner e configura a inicialização automática da aplicação.

### 2. Executar a aplicação com Docker

Após construir a imagem, execute:

```bash
docker run -it --rm tasktracker
```

O comando inicia o TaskTracker em modo interativo, permitindo ao usuário visualizar o menu, cadastrar tarefas e consultar os registros.

Os parâmetros utilizados possuem as seguintes funções:

- `-i`: mantém a entrada de dados disponível.
- `-t`: disponibiliza um terminal interativo.
- `--rm`: remove automaticamente o contêiner após o encerramento da execução.

### 3. Executar com Docker Compose

O projeto também pode ser executado utilizando Docker Compose.

No terminal, dentro da pasta principal do projeto, execute:

```bash
docker compose run --rm tasktracker-app
```

Esse comando utiliza a configuração do arquivo `docker-compose.yml` para construir a imagem, caso necessário, e iniciar o serviço `tasktracker-app`.

O arquivo de configuração contém as opções `stdin_open: true` e `tty: true`, que permitem a interação do usuário com o menu da aplicação.

### 4. Funcionamento da aplicação no Docker

Após a inicialização, será apresentado o menu:

```text
============================
       TASKTRACKER
============================
1 - Cadastrar nova tarefa
2 - Visualizar tarefas cadastradas
3 - Sair da aplicação
```

O usuário poderá cadastrar tarefas informando:

- Título da tarefa.
- Descrição.
- Prioridade.
- Data limite.

O status inicial será definido automaticamente como **Pendente**.

Durante o cadastro, o programa verifica se o título foi preenchido corretamente e se a prioridade corresponde a uma das opções permitidas: Alta, Média/Media ou Baixa.

Após o cadastro, a opção de visualização permite consultar as tarefas registradas durante a execução.

### 5. Armazenamento das tarefas

Na versão atual, as tarefas são armazenadas temporariamente na memória do programa.

Isso significa que os registros permanecem disponíveis enquanto a aplicação estiver em execução.

Ao encerrar o programa, as tarefas cadastradas não são preservadas. Portanto, uma nova execução inicia com uma lista vazia.

O armazenamento permanente dos dados poderá ser implementado em versões futuras.

---

## Arquivos de configuração Docker

### Dockerfile

O arquivo `Dockerfile` contém as instruções necessárias para construir a imagem da aplicação:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY src/ /app/src/

CMD ["python", "src/main.py"]
```

As instruções definem a imagem base do Python, o diretório de trabalho, a configuração de saída do terminal, a cópia do código-fonte e o comando de inicialização do programa.

### docker-compose.yml

O arquivo `docker-compose.yml` contém a configuração do serviço:

```yaml
services:
  tasktracker-app:
    build: .
    stdin_open: true
    tty: true
```

O serviço `tasktracker-app` utiliza o Dockerfile presente na raiz do projeto e habilita a entrada de dados e o terminal interativo.

Essas configurações são necessárias para que o usuário consiga interagir com as opções do menu do TaskTracker.

---

## Desenvolvimento e testes no GitHub Codespaces

A construção e os testes da aplicação conteinerizada foram realizados no **GitHub Codespaces**, ambiente de desenvolvimento Linux disponibilizado pelo GitHub.

O Codespaces permitiu utilizar o Docker diretamente pelo navegador, sem a necessidade de instalar o Docker Desktop no computador local.

### Ambiente utilizado

- Sistema operacional: Ubuntu 24.04 LTS.
- Docker Engine: versão 29.8.0.
- Docker Compose: versão 5.5.1.
- Imagem base da aplicação: Python 3.11 Slim.

### Testes realizados

Foram realizados os seguintes procedimentos:

1. Verificação da instalação e funcionamento do Docker utilizando `docker --version` e `docker info`.
2. Construção da imagem com `docker build -t tasktracker .`.
3. Execução da aplicação utilizando `docker run -it --rm tasktracker`.
4. Verificação da apresentação do menu principal.
5. Cadastro de uma tarefa com título, descrição, prioridade e data limite.
6. Visualização da tarefa cadastrada.
7. Encerramento da aplicação pelo menu.
8. Execução utilizando `docker compose run --rm tasktracker-app`.
9. Cadastro e visualização de tarefas durante a execução pelo Docker Compose.

### Resultados

A imagem Docker foi construída com sucesso e o TaskTracker iniciou corretamente nos dois modos de execução.

O programa apresentou o menu interativo e permitiu cadastrar e visualizar tarefas dentro dos contêineres.

Os testes demonstraram o funcionamento da aplicação conteinerizada, atendendo ao objetivo técnico da Etapa Final do Bootcamp II.

---

## Versionamento do projeto

O desenvolvimento do TaskTracker foi realizado progressivamente, utilizando Git e GitHub para registrar as alterações do código e da documentação.

Na Etapa Inicial, foram elaborados o planejamento lógico e a estrutura arquitetural do projeto.

Na Etapa Intermediária, foi implementada a aplicação em Python, incluindo menu principal, cadastro de tarefas, validações e visualização dos registros.

Na Etapa Final, foram adicionados os arquivos de configuração Docker e Docker Compose, permitindo executar a aplicação em um ambiente conteinerizado.

O histórico de commits do repositório registra a evolução das funcionalidades e da documentação ao longo das etapas do Bootcamp II.

## Autor

**Eltern Camargos Vieira**

Curso: Ciência de Dados e Machine Learning

Bootcamp II

## Repositório

https://github.com/elterncamargos/tasktracker-projeto
