from flask import Blueprint, request, jsonify
from services.veiculo_service import VeiculoService

veiculos_bp = Blueprint('veiculos', __name__)

@veiculos_bp.route('/veiculos', methods=['GET'])
def listar_veiculos():
    veiculos = VeiculoService.listar_veiculos()
    return jsonify([v.to_dict() for v in veiculos])

@veiculos_bp.route('/veiculos/<int:id>', methods=['GET'])
def obter_veiculo(id):
    veiculo = VeiculoService.obter_veiculo(id)
    return jsonify(veiculo.to_dict()) if veiculo else ('', 404)


@veiculos_bp.route('/veiculos', methods=['POST'])
def criar_veiculo():
    dados = request.get_json()
    veiculo = VeiculoService.criar_veiculo(dados)
    return jsonify(veiculo.to_dict()), 201

@veiculos_bp.route('/veiculos/<int:id>', methods=['PUT'])
def atualizar_veiculo(id):
    dados = request.get_json()
    veiculo = VeiculoService.atualizar_veiculo(id, dados)
    return jsonify(veiculo.to_dict()) if veiculo else ('', 404)

@veiculos_bp.route('/veiculos/<int:id>', methods=['DELETE'])
def deletar_veiculo(id):
    veiculo = VeiculoService.deletar_veiculo(id)
    return ('', 204) if veiculo else ('', 404)
