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
    def consultaGeneral(self):  # select * from opciones
        lista = db.session.query(Publicaciones).all()
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

    def agregarPublicacion(self,json_data):
      try:
       publicacion=Publicaciones( tituloPublicaciones = json_data['tituloPublicaciones'],
        descripcionPublicaciones = json_data['descripcionPublicaciones'],
        linkPublicaciones = json_data['linkPublicaciones'],
        fkIdUsuario = json_data['fkIdUsuario'],
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


    def to_json(self):
        return {
            'idPublicaciones': self.idPublicaciones,
            'tituloPublicaciones': self.tituloPublicaciones,
            'descripcionPublicaciones': self.descripcionPublicaciones,
            'linkPublicaciones': self.linkPublicaciones,
            'fkIdUsuario': self.fkIdUsuario
        }
