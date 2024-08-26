from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ClienteModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(10), nullable=False, unique=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefono = db.Column(db.String(15), nullable=False)

    def __init__(self, id, nombre, apellido, email, telefono, dni):
        self.id = id
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def __repr__(self):
        return f'<Cliente {self.nombre} {self.apellido}>'
    
    def to_JSON(self):
        return {
            'id' : self.id,
            'dni' : self.dni,
            'nombre' : self.nombre,
            'apellido' : self.apellido,
            'email' : self.email,
            'telefono' : self.telefono,
        }



    @classmethod
    def get_clientes(self):
        try:
            return self.query.all()
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_cliente(self, id):
        try:
            return self.query.get(id)
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def añadir_cliente(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as ex:
            raise Exception(ex)
        

    # @classmethod
    # def actualizar_cliente(self, nombre=None, apellido=None, email=None, telefono=None):
    #     try:
    #         if nombre:
    #             self.nombre = nombre
    #         if apellido:
    #             self.apellido = apellido
    #         if email:
    #             self.email = email
    #         if telefono:
    #             self.telefono = telefono
    #     except:
