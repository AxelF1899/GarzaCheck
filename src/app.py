from flask import Flask, redirect, url_for, session, render_template, request, jsonify,flash
from flask_oauthlib.client import OAuth
from models import db, Alumno, Maestro
from datetime import datetime, timedelta
import time
from big_functions.strategy import determinar_estrategia



app = Flask(__name__)
app.secret_key = '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' #Guardar y borrar por ahora

scopes = ['https://www.google.com/auth/userinfo.profile', 'https://www.google.com/auth/userinfo.email']

oauth = OAuth(app)

google = oauth.remote_app(
    'google',
    consumer_key='875442195195-g3rje2pdqa7iuk0our7h8dfdgcu9qndo.apps.googleusercontent.com',
    consumer_secret='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',
    request_token_params={
        'scope': 'email profile',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

@app.route('/')
def landing_page():
    current_year = 2023
    return render_template('landing.html', current_year=current_year)

@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))

@app.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect(url_for('landing_page'))


@app.route('/login/authorized')
def authorized():
    response = google.authorized_response()
    
    if response is None or response.get('access_token') is None:
        return 'Acceso denegado: Razón={} error={}'.format(
            request.args['error_reason'],
            request.args['error_description']
        )
    
    
    session['google_token'] = (response['access_token'], '')
    
    if 'google_token' in session:
        access_token = session['google_token'][0]

        user_info_response = google.get('userinfo', token=(access_token, ''))

        if user_info_response.status == 200:
            user_data = user_info_response.data
            user_name = user_data.get('name', 'Nombre no disponible')
            user_email = user_data.get('email', 'Correo electrónico no disponible')
        else:
            print("No se pudo obtener la información del usuario")

        #####################esto ase la verificación de correo en la base de datos ###############################
        existing_user = Alumno.query.filter_by(correo_electronico=user_email).first()
        if not existing_user:
            
            return redirect(url_for('sign_up'))

        
        names = user_data.get('name', 'Nombre no disponible').split()
        first_name = " ".join(names[:-2])
        father_lastname = names[-2]
        mother_lastname = names[-1]

        account_number = int(user_email[2:8])

        # información en la sesión
        session['first_name'] = first_name
        session['father_lastname'] = father_lastname
        session['mother_lastname'] = mother_lastname
        session['account_number'] = account_number

        
        return redirect(url_for('home'))

    return redirect(url_for('landing_page'))


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        account_number = request.form.get('account_number')
        correo = request.form.get('correo')

        existing_user = Alumno.query.filter_by(id_numero_cuenta=account_number).first()
        if existing_user:
            return "El número de cuenta ya está registrado"

        existing_user = Alumno.query.filter_by(correo_electronico=correo).first()
        if existing_user:
            return "El correo ya está registrado"
        
        nombre = request.form.get('nombre')
        apellido_paterno = request.form.get('apellido_paterno')
        apellido_materno = request.form.get('apellido_materno')
        telefono = request.form.get('telefono')
        carrera = request.form.get('carrera')
        grupo = request.form.get('grupo')
        semestre = request.form.get('semestre')
        promedio = request.form.get('promedio')
        get_fecha_nacimiento = request.form.get('fecha_nacimiento')
        fecha_ultima_encuesta = '2000-01-01 22:10:09'

        fecha_nacimiento = get_fecha_nacimiento
        new_user = Alumno(
            id_numero_cuenta=account_number,
            nombres_alumno=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            correo_electronico=correo,
            numero_telefono=telefono,
            promedio=promedio,
            programa_educativo = carrera,
            grupo = grupo,
            semestre = semestre,
            fecha_nacimiento = fecha_nacimiento,
            fecha_ultima_encuesta = fecha_ultima_encuesta
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('landing_page'))

    return render_template('sign_up.html')



@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        numero_cuenta = session.get('account_number')
        existing_user = Alumno.query.filter_by(id_numero_cuenta=numero_cuenta).first()

        flash('Puntuación guardada en la base de datos.', 'success')
        if existing_user:
            existing_user.fecha_ultima_encuesta = datetime.now()
            db.session.commit()

        last_survey_date = existing_user.fecha_ultima_encuesta.strftime("%Y-%m-%dT%H:%M:%S")
    else:
        numero_cuenta = session.get('account_number')
        existing_user = Alumno.query.filter_by(id_numero_cuenta=numero_cuenta).first()

        if existing_user:
            first_name = existing_user.nombres_alumno
            father_lastname = existing_user.apellido_paterno
            mother_lastname = existing_user.apellido_materno
            account_number = existing_user.id_numero_cuenta
            avg = existing_user.promedio

            # Determinar la puntuación emocional y la estrategia correspondiente
            puntuacion_emocional = existing_user.puntuacion_psicologica
            estrategia = determinar_estrategia(puntuacion_emocional)
        else:
            first_name = 'Nombre no disponible'
            father_lastname = 'Apellido paterno no disponible'
            mother_lastname = 'Apellido materno no disponible'
            account_number = 'Número de cuenta no disponible'
            avg = 0.0
            estrategia = 'No se ha encontrado información de puntuación emocional para este estudiante'

        last_survey_date = existing_user.fecha_ultima_encuesta.strftime("%Y-%m-%dT%H:%M:%S")

    return render_template('home.html', first_name=first_name, father_lastname=father_lastname, mother_lastname=mother_lastname, account_number=account_number, avg=avg, last_survey_date=last_survey_date, estrategia=estrategia)



