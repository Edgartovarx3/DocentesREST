from sqlalchemy.orm import relationship
from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, Integer, String
from . import db

class Asesores(db.Model):
    __tablename__ = 'Asesores'
    idAsesores = db.Column(db.Integer, primary_key=True)
    esAsesor = db.Column(db.Boolean)
    asesorados = db.Column(db.Integer)
    alumnosAsesorados = db.Column(db.String(50))
    proyectosAsesorados = db.Column(db.Integer)
    fkIdUsuario = db.Column(db.Integer, db.ForeignKey('Usuarios.idUsuario'))
    usuario = db.relationship('Usuario',backref='Asesores')

    def consultaGeneral(self):  # select * from opciones
        lista = db.session.query(Publicaciones).all()
        respuesta = {"estatus": "", "mensaje": ""}
        try:
            if len(lista) > 0:
                respuesta["estatus"] = "OK"
                respuesta["mensaje"] = "Listado de Horarios."
                respuesta["Usuarios"] = [o.to_json() for o in lista]
            else:
                respuesta["estatus"] = "OK"
                respuesta["mensaje"] = "No hay usuarios registrados"
                respuesta["Usuarios"] = []
        except:
            respuesta["estatus"] = "Error"
            respuesta["mensaje"] = "Problemas de al ejecutar la consulta de opciones"
        return respuesta

    def to_json(self):
        return {
            'idAsesores': self.idAsesores,
            'esAsesor': self.esAsesor,
            'asesorados': self.asesorados,
            'alumnosAsesorados': self.alumnosAsesorados,
            'proyectosAsesorados': self.proyectosAsesorados,
            'fkIdUsuario': self.fkIdUsuario
        }
