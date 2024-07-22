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
    "measurementId": "G-K1R0365HDY",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        quote = request.form["quote"]
        if 'quotes' not in login_session:
            login_session['quotes'] = []
        login_session['quotes'].append(quote)
        return redirect(url_for('thanks'))
    return render_template("home.html", quotes=login_session.get('quotes', []))

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            login_session['user'] = user
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
    return render_template("display.html", quotes=login_session.get('quotes', []))

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
