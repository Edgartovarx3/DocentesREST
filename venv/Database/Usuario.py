from flask import jsonify,request
from Database import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String,text
import json

class Usuario(db.Model):
    __tablename__ = 'Usuarios'
    idUsuario = Column(Integer, primary_key=True)
    nombreUsuario = Column(String(30))
    apellidoPaUsuario = Column(String(30))
    apellidoMaUsuario = Column(String(30))
    correoUsuario = Column(String(50))
    passwordUsuario = Column(String(40))
    tipoUsuario = Column(String(1))

    def consultaGeneral(self):  # select * from opciones
        lista = db.session.query(Usuario).all()
        respuesta = {"estatus": "", "mensaje": ""}
        try:
            if len(lista) > 0:
                respuesta["estatus"] = "OK"
                respuesta["mensaje"] = "Listado de Usuarios."
                respuesta["Usuarios"] = [o.to_json() for o in lista]
            else:
                respuesta["estatus"] = "OK"
                respuesta["mensaje"] = "No hay usuarios registrados"
                respuesta["Usuarios"] = []
        except:
            respuesta["estatus"] = "Error"
            respuesta["mensaje"] = "Problemas de al ejecutar la consulta de opciones"
        return respuesta

    def consultar_usuario(self,id_usuario):
        usuario = Usuario.query.get(id_usuario)
        try:

            if usuario is not None:
                return jsonify({
                    'estatus': 'OK',
                    'mensaje': 'Usuario encontrado',
                    'usuario': usuario.to_json()
                })
            else:
                return jsonify({
                    'estatus': 'Error',
                    'mensaje': 'Usuario no encontrado'
                })
        except Exception as e:
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Error al consultar el usuario',
                'detalle': str(e)
            })

    def agregar(self, usuario_data,idUsuario):
        # Crea una expresión textual del procedimiento almacenado
        procedure = text(
            "EXEC sp_InsertUsuario :nombreUsuario, :apellidoPaUsuario, :apellidoMaUsuario, :correoUsuario, :passwordUsuario, :tipoUsuario"
        )

        try:

            # Ejecuta el procedimiento almacenado con los parámetros del diccionario
            result = db.session.execute(
                procedure,
                {
                    'nombreUsuario': usuario_data['nombreUsuario'],
                    'apellidoPaUsuario': usuario_data['apellidoPaUsuario'],
                    'apellidoMaUsuario': usuario_data['apellidoMaUsuario'],
                    'correoUsuario': usuario_data['correoUsuario'],
                    'passwordUsuario': usuario_data['passwordUsuario'],
                    'tipoUsuario': usuario_data['tipoUsuario']
                }
            )
            id_usuario = result.scalar()
            # Confirma los cambios en la sesión de base de datos
            db.session.commit()

            # Devuelve una respuesta exitosa
            return jsonify ({
                'estatus': 'OK',
                'mensaje': 'Usuario agregado correctamente si',
                'idUsuario': id_usuario
            })
        except Exception as e:
            # Maneja cualquier excepción y realiza un rollback en caso de error
            db.session.rollback()
            return jsonify( {
                'estatus': 'Error',
                'mensaje': 'Error al agregar el usuario',
                'detalle': str(e)
            })

    def Actualizar(self, idUsuario ):
        usuario = Usuario.query.get(idUsuario)

        if usuario is None:
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Usuario no encontrado'
            }), 404

        try:
            # Actualizar los campos del usuario según los datos proporcionados en el cuerpo de la solicitud
            if 'nombreUsuario' in request.json:
                usuario.nombreUsuario = request.json['nombreUsuario']
            if 'apellidoPaUsuario' in request.json:
                usuario.apellidoPaUsuario = request.json['apellidoPaUsuario']
            if 'apellidoMaUsuario' in request.json:
                usuario.apellidoMaUsuario = request.json['apellidoMaUsuario']
            if 'correoUsuario' in request.json:
                usuario.correoUsuario = request.json['correoUsuario']
            if 'passwordUsuario' in request.json:
                usuario.passwordUsuario = request.json['passwordUsuario']
            if 'tipoUsuario' in request.json:
                usuario.tipoUsuario = request.json['tipoUsuario']

            # Guardar los cambios en la base de datos
            db.session.commit()

            return jsonify({
                'estatus': 'OK',
                'mensaje': 'Usuario actualizado correctamente'
            }), 200

        except Exception as e:
            # Realizar rollback en caso de error
            db.session.rollback()

            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Error al actualizar el usuario',
                'detalle': str(e)
            }), 500

    def eliminar_por_id(self,usuarioid):
        try:
            usuario = Usuario.query.get(usuarioid)
            if usuario:
                db.session.delete(usuario)
                db.session.commit()
                return jsonify({
                    'estatus': 'OK',
                    'mensaje': 'Usuario eliminado correctamente'
                })
            else:
                return jsonify({
                    'estatus': 'Error',
                    'mensaje': 'Usuario no encontrado'
                })
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Error al eliminar el usuario',
                'detalle': str(e)
            })





    def to_json(self):
        usuario_json = {
            'idUsuario': self.idUsuario,
            'nombreUsuario': self.nombreUsuario,
            'apellidoPaUsuario': self.apellidoPaUsuario,
            'apellidoMaUsuario': self.apellidoMaUsuario,
            'correoUsuario': self.correoUsuario,
            'passwordUsuario': self.passwordUsuario,
            'tipoUsuario': self.tipoUsuario
        }
        return usuario_json

