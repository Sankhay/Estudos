from flask import Blueprint

rotas2_bp = Blueprint('2', __name__)

@rotas2_bp.route('/rota3')
def rota3():
    return 'Esta é a rota 3'

@rotas2_bp.route('/rota4')
def rota4():
    return 'Esta é a rota 4'
