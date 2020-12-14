from flask import Flask

app = Flask(__name__) # Flask --> class --> object --> app
# __name__ ??
# make object of PWD so that later it will read everything from current working directory

@app.route("/")  # route --> decorator --> takes path as an argument 
# / --> domain , / --> localhost(127.0.0.1)
def index():
    return "WELCOME TO MY FLASK PROJECT"

@app.route("/home/") # localhost/home/
def home():
    return "<h1 style='color:red'>This is my first flask project welcome to my home</h1>"

@app.route("/home/<name>")
def home_name(name):
    return f"<h1 style='color:red'>This is my first flask project welcome to my home <i>{name.upper()}</i></h1>"

@app.route("/home/<name>/<int:age>/")
def check_vote(name, age):
    if age>=18:
        return f"<h1 style='color:blue'>{name.upper()} can vote"
    else:
        return f"<h1 style='color:blue'>{name.upper()} cannot vote"
        

# task

# localhost/simran/80/90/100
# return string simran got 80+90+100/3 and got so and so grade
app.run(host="localhost", port=80, debug=True)
# debug --> Show the errors on browser