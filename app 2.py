📂 Folder: Task2_EventRegistrationSystem
1️⃣ app.py
python
Copy
Edit
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Create database table
def init_db():
    conn = sqlite3.connect("registrations.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            event TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    event = request.form['event']

    conn = sqlite3.connect("registrations.db")
    c = conn.cursor()
    c.execute("INSERT INTO registrations (name, email, phone, event) VALUES (?, ?, ?, ?)",
              (name, email, phone, event))
    conn.commit()
    conn.close()

    return redirect(url_for('registrations'))

@app.route('/registrations')
def registrations():
    conn = sqlite3.connect("registrations.db")
    c = conn.cursor()
    c.execute("SELECT * FROM registrations")
    data = c.fetchall()
    conn.close()
    return render_template('registrations.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
2️⃣ templates/index.html
html
Copy
Edit
<!DOCTYPE html>
<html>
<head>
    <title>Event Registration</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h2>Event Registration Form</h2>
    <form method="POST" action="/register">
        <label>Name:</label><input type="text" name="name" required><br>
        <label>Email:</label><input type="email" name="email" required><br>
        <label>Phone:</label><input type="text" name="phone" required><br>
        <label>Event:</label>
        <select name="event" required>
            <option value="Workshop">Workshop</option>
            <option value="Seminar">Seminar</option>
            <option value="Hackathon">Hackathon</option>
        </select><br>
        <button type="submit">Register</button>
    </form>
    <br>
    <a href="/registrations">View All Registrations</a>
</body>
</html>
3️⃣ templates/registrations.html
html
Copy
Edit
<!DOCTYPE html>
<html>
<head>
    <title>Registrations</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h2>All Registrations</h2>
    <table border="1">
        <tr>
            <th>ID</th><th>Name</th><th>Email</th><th>Phone</th><th>Event</th>
        </tr>
        {% for row in data %}
        <tr>
            <td>{{ row[0] }}</td>
            <td>{{ row[1] }}</td>
            <td>{{ row[2] }}</td>
            <td>{{ row[3] }}</td>
            <td>{{ row[4] }}</td>
        </tr>
        {% endfor %}
    </table>
    <br>
    <a href="/">Back to Registration</a>
</body>
</html>
4️⃣ static/style.css
css
Copy
Edit
body {
    font-family: Arial, sans-serif;
    background: #f2f2f2;
    padding: 20px;
}
h2 {
    color: #333;
}
form {
    background: white;
    padding: 15px;
    border-radius: 5px;
}
input, select {
    width: 100%;
    padding: 8px;
    margin: 5px 0;
}
button {
    background: green;
    color: white;
    padding: 10px;
    border: none;
    cursor: pointer;
}
table {
    width: 100%;
    background: white;
    border-collapse: collapse;
}
th, td {
    padding: 10px;
    text-align: center;
}
th {
    background: #555;
    color: white;
}
5️⃣ README.md
markdown
Copy
Edit
# Task 2 - Event Registration System

## Description
A Flask web app for registering participants for events and viewing the registration list. Data is stored in SQLite.

## How to Run
1. Install Flask:
   ```bash
   pip install flask
Run the app:

bash
Copy
Edit
python app.py
Open in browser:

cpp
Copy
Edit
http://127.0.0.1:5000/
Features
Register for an event with name, email, phone.

View all registered participants.

Data stored in SQLite database.


---

