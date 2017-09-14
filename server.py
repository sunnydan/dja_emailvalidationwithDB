from flask import Flask, render_template, redirect, request, session
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "DINGUS"
mysql = MySQLConnector(app, 'emails')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    try:
        return render_template("index.html", emails=mysql.query_db("SELECT * FROM emails"), invalid=session['invalidmessage']);
    except KeyError:
        session['invalidmessage'] = False
        return redirect('/')
@app.route('/process', methods=["POST"])
def emails():
    if EMAIL_REGEX.match(request.form['email']):
        emaillist=mysql.query_db("SELECT * FROM emails")
        for email in emaillist:
            if email['email'] == request.form['email']:
                session['invalidmessage'] = "Email already exists in database!"
                return redirect("/")
        query = "INSERT INTO emails (email, created_at) VALUES (:email, NOW())" 
        data = {'email': request.form['email']}
        mysql.query_db(query, data)
        session['invalidmessage'] = False
    else:
        session['invalidmessage'] = "Email is not valid!"
    return redirect("/")    

@app.route('/remove_email/<email_id>', methods=['POST'])
def delete(email_id):
    query = "DELETE FROM emails WHERE id = :id"
    data = {'id': email_id}
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/reset', methods=["POST"])
def reset():
    mysql.query_db("DELETE FROM emails WHERE id > 0")
    return redirect('/')

app.run(debug=True)
