from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Examen con Puerto 5800'

if __name__ == '__main__':
    app.run(port=5800)
