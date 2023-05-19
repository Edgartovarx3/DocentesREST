# Database/TemasInteres.py

from sqlalchemy.orm import relationship
from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, Integer, String
from . import db
from flask import jsonify

class TemasInteres(db.Model):
    __tablename__ = 'TemasInteres'
    idTemaInteres = db.Column(db.Integer, primary_key=True)
    areaProfesional = db.Column(db.String(40))
    experiencia = db.Column(db.String(200))
    fkIdUsuario = db.Column(db.Integer, db.ForeignKey('Usuarios.idUsuario'))
    usuario = relationship('Usuario', backref='TemasInteres')

    def consultaGeneral(self, idUsuario):
        lista = db.session.query(TemasInteres).filter_by(fkIdUsuario=idUsuario).all()

        respuesta = {"estatus": "", "mensaje": ""}
        try:
            if len(lista) > 0:
                respuesta["estatus"] = "OK"
                respuesta["mensaje"] = "Listado de Temas de Interés."
                respuesta["TemasInteres"] = [o.to_json() for o in lista]
            else:
                respuesta["estatus"] = "OK"
                respuesta["mensaje"] = "No hay temas de interés registrados"
                respuesta["TemasInteres"] = []
        except:
            respuesta["estatus"] = "Error"
            respuesta["mensaje"] = "Problemas al ejecutar la consulta de temas de interés"
        return respuesta

    def agregarTemaInteres(self, tema_data, idUsuario):
        try:
            tema = TemasInteres(
                areaProfesional=tema_data['areaProfesional'],
                experiencia=tema_data['experiencia'],
                fkIdUsuario=idUsuario
            )
            if tema.fkIdUsuario != idUsuario:
                return jsonify({
                    'estatus': 'Error',
                    'mensaje': 'No tienes permisos para agregar este tema de interés a otro docente'
                })

            db.session.add(tema)
            db.session.commit()

            return jsonify({
                'estatus': 'OK',
                'mensaje': 'Tema de interés agregado correctamente',
                'idTemaInteres': tema.idTemaInteres
            })
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Error al agregar el tema de interés',
                'detalle': str(e)
            })

    def modificarTemaInteres(self, tema_id, tema_data, idUsuario):
        try:
            tema = TemasInteres.query.get(tema_id)

            if not tema:
                return jsonify({
                    'estatus': 'Error',
                    'mensaje': 'Tema de interés no encontrado'
                })

            if tema.fkIdUsuario != idUsuario:
                return jsonify({
                    'estatus': 'Error',
                    'mensaje': 'No tienes permisos para modificar este tema de interés'
                })

            tema.areaProfesional = tema_data.get('areaProfesional', tema.areaProfesional)
            tema.experiencia = tema_data.get('experiencia', tema.experiencia)
            tema.fkIdUsuario = idUsuario

            db.session.commit()

            return jsonify({
                'estatus': 'OK',
                'mensaje': 'Tema de interés modificado correctamente',
            })
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Error al modificar el tema de interés',
                'detalle': str(e)
            })

    def eliminarTemaInteres(self, tema_id, idUsuario):
        tema = TemasInteres.query.get(tema_id)

        if not tema:
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Tema de interés no encontrado'
            })

        if tema.fkIdUsuario != idUsuario:
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'No tienes permisos para eliminar este tema de interés'
            })

        try:
            db.session.delete(tema)
            db.session.commit()

            return jsonify({
                'estatus': 'OK',
                'mensaje': 'Tema de interés eliminado correctamente',
            })
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Error al eliminar el tema de interés',
                'detalle': str(e)
            })

    def consultarTemaInteres(self, tema_id, idUsuario):
        tema = TemasInteres.query.get(tema_id)

        if not tema:
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Tema de interés no encontrado'
            })

        if tema.fkIdUsuario != idUsuario:
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'No tienes permisos para consultar este tema de interés'
            })

        return jsonify({
            'estatus': 'OK',
            'mensaje': 'Tema de interés encontrado',
            'TemaInteres': tema.to_json()
        })

    def to_json(self):
        return {
            'idTemaInteres': self.idTemaInteres,
            'areaProfesional': self.areaProfesional,
            'experiencia': self.experiencia,
            'fkIdUsuario': self.fkIdUsuario
        }
