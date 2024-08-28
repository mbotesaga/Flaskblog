from flask import Flask, render_template, url_for

app = Flask(__name__)

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
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)