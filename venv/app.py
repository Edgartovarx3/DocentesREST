from flask import Flask,url_for, request, redirect,flash,jsonify,g
from flask_sqlalchemy import SQLAlchemy
from werkzeug.serving import run_simple
from werkzeug.debug import DebuggedApplication

from Database.Usuario import Usuario
from Database import db
from Database.TrayectoriaProfesional import TrayectoriaProfesional
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)

app.config.from_pyfile('config.py')
db.init_app(app)
auth = HTTPBasicAuth()



########################Todo lo de la Autenticacion##################################


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
######################################################################################################################




###################Usuarios#####################3
@app.route('/usuarios', methods=['GET'])
def consulta_general():
    usuario = Usuario()
    respuesta = usuario.consultaGeneral()
    return jsonify(respuesta)

@app.route('/consultarUsuario/<int:id_usuario>', methods=['GET'])
def consultar_usuario(id_usuario):
    usuario=Usuario()
    return (usuario.consultar_usuario(id_usuario))

@app.route('/agregarUsuario', methods=['POST'])
@auth.login_required(role='A')
def agregarUsuario():
    # Obtén los datos del formulario JSON
    json_data = request.get_json()
    usuario = Usuario()
    # Devuelve una respuesta exitosa
    return  usuario.agregar(json_data)

@app.route('/usuarios/<int:idUsuario>', methods=['PUT'])
def actualizar_usuario(idUsuario):
    usuario=Usuario()

    return usuario.Actualizar(idUsuario)

@app.route('/eliminarUsuario/<int:id_usuario>', methods=['DELETE'])
def eliminar_usuario(id_usuario):
    usuario=Usuario()
    try:
        respuesta = usuario.eliminar_por_id(id_usuario)
        return respuesta
    except Exception as e:
        return jsonify({
            'estatus': 'Error',
            'mensaje': 'Error al eliminar el usuario',
            'detalle': str(e)
        })




#
@app.route('/consulta/Trayectoria', methods=['GET'])
@auth.login_required(role='D')
def consulta_general_trayectoria():
    trayectoria_profesional = TrayectoriaProfesional()
    respuesta = trayectoria_profesional.consultaGeneral()
    return jsonify(respuesta)

@app.route('/trayectorias/<int:id_trayectoria>', methods=['GET'])
@auth.login_required(role='D')
def obtener_trayectora(id_trayectoria):
    trayectoria=TrayectoriaProfesional()
    return trayectoria.obtener_trayectoria_por_id(id_trayectoria , g.current_user.idUsuario)

@app.route('/agregarTrayectoria', methods=['POST'])
@auth.login_required(role='D')
def agregarTrayectoria():

    # Obtén los datos del formulario JSON
    json_data = request.get_json()
    trayectoriaProfesional = TrayectoriaProfesional()
    # Devuelve una respuesta exitosa
    return  trayectoriaProfesional.agregar_trayectoria_profesional(json_data,g.current_user.idUsuario)

@app.route('/trayectorias/<int:id_trayectoria>', methods=['PUT'])
@auth.login_required
def modificar_trayectoria(id_trayectoria):
    trayectoria_data = request.json
    trayectoriaProfesional=TrayectoriaProfesional()
    trayectoria = trayectoriaProfesional.modificar_trayectoria_profesional(id_trayectoria,trayectoria_data, g.current_user.idUsuario)
    return trayectoria

@app.route('/trayectorias/<int:id_trayectoria>', methods=['DELETE'])
@auth.login_required
def eliminar_trayectoria(id_trayectoria):
    trayectoria=TrayectoriaProfesional()

    return trayectoria.eliminar_trayectoria_profesional(id_trayectoria,g.current_user.idUsuario)




####################################################



if __name__ == '__main__':
    app.debug = True
    app = DebuggedApplication(app, evalex=True)
    run_simple('localhost', 5000, app, use_reloader=True)