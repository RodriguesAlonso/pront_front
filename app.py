from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello Medium"

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/editar-evento')
def editarEvento():
        return render_template('editarEvento.html')

@app.route('/editar-prontuario')
def editarProntuario():
        return render_template('editarProntuario.html')

@app.route('/editar-usuario')
def editarUsuario():
        return render_template('editarUsuario.html')

@app.route('/evento')
def evento():
        return render_template('evento.html')

@app.route('/login')
def login():
        return render_template('login.html')

@app.route('/medico')
def medico():
        return render_template('medico.html')

@app.route('/prontuario')
def prontuario():
        return render_template('prontuario.html')
    
@app.route('/consulta-paciente')
def consultaPaciente():
        return render_template('telaConsultaPaciente.html')

@app.route('/usuario')
def usuario():
        return render_template('usuario.html')

if __name__ == '__main__':
    app.run(port=5000)