create database Docente
use Docente



CREATE TABLE Usuarios(
idUsuario int IDENTITY(1, 1) PRIMARY KEY,
nombreUsuario VARCHAR(30),
apellidoPaUsuario VARCHAR(30),
apellidoMaUsuario VARCHAR(30),
correoUsuario VARCHAR(50),
passwordUsuario varchar(40),
tipoUsuario VARCHAR(1),
);


INSERT INTO Administrador (correoAdministrador, passwordAdministrador)
VALUES ('egaribay072@accitesz.com', 'Hola.123');

---tablas bd-------
CREATE TABLE Asesores (
    idAsesores int IDENTITY(1, 1) PRIMARY KEY,
    esAsesor BIT,
    asesorados INT,
    alumnosAsesorados VARCHAR(50),
    proyectosAsesorados INT,
    fkIdUsuario INT,
    FOREIGN KEY (fkIdUsuario) REFERENCES Usuarios (idUsuario)
);

CREATE TABLE Publicaciones (
    idPublicaciones int IDENTITY(1, 1) PRIMARY KEY,
    tituloPublicaciones VARCHAR(80),
    descripcionPublicaciones VARCHAR(200),
    linkPublicaciones TEXT,
    fkIdUsuario INT,
    FOREIGN KEY (fkIdUsuario) REFERENCES Usuarios(idUsuario)
);


CREATE TABLE Horarios (
    idHorario int IDENTITY(1, 1) PRIMARY KEY,
    horaInicio DATE,
    horaFin DATE,
    fkIdUsuario INT,
    FOREIGN KEY (fkIdUsuario) REFERENCES Usuarios(idUsuario)
);

CREATE TABLE TrayectoriaProfesional (
    idTrayectoria int IDENTITY(1, 1) PRIMARY KEY,
    tipoParticipacion VARCHAR(40),
    tituloParticipacion VARCHAR(30),
    Descripcion VARCHAR(200),
    fkIdUsuario INT,
    FOREIGN KEY (fkIdUsuario) REFERENCES Usuarios(idUsuario)
);

CREATE TABLE TemasInteres (
    idTemaInteres int IDENTITY(1, 1) PRIMARY KEY,
    areaProfesional VARCHAR(40),
    experiencia VARCHAR(200),
    fkIdUsuario INT,
    FOREIGN KEY (fkIdUsuario) REFERENCES Usuarios(idUsuario)
);



-- Inserción de datos en la tabla Usuarios
INSERT INTO Usuarios (nombreUsuario, apellidoPaUsuario, apellidoMaUsuario, correoUsuario, passwordUsuario, tipoUsuario)
VALUES ('Juan', 'Pérez', 'Gómez', 'juan.perez@example.com', '123.Hola', 'D');
INSERT INTO Usuarios (nombreUsuario, apellidoPaUsuario, apellidoMaUsuario, correoUsuario, passwordUsuario, tipoUsuario)
VALUES ('María', 'González', 'López', 'maria.gonzalez@example.com', '123.Hola', 'A');
INSERT INTO Usuarios (nombreUsuario, apellidoPaUsuario, apellidoMaUsuario, correoUsuario, passwordUsuario, tipoUsuario)
VALUES ('Pedro', 'Rodríguez', 'Sánchez', 'pedro.rodriguez@example.com', '123.Hola', 'D');
INSERT INTO Usuarios (nombreUsuario, apellidoPaUsuario, apellidoMaUsuario, correoUsuario, passwordUsuario, tipoUsuario)
VALUES ('Laura', 'Sánchez', 'Hernández', 'laura.sanchez@example.com', '123.Hola', 'A');
INSERT INTO Usuarios (nombreUsuario, apellidoPaUsuario, apellidoMaUsuario, correoUsuario, passwordUsuario, tipoUsuario)
VALUES ('Ana', 'López', 'Pérez', 'ana.lopez@example.com', '123.Hola', 'D');

