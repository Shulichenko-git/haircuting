from flask import render_template, flash, redirect, url_for
from f_app import app
from f_app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Artem"}
    posts = [
        {
            'author': {'username': "Oksana"},
            'body': "I selected Canada!"
        },
        {
            'author': {'username': "Elena"},
            'body': "I selected Germany!"
        },
        {
            'author': {'username': "Alexandra"},
            'body': "I selected Germany too!"
        },
        {
            'author': {'username': "Vanya"},
            'body': "I selected Ukraine!"
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me{}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)