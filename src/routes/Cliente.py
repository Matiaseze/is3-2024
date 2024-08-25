from flask import Blueprint, flash, render_template, request, redirect, url_for
from models.Cliente import ClienteModel, db

cliente_route = Blueprint('cliente_bp', __name__)

@cliente_route.route('/alta', methods=['GET', 'POST'])
def alta_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        dni = request.form['dni']
        
        cliente_existente = ClienteModel.query.filter_by(dni=dni).first()
        if cliente_existente:
            flash("El cliente con este DNI ya existe.", "error")
            return redirect(url_for('cliente_bp.alta_cliente'))


        nuevo_cliente = ClienteModel(nombre=nombre, apellido=apellido, email=email, telefono=telefono, dni=dni)
        db.session.add(nuevo_cliente)
        db.session.commit()

        flash("Cliente añadido exitosamente.", "success")
        return redirect(url_for('cliente_bp.listado_clientes'))
        # except Exception as ex:
        #     message = "Error al tratar de añadir un cliente"
        #     cliente_existe = ClienteModel.query.filter_by(dni=dni).first()
        #     if cliente_existe:
        #         message = "Cliente ya existe, por favor ingrese otro"
        #     flash(message, 'danger')
                
    return render_template('alta_cliente.html')

@cliente_route.route('/listado', methods=['GET'])
def listado_clientes():
    filtro_nombre = request.args.get('nombre')
    filtro_dni = request.args.get('dni')

    # Consultar la base de datos
    clientes = ClienteModel.query.all()

    if filtro_nombre:
        clientes = ClienteModel.query.filter(ClienteModel.nombre.ilike(f'%{filtro_nombre}%')).all()
    if filtro_dni:
        clientes = ClienteModel.query.filter_by(dni=filtro_dni).all()

    return render_template('listado_clientes.html', clientes=clientes)