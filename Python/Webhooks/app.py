from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        data = request.json
        print(data['name'])
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run(port=4999)