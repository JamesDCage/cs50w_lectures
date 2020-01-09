from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return '<a href="/poem.html">Poem</a>'

@app.route("/<string:name>")
def any(name):
    return f"Hello {name.capitalize()}!"

@app.route("/poem.html")
def poem():
    return 'Standing on Mount Cheha<br><a href="/">back</a>'

@app.route("/variable.html")
def variable():
    linker = '''This is a variable.<br><a href="/">back</a>'''
    return render_template("variable.html", linker=linker)
