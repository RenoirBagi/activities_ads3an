from flask import jsonify
from config import db
from clients.pessoa_service_client import AtividadeServiceClient

class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, nullable=False)
    enunciado = db.Column(db.String(255), nullable=False)
    respostas = db.relationship('Resposta', back_populates = 'atividade')

    def __init__(self, professor_id, enunciado):
        self.professor_id = professor_id
        self.enunciado = enunciado

    def to_dict(self):
        return {
            'id': self.id,
            'professor_id': self.professor_id,
            'enunciado': self.enunciado,
            "respostas": [resposta.to_dict() for resposta in self.respostas]
        }

class AtividadeNotFound(Exception):
    pass

def getAtividades():
    atividades = Atividade.query.all()
    lista_atividades = []
    for atividade in atividades:
        lista_atividades.append(atividade.to_dict())
    return lista_atividades

def getAtividadeById(id_atividade):
    atividade = Atividade.query.get(id_atividade)
    if not atividade:
        raise AtividadeNotFound
    return atividade.to_dict()

def createAtividade(dados):
    professor_id = dados.get("professor_id")

    if not AtividadeServiceClient.validar_professor(professor_id):
        return jsonify({
            'erro': "Professor não encontrado",
            "codigo": 400
        })

    novaAtividade = Atividade(
        professor_id = professor_id,
        enunciado = dados.get("enunciado")
    )

    db.session.add(novaAtividade)
    db.session.commit()
    return novaAtividade.to_dict()