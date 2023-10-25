from flask_sqlalchemy import SQLAlchemy
import mysql.connector


db = SQLAlchemy()

class Alumno(db.Model):
    id_numero_cuenta = db.Column(db.Integer, primary_key=True)
    nombres_alumno = db.Column(db.String(20), nullable=False)
    apellido_paterno = db.Column(db.String(15), nullable=False)
    apellido_materno = db.Column(db.String(15), nullable=False)
    promedio = db.Column(db.Float, nullable=False)
    correo_electronico = db.Column(db.String(55), nullable=False)
    numero_telefono = db.Column(db.BigInteger, nullable=False)
    contraseña = db.Column(db.String(55), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    grupo = db.Column(db.SmallInteger, nullable=False)
    semestre = db.Column(db.SmallInteger, nullable=False)
    programa_educativo = db.Column(db.String(55), nullable=False)
    foto_perfil = db.Column(db.LargeBinary, nullable=False)
    puntuacion_psicologica = db.Column(db.SmallInteger, nullable=False)

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
