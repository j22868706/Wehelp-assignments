from flask import *
import mysql.connector
import json

app=Flask (__name__, static_folder = "static", static_url_path = "/")
app.secret_key = "MysecretkeyonlyIknow"
app.debug = True

@app.route('/', methods = ["GET"])
def index():
    return render_template('index.html')

@app.route('/signup', methods=["POST"])
def singup():
    con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="website"
    )
    signupName=request.form["signupName"]
    signupUsername=request.form["signupUsername"]
    signupPassword=request.form["signupPassword"]
    cursor=con.cursor()
    cursor.execute("SELECT * FROM member Where username = %s", (signupUsername,))
    signupMemberData=cursor.fetchall()
    
    for signupRow in signupMemberData:
        if signupRow[2] == signupUsername:
            return redirect('/error?message=This username is already taken !')

    cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)",
                   (signupName, signupUsername, signupPassword)) 
    con.commit()
    
    return redirect(url_for("index"))

@app.route('/signin', methods=["POST"])
def signin():
    con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="website"
    )
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
    con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="website"
    )
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
    con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="website"
    )
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

@app.route('/api/member', methods=['GET'])
def apiMember():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root1234",
        database="website"
    )
    usernameSearch = request.args.get("username")
    cursor = con.cursor(dictionary=True)

    userSearchQuery = "SELECT * FROM member WHERE username = %s"
    cursor.execute(userSearchQuery, (usernameSearch,))
    userSearchMember = cursor.fetchone()

    cursor.close()
    con.close()

    if userSearchMember:
        response = {
            "data": {
                "id": userSearchMember["id"],
                "name": userSearchMember["name"],
                "username": userSearchMember["username"]
            }
        }
    else:
        response = {
            "data": None
        }
    jsonResponse=json.dumps(response)
    print(jsonResponse)
    return jsonify(response)

@app.route('/api/member', methods=['PATCH'])
def updateMemberUsername():
    usernameUpdateResponse = {"error": True}

    newName = request.json.get("name")
    userId = session["userId"]

    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root1234",
        database="website"
    )

    if newName:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM member WHERE name = %s", (newName,))
        usernameUpdateMemberData = cursor.fetchall()

        if len(usernameUpdateMemberData) > 0 and usernameUpdateMemberData[0][1] == newName:
            con.rollback()
            usernameUpdateResponse = {"error": True}
            print(usernameUpdateResponse)

        else:
            query = "UPDATE member SET name = %s WHERE id = %s"
            cursor.execute(query, (newName, userId))  
            con.commit()
            cursor.close()
            usernameUpdateResponse = {"ok": True}
            print(usernameUpdateResponse)

    return jsonify(usernameUpdateResponse)



app.run(port=3000) 