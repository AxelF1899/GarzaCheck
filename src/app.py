from flask import Flask, redirect, url_for, session, render_template, request
from flask_oauthlib.client import OAuth

app = Flask(__name__)

app.secret_key = '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'
oauth = OAuth(app)

google = oauth.remote_app(
    'google',
    consumer_key='875442195195-g3rje2pdqa7iuk0our7h8dfdgcu9qndo.apps.googleusercontent.com',
    consumer_secret='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',
    request_token_params={
        'scope': 'email profile',  # Puedes personalizar los alcances necesarios
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)


'''
'''
# Función tokengetter

@app.route('/')
def landing_page():
    # Tu contenido de landing page aquí
    current_year = 2023  # Puedes obtener el año actual de manera dinámica si lo deseas

    return render_template('landing.html', current_year=current_year, user_name='Axel')

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
    
    # Almacena el token de acceso en la sesión
    session['google_token'] = (response['access_token'], '')

    # Redirige al usuario a la página de inicio (home)
    return redirect(url_for('home'))


@app.route('/home')
def home():
    # Esta es la nueva interfaz después de iniciar sesión
    return render_template('home.html')

@app.route('/informacion_personal')
def informacion_personal():
    # Obtén los datos del usuario, como el grupo, número de cuenta, semestre y carrera, desde donde los almacenes
    # Puedes guardar estos datos en variables o recuperarlos de una base de datos, según cómo estén almacenados en tu aplicación
    
    # Luego, pasa estos datos a tu plantilla HTML
    return render_template('personal_info.html', grupo=1, numero_cuenta=385309, semestre=5, carrera='Ingeniería en software')


@app.route('/editar_informacion_personal', methods=['POST'])
def editar_informacion_personal():
    if request.method == 'POST':
        # Obtén los datos enviados por el formulario
        grupo = request.form['grupo']
        numero_cuenta = request.form['numero_cuenta']
        semestre = request.form['semestre']
        carrera = request.form['carrera']
        
        # Actualiza los datos del usuario con los nuevos valores (esto puede variar según cómo almacenes los datos)
        # Puedes guardar estos datos en una base de datos, en una variable de sesión, etc.
        
        # Después de actualizar los datos, redirige al usuario a la página de información personal
        return redirect(url_for('informacion_personal'))

@app.route('/horarios')
def horarios():
    # Obtén los datos del usuario, como el grupo, número de cuenta, semestre y carrera, desde donde los almacenes
    # Puedes guardar estos datos en variables o recuperarlos de una base de datos, según cómo estén almacenados en tu aplicación
    
    # Luego, pasa estos datos a tu plantilla HTML
    return render_template('schedules.html')


if __name__ == '__main__':
    app.run(debug=True)
