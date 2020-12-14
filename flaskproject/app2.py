from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("one.html")
# render_template function automatically moves to templates folder
# html_file --> templates/html/one.html
# render_template("html/one.html")

@app.route("/home/<name>/")
def home(name):
    return render_template("one.html", naam = name.upper())

@app.route('/<name>/<int:maths>/<int:sci>/<int:eng>/')
def show(name, maths, sci, eng):
    data = {
        "Name" : name,
        "Maths" : maths,
        "Science" : sci,
        "English" : eng
    }
    return render_template("one.html", data1=data)  # data --> key, right data --> value
app.run(debug=True) 