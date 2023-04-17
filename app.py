from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]
        with sqlite3.connect("emails.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO emails (email) VALUES (?)", (email,))
        return redirect("/")
    return render_template("index.html")

def create_table():
    with sqlite3.connect("emails.db") as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS emails (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT NOT NULL)")

if __name__ == "__main__":
    create_table()
    app.run(debug=True)
