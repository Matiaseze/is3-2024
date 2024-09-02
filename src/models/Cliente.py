from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(10), nullable=False, unique=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefono = db.Column(db.String(15), nullable=False)

    def __init__(self, id, dni, nombre, apellido, telefono, email):
        self.id = id
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

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
    def añadir_cliente(self, cliente):
        
        try:
            db.session.add(cliente)
            db.session.commit()
        except Exception as ex:
            raise Exception(ex)
    @classmethod     
    def editar_cliente(self,id, dni, nombre, apellido, telefono, email):
        try:
            if id:
                self.id = id
            if dni:
                self.dni = dni
            if nombre:
                self.nombre = nombre
            if apellido:
                self.apellido = apellido
            if email:
                self.email = email
            if telefono:
                self.telefono = telefono
            db.session.commit()
        except Exception as ex:
            db.session.rollback()
            raise Exception(ex)
        
    # Eliminar cliente
    @classmethod 
    def eliminar_cliente(self, cliente):
        try:
            db.session.delete(cliente)
            db.session.commit()
        except Exception as ex:
            db.session.rollback()
            raise Exception(ex)