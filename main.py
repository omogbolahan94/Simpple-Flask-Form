from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[InputRequired(), Email(check_deliverability=True)])
    password = PasswordField(label='Password', validators=[InputRequired()])
    submit = SubmitField('Log In')


app = Flask(__name__)

Bootstrap(app)

app.secret_key = "123abc()"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'ola@gmail.com' and login_form.password.data == '1234':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


@app.route("/bts-flask-form")
def bts_form():
    return render_template('bts_flask_form.html', form=LoginForm())


if __name__ == '__main__':
    app.run(debug=True)