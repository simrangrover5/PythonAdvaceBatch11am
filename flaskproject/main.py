from flask import Flask, render_template, request, make_response, session, redirect, jsonify
import pymysql as sql
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from passlib.hash import pbkdf2_sha256 as sha
import requests
# from flask_oauth import OAuth
import requests_oauthlib as r_oauth 
from requests_oauthlib.compliance_fixes import facebook_compliance_fix 
import os

app = Flask(__name__)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
app.secret_key = "hijfpipjjpijeijijiohohiohgyyhfuifjij123445pjpijpij"
FB_APP_CLIENTID = "2448004112170013"
FB_APP_CLIENTKEY = "2ddcec1d98ee74c071eff506cab5aaed"

URL = "https://1957f899ce89.ngrok.io/"

FB_AUTHORIZATION_BASE_URL = "https://www.facebook.com/dialog/oauth"
FB_TOKEN_URL = "https://graph.facebook.com/oauth/access_token"

def connect():
    db = sql.connect(host="localhost", port=3306, user="root", password="", database="batch11am")
    cursor = db.cursor()
    return db, cursor

@app.route("/")
def index():
    if request.cookies.get("islogin"):
        return render_template("afterlogin.html")
    return render_template("nav.html")

@app.route("/login/")
def login():
    if request.cookies.get("islogin"):
        return render_template("afterlogin.html")
    else:
        return render_template("login.html")

@app.route("/afterlogin/", methods=['GET', 'POST'])
def afterlogin():
    if request.method == "POST":
        email = request.form.get("email")
        passwd = request.form.get("passwd")
        db, cursor = connect()
        cmd = f"select * from users where email='{email}'"
        cursor.execute(cmd)
        data = cursor.fetchone()
        if data:
            # resp = make_response(render_template("afterlogin.html"))
            # resp.set_cookie("email", email)
            # resp.set_cookie("islogin", "true")
            # return resp
            passwd2 = data[3]
            if sha.verify(passwd, passwd2):
                session['email'] = email
                session['islogin'] = "true"
                return render_template("afterlogin.html") 
            else:
                msg = "Invalid password"
                return render_template('login.html', msg=msg)
        else:
            msg = "Invalid email"
            return render_template('login.html', msg=msg)
    else:
        return render_template("login.html")

@app.route("/register/")
def register():
    return render_template("register.html")

@app.route("/aftersignup/", methods=['GET', 'POST'])
def aftersignup():
    if request.method == "GET":
        return render_template("register.html")
    else:
        db, cursor = connect()
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        passwd = request.form.get("passwd")
        email = request.form.get("email")
        gender = request.form.get("gender")
        cmd = f"select * from users where email='{email}'"
        cursor.execute(cmd)
        data = cursor.fetchone()
        print(data)
        if data: # data = ('simran', 'grover', 'simrangrover5@gmail.com', 'admin', 'female')
            msg = "User already exists....."
            return render_template("register.html", msg=msg)
        else: # data = None or ()
            if len(passwd) >= 8:
                upp = 0
                low = 0
                sp = 0
                num = 0
                for i in passwd:
                    if i.isupper():
                        upp += 1
                    elif i.islower():
                        low += 1
                    elif i in "#@%$&^!.*":
                        sp += 1
                    elif i in "1234567890":
                        num += 1
                if upp >= 1 and low>=1 and num>=1 and sp>=1:
                    message = MIMEMultipart()
                    message['To'] = email
                    message['From'] = "simrangrover5@gmail.com"
                    message['Subject'] = "MAIL FOR EMAIL VALIDATION"
                    msg = """
                            <h1>This is Mail from SIMRAN GROVER from Grras Solutions Pvt. Ltd.</h1>
                            <h2 style='color:red'>Hope you are doing well</h2>
                            <p style='font-style:italic;color:blue'>This is mail for email validation please click on the link below to validate your email</p>
                            <a href="localhost/afterlink/">CLICK ON THIS LINK</a>
                    """
                    html = MIMEText(msg, "html")
                    message.attach(html)
                    host = "smtp.gmail.com"
                    port = 465
                    from_email = "simrangrover5@gmail.com"
                    password = os.environ.get("EMAIL_HOST_PASSWORD")
                    try:
                        with smtplib.SMTP_SSL(host, port, context=ssl.create_default_context()) as server:
                            server.login(from_email, password)
                            server.sendmail(from_email, email, message.as_string())
                    except Exception as e:
                        return f"ERROR : {e} "
                    else:
                        msg = "MAIL SEND SUCCESSFULLY PLEASE CHECK YOUR MAIL TO VALIDATE"
                        session['fname'] = fname
                        session['lname'] = lname
                        session['email'] = email
                        session['password'] = passwd
                        session['gender'] = gender
                        return render_template("register.html", msg=msg)
                else:
                    msg = "Invalid Password"
                    return render_template("register.html", msg=msg)
            else:
                msg = "Password is not 8 characters long"
                return render_template("register.html", msg=msg)

