from flask import Blueprint, jsonify, request
from clients.pessoa_service_client import AtividadeServiceClient
from models.atividade_model import getAtividades, getAtividadeById, createAtividade, AtividadeNotFound

atividade_bp = Blueprint('atividade_bp', __name__)

@atividade_bp.route('/atividades', methods=['GET'])
def listar_atividades():
    atividades = getAtividades()
    return jsonify(atividades)

@atividade_bp.route('/atividades/<int:id_atividade>', methods=['GET'])
def obter_atividade(id_atividade):
    try:
        atividade = getAtividadeById(id_atividade)
        return jsonify(atividade)
    except AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada', "codigo": 404})

@atividade_bp.route('/atividades', methods=['POST'])
def criar_atividade():
    dados = request.json
    atividade = createAtividade(dados)
    return atividade