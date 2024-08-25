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

    def get_cliente(self):
        return ClienteModel