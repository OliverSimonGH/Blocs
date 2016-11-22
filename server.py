from flask import Flask, request, render_template, jsonify, redirect
import database
import sqlite3
import os, re

app = Flask(__name__, static_url_path="/static")
app.secret_key = "this_is_a_secret"
DATABASE = "Blocs.db"

#Home section - Adding blocks to database and removing from database
@app.route("/")
@app.route("/home")
def home():
    #database.select_all()
    return render_template('index.html')

@app.route("/uploadBloc", methods=['POST'])
def upload_bloc():
    parameters = [request.form["url"], request.form["title"], request.form["notes"], request.form["category"]]
    database.write_bloc_to_database(parameters)
    db_result = database.select_all()
    result_list = []
    current_list = []

    for row in db_result:
        current_list.append(row[0])
        current_list.append(row[1])
        current_list.append(row[2])
        current_list.append(row[3])
        current_list.append(row[4])
        result_list.append(current_list)

    return render_template('index.html', result=result_list)


@app.route("/sendEmail", methods=['POST'])
def sendEmail():
    email_sent = request.form.get('send-email')
    email_radio = request.form.get('send-radio')
    check = bool(email_radio)
    email_val = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    if email_sent == "":
        msg = "Please enter an e-mail address"

    elif not email_val.match(email_sent):
        msg = "Please enter a valid e-mail address"

    else:
        # store data into database
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO Emails ('emailAddress', 'emailList')\
                     VALUES (?,?)", (email_sent, check))
        conn.commit()
        msg = "You have sent an e-mail to: " + email_sent
    return render_template("index.html", msg=msg)

@app.route("/readBloc", methods=['GET'])
def read_bloc():
    pass

#Emails - CRUD emails
@app.route("/emails", methods=['GET'])
def emails():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT emailAddress FROM Emails WHERE emailList = 1")
    email_address = cur.fetchall()
    conn.close()
    return render_template('emails.html',  email_address = email_address)

#Logs - Add and view logs
@app.route("/logs")
def logs():
    return render_template('logs.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/settings")
def settings():
    return render_template('settings.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    database.delete_tables()
    database.create_tags()
    database.create_tables()
    database.populate_tables()
    database.select_all()
    app.run(debug=True)
