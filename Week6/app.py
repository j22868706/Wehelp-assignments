from flask import *

import mysql.connector

con=mysql.connector.connect(
  host="localhost",
  user="root",
  password="root1234",
  database="website"
)

app=Flask (__name__, static_folder = "static", static_url_path = "/")
app.secret_key = "MysecretkeyonlyIknow"
app.debug = True

@app.route('/', methods = ["GET"])
def index():
    return render_template('index.html')

@app.route('/signup', methods=["POST"])
def singup():
    signupName=request.form["signupName"]
    signupUsername=request.form["signupUsername"]
    signupPassword=request.form["signupPassword"]
    cursor=con.cursor()
    cursor.execute("SELECT * FROM member")
    memberData=cursor.fetchall()
    
    for signupRow in memberData:
        if signupRow[2] == signupUsername:
            return redirect('/error?message=That username is already taken.')

    cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)",
                   (signupName, signupUsername, signupPassword)) 
    con.commit()
    
    return redirect(url_for("index"))

@app.route('/signin', methods=["POST"])
def signin():
    signinUsername=request.form["signinUsername"]
    signinPassword=request.form["signinPassword"]
    cursor=con.cursor()
    cursor.execute("SELECT * FROM member")
    memberData=cursor.fetchall()
    for signinRow in memberData:
        if signinRow[2] == signinUsername and signinRow[3] == signinPassword:
            session["userName"]= signinRow[1]
            return redirect('/member') 
        
    return redirect('/error?message=Username or password is not correct')


@app.route('/member')
def memberPage():
    if "userName" in session:
        userName = session["userName"]    
        return render_template('successPage.html', userName=userName)
    else:
        return render_template('index.html')


@app.route('/error', methods = ["GET"])
def errorPage():
    message = request.args.get("message", 'An error occurred.') 
    return render_template('errorPage.html', message = message)

@app.route('/signout', methods=['GET'])
def signout():
    del session["userName"]  
    return redirect(url_for("index"))

@app.route('/home', methods=['GET'])
def home():
    return redirect(url_for("index"))


app.run(port=3000) 