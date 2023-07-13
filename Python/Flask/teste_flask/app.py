from flask import Flask, render_template, jsonify
from rotas1 import rotas1_bp
from rotas2 import rotas2_bp

app = Flask(__name__)

app.register_blueprint(rotas1_bp)
app.register_blueprint(rotas2_bp)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get_number", methods=["GET"])
def get_number():
    return jsonify(5)

if __name__ == "__main__":
    app.run()
