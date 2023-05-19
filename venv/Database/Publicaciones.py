from sqlalchemy.orm import relationship
from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, Integer, String
from . import db
from flask import jsonify

class Publicaciones(db.Model):
    __tablename__ = 'Publicaciones'
    idPublicaciones = db.Column(db.Integer, primary_key=True)
    tituloPublicaciones = db.Column(db.String(80))
    descripcionPublicaciones = db.Column(db.String(200))
    linkPublicaciones = db.Column(db.Text)
    fkIdUsuario = db.Column(db.Integer, db.ForeignKey('Usuarios.idUsuario'))
    usuario = db.relationship('Usuario', backref='publicaciones')




    ####Todos los metodos aqui####
    def consultaGeneral(self,idUsuario):  # select * from opciones
        lista = db.session.query(Publicaciones).filter_by(fkIdUsuario=idUsuario).all()
        respuesta = {"estatus": "", "mensaje": ""}
        try:
            if len(lista) > 0:
                respuesta["estatus"] = "OK"
                respuesta["mensaje"] = "Listado de publicaciones."
                respuesta["Usuarios"] = [o.to_json() for o in lista]
            else:
                respuesta["estatus"] = "OK"
                respuesta["mensaje"] = "No hay usuarios registrados"
                respuesta["Usuarios"] = []
        except:
            respuesta["estatus"] = "Error"
            respuesta["mensaje"] = "Problemas de al ejecutar la consulta de opciones"
        return respuesta

    def consultaIndividual(self,publicacion_id,idUsuario):
        respuesta = {"estatus": "", "mensaje": ""}
        try:
            # Realizar la verificación de autenticación y obtener el idUsuario
            # Lógica para obtener self.idUsuario según la autenticación

            publicacion = Publicaciones.query.get(publicacion_id)

            if not publicacion:
                respuesta["estatus"] = "Error"
                respuesta["mensaje"] = "Publicación no encontrada"
            elif publicacion.fkIdUsuario != idUsuario:
                respuesta["estatus"] = "Error"
                respuesta["mensaje"] = "No tienes permiso para ver esta publicación"
            else:
                respuesta["estatus"] = "OK"
                respuesta["mensaje"] = "Publicación encontrada"
                respuesta["Publicacion"] = publicacion.to_json()
        except Exception as e:
            respuesta["estatus"] = "Error"
            respuesta["mensaje"] = "Problemas al ejecutar la consulta de publicación"
            respuesta["detalle"] = str(e)
        return respuesta

    def agregarPublicacion(self,json_data,idUsuario):


      try:
       publicacion=Publicaciones( tituloPublicaciones = json_data['tituloPublicaciones'],
        descripcionPublicaciones = json_data['descripcionPublicaciones'],
        linkPublicaciones = json_data['linkPublicaciones'],
        fkIdUsuario = idUsuario
       )

       db.session.add(publicacion)
       db.session.commit()

       return jsonify({
        'estatus': 'OK',
        'mensaje': 'Usuario agregado correctamente si',

    })
      except Exception as e:
    # Maneja cualquier excepción y realiza un rollback en caso de error
         db.session.rollback()
         return jsonify({
            'estatus': 'Error',
            'mensaje': 'Error al agregar el usuario',
            'detalle': str(e)
        })

    def modificarPublicacion(self, publicacion_id, json_data,idUsuario):
        try:
            publicacion = Publicaciones.query.get(publicacion_id)

            if not publicacion:
                return jsonify({
                    'estatus': 'Error',
                    'mensaje': 'Publicación no encontrada'
                })

            if publicacion.fkIdUsuario != idUsuario:
                return jsonify({
                    'estatus': 'Error',
                    'mensaje': 'No tienes permiso para modificar esta publicación'
                })

            publicacion.tituloPublicaciones = json_data['tituloPublicaciones']
            publicacion.descripcionPublicaciones = json_data['descripcionPublicaciones']
            publicacion.linkPublicaciones = json_data['linkPublicaciones']

            db.session.commit()

            return jsonify({
                'estatus': 'OK',
                'mensaje': 'Publicación modificada correctamente',
            })

        except Exception as e:
            # Maneja cualquier excepción y realiza un rollback en caso de error
            db.session.rollback()
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Error al modificar la publicación',
                'detalle': str(e)
            })

    def eliminarPublicacion(self, publicacion_id, idUsuario):
        try:
            # Realizar la verificación de autenticación y obtener el idUsuario
            # Lógica para obtener self.idUsuario según la autenticación

            publicacion = Publicaciones.query.get(publicacion_id)

            if not publicacion:
                return jsonify({
                    'estatus': 'Error',
                    'mensaje': 'Publicación no encontrada'
                })

            if publicacion.fkIdUsuario != idUsuario:
                return jsonify({
                    'estatus': 'Error',
                    'mensaje': 'No tienes permiso para eliminar esta publicación'
                })

            db.session.delete(publicacion)
            db.session.commit()

            return jsonify({
                'estatus': 'OK',
                'mensaje': 'Publicación eliminada correctamente',
            })

        except Exception as e:
            # Maneja cualquier excepción y realiza un rollback en caso de error
            db.session.rollback()
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Error al eliminar la publicación',
                'detalle': str(e)
            })

    def to_json(self):
        return {
            'idPublicaciones': self.idPublicaciones,
            'tituloPublicaciones': self.tituloPublicaciones,
            'descripcionPublicaciones': self.descripcionPublicaciones,
            'linkPublicaciones': self.linkPublicaciones,
            'fkIdUsuario': self.fkIdUsuario
        }
