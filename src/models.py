from flask_sqlalchemy import SQLAlchemy
import mysql.connector


db = SQLAlchemy()

class Alumno(db.Model):
    id_numero_cuenta = db.Column(db.Integer, primary_key=True)
    nombres_alumno = db.Column(db.String(20), nullable=True)
    apellido_paterno = db.Column(db.String(15), nullable=True)
    apellido_materno = db.Column(db.String(15), nullable=True)
    promedio = db.Column(db.Float, nullable=True)
    correo_electronico = db.Column(db.String(55), nullable=True)
    numero_telefono = db.Column(db.BigInteger, nullable=True)
    contraseña = db.Column(db.String(55), nullable=True, default="")
    fecha_nacimiento = db.Column(db.Date, nullable=True)
    grupo = db.Column(db.SmallInteger, nullable=True)
    semestre = db.Column(db.SmallInteger, nullable=True)
    programa_educativo = db.Column(db.String(55), nullable=True)
    foto_perfil = db.Column(db.LargeBinary, nullable=True)
    puntuacion_psicologica = db.Column(db.SmallInteger, nullable=True, default=0)
    fecha_ultima_encuesta = db.Column(db.DateTime, nullable=True)

class Curso(db.Model):
    id_curso = db.Column(db.Integer, primary_key=True)
    nombre_curso = db.Column(db.String(55), nullable=False)
    semestre_curso = db.Column(db.SmallInteger, nullable=False)
    calificacion_curso = db.Column(db.Float, nullable=False)
    promedio_calificaciones = db.Column(db.Float, nullable=False)
    catedratico = db.Column(db.Integer, db.ForeignKey('maestro.id_maestro'), nullable=False)

class Inscripcion(db.Model):
    id_inscripcion = db.Column(db.Integer, primary_key=True)
    id_alumno = db.Column(db.Integer, db.ForeignKey('alumno.id_numero_cuenta'), nullable=False)
    id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=False)
    
class Maestro(db.Model):
    id_maestro = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(55), nullable=False)
    apellido_paterno = db.Column(db.String(55), nullable=False)
    apellido_materno = db.Column(db.String(55), nullable=False)
    titulo_academico = db.Column(db.String(55), nullable=False)
    calificacion = db.Column(db.Float, nullable=False)
    etiquetas = db.Column(db.String(255))  # Almacena las etiquetas separadas por comas
    votos_etiquetas = db.Column(db.Integer, default=0)