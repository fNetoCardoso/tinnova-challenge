from datetime import datetime
from db import db


class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    veiculo = db.Column(db.String(255), nullable=False)
    marca = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    vendido = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "veiculo": self.veiculo,
            "marca": self.marca,
            "ano": self.ano,
            "descricao": self.descricao,
            "vendido": self.vendido,
            "created": self.created.isoformat(),
            "updated": self.updated.isoformat()
        }
