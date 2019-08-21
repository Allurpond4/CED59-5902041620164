from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import InputRequired,Length,AnyOf

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissecret !'
class LoginForm(FlaskForm):
    username = StringField('username', validators = [InputRequired('A Username is required ! ')]), Length(min=5, max=10 , message='Must be 5')
    password = PasswordField('password', validators = [InputRequired('Passwordis required ! ')]), AnyOf(values=['password','secret'])

@app.route('/form',methods=['GET,POST'])
def form():
    form= LoginForm()
    if form.validate_on_submit():
        return '<h1>The Username is {}. The Password is {} .'.format(form.username.data,form.password.data)
    return render_template('form1.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
