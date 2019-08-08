from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')

def index():
    return render_template('form1.html')

def register():
    return 'Welcome to my world'


if __name__ == '__main__':

  app.run()