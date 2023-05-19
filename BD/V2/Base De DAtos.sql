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



-- Inserci�n de datos en la tabla Usuarios
INSERT INTO Usuarios (nombreUsuario, apellidoPaUsuario, apellidoMaUsuario, correoUsuario, passwordUsuario, tipoUsuario)
VALUES ('Juan', 'P�rez', 'G�mez', 'juan.perez@example.com', '123.Hola', 'D');
INSERT INTO Usuarios (nombreUsuario, apellidoPaUsuario, apellidoMaUsuario, correoUsuario, passwordUsuario, tipoUsuario)
VALUES ('Mar�a', 'Gonz�lez', 'L�pez', 'maria.gonzalez@example.com', '123.Hola', 'A');
INSERT INTO Usuarios (nombreUsuario, apellidoPaUsuario, apellidoMaUsuario, correoUsuario, passwordUsuario, tipoUsuario)
VALUES ('Pedro', 'Rodr�guez', 'S�nchez', 'pedro.rodriguez@example.com', '123.Hola', 'D');
INSERT INTO Usuarios (nombreUsuario, apellidoPaUsuario, apellidoMaUsuario, correoUsuario, passwordUsuario, tipoUsuario)
VALUES ('Laura', 'S�nchez', 'Hern�ndez', 'laura.sanchez@example.com', '123.Hola', 'A');
INSERT INTO Usuarios (nombreUsuario, apellidoPaUsuario, apellidoMaUsuario, correoUsuario, passwordUsuario, tipoUsuario)
VALUES ('Ana', 'L�pez', 'P�rez', 'ana.lopez@example.com', '123.Hola', 'D');

-- Inserci�n de datos en la tabla Publicaciones
INSERT INTO Publicaciones ( tituloPublicaciones, descripcionPublicaciones, linkPublicaciones, fkIdUsuario)
VALUES ( 'Introducci�n a la programaci�n', 'Un libro introductorio sobre programaci�n', 'https://ejemplo.com/intro-programacion', 1);
INSERT INTO Publicaciones ( tituloPublicaciones, descripcionPublicaciones, linkPublicaciones, fkIdUsuario)
VALUES ( 'Machine Learning aplicado a la medicina', 'Un estudio sobre el uso de t�cnicas de Machine Learning en el diagn�stico m�dico', 'https://ejemplo.com/ml-medicina', 4);
INSERT INTO Publicaciones ( tituloPublicaciones, descripcionPublicaciones, linkPublicaciones, fkIdUsuario)
VALUES ( 'Desarrollo de aplicaciones m�viles', 'Un art�culo sobre las mejores pr�cticas en el desarrollo de aplicaciones m�viles', 'https://ejemplo.com/apps-moviles', 5);
INSERT INTO Publicaciones ( tituloPublicaciones, descripcionPublicaciones, linkPublicaciones, fkIdUsuario)
VALUES ( 'Seguridad en redes', 'Una gu�a sobre las medidas de seguridad en redes inform�ticas', 'https://ejemplo.com/seguridad-redes', 4);
INSERT INTO Publicaciones ( tituloPublicaciones, descripcionPublicaciones, linkPublicaciones, fkIdUsuario)
VALUES ( 'Inteligencia Artificial en el sector financiero', 'Un an�lisis sobre el impacto de la Inteligencia Artificial en las finanzas', 'https://ejemplo.com/ia-finanzas', 5);

-- Inserci�n de datos en la tabla Horarios
INSERT INTO Horarios ( horaInicio, horaFin, fkIdUsuario)
VALUES ('2023-01-01 09:00:00', '2023-01-01 12:00:00', 2);
INSERT INTO Horarios ( horaInicio, horaFin, fkIdUsuario)
VALUES ('2023-01-01 14:00:00', '2023-01-01 17:00:00', 4);
INSERT INTO Horarios ( horaInicio, horaFin, fkIdUsuario)
VALUES ('2023-01-01 10:00:00', '2023-01-01 13:00:00', 2);


-- Inserci�n de datos en la tabla TrayectoriaProfesional
INSERT INTO TrayectoriaProfesional ( tipoParticipacion, tituloParticipacion, Descripcion, fkIdUsuario)
VALUES ( 'Conferencista', 'T�tulo de la conferencia', 'Descripci�n de la participaci�n en la conferencia', 1);
INSERT INTO TrayectoriaProfesional ( tipoParticipacion, tituloParticipacion, Descripcion, fkIdUsuario)
VALUES ( 'Autor', 'T�tulo del libro', 'Descripci�n de la participaci�n como autor de un libro', 2);
INSERT INTO TrayectoriaProfesional ( tipoParticipacion, tituloParticipacion, Descripcion, fkIdUsuario)
VALUES ( 'Investigador', 'proyecto de investigaci�n', 'Descripci�n de la participaci�n como investigador en un proyecto', 3);

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

-- Inserci�n de datos en la tabla TemasInteres
INSERT INTO TemasInteres ( areaProfesional, experiencia, fkIdUsuario)
VALUES ( 'Inteligencia Artificial', 'Experiencia en IA y Machine Learning', 1);
INSERT INTO TemasInteres (areaProfesional, experiencia, fkIdUsuario)
VALUES ( 'Marketing Digital', 'Experiencia en estrategias de marketing en l�nea', 2);
INSERT INTO TemasInteres ( areaProfesional, experiencia, fkIdUsuario)
VALUES ( 'Neuropsicolog�a', 'Experiencia en el estudio de los trastornos neuropsicol�gicos', 3);


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