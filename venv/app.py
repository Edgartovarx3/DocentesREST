from flask import Flask,url_for, render_template, request, redirect,flash,jsonify,g
from flask_sqlalchemy import SQLAlchemy
from werkzeug.serving import run_simple
from werkzeug.debug import DebuggedApplication
from Database.TemasInteres import TemasInteres
from Database.Usuario import Usuario
from Database import db
from flask_httpauth import HTTPBasicAuth


@app = Flask(__name__)

@app.config.from_pyfile('config.py')
db.init_app(app)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(correo, password):
    # Buscar el usuario en la base de datos
    usuario = Usuario.query.filter_by(correoUsuario=correo).first()

    if usuario and usuario.passwordUsuario == password:
        g.current_user=usuario
        return usuario
@auth.get_user_roles
def get_user_roles(usuario):
    tipo_usuario = usuario.tipoUsuario

    roles = []
    if tipo_usuario == "D":
        roles.append("D")
    elif tipo_usuario == "A":
        roles.append("A")
    return roles
@auth.error_handler
def auth_error():
    return jsonify({
        'estatus': 'Error',
        'mensaje': 'No tienes permiso',
        'detalle': 'El usuario que se inicio sesion no tiene los permisos para realizar esta accion'
    }), 401
@app.route('/login')
@auth.login_required(role=['D','A'])
def login():
    # Obtener el usuario autenticado
    usuario = auth.current_user()
    return jsonify({'message': 'Inicio de sesión exitoso', 'usuario': usuario.to_json()})

@app.route('/usuarios', methods=['GET'])
@auth.login_required(role='A')
def consulta_general():
    usuario = Usuario()
    respuesta = usuario.consultaGeneral()
    return jsonify(respuesta)

@app.route('/consultarUsuario', methods=['GET'])
@auth.login_required(role=['A','D'])
def consultar_usuario():
    usuario=Usuario()
    return (usuario.consultar_usuario(g.current_user.idUsuario))

@app.route('/agregarUsuario', methods=['POST'])
@auth.login_required(role='A')
def agregarUsuario():
    # Obtén los datos del formulario JSON
    json_data = request.get_json()
    usuario = Usuario()
    # Devuelve una respuesta exitosa
    return  usuario.agregar(json_data,g.current_user.idUsuario)

@app.route('/usuarios', methods=['PUT'])
@auth.login_required(role='A')
def actualizar_usuario():
    usuario=Usuario()

    return usuario.Actualizar(g.current_user.idUsuario)

@app.route('/eliminarUsuario/<int:usuarioid>', methods=['DELETE'])
@auth.login_required(role='A')
def eliminar_usuario(usuarioid):
    usuario=Usuario()
    try:
        respuesta = usuario.eliminar_por_id(usuarioid)
        return respuesta
    except Exception as e:
        return jsonify({
            'estatus': 'Error',
            'mensaje': 'Error al eliminar el usuario',
            'detalle': str(e)
        })

@app.route('/temasinteres/consulta/<int:tema_id>', methods=['GET'])
@auth.login_required
def consultarTemasInteres():
    temas_interes = TemasInteres()
    return temas_interes.consultaGeneral(g.current_user.idUsuario)

@app.route('/temasinteres/agregar', methods=['POST'])
@auth.login_required
def agregarTemaInteres():
    temas_interes = TemasInteres()
    tema_data = request.get_json()
    return temas_interes.agregarTemaInteres(tema_data, g.current_user.idUsuario)

@app.route('/temasinteres/modificar/<int:tema_id>', methods=['PUT'])
@auth.login_required
def modificarTemaInteres(tema_id):
    temas_interes = TemasInteres()
    tema_data = request.get_json()
    return temas_interes.modificarTemaInteres(tema_id, tema_data, g.current_user.idUsuario)

@app.route('/temasinteres/eliminar/<int:tema_id>', methods=['DELETE'])
@auth.login_required
def eliminarTemaInteres(tema_id):
    temas_interes = TemasInteres()
    return temas_interes.eliminarTemaInteres(tema_id, g.current_user.idUsuario)

@app.route('/temasinteres/consultar/<int:tema_id>', methods=['GET'])
@auth.login_required
def consultarTemaInteres(tema_id):
    temas_interes = TemasInteres()
    return temas_interes.consultarTemaInteres(tema_id, g.current_user.idUsuario)


if __name__ == '__main__':
    app.debug = True
    app = DebuggedApplication(app, evalex=True)
    run_simple('localhost', 5000, app, use_reloader=True)