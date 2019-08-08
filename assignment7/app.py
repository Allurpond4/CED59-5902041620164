from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtfforms.validators import DataRequired

app = Flask(__name__)


@app.route('/', method=['POST'])
def index():
    return render_template('form1.html')


def register():
    return 'Welcome to my world'


if __name__ == '__main__':
    app.run()
