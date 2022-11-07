from flask import render_template, flash, redirect, url_for
from . import app
from .forms import LoginForm, RegistrationForm
from .models import Post, User


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route("/")
@app.route("/home")
def home():
    postAll = Post.query.all()
    print(postAll)
    user = User.query.get_or_404(1)
    print(user)
    return render_template('index.html', posts=postAll)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
