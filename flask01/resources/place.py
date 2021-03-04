from flask import make_response, jsonify
from datetime import datetime

from flask import request
from flask_restful import Resource, reqparse
from models.place import PlaceModel
from datetime import datetime, date
from schemas.place import PlaceSchema

from sqlalchemy.exc import SQLAlchemyError

from alchemy import db


schema = PlaceSchema()


class PlaceListResource(Resource):

    def get(self):
        places = PlaceModel.query.all()
        result = schema.dump(places, many=True)
        if result:
            return result
        return {'message': 'list of places not found'}, 404  # not found

    def post(self):
        request_dict = request.get_json()
        if not request_dict:
            response = {'places': 'No inpput data provided'}
            return make_response(response, 400)
        errors = schema.validate(request_dict)
        if errors:
            return make_response(errors, 400)  # bad request
        try:
            place = PlaceModel(
                request_dict['nome'],
                request_dict['endereco'],
            )
            place.save()
            query = PlaceModel.find(place.id)
            result = schema.dump(query)
            return make_response(jsonify(result), 201)  # created
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({'error': str(e)})
            return make_response(resp, 500)


class PlaceResource(Resource):

    def get(self, id):
        place = PlaceModel.find(id)
        if place:
            return schema.dump(place)
        return {'message': 'place not found'}, 404  # not found

    def put(self, id):
        target = PlaceModel.find(id)
        if not target:
            response = {
                'error': "Given ID doesn't match any place in the database"
            }
            # not found
            return make_response(response, 404)
        request_dict = request.get_json()
        if not request_dict:
            response = {
                'error': 'No input data provided'
            }
            return make_response(response, 400)  # bad request
        errors = schema.validate(request_dict)
        if errors:
            return make_response(errors, 400)  # bad request

        try:
            place = PlaceModel(
                request_dict['nome'],
                request_dict['endereco'],

                id=id
            )
            target.delete()
            place.save()
            return self.get(id)
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({'error': str(e)})
            return make_response(resp, 500)  # internal server error

    def delete(self, id):
        place = PlaceModel.find(id)
        if place:
            try:
                place.delete()
            except Exception as e:
                print(e)
                return {'message': 'An error ocurred trying to delete.'},
            return {'message': 'place deleted.'}, 204  # not found
        return {'message': 'place not found'}, 404
