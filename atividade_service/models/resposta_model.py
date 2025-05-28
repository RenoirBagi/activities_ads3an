from flask import jsonify
from config import db
from clients.pessoa_service_client import AtividadeServiceClient

class Resposta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_aluno = db.Column(db.Integer, nullable=False)
    resposta = db.Column(db.String(255), nullable=False)
    nota = db.Column(db.Float, nullable=False)
    atividade_id = db.Column(db.Integer, db.ForeignKey('atividade.id'))

    def __init__(self, id_aluno, resposta, nota, atividade_id):
        self.id_aluno = id_aluno
        self.resposta = resposta
        self.nota = nota
        self.atividade_id = atividade_id

    def to_dict(self):
        return{
            'id': self.id,
            'id_aluno': self.id_aluno,
            'resposta': self.resposta,
            'nota': self.nota,
            'atividade_id': self.atividade_id
        }
    
class RespostaNotFound(Exception):
    pass

def getRespostas():
    respostas = Resposta.query.all()
    lista_respostas = []
    for resposta in respostas:
        lista_respostas.append(resposta.to_dict())
    return lista_respostas

def getRespostaById(resposta_id):
    resposta = Resposta.query.get(resposta_id)
    if not resposta:
        raise RespostaNotFound
    return resposta.to_dict()

def createResposta(dados):
    aluno_id = dados.get("aluno_id")

    if not AtividadeServiceClient.validar_aluno(aluno_id):
        return jsonify({
            'erro': "Aluno não encontrado",
            'codigo': 400
        })
    
    novaResposta = Resposta(
        aluno_id = aluno_id,
        resposta = dados.get("resposta")
    )

    db.session.add(novaResposta)
    db.session.commit()
    return novaResposta.to_dict()