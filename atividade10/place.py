from sqlalchemy import types, Column
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy import create_engine
engine = create_engine('sqlite:///lugares.db', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()



from sqlalchemy.orm import sessionmaker
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

class PlaceModel(Base):
    __tablename__ = 'Lugares'
    id = Column(types.Integer, primary_key=True)
    nome = Column(types.String(45))
    endereco = Column(types.String(100))


    def __init__(
            self,
            nome=None,
            endereco=None,
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
        place = session.query(PlaceModel).filter_by(id=id).first()
        if place:
            return place
        return None

    def save(self):
        session.add(self)
        session.commit()

    def update(
            self,
            nome,
            endereco,
    ):
        self.nome = nome
        self.endereco = endereco

    def delete(self):
        session.delete(self)
        session.commit()


    def insertPlace(self,place):
        try:
            place.save()
            query = PlaceModel.find(place.id)
            return query  # created
        except SQLAlchemyError as e:
            print(f'erro: {e}')
            session.rollback()
            return None

Base.metadata.create_all(engine)


# from banco import Banco

# class Clientes(object):

#     def __init__(self, idusuario = 0, nome = "", telefone = "", email = "", usuario = "", senha = ""):
#         self.info = {}
#         self.idusuario = idusuario
#         self.nome = nome
#         self.telefone = telefone
#         self.email = email
#         self.usuario = usuario
#         self.senha = senha


#     def insertUser(self):

#         banco = Banco()
#         try:

#             c = banco.conexao.cursor()
#             c.execute("insert into usuarios (nome, telefone, email,usuario,senha) values (" + self.nome + "', '" +
#                                             self.telefone + "', '" + self.email + "', '" +
#                                             self.usuario + "', '" + self.senha + "' )")

#             banco.conexao.commit()
#             c.close()

#             return "Usuário cadastrado com sucesso!"
#         except Exception as e:
#             return f"Ocorreu um erro na inserção do usuário: {e}"

#     def updateUser(self):

#         banco = Banco()
#         try:

#             c = banco.conexao.cursor()

#             c.execute("update usuarios set nome = " + self.nome +  " telefone = " + self.telefone + ", email = " + 
#                       self.email + ", usuario = " + self.usuario + " , senha = '" + self.senha +
#                 "' where idusuario = " + self.idusuario + " ")

#             banco.conexao.commit()
#             c.close()

#             return "Usuário atualizado com sucesso!"
#         except:
#             return "Ocorreu um erro na alteração do usuário"

#     def deleteUser(self):

#         banco = Banco()
#         try:

#             c = banco.conexao.cursor()

#             c.execute("delete from usuarios where idusuario = " + self.idusuario + "; ")

#             banco.conexao.commit()
#             c.close()

#             return "Usuário excluído com sucesso!"
#         except:
#             return "Ocorreu um erro na exclusão do usuário"

#     def selectUser(self, idusuario):
#         banco = Banco()
#         try:

#             c = banco.conexao.cursor()

#             c.execute("select * from usuarios where idusuario = " + idusuario + "; ")

#             for linha in c:
#                 self.idusuario = linha[0]
#                 self.nome = linha[1]
#                 self.telefone = linha[2]
#                 self.email = linha[3]
#                 self.usuario = linha[4]
#                 self.senha = linha[5]

#             c.close()

#             return "Busca feita com sucesso!"
#         except:
#             return "Ocorreu um erro na busca do usuário"


