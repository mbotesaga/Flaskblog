from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dff110a589f30f002f8bf7a72cd4254f'

posts= [
    {
        'author': 'Cleg Peter Ovil',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'Aug-27-2024'
    },
    {
        'author': 'Guively Noel',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'Aug-28-2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)