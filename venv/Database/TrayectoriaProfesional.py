# Database/TrayectoriaProfesional.py
from . import db
from flask import jsonify,request
from . import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.exc import SQLAlchemyError



class TrayectoriaProfesional(db.Model):
    __tablename__ = 'TrayectoriaProfesional'
    idTrayectoria = db.Column(db.Integer, primary_key=True)
    tipoParticipacion = db.Column(db.String(40))
    tituloParticipacion = db.Column(db.String(30))
    Descripcion = db.Column(db.String(200))
    fkIdUsuario = db.Column(db.Integer, db.ForeignKey('Usuarios.idUsuario'))
    usuario = db.relationship('Usuario', backref='TrayectoriaProfesional')

    def consultaGeneral(self):  # select * from opciones
        lista =db.session.query(TrayectoriaProfesional).all()
        respuesta = {"estatus": "", "mensaje": ""}
        try:
            if len(lista) > 0:
                respuesta["estatus"] = "OK"
                respuesta["mensaje"] = "Listado de opciones de titulacion."
                respuesta["opciones"] = [o.to_json() for o in lista]
            else:
                respuesta["estatus"] = "OK"
                respuesta["mensaje"] = "No hay opciones registradas"
                respuesta["opciones"] = []
        except:
            respuesta["estatus"] = "Error"
            respuesta["mensaje"] = "Problemas de al ejecutar la consulta de opciones"
        return respuesta
    def obtener_trayectoria_por_id(self, id_trayectoria,idUsuario):
        try:
            trayectoria = TrayectoriaProfesional.query.get(id_trayectoria)

            if not trayectoria:
                return jsonify({
                    'estatus': 'Error',
                    'mensaje': 'Trayectoria profesional no encontrada'
                })
            if trayectoria.fkIdUsuario != idUsuario:
                return jsonify({
                    'estatus': 'Error',
                    'mensaje': 'No tienes permiso para ver esta trayectoria profesional'
                })

            trayectoria_data = {
                'idTrayectoria': trayectoria.idTrayectoria,
                'tipoParticipacion': trayectoria.tipoParticipacion,
                'tituloParticipacion': trayectoria.tituloParticipacion,
                'Descripcion': trayectoria.Descripcion,
                'fkIdUsuario': trayectoria.fkIdUsuario
            }

            return jsonify(trayectoria_data)

        except Exception as e:
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Error al obtener la trayectoria profesional',
                'detalle': str(e)
            })

    def agregar_trayectoria_profesional(self, trayectoria_data,idUsuario):
        try:
            # Crea una instancia del modelo TrayectoriaProfesional con los datos proporcionados
            trayectoria = TrayectoriaProfesional(
                tipoParticipacion=trayectoria_data['tipoParticipacion'],
                tituloParticipacion=trayectoria_data['tituloParticipacion'],
                Descripcion=trayectoria_data['Descripcion'],
                fkIdUsuario=idUsuario  # Asigna el ID del usuario actual
            )

            # Agrega la instancia a la sesión de base de datos
            db.session.add(trayectoria)
            # Confirma los cambios en la sesión de base de datos
            db.session.commit()

            # Devuelve una respuesta exitosa
            return jsonify({
                'estatus': 'OK',
                'mensaje': 'Trayectoria profesional agregada correctamente',
                'idTrayectoria': trayectoria.idTrayectoria
            })
        except SQLAlchemyError as e:
            # Maneja cualquier excepción de SQLAlchemy y realiza un rollback en caso de error
            db.session.rollback()
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Error al agregar la trayectoria profesional',
                'detalle': str(e)
            })
        except Exception as e:
            # Maneja cualquier otra excepción y realiza un rollback en caso de error
            db.session.rollback()
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Error al agregar la trayectoria profesional',
                'detalle': str(e)
            })

    def modificar_trayectoria_profesional(self,id_trayectoria, trayectoria_data, idUsuario):
        try:
            # Busca la trayectoria profesional por su ID
            trayectoria = TrayectoriaProfesional.query.get(id_trayectoria)

            if not trayectoria:
                return jsonify({
                    'estatus': 'Error',
                    'mensaje': 'Trayectoria profesional no encontrada'
                })

            # Verifica si el ID de usuario coincide con el de la trayectoria
            if trayectoria.fkIdUsuario != idUsuario:
                return jsonify({
                    'estatus': 'Error',
                    'mensaje': 'No tienes permiso para modificar esta trayectoria profesional'
                })

            # Actualiza los datos de la trayectoria profesional
            trayectoria.tipoParticipacion = trayectoria_data.get('tipoParticipacion', trayectoria.tipoParticipacion)
            trayectoria.tituloParticipacion = trayectoria_data.get('tituloParticipacion',
                                                                   trayectoria.tituloParticipacion)
            trayectoria.Descripcion = trayectoria_data.get('Descripcion', trayectoria.Descripcion)

            # Realiza la actualización en la base de datos
            db.session.commit()

            # Devuelve una respuesta exitosa
            return jsonify({
                'estatus': 'OK',
                'mensaje': 'Trayectoria profesional modificada correctamente',
                'idTrayectoria': trayectoria.idTrayectoria
            })

        except Exception as e:
            # Maneja cualquier excepción y realiza un rollback en caso de error
            db.session.rollback()
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Error al modificar la trayectoria profesional',
                'detalle': str(e)
            })

    def eliminar_trayectoria_profesional(self,id_trayectoria,idUsuario):
        try:
            # Busca la trayectoria profesional por su ID
            trayectoria = TrayectoriaProfesional.query.get(id_trayectoria)

            if not trayectoria:
                return jsonify({
                    'estatus': 'Error',
                    'mensaje': 'Trayectoria profesional no encontrada'
                })

            # Verifica si el ID de usuario coincide con el de la trayectoria
            if trayectoria.fkIdUsuario != idUsuario:
                return jsonify({
                    'estatus': 'Error',
                    'mensaje': 'No tienes permiso para eliminar esta trayectoria profesional'
                })

            # Elimina la trayectoria profesional de la base de datos
            db.session.delete(trayectoria)
            db.session.commit()

            # Devuelve una respuesta exitosa
            return jsonify({
                'estatus': 'OK',
                'mensaje': 'Trayectoria profesional eliminada correctamente',
                'idTrayectoria': id_trayectoria
            })

        except Exception as e:
            # Maneja cualquier excepción y realiza un rollback en caso de error
            db.session.rollback()
            return jsonify({
                'estatus': 'Error',
                'mensaje': 'Error al eliminar la trayectoria profesional',
                'detalle': str(e)
            })

    def to_json(self):
        trayectoria_json = {
            "idTrayectoria": self.idTrayectoria,
            "tipoParticipacion": self.tipoParticipacion,
            "tituloParticipacion": self.tituloParticipacion,
            "Descripcion": self.Descripcion,
            "fkIdUsuario": self.fkIdUsuario
        }
        return trayectoria_json
