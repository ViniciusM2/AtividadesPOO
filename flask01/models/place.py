
from alchemy import db
from sqlalchemy import types, Column
from flask_marshmallow.fields import Hyperlinks, URLFor

from datetime import date, datetime
import enum
import json

from marshmallow import Schema, fields
from marshmallow import validate
from alchemy import ma

class PlaceModel(db.Model):
    __tablename__ = 'Lugares'
    id = Column(types.Integer, primary_key=True)
    nome = Column(types.String(45))
    endereco = Column(types.String(100))


    def __init__(
            self,
            nome,
            endereco,
            id=None,
    ):
        if id:
            self.id = id

        self.nome = nome
        self.endereco = endereco


    @classmethod
    def json_serial(self, obj):
        """JSON serializer for objects not serializable by default json code"""

        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        raise TypeError("Type %s not serializable" % type(obj))

    @classmethod
    def find(cls, id):
        cliente = cls.query.filter_by(id=id).first()
        if cliente:
            return cliente
        return None

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(
            self,
            nome,
            endereco,
    ):
        self.nome = nome
        self.endereco = endereco

    def delete(self):
        db.session.delete(self)
        db.session.commit()



