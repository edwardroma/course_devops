#11
from flask import Flask
app = Flask(__name__)

@app.route('/content')
def read():
    return open("words.txt").read(), 200

@app.route('/register')
def register():
    open("words.txt", 'w').write("hello")
    return "success", 201

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=30000)
