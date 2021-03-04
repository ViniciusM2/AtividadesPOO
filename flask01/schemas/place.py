from flask_marshmallow.fields import Hyperlinks, URLFor

from marshmallow import Schema, fields
from marshmallow import validate
from alchemy import ma

class PlaceSchema(ma.Schema):
    class Meta:
        ordered = True
    id = fields.Integer(dump_only=True)
    nome = fields.String()
    endereco = fields.String()

