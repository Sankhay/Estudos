from jogoteca import app


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    if usuario:
        if form.senha.data == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            print(proxima_pagina)
            if proxima_pagina != 'None':
                print('oi')
                proxima_pagina = '/' + proxima_pagina
                return redirect(proxima_pagina)
            else:
                print('ola')
                return redirect('/')
    else:
        print('hello world')
        return redirect('/')

    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')


from flask import request, redirect, flash, session, render_template
from models import Usuarios
from helpers import FormularioUsuario