@app.route("/logout/")
def logout():
    # resp = make_response(render_template("nav.html"))
    # resp.delete_cookie("email")
    # resp.delete_cookie("islogin")
    # return resp
    del session['email']
    del session['islogin']
    return render_template("nav.html") 

@app.route("/afterlink/") 
def get_email_validate():
    fname = session['fname']
    lname = session['lname']
    email = session['email']
    passwd = session['password']
    gender = session['gender']
    passwd = sha.hash(passwd)
    cmd = f"insert into users values('{fname}', '{lname}', '{email}', '{passwd}', '{gender}')"
    db, cursor = connect()
    cursor.execute(cmd)
    db.commit()
    del session['fname']
    del session['lname']
    del session['email']
    del session['password']
    del session['gender']
    msg = "Successfully Registered... Login to continue..."
    return render_template("login.html", msg=msg)
# password validation (uppercase, lowercase, sp, number, 8 or more char long)
# solve the error of duplicate of emails
# smtp

def get_place_id(place):
    """
        It takes place as an argument and search the place 
        It prints the results it finds for the particular place
    """
    parameters = {
                "key" : "AIzaSyB6AhDcEux73PWbJaa1t6Oo7jBVGLrudfw",
                "input" : place,
                "inputtype" : "textquery",
                "fields" : "business_status,formatted_address,geometry,name,permanently_closed,photos,place_id,opening_hours,price_level,rating,user_ratings_total" 
                }
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
    data = requests.get(url, params=parameters)
    if data.status_code == 200:
        data = data.json()
        place_id = data['candidates'][0]['place_id']
        return place_id
    else:
        msg =  "Invalid Details"
        return render_template("search.html", msg=msg)
    
def get_details_place(place):
    place_id = get_place_id(place)
    parameters = {
                "key" : "AIzaSyB6AhDcEux73PWbJaa1t6Oo7jBVGLrudfw",
                "place_id" : place_id,
                "inputtype" : "textquery",
                "fields" : "business_status,formatted_address,geometry,name,permanently_closed,photos,place_id,opening_hours,price_level,rating,user_ratings_total,reviews,formatted_phone_number,website"
                }
    url = "https://maps.googleapis.com/maps/api/place/details/json?"
    data = requests.get(url, params=parameters)
    if data.status_code == 200:
        data = data.json()
        all_data = {
            "Address" : data['result'].get('formatted_address'),
            "Phone Number" : data['result'].get('formatted_phone_number'),
            "Rating" : data['result'].get("rating"),
            "Website" : data['result'].get("website"),
        }
        opening_hours = data['result'].get("opening_hours")
        reviews = data['result'].get("reviews")
        photos = data['result'].get("photos")
        photo_ref = [i.get("photo_reference") for i in photos]
        return (all_data, opening_hours, reviews, photo_ref) 
    else:
        msg = "\n Invalid details"
        return render_template("search.html", msg=msg)

@app.route("/searchplace/", methods=['GET', 'POST'])
def search():
    if request.method == "GET":
        return render_template("search.html")
    else:
        place = request.form.get("place")
        all_data, open, reviews, photo_ref = get_details_place(place)
        key = "AIzaSyB6AhDcEux73PWbJaa1t6Oo7jBVGLrudfw"
        return render_template("showdata.html", data=all_data, open = open, reviews=reviews, key=key, photo_ref=photo_ref)

@app.route("/fblogin/")
def fb_login():
    facebook = r_oauth.OAuth2Session(
        FB_APP_CLIENTID, scope=['email'], redirect_uri=URL+"callback/"
    )
    authorize_url, _ = facebook.authorization_url(FB_AUTHORIZATION_BASE_URL)
    print(authorize_url, _)
    return redirect(authorize_url)

@app.route("/callback/")
def callback():
    facebook = r_oauth.OAuth2Session(
        FB_APP_CLIENTID, scope=['email'], redirect_uri=URL + "callback/"
    )
    facebook = facebook_compliance_fix(facebook)
    facebook.fetch_token(
        FB_TOKEN_URL,
        client_secret = FB_APP_CLIENTKEY,
        authorization_response= request.url 
    )
    data = facebook.get(
        "https://graph.facebook.com/v9.0/me?fields=email,name,id,likes"
    )
    data = data.json()
    #return f"{data}"
    return render_template("login.html", msg="Successfully Registered... Login to continue...")

@app.route("/data/api/")
def get_api():
    db, cursor = connect()
    cmd = "select fname,lname,email,gender from users"
    cursor.execute(cmd)
    data = cursor.fetchall()
    return jsonify(data)

app.run(host="localhost", port=80, debug=True)