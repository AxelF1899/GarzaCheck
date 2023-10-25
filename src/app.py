from flask import Flask, redirect, url_for, session, render_template, request
from flask_oauthlib.client import OAuth
from models import db, Alumno

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
    
    # Almacenamiento del token de acceso en la sesión
    session['google_token'] = (response['access_token'], '')
    #Verificación de la sesión
    if 'google_token' in session:
        access_token = session['google_token'][0]

        user_info_response = google.get('userinfo', token=(access_token, ''))

        if user_info_response.status == 200:
            user_data = user_info_response.data
            user_name = user_data.get('name', 'Nombre no disponible')
            user_email = user_data.get('email', 'Correo electrónico no disponible')
        else:
            print("No se pudo obtener la información del usuario")

        names = user_name.split()
        first_name = " ".join(names[:-2])
        father_lastname = names[-2]
        mother_lastname = names[-1]

        account_number = int(user_email[2:8])

        # Almacena los valores en la sesión para usarlos en otras rutas
        session['first_name'] = first_name
        session['father_lastname'] = father_lastname
        session['mother_lastname'] = mother_lastname
        session['account_number'] = account_number

    return redirect(url_for('home'))

@app.route('/home')
def home():
    numero_cuenta = session.get('account_number')
    existing_user = Alumno.query.filter_by(id_numero_cuenta=numero_cuenta).first()
    if existing_user:
        
        first_name = existing_user.nombres_alumno
        father_lastname = existing_user.apellido_paterno
        mother_lastname = existing_user.apellido_materno
        account_number = existing_user.id_numero_cuenta
        avg = existing_user.promedio
        

    else:
        
        first_name = 'Nombre no disponible'
        father_lastname = 'Apellido paterno no disponible'
        mother_lastname = 'Apellido materno no disponible'
        account_number = 'Número de cuenta no disponible'
        avg = 0.0
        

    return render_template('home.html', first_name=first_name, father_lastname=father_lastname, mother_lastname=mother_lastname, account_number=account_number, avg = avg)

@app.route('/informacion_personal')
def informacion_personal():

    numero_cuenta = session.get('account_number')
    existing_user = Alumno.query.filter_by(id_numero_cuenta=numero_cuenta).first()

    if existing_user:
        
        first_name = existing_user.nombres_alumno
        father_lastname = existing_user.apellido_paterno
        mother_lastname = existing_user.apellido_materno
        account_number = existing_user.id_numero_cuenta
        avg = existing_user.promedio
        

    else:
        
        first_name = 'Nombre no disponible'
        father_lastname = 'Apellido paterno no disponible'
        mother_lastname = 'Apellido materno no disponible'
        account_number = 'Número de cuenta no disponible'
        avg = 0.0

    return render_template('personal_info.html', first_name=first_name, father_lastname=father_lastname, mother_lastname=mother_lastname, account_number=account_number, semestre = 1, grupo =1)

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

if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/project5'
    db.init_app(app)  
    app.run(debug=True)
