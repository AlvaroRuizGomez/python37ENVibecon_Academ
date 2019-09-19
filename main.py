from flask import Flask, request, make_response, request, redirect,render_template
app = Flask(__name__)


@app.route('/')
def home():
    ip = request.remote_addr
    respuesta = make_response(redirect('/info'))
    respuesta.set_cookie('user_ip', ip)
    return respuesta
    

@app.route('/info')
def info():
    usuario_ip = request.cookies.get('user_ip')
    
    variables = {
        'ip' : usuario_ip,
        'cosa': 'cosa',
    }
# **Nombre del diccionario abre el diccionario entero
    return render_template('info.html', **variables)

@app.route('/contactar')
def contactar():
    return render_template('contactar.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

@app.errorhandler(404)
def error404(error):
    return '<h1>Pagina no encontrada... </h1>'

if  __name__== "__main__":
    app.run('0.0.0.0', 5000, debug=True)