import requests
import urllib.parse
from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

firebaseConfig = {
  "apiKey": "AIzaSyCCaIQqMz-8O63U0mVUBOqVvbr5r7-PGcc",
  "authDomain": "first-project-41406.firebaseapp.com",
  "projectId": "first-project-41406",
  "storageBucket": "first-project-41406.appspot.com",
  "messagingSenderId": "978522956316",
  "appId": "1:978522956316:web:b64af561d98d2a090ef5d9",
  "measurementId": "G-VP3W681SE5" , 
  "databaseURL": "https://first-project-41406-default-rtdb.europe-west1.firebasedatabase.app/"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user
            return redirect(url_for('home'))
        except Exception as e:
            print(e)
            return "Sign in failed. Please try again."
    return render_template("signin.html")

@app.route("/", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = user
            user_id = session["user"]["localId"]
            db.child("User").child(user_id).set({"email" : email , "password" : password})
            return redirect(url_for('home'))
            
        except Exception as e:
            print(e)
            return "Sign up failed. Please try again."
    return render_template("signup.html")

@app.route("/home",methods=['GET', 'POST'])
def home():
    if 'user' not in session:
        return redirect(url_for('signin'))
    return render_template("home.html")

@app.route("/profile", methods=['GET', 'POST'])
def profile():
    if 'user' not in session:
        return redirect(url_for('signin'))
    
    if request.method == 'POST':
        goal = request.form['goal']
        user_id = session['user']['localId']
        db.child("goals").push({"user_id": user_id, "goal": goal})

    
    user_id = session['user']['localId']
    
    return render_template("profile.html")

@app.route("/public")
def public():
    goals = db.child("goals").get()
    return render_template("public.html", goals=goals.val())

@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)
