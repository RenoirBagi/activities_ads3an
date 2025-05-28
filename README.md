# API de Controle de Atividades📚

API para controle de Atividades, integrada com ao serviço de Sistema Escolar.

## Descrição

- Realiza o controle das atividades, recebendo as respectivas respostas.
- Valida a existência de Professores e Alunos baseada na integração com o microsserviço de Sistema Escolar.
- Tecnologias utilizadas: Python/Flask, SQLAlchemy e Docker.


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

#### Principais Endpoints

- GET/atividades - Lista todas as atividades.
- GET/atividades/< id > - Lista uma atividade baseada em seu ID.
- POST/atividades - Cria uma nova atividade.
------------------------------------------------------------------------------------
- GET/respostas - Listas todas as respostas.
- GET/respostas/< id > - Lista uma resposta baseada no seu ID.
- POST/repostas - Cria uma nova resposta.

### Fluxo Principal

- aaa
- aa
- a

### Protocolos de Integração

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

### Desenvolvimento - Estrutura dos Arquivos

```bash
ACTIVITIES_ADS3AN/
      ├──atividade_service/
         ├── clients/         
         │   └── pessoa_service_client.py   
         ├── controllers/              
         │   ├── atividade_controller.py
             └── resposta_controller.py    
         ├── instance/            
         │   └── atividades.db
         ├── models/
         │    ├── atividade_model.py
              └── resposta_model.py      
         ├── app.py                
         └── config.py                   
      ├──.gitgnore
      ├──Dockerfile
      ├──README.md
      ├──requirements.txt
```

### Exemplo de Requisição

#### Para Atividade
```bash
{
    "professor_id": 2, 
    "enunciado": "Redija um texto sobre microsserviços"
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
