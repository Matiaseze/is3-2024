from flask import Flask, render_template, request, redirect, url_for
from config import config
from models.Cliente import db
from routes.Cliente import cliente_route

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(cliente_route)


@app.route('/')
def home():
    return render_template('home.html') 

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.config.from_object(config['development'])

   
    app.run(debug=True)