from models.veiculo_models import Veiculo
from db import db

class VeiculoService:
    @staticmethod
    def listar_veiculos():
        return Veiculo.query.all()

    @staticmethod
    def obter_veiculo(id):
        return Veiculo.query.get(id)

    @staticmethod
    def criar_veiculo(dados):
        veiculo = Veiculo(**dados)
        db.session.add(veiculo)
        db.session.commit()
        return veiculo

    @staticmethod
    def atualizar_veiculo(id, dados):
        veiculo = Veiculo.query.get(id)
        if veiculo:
            for key, value in dados.items():
                setattr(veiculo, key, value)
            db.session.commit()
        return veiculo

    @staticmethod
    def deletar_veiculo(id):
        veiculo = Veiculo.query.get(id)
        if veiculo:
            db.session.delete(veiculo)
            db.session.commit()
        return veiculo
