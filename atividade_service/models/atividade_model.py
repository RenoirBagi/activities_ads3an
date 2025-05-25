from flask import jsonify
from app import db

# atividades = [
#     {
#         'id_atividade': 1,
#         'id_disciplina': 1,
#         'enunciado': 'Crie um app de todo em Flask',
#         'respostas': [
#             {'id_aluno': 1, 'resposta': 'todo.py', 'nota': 9},
#             {'id_aluno': 2, 'resposta': 'todo.zip.rar'},
#             {'id_aluno': 4, 'resposta': 'todo.zip', 'nota': 10}
#         ]
#     },
#     {
#         'id_atividade': 2,
#         'id_disciplina': 1,
#         'enunciado': 'Crie um servidor que envia email em Flask',
#         'respostas': [
#             {'id_aluno': 4, 'resposta': 'email.zip', 'nota': 10}
#         ]
#     }
# ]

class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    disciplina_id = db.Column(db.Integer, nullable=False)
    enunciado = sala = db.Column(db.String(255), nullable=False)

    def __init__(self, disciplina_id, enunciado):
        self.disciplina_id = disciplina_id
        self.enunciado = enunciado

    def to_dict(self):
        return {
            'id': self.id,
            'disciplina_id': self.disciplina_id,
            'enunciado': self.enunciado
        }

class AtividadeNotFound(Exception):
    pass

def listar_atividades():
    atividades = Atividade.query.all()
    lista_atividades = []
    for atividade in atividades:
        lista_atividades.append(atividade.to_dict())
    return lista_atividades

def obter_atividade(id_atividade):
    atividade = Atividade.query.get(id_atividade)
    if not atividade:
        raise AtividadeNotFound
    return atividade.to_dict()
