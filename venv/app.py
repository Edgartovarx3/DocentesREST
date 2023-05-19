from flask import Flask,url_for, render_template, request, redirect,flash,jsonify,g
from flask_sqlalchemy import SQLAlchemy
from werkzeug.serving import run_simple
from werkzeug.debug import DebuggedApplication

from Database.Usuario import Usuario

from Database import db
from Database.Publicaciones import Publicaciones
from Database.Asesores import Asesores

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
################################################






##################publicaciones#######################
@app.route('/publicaciones', methods=['GET'])
@auth.login_required(role='D')
def consulta_general_route():
    publicacion=Publicaciones()
    respuesta = publicacion.consultaGeneral(g.current_user.idUsuario)  # Lógica para obtener self.idUsuario según la autenticación
    return jsonify(respuesta)

@app.route('/publicaciones/<int:publicacion_id>', methods=['GET'])
@auth.login_required(role='D')
def consulta_individual_route(publicacion_id):
    publicacion=Publicaciones()
    respuesta = publicacion.consultaIndividual(publicacion_id,g.current_user.idUsuario)
    return jsonify(respuesta)
@app.route('/agregarPublicacion', methods=['POST'])
@auth.login_required(role='D')
def agregarPublicacion():

        json_data = request.get_json()

        # Crea una instancia de la clase Publicaciones
        publicacion = Publicaciones()
        # Devuelve una respuesta exitosa
        return publicacion.agregarPublicacion(json_data,g.current_user.idUsuario)

@app.route('/publicaciones/<int:publicacion_id>', methods=['PUT'])
@auth.login_required(role='D')
def modificar_publicacion(publicacion_id):
    json_data = request.get_json()
    publicacion=Publicaciones()
    response = publicacion.modificarPublicacion(publicacion_id, json_data,g.current_user.idUsuario)
    return response

@app.route('/publicaciones/<int:publicacion_id>', methods=['DELETE'])
@auth.login_required(role='D')
def eliminar_publicacion(publicacion_id):
    publicacion=Publicaciones()
    response = publicacion.eliminarPublicacion(publicacion_id,g.current_user.idUsuario)
    return response


#####################################################







######################Asesores###############################

@app.route('/asesores', methods=['POST'])
@auth.login_required(role='D')
def agregar_asesor_route():
    asesor_data = request.get_json()
    asesor = Asesores()
    return asesor.agregarAsesor(asesor_data,g.current_user.idUsuario)

# Ruta para modificar un asesor
@app.route('/asesores/<int:asesor_id>', methods=['PUT'])
@auth.login_required(role='D')
def modificar_asesor_route(asesor_id):
    asesor = Asesores()
    asesor_data = request.get_json()
    return asesor.modificarAsesor(asesor_id, asesor_data,g.current_user.idUsuario)

# Ruta para eliminar un asesor
@app.route('/asesores/<int:asesor_id>', methods=['DELETE'])
@auth.login_required(role='D')
def eliminar_asesor(asesor_id):
    asesor = Asesores()
    return asesor.eliminarAsesor(asesor_id,g.current_user.idUsuario)

# Ruta para consultar un asesor por su ID
@app.route('/asesores/<int:asesor_id>', methods=['GET'])
@auth.login_required(role='D')
def consultar_asesor(asesor_id):
    asesor = Asesores()
    return asesor.consultarAsesor(asesor_id,g.current_user.idUsuario)

@app.route('/asesores', methods=['GET'])
@auth.login_required(role='D')
def consultaGeneralAsesor():
    asesor=Asesores()
    return asesor.consultaGeneral(g.current_user.idUsuario)

#####################################################






#



if __name__ == '__main__':
    app.debug = True
    app = DebuggedApplication(app, evalex=True)
    run_simple('localhost', 5000, app, use_reloader=True)