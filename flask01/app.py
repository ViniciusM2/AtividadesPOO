# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return '<h1>Alô Mundo ! Aqui é o Vinícius Menezes Monte  testando o Flask !</h1>'


# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask
from flask_restful import Api
from resources.place import PlaceListResource, PlaceResource



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'flaskifce'
app.config['JSON_SORT_KEYS'] = False
api = Api(app)


@app.before_first_request
def cria_banco():
    db.create_all()
api.add_resource(PlaceListResource, '/clientes')
api.add_resource(PlaceResource, '/clientes/<string:id>')
# flask configs
if __name__ == '__main__':
    from alchemy import db
    db.init_app(app) 
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True)
