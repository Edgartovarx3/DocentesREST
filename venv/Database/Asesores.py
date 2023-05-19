from sqlalchemy.orm import relationship
from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, Integer, String
from . import db
from flask import jsonify
class Asesores(db.Model):
    __tablename__ = 'Asesores'
    idAsesores = db.Column(db.Integer, primary_key=True)
    esAsesor = db.Column(db.Boolean)
    asesorados = db.Column(db.Integer)
    alumnosAsesorados = db.Column(db.String(50))
    proyectosAsesorados = db.Column(db.Integer)
    fkIdUsuario = db.Column(db.Integer, db.ForeignKey('Usuarios.idUsuario'))
    usuario = db.relationship('Usuario',backref='Asesores')

    def consultaGeneral(self,idUsuario):  # select * from opciones
        lista = db.session.query(Asesores).filter_by(fkIdUsuario=idUsuario).all()

        respuesta = {"estatus": "", "mensaje": ""}
        try:
            if len(lista) > 0:
                respuesta["estatus"] = "OK"
                respuesta["mensaje"] = "Listado de Asesores."
                respuesta["Usuarios"] = [o.to_json() for o in lista]
            else:
                respuesta["estatus"] = "OK"
                respuesta["mensaje"] = "No hay usuarios registrados"
                respuesta["Usuarios"] = []
        except:
            respuesta["estatus"] = "Error"
            respuesta["mensaje"] = "Problemas de al ejecutar la consulta de opciones"
        return respuesta

    def agregarAsesor(self, asesor_data,idUsuario):
        try:

            asesor = Asesores(
                esAsesor=asesor_data['esAsesor'],
                asesorados=asesor_data['asesorados'],
                alumnosAsesorados=asesor_data['alumnosAsesorados'],
                proyectosAsesorados=asesor_data['proyectosAsesorados'],
                fkIdUsuario=idUsuario
            )
            if asesor.fkIdUsuario != idUsuario:
                return jsonify({
                    'estatus': 'Error',
                    'mensaje': 'No tienes permisos para agregar este asesor a otro docente'
                })

            db.session.add(asesor)
            db.session.commit()

            return jsonify({
                'estatus': 'OK',
                'mensaje': 'Asesor agregado correctamente',
                'idAsesores': asesor.idAsesores
            })
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Error al agregar el asesor',
                'detalle': str(e)
            })

    def modificarAsesor(self,asesor_id, asesor_data,idUsuario):
        try:
            asesor = Asesores.query.get(asesor_id)

            if not asesor:
                return jsonify({
                    'estatus': 'Error',
                    'mensaje': 'Asesor no encontrado'
                })
            if asesor.fkIdUsuario != idUsuario:
                return jsonify({
                    'estatus': 'Error',
                    'mensaje': 'No tienes permisos para modificar este asesor'
                })

            asesor.esAsesor = asesor_data.get('esAsesor', asesor.esAsesor)
            asesor.asesorados = asesor_data.get('asesorados', asesor.asesorados)
            asesor.alumnosAsesorados = asesor_data.get('alumnosAsesorados', asesor.alumnosAsesorados)
            asesor.proyectosAsesorados = asesor_data.get('proyectosAsesorados', asesor.proyectosAsesorados)
            asesor.fkIdUsuario = idUsuario

            db.session.commit()

            return jsonify({
                'estatus': 'OK',
                'mensaje': 'Asesor modificado correctamente',
            })
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Error al modificar el asesor',
                'detalle': str(e)
            })

    def eliminarAsesor(self,asesor_id,idUsuario):


        asesor = Asesores.query.get(asesor_id)

        if not asesor:
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Asesor no encontrado'
            })

        if asesor.fkIdUsuario != idUsuario:
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'No tienes permisos para eliminar este asesor'
            })

        try:
            db.session.delete(asesor)
            db.session.commit()

            return jsonify({
                'estatus': 'OK',
                'mensaje': 'Asesor eliminado correctamente',
            })
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Error al eliminar el asesor',
                'detalle': str(e)
            })

    def consultarAsesor(self, asesor_id,idUsuario):
        asesor = Asesores.query.get(asesor_id)

        if not asesor:
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Asesor no encontrado'
            })

        if asesor.fkIdUsuario != idUsuario:
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'No tienes permisos para consultar este asesor'
            })

        return jsonify({
            'estatus': 'OK',
            'mensaje': 'Asesor encontrado',
            'Asesor': asesor.to_json()
        })

    def to_json(self):
        return {
            'idAsesores': self.idAsesores,
            'esAsesor': self.esAsesor,
            'asesorados': self.asesorados,
            'alumnosAsesorados': self.alumnosAsesorados,
            'proyectosAsesorados': self.proyectosAsesorados,
            'fkIdUsuario': self.fkIdUsuario
        }
