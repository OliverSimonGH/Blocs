from flask import Flask, request, render_template, jsonify
import database
import sqlite3
app = Flask(__name__, static_url_path="/static")

#Home section - Adding blocks to database and removing from database
@app.route("/")
@app.route("/home")
def home():
    database.select_all()
    return render_template('index.html')

@app.route("/uploadBloc", methods=['POST'])
def upload_bloc():
    parameters = ["Second bloc", "This is the second bloc", "http://www.google.co.uk"]
    database.write_bloc_to_database(parameters)
    result = database.select_all()
    print(result)
    result = jsonify(result)
    return result
#Emails - CRUD emails
@app.route("/emails")
def emails():
    return render_template('emails.html')

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
    app.run(debug=True)
    database.delete_tables()
    database.create_tables()
    database.populate_tables()
    database.select_all()
