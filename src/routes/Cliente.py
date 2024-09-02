from flask import Blueprint, flash, render_template, request, redirect, url_for
from models.Cliente import Cliente

cliente_route = Blueprint('cliente_bp', __name__)

@cliente_route.route('/alta', methods=['GET', 'POST'])
def alta_cliente():
    if request.method == 'POST':
        dni = request.form['dni']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        email = request.form['email']
        
        cliente_existente = Cliente.query.filter_by(dni=dni).first()
        if cliente_existente:
            flash("El cliente con este DNI ya existe.", "error")
            return redirect(url_for('cliente_bp.alta_cliente'))
        id = Cliente.query.order_by(Cliente.id.desc()).first()
        print(f'Cliente con id: {id}')
        nuevo_cliente = Cliente(id, dni, nombre, apellido, telefono, email)
        Cliente.añadir_cliente(nuevo_cliente)

        flash("Cliente añadido exitosamente.", "success")
        return redirect(url_for('cliente_bp.listado_clientes'))

    return render_template('alta_cliente.html')

@cliente_route.route('/listado', methods=['GET'])
def listado_clientes():
    filtro_nombre = request.args.get('nombre')
    filtro_dni = request.args.get('dni')

    # Consultar la base de datos
    clientes = Cliente.query.all()

    if filtro_nombre:
        clientes = Cliente.query.filter(Cliente.nombre.ilike(f'%{filtro_nombre}%')).all()
    if filtro_dni:
        clientes = Cliente.query.filter_by(dni=filtro_dni).all()

    return render_template('listado_clientes.html', clientes=clientes)

@cliente_route.route('/editar/<int:id>', methods=['GET', 'POST'])



def editar_cliente(id):

    cliente = Cliente.query.get_or_404(id)

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']

        try:
            Cliente.editar_cliente(nombre=nombre, apellido=apellido, email=email, telefono=telefono)
            flash("Cliente actualizado exitosamente.", "success")
            return redirect(url_for('cliente_bp.listado_clientes'))
        except Exception as ex:
            flash(f"Error al actualizar el cliente: {ex}", "error")

    return render_template('editar_cliente.html', cliente=cliente)

@cliente_route.route('/eliminar/<id>', methods=['GET','POST'])

def eliminar_cliente(id):

    if request.method == 'GET':
        clientes = Cliente.query.all()
        try:

            cliente = Cliente.query.get(id)        
            print(f'el cliente a eliminar es: {cliente}')
            if cliente is not None:
                Cliente.eliminar_cliente(cliente)
                flash("Cliente eliminado exitosamente.", "success")
                clientes = Cliente.query.all()
                return render_template('listado_clientes.html', clientes=clientes)
            else:
                flash(f"Error al eliminar el cliente", "error")
        except Exception as ex:
                flash(f"Cliente no existe: {ex}", "error")
                return render_template('listado_clientes.html', clientes=clientes)

