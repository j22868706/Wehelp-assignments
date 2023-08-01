from flask import (
    Flask, 
    render_template, 
    request,
    session,
    url_for,
    redirect,
    g
) 

class User:
    def __init__(self, id, username, password):
        self.id= id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username = 'test', password='test'))


app=Flask (__name__, static_folder = "static", static_url_path = "/")
app.secret_key = "MysecretkeyonlyIknow"
app.debug = True

@app.before_request
def before_request():
    g.user =  None
    if "user_id" in session:
        user = [ x for x in users if x.id == session["user_id"]][0]
        g.user = user

    
@app.route('/', methods = ["GET"])
def index():
    return render_template('index.html')

@app.route('/signin', methods=["POST"])
def signin():
    if request.method == "POST":
        session.pop("user_id", None)
        username = request.form["username"]
        password = request.form["password"]

        if not username or not password:
            return redirect('/error?message=Please enter username and password')

        user = next((x for x in users if x.username == username), None)
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for("memberPage"))

        return redirect('/error?message=Username or password is not correct')

    return render_template("index.html")

@app.route('/member')
def memberPage():
    if not g.user:
        return redirect(url_for("index"))
    
    return render_template('successPage.html')


@app.route('/error', methods = ["GET"])
def errorPage():
    message = request.args.get("message", 'An error occurred.') 
    return render_template('errorPage.html', message = message)

@app.route('/signout', methods=['GET'])
def signout():
    session.pop('user_id', None)  
    return redirect(url_for("index"))

app.run(port=3000) 