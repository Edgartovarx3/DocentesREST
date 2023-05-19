# Database/Horarios.py

from Database import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String

class Horarios(db.Model):
    __tablename__ = 'Horarios'
    idHorario = db.Column(db.Integer, primary_key=True)
    horaInicio = db.Column(db.Date)
    horaFin = db.Column(db.Date)
    fkIdUsuario = db.Column(db.Integer, db.ForeignKey('Usuarios.idUsuario'))
    usuario = db.relationship('Usuario', backref='Horarios')



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


