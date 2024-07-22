from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  

fortunes = [
    "To Kill a Mockingbird by Harper Lee",
    "1984 by George Orwell",
    "The Great Gatsby by F. Scott Fitzgerald",
    "The Catcher in the Rye by J.D. Salinger",
    "Pride and Prejudice by Jane Austen",
    "The Lord of the Rings by J.R.R. Tolkien",
    "The Hobbit by J.R.R. Tolkien",
    "Moby Dick by Herman Melville",
    "War and Peace by Leo Tolstoy",
    "The Odyssey by Homer"
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
