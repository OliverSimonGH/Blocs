
from flask import Flask, request, render_template, jsonify, redirect, Markup
import database
import sqlite3
import os, re
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_PATH = 'static/uploads'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_PATH)

app.secret_key = "this_is_a_secret"
DATABASE = "Blocs.db"


@app.route("/uploadBloc", methods=['POST'])
def upload_bloc():
    parameters = [request.form["url"], request.form["title"], request.form["notes"], request.form["category"]]
    database.write_bloc_to_database(parameters)

    return redirect("/")

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


@app.route('/')
def index():
    all_image_files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        if (isImageFormat(filename)):
            all_image_files.append(filename)

    result = database.select_all()
    result_list = []


    for row in result:
        tup = (row[0], row[2])
        result_list.append(tup)

    return render_template('index.html', result=result_list);

def correctFormat(link):
    if (link.find('.jpg') > -1 or link.find('.png') > -1 or link.find('.gif') > -1 or link.find('.jpeg') > -1):
        return True;
    return False;

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        upload_path = '{}/{}'.format(UPLOAD_FOLDER, file.filename)
        file.save(upload_path)
        return 'ok'

@app.route('/editBloc', methods=['POST'])
def editBlocForm():
    parameters = [request.form["title"], request.form["link"], request.form["description"], request.form["idValue"]]
    database.update_table(parameters)
    return redirect('/')

if __name__ == "__main__":
   database.delete_tables()
   database.create_tags()
   database.create_tables()
   database.populate_tables()
   database.select_all()
   app.run(debug=True)