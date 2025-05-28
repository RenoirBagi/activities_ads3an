from flask import Blueprint, jsonify, request
from clients.pessoa_service_client import AtividadeServiceClient
from models.resposta_model import getRespostas, getRespostaById, createResposta, RespostaNotFound

resposta_bp = Blueprint('resposta_bp', __name__)

@resposta_bp.route('/respostas', methods = ['GET'])
def listar_respostas():
    respostas = getRespostas()
    return jsonify(respostas)

@resposta_bp.route('/respostas/<int:id_resposta>', methods = ['GET'])
def obter_resposta(id_resposta):
    try:
        resposta = getRespostaById(id_resposta)
        return jsonify(resposta)
    
    except RespostaNotFound:
        return jsonify({"erro": 'Resposta não encontrada', "codigo": 404})
    
@resposta_bp.route('/respostas', methods = ['POST'])
def criar_resposta():
    dados = request.json
    atividade = createResposta
    return atividade