-- Inserción de datos en la tabla Publicaciones
INSERT INTO Publicaciones ( tituloPublicaciones, descripcionPublicaciones, linkPublicaciones, fkIdUsuario)
VALUES ( 'Introducción a la programación', 'Un libro introductorio sobre programación', 'https://ejemplo.com/intro-programacion', 1);
INSERT INTO Publicaciones ( tituloPublicaciones, descripcionPublicaciones, linkPublicaciones, fkIdUsuario)
VALUES ( 'Machine Learning aplicado a la medicina', 'Un estudio sobre el uso de técnicas de Machine Learning en el diagnóstico médico', 'https://ejemplo.com/ml-medicina', 4);
INSERT INTO Publicaciones ( tituloPublicaciones, descripcionPublicaciones, linkPublicaciones, fkIdUsuario)
VALUES ( 'Desarrollo de aplicaciones móviles', 'Un artículo sobre las mejores prácticas en el desarrollo de aplicaciones móviles', 'https://ejemplo.com/apps-moviles', 5);
INSERT INTO Publicaciones ( tituloPublicaciones, descripcionPublicaciones, linkPublicaciones, fkIdUsuario)
VALUES ( 'Seguridad en redes', 'Una guía sobre las medidas de seguridad en redes informáticas', 'https://ejemplo.com/seguridad-redes', 4);
INSERT INTO Publicaciones ( tituloPublicaciones, descripcionPublicaciones, linkPublicaciones, fkIdUsuario)
VALUES ( 'Inteligencia Artificial en el sector financiero', 'Un análisis sobre el impacto de la Inteligencia Artificial en las finanzas', 'https://ejemplo.com/ia-finanzas', 5);

-- Inserción de datos en la tabla Horarios
INSERT INTO Horarios ( horaInicio, horaFin, fkIdUsuario)
VALUES ('2023-01-01 09:00:00', '2023-01-01 12:00:00', 2);
INSERT INTO Horarios ( horaInicio, horaFin, fkIdUsuario)
VALUES ('2023-01-01 14:00:00', '2023-01-01 17:00:00', 4);
INSERT INTO Horarios ( horaInicio, horaFin, fkIdUsuario)
VALUES ('2023-01-01 10:00:00', '2023-01-01 13:00:00', 2);


-- Inserción de datos en la tabla TrayectoriaProfesional
INSERT INTO TrayectoriaProfesional ( tipoParticipacion, tituloParticipacion, Descripcion, fkIdUsuario)
VALUES ( 'Conferencista', 'Título de la conferencia', 'Descripción de la participación en la conferencia', 1);
INSERT INTO TrayectoriaProfesional ( tipoParticipacion, tituloParticipacion, Descripcion, fkIdUsuario)
VALUES ( 'Autor', 'Título del libro', 'Descripción de la participación como autor de un libro', 2);
INSERT INTO TrayectoriaProfesional ( tipoParticipacion, tituloParticipacion, Descripcion, fkIdUsuario)
VALUES ( 'Investigador', 'proyecto de investigación', 'Descripción de la participación como investigador en un proyecto', 3);

INSERT INTO Asesores ( esAsesor, asesorados, alumnosAsesorados, proyectosAsesorados, fkIdUsuario)
VALUES ( 1, 10, 'Juan Perez', 5, 1);

INSERT INTO Asesores ( esAsesor, asesorados, alumnosAsesorados, proyectosAsesorados, fkIdUsuario)
VALUES ( 0, 0, NULL, 0, 5);

INSERT INTO Asesores ( esAsesor, asesorados, alumnosAsesorados, proyectosAsesorados, fkIdUsuario)
VALUES ( 1, 5, 'Maria Rodriguez', 3, 2);

INSERT INTO Asesores ( esAsesor, asesorados, alumnosAsesorados, proyectosAsesorados, fkIdUsuario)
VALUES ( 1, 8, 'Pedro Gomez', 2, 3);

INSERT INTO Asesores ( esAsesor, asesorados, alumnosAsesorados, proyectosAsesorados, fkIdUsuario)
VALUES ( 1, 12, 'Laura Sanchez', 6, 1);

-- Inserción de datos en la tabla TemasInteres
INSERT INTO TemasInteres ( areaProfesional, experiencia, fkIdUsuario)
VALUES ( 'Inteligencia Artificial', 'Experiencia en IA y Machine Learning', 1);
INSERT INTO TemasInteres (areaProfesional, experiencia, fkIdUsuario)
VALUES ( 'Marketing Digital', 'Experiencia en estrategias de marketing en línea', 2);
INSERT INTO TemasInteres ( areaProfesional, experiencia, fkIdUsuario)
VALUES ( 'Neuropsicología', 'Experiencia en el estudio de los trastornos neuropsicológicos', 3);


SELECT * FROM Usuarios;
SELECT * FROM Publicaciones;
SELECT * FROM Asesores;
SELECT * FROM Horarios;
SELECT * FROM TrayectoriaProfesional;
SELECT * FROM TemasInteres;


DELETE FROM TemasInteres;
DELETE FROM Publicaciones
DELETE  from Docentes;
DELETE FROM Asesores
DELETE FROM TrayectoriaProfesional
DELETE FROM Horarios