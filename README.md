# API de Controle de Atividades📚

API para controle de Atividades, integrada com ao serviço de Sistema Escolar.

## Descrição

A API de Atividades é um microsserviço responsável por controlar a entrega de atividades e respostas, permitindo a consulta e criação de uma atividade ou de uma resposta. Esse serviço opera de forma integrada com a API Sistema Escolar, da qual depende para validações essenciais.

## Funcionalidades principais
#### Criação de uma atividade ou resposta: Ao receber uma solicitação de atividade ou resposta, a API realiza:

###### Para atividades:
- Validação da existência de um professor da atividade solicitada, por meio de consulta a API Sistema Escolar.

###### Para respostas:
- Validação da existência de um aluno da resposta solicitada, por meio de consulta a API Sistema Escolar.
-------------------------------------------------------------------------------------------------------------
#### Consulta - O que é possível buscar:
###### Para atividades
- Uma atividade específica, a partir do seu ID.
- Todas as atividades registradas.

###### Para respostas
- Uma resposta específica, a partir do seu ID.
- Todas as respostas registradas.

## Tecnologias utilizadas
- Python com Flask (framework web)
- SQLAlchemy (ORM para acesso ao banco de dados)
- Docker (containerização do serviço)

## Execução com Docker

### Pré-requisitos

- Tenha o Docker instalado em sua máquina.

### Passos

1. Construa a imagem:
   ```bash
   docker build -t atividade-app .

2. Execute o container:
   ```bash
   docker run -d -p 5002:5002 --name atividade-app atividade-app

3. Copie e cole a seguinte URL em seu navegador:
   ```bash
   http://localhost:5002/atividades

## Endpoints Principais

- GET/atividades - Lista todas as atividades.
- GET/atividades/< id > - Lista uma atividade baseada em seu ID.
- POST/atividades - Cria uma nova atividade.
------------------------------------------------------------------------------------
- GET/respostas - Listas todas as respostas.
- GET/respostas/< id > - Lista uma resposta baseada no seu ID.
- POST/repostas - Cria uma nova resposta.

## Ecossistema de Microsserviços para Sistema Escolar
#### Validação de professor (professor_id):
- Ao longo do processo de criação de uma atividade, o arquivo pessoa_service_client.py realiza uma requisição a API Sistema Escolar, enviando o professor_id fornecido na solicitação.
- Dessa forma, a API Sistema Escolar consulta a tabela de professores no banco de dados app.db, buscando um professor com um id correspondente.
- Caso o professor seja encontrado (isto é, o id retornado seja igual ao professor_id enviado), a validação de professor é considerada bem sucessida, assim concluindo a primeira etapa do processo de criação da atividade.

#### Validação de aluno (aluno_id):
- Ao longo do processo de criação de uma resposta, o arquivo pessoa_service_client.py realiza uma requisição a API Sistema Escolar, enviando o aluno_id fornecido na solicitação.
- Dessa forma, a API Sistema Escolar consulta a tabela de alunos no banco de dados app.db, buscando um aluno com um id correspondente.
- Caso o aluno seja encontrado (isto é, o id retornado seja igual ao aluno_id enviado), a validação de aluno é considerada bem sucessida, assim concluindo a primeira etapa do processo de criação de resposta.


## Protocolos de Integração

- Comunicação síncrona via HTTP REST
- Formato JSON para todas as requisições


### Modelos de Dados - Em Python

  ```bash
  class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, nullable=False)
    enunciado = db.Column(db.String(255), nullable=False)
    respostas = db.relationship('Resposta', back_populates = 'atividade')
```
 -----------------------------------------------------------------------------
 
  ```bash
  class Resposta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, nullable=False)
    resposta = db.Column(db.String(255), nullable=False)
    nota = db.Column(db.Float, nullable=False)
    atividade_id = db.Column(db.Integer, db.ForeignKey('atividade.id'))
    atividade = db.relationship('Atividade', back_populates = 'respostas')
```

### Desenvolvimento 

## Arquitetura 
### MVC

O projeto segue o padrão de arquitetura MVC (Model-View-Controller), promovendo a separação de responsabilidades, assim, facilitando a manutenção e escalabilidade do sistema.

- Model (Modelo)
  - Local: atividade_service/models/atividade_model.py e resposta_model.py
  - Função: Define a estruturas das entidades Atividade e Resposta com o SQLAlchemy. Responsável por representar os dados e regras de persistência da aplicação

- Controller
  - Local: atividade_service/controllers/atividade_controller.py e resposta_controller.py
  - Função: Define as rotas (endpoints) da API, recebendo as requisições e encaminhado-as para os serviços apropriados. Atua como a camada que interage diretamente com o cliente da API (ex: front-end, algum outro sistema, etc).

### Estrutura de Arquivos
```bash
ACTIVITIES_ADS3AN/
      ├──atividade_service/
         ├── clients/         
         │   └── pessoa_service_client.py     # Conexão com a API Sistema Escolar  
         ├── controllers/              
         │   ├── atividade_controller.py      # Rotas
             └── resposta_controller.py    
         ├── instance/            
         │   └── atividades.db                # Banco de Dados
         ├── models/
         │    ├── atividade_model.py          # Modelos de dados
              └── resposta_model.py      
         ├── app.py                           # Aplicação principal       
         └── config.py                        # Configuração do banco 
      ├──.gitgnore                            # Define quais arquivos/pastas o Git deve ignorar
      ├──Dockerfile                           # Criar imagem Docker
      ├──README.md                            # Documentação
      ├──requirements.txt                     # Dependências
```

### Exemplo de Requisição

#### Para Atividade
```bash
{
    "id": 1
    "professor_id": 2, 
    "enunciado": "Redija um texto sobre microsserviços"
    "repostas": "texto.txt"
}
```

#### Para Resposta
```bash
{
    "aluno_id": 2, 
    "atividade_id": 1,
    "resposta": "texto.txt",
    "nota": 8.0
}
```
