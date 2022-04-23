from flask import Blueprint, render_template, request

bp = Blueprint("site", __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/editar-evento')
def editarEvento():
    return render_template('editarEvento.html')

@bp.route('/editar-prontuario')
def editarProntuario():
    return render_template('editarProntuario.html')

@bp.route('/editar-usuario')
def editarUsuario():
    return render_template('editarUsuario.html')

@bp.route('/evento')
def evento():
    return render_template('evento.html')

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/medico')
def medico():
    return render_template('medico.html')

@bp.route('/prontuario')
def prontuario():
    return render_template('prontuario.html')

@bp.route('/consulta-paciente')
def consultaPaciente():
    return render_template('telaConsultaPaciente.html')

@bp.route('/usuario')
def usuario():
    return render_template('usuario.html')