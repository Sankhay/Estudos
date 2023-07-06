from flask import Flask, render_template, redirect, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_url_path='/static')

app = Flask(__name__, static_url_path='/static')

# Set the MySQL connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:4093@127.0.0.1/velha'

db = SQLAlchemy(app)

class Jogadores(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    vitorias = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Name %r>' % self.name
    


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    with app.app_context():
        jogador = Jogadores(nome=nome, vitorias=0)
        db.session.add(jogador)
        db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

