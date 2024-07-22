from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Replace with a more secure key in production

fortunes = [
    "You will find love in an unexpected place.",
    "A great opportunity is on the horizon.",
    "Your hard work will soon pay off.",
    "An old friend will re-enter your life.",
    "You will come into a small fortune.",
    "A surprise journey is in your near future.",
    "Trust your intuition; it will guide you well.",
    "You will discover a hidden talent.",
    "A new hobby will bring you great joy.",
    "Someone close to you has good news to share."
]

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['birth_month'] = request.form['birth_month']
        return redirect(url_for('home'))
    return render_template("login.html")

@app.route("/home")
def home():
    if 'name' not in session:
        return redirect(url_for('login'))
    name = session['name']
    return render_template("home.html", name=name)

@app.route('/fortune')
def fortune():
    if 'name' not in session:
        return redirect(url_for('login'))

    name = session['name']
    birth_month = session['birth_month']
    if len(name) < 10:
        random_fortune = fortunes[len(name)]
    else:
        random_fortune = random.choice(fortunes)
    
    session['fortune'] = random_fortune
    return render_template("fortune.html", name=name, fortune=random_fortune)

if __name__ == '__main__':
    app.run(debug=True)
