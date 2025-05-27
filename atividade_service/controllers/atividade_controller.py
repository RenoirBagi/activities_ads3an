from flask import Blueprint, jsonify, request
# from models import atividade_model
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

# @atividade_bp.route('/<int:id_atividade>/professor/<int:id_professor>', methods=['GET'])
# def obter_atividade_para_professor(id_atividade, id_professor):
#     try:
#         atividade = getAtividadeById(id_atividade)
#         if not PessoaServiceClient.verificar_leciona(id_professor, atividade['id_disciplina']):
#             atividade = atividade.copy()
#             atividade.pop('respostas', None)
#         return jsonify(atividade)
#     except AtividadeNotFound:
#         return jsonify({'erro': 'Atividade não encontrada'}), 404

@atividade_bp.route('/atividades', methods=['POST'])
def criar_atividade():
    dados = request.json
    atividade = createAtividade(dados)
    return atividade