@app.route('/procesar_encuesta', methods=['POST'])
def procesar_encuesta():
    if 'account_number' in session:
        respuestas = request.form
        puntuacion = 0

        for pregunta, respuesta in respuestas.items():
            if respuesta:
                puntuacion += int(respuesta)
            else:
                flash('Por favor, complete todas las preguntas antes de enviar la encuesta.', 'error')
                time.sleep(2)
                return redirect(url_for('home'))

        numero_cuenta = session['account_number']

        alumno = Alumno.query.filter_by(id_numero_cuenta=numero_cuenta).first()
        if alumno:
            alumno.fecha_ultima_encuesta = datetime.now()
            alumno.puntuacion_psicologica = puntuacion
            db.session.commit()
            flash('Puntuación guardada en la base de datos.', 'success')
            time.sleep(2)
            return redirect(url_for('home'))
        time.sleep(2)
        return redirect(url_for('home'))
    else:
        time.sleep(2)
        return redirect(url_for('home'))


@app.route('/informacion_personal')
def informacion_personal():

    numero_cuenta = session.get('account_number')
    existing_user = Alumno.query.filter_by(id_numero_cuenta=numero_cuenta).first()

    if existing_user:
        
        first_name = existing_user.nombres_alumno
        father_lastname = existing_user.apellido_paterno
        mother_lastname = existing_user.apellido_materno
        account_number = existing_user.id_numero_cuenta
        semester = existing_user.semestre
        group = existing_user.grupo
        avg = existing_user.promedio
        phone = existing_user.numero_telefono
        educational_program = existing_user.programa_educativo
        

    else:
        
        first_name = 'Nombre no disponible'
        father_lastname = 'Apellido paterno no disponible'
        mother_lastname = 'Apellido materno no disponible'
        account_number = 'Número de cuenta no disponible'
        avg = 0.0

    return render_template('personal_info.html', first_name=first_name, father_lastname=father_lastname, mother_lastname=mother_lastname, account_number=account_number, semestre = semester, grupo =group, average = avg, phone =phone, educational_program = educational_program)

@app.route('/editar_informacion_personal', methods=['POST'])
def editar_informacion_personal():
    if request.method == 'POST':
        
        nombre = request.form['nombre']
        apellido_paterno = request.form['apellido_paterno']
        apellido_materno = request.form['apellido_materno']
        carrera = request.form['carrera']
        grupo = request.form['grupo']
        semestre = request.form['semestre']
        numero_cuenta = session.get('account_number')  
        promedio = request.form['promedio']

        
        existing_user = Alumno.query.filter_by(id_numero_cuenta=numero_cuenta).first()

        if existing_user:
            
            existing_user.nombres_alumno = nombre
            existing_user.apellido_paterno = apellido_paterno
            existing_user.apellido_materno = apellido_materno
            existing_user.programa_educativo = carrera
            existing_user.grupo = grupo
            existing_user.semestre = semestre
            existing_user.promedio = promedio

            
            db.session.commit()

            return redirect(url_for('home'))

        else:
            
            alumno = Alumno(
                id_numero_cuenta=numero_cuenta,
                nombres_alumno=nombre,
                apellido_paterno=apellido_paterno,
                apellido_materno=apellido_materno,
                programa_educativo=carrera,
                grupo=grupo,
                semestre=semestre
            )

           
            db.session.add(alumno)
            db.session.commit()

        return redirect(url_for('home'))

@app.route('/horarios')
def horarios():
    return render_template('schedules.html')

@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    if request.method == 'POST':
        try:
            semester_values = []
            
            for i in range(1, 10):
                value = request.form.get(f'semester{i}', '')
                if value:
                    semester_values.append(float(value))

            nuevos_promedios = [9.14, 9.34, 9.23, 9.42, 9.17, 9.31, 9.01, 9.77, 10.0]

            current_average = sum(semester_values) / len(semester_values)
            semesters_remaining = 9 - len(semester_values)
            prediction_results = []
            for i in range(1, semesters_remaining + 1):
                current_average = ((current_average + nuevos_promedios[i - 1]) / 2.0)+0.27
                prediction_results.append({
                    'semester': len(semester_values) + i,
                    'prediction': round(current_average, 2),
                })

            return jsonify(prediction_results)
        except Exception as e:
            return f"Error: {str(e)}", 500

    return render_template('prediction.html')

@app.route('/top_docentes')
def top_docentes():
    
    profesores = Maestro.query.all()

    return render_template('top_doc.html', profesores=profesores)


if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/project5'
    db.init_app(app)  
    app.run(debug=True)
