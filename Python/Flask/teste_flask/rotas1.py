from flask import Blueprint

rotas1_bp = Blueprint('1', __name__)

@rotas1_bp.route('/oi')
def rota1():
    return 'Esta é a rota 1'

@rotas1_bp.route('/outra_rota')
def rota2():
    return 'Esta é a outra rota'
