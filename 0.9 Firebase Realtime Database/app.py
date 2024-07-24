from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

firebaseConfig = {
    "apiKey": "AIzaSyB8fyRQ82lW5MIxyEQG1Cuwc78xcjR_2Sg",
    "authDomain": "first-lap-in-the-second-week.firebaseapp.com",
    "projectId": "first-lap-in-the-second-week",
    "storageBucket": "first-lap-in-the-second-week.appspot.com",
    "messagingSenderId": "243459541669",
    "appId": "1:243459541669:web:0b1c9a1b8fc6fbb8c15b4c",
    "measurementId":"G-K1R0365HDY",
    "databaseURL": "https://first-lap-in-the-second-week.firebaseio.com"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        quote_text = request.form["quote"]
        said_by = request.form["said_by"]
        quote = {
            "text": quote_text,
            "said_by": said_by,
            "uid": login_session['user']['localId']
        }
        db.child("Quotes").push(quote)
        return redirect(url_for('thanks'))
    return render_template("home.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form['full_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            login_session['user'] = user
            user_data = {
                "full_name": full_name,
                "email": email,
                "username": username
            }
            db.child("Users").child(user['localId']).set(user_data)
            return redirect(url_for('home'))
        except:
            error = "Signup failed. Please try again."
            return render_template("signup.html", error=error)
    return render_template("signup.html")

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            login_session['user'] = user
            return redirect(url_for('home'))
        except:
            error = "Signin failed. Please try again."
            return render_template("signin.html", error=error)
    return render_template("signin.html")

@app.route("/display")
def display():
    quotes = db.child("Quotes").get().val()
    return render_template("display.html", quotes=quotes)

@app.route("/thanks")
def thanks():
    return render_template("thanks.html")

@app.route("/signout")
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('signup'))

if __name__ == '__main__':
    app.run(debug=True)
