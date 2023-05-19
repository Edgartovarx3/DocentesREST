from app import db

class Carreras(db.Model):
    idCarrera = db.Column(db.Integer, primary_key=True)
    nombreCarrera = db.Column(db.String(50))
    planEstudio = db.Column(db.String(200))
    fkIdDocente = db.Column(db.Integer, db.ForeignKey('Docentes.idDocente'))


class Docentes(db.Model):
    idDocente = db.Column(db.Integer, primary_key=True)
    nombreDocente = db.Column(db.String(30))
    apellidoPaDocente = db.Column(db.String(30))
    apellidoMaDocente = db.Column(db.String(30))
    correoDocente = db.Column(db.String(50))
    RFC = db.Column(db.String(13))
    numeroDocente = db.Column(db.String(15))
    Domicilio = db.Column(db.String(150))

class Materias(db.Model):
    idMateria = db.Column(db.Integer, primary_key=True)
    nombreMateria = db.Column(db.String(30))
    semestre = db.Column(db.String(30))
    fkIdCarrera = db.Column(db.Integer, db.ForeignKey('Carreras.idCarrera'))

class Horarios(db.Model):
    idHorario = db.Column(db.Integer, primary_key=True)
    horaInicio = db.Column(db.Date)
    horaFin = db.Column(db.Date)
    fkIdDocente = db.Column(db.Integer, db.ForeignKey('docentes.idDocente'))

class TrayectoriaProfesional(db.Model):
    idTrayectoria = db.Column(db.Integer, primary_key=True)
    tipoParticipacion = db.Column(db.String(40))
    tituloParticipacion = db.Column(db.String(30))
    Descripcion = db.Column(db.String(200))
    fkIdDocente = db.Column(db.Integer, db.ForeignKey('docentes.idDocente'))

class TemasInteres(db.Model):
    idTemas = db.Column(db.Integer, primary_key=True)
    AreaProfesional = db.Column(db.String(40))
    Experiencia = db.Column(db.String(200))
    fkIdDocente = db.Column(db.Integer, db.ForeignKey('docentes.idDocente'))