create database DocentesDB
use DocentesDB

create table Docentes(
idDocente int not null primary key,
nombreDocente varchar(30) not null,
apellidoPaDocentes varchar(30),
apellidoMaDocentes varchar(30),
correoDocente varchar(30),
RFC varchar(13),
numeroTelDocente varchar(20),
domicilio varchar(50)
)
go

insert Docentes values(1,'Roberto', 'Gomez', 'Bolaños', 'borlaquetes@gmail.com', 'DGFE1495', '43951053354', 'si')

create table TemasDeInteres(
areaProfesional varchar(30) not null,
experiencia varchar(120)not null,
fkidDocente int  not null,
foreign key (fkidDocente) references Docentes(idDocente)
)
go

insert TemasDeInteres values( 'Ciencias', '3 anios', 1 )

create table TrayectoriaProfesional(
tipoTrayectoria varchar(30) not null,
tituloTrayectoria varchar(50) not null,
descripcion varchar(300) not null,
fkidDocente int  not null,
emisorCertificado binary not null,
fechaAcreditacion date not null,
foreign key (fkidDocente) references Docentes(idDocente)
)

insert TrayectoriaProfesional values('Doctorado', 'En drogas', 'doctorado en drogas',1, 1101110110,'10-12-2055')
go

create table Horario(
idHorario int not null primary key,
horaInicio date not null,
horaFin date not null,
fkidDocente int  not null,
foreign key (fkidDocente) references Docentes(idDocente)
)
go

insert Horario values(1, '10-12-2001', '10-12-2022',1)

create table Publicaciones(
idPublicaciones int not null,
tituloPublicaciones varchar(50),
descripcionPublicaciones varchar(300),
linkPublicaciones text,
fkidDocente int  not null,
foreign key (fkidDocente) references Docentes(idDocente)
)
go
insert Publicaciones values(1, 'la grande', 'es muy grande', 'www.lagrande.com',1)

create table Asesores(
idAsesores int not null,
esAsesor  bit not null,
asesorados int not null,
alumnosAsesorados varchar(50) not null,
proyectosAsesorados int not null,
fkidDocente int  not null,
foreign key (fkidDocente) references Docentes(idDocente)
)
go

insert Asesores values(1, 1, 0,0,0,1)

SELECT
    *
FROM  Asesores
    FOR JSON PATH, 
        INCLUDE_NULL_VALUES
GO
