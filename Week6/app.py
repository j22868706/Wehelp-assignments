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
    cursor.execute("SELECT * FROM member Where username = %s", (signupUsername,))
    signupMemberData=cursor.fetchall()
    
    for signupRow in signupMemberData:
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
    cursor.execute("SELECT * FROM member WHERE username = %s AND password = %s", (signinUsername, signinPassword,))
    singinMemberData=cursor.fetchall()
    for signinRow in singinMemberData:
        if signinRow[2] == signinUsername and signinRow[3] == signinPassword:
            session["userName"]= signinRow[1]
            session["userId"] = signinRow[0]
            return redirect('/member') 
        
    return redirect('/error?message=Username or password is not correct')


@app.route('/member')
def memberPage():
    if "userName" in session:
        userName = session["userName"]
        query = 'SELECT member.name, message.content FROM message JOIN member ON message.member_id = member.id ORDER BY message.time DESC;'
        cursor = con.cursor()
        cursor.execute(query)
        messages = cursor.fetchall()
        return render_template('successPage.html', userName=userName, messages=messages)
    else:
        return render_template('index.html')


@app.route('/createMessage', methods=['POST'])
def createMessage():
    content = request.form.get('Messagecontent')
    userId = session["userId"]

    cursor=con.cursor()
    cursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)", (userId, content))
    con.commit()
    cursor.close()
    return redirect('/member')

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