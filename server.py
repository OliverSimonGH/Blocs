from flask import Flask, request, render_template, jsonify, redirect
import database
import sqlite3
from sendEmail import send_email, set_emails
import os, re, time
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_PATH = 'static/uploads'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_PATH)

app.secret_key = "this_is_a_secret"
DATABASE = "blocs.db"

#Home section - Adding blocks to database and removing from database
@app.route("/")
@app.route("/home")
def home():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM `Blocs`")
    data = cur.fetchall()
    cur.execute("SELECT * FROM `UserProfile` WHERE profileid=1")
    data1 = cur.fetchall()
    return render_template('index.html', data=data, data1=data1)

@app.route("/uploadBloc", methods=['POST'])
def upload_bloc():
    fav = request.form.get('fav')
    url = request.form.get('url')
    imgurl = request.form.get('imgurl')
    title = request.form.get('title')
    notes = request.form.get('notes')
    category = request.form.get('category')

    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT INTO `Blocs`(`weburl`, `imgurl`, `title`, `notes`, `category`,`favourite`)\
                VALUES(?,?,?,?,?,?)", (url, imgurl, title, notes, category, fav))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/sendEmail", methods=['POST'])
def sendEmail():
    local_from_email = "blocstest@outlook.com"
    email_sent = str(request.json['emailForm'])
    check = int(request.json['checkRadio'])
    bloc_Array = str(request.json['blocArray'])
    print(request.json['blocArray'])
    date_time = time.strftime("%x")
    day_time = time.strftime("%X")
    email_val = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    print("Email: {} \nBool: {} \nArray: {}".format(email_sent, check, bloc_Array))
    conn = sqlite3.connect(DATABASE)
    # http://stackoverflow.com/questions/2854011/get-a-list-of-field-values-from-pythons-sqlite3-not-tuples-representing-rows
    conn.row_factory = lambda cursor, row: row[0]
    cur = conn.cursor()
    cur.execute("SELECT emailAddress FROM Emails")
    data = cur.fetchall()

    parameters = [email_sent, local_from_email, date_time, day_time, bloc_Array]
    set_emails(email_sent, local_from_email)

    if email_sent == "" or not email_val.match(email_sent):
        msg = "Please enter a valid e-mail address"

    elif email_sent in data:
        print("Email already exists")
        if check == 1:
            database.write_log(parameters)
            cur.execute("UPDATE Emails SET emailList=1 WHERE emailAddress=?",(email_sent,))
        if check == 0:
            database.write_log(parameters)

        msg = "You have sent an e-mail to: " + email_sent
        #Send email
        sendEmail.target_email = email_sent
        sendEmail.from_email = local_from_email
        send_email()

    else:
        # store new email sent into the database
        database.create_email(email_sent, check)
        database.write_log(parameters)
        # send email
        msg = "You have sent an e-mail to: " + email_sent
        sendEmail.target_email = email_sent
        sendEmail.from_email = local_from_email
        send_email()

    conn.commit()
    conn.close()
    return msg

@app.route('/deleteEmail', methods=['POST'])
def delete_email():
    email = request.form.get('email_add')
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("UPDATE Emails SET emailList=0 WHERE emailList=1 and emailAddress=?", (email,))
    conn.commit()
    conn.close()
    return redirect("/emails")

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
    results = database.read_logs()
    return render_template('logs.html', results=results)

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
    return render_template('index.html', **locals());

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
    blocid = request.form.get('blocid')
    url = request.form.get('url')
    imgurl = request.form.get('imgurl')
    title = request.form.get('title')
    notes = request.form.get('notes')
    category = request.form.get('category')

    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("UPDATE `Blocs` SET `weburl`=?, `imgurl`=?, `title`=?, `notes`=?, `category`=? WHERE `blocid`=?", (url, imgurl, title, notes, category, blocid))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route('/deleteBloc', methods=['POST'])
def deleteBlocForm():
    blocNum = request.form.get('del_block')
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("DELETE FROM `Blocs` WHERE `blocid`=?", (blocNum,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route('/favBloc', methods=['POST'])
def favBloc():
    blocid = request.form['id']
    fav = request.form['fav']
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("UPDATE Blocs SET favourite=? WHERE blocid=?", (fav, blocid))
    conn.commit()
    conn.close()
    return "Favourited"

@app.route('/unfavBloc', methods=['POST'])
def unfavBloc():
    blocid = request.form['id']
    fav = request.form['fav']
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("UPDATE Blocs SET favourite=? WHERE blocid=?", (fav, blocid))
    conn.commit()
    conn.close()
    return "Unfavourited"

@app.route('/Login')
def LoginUser():
    return render_template("login.html")

@app.route('/Register', methods=['GET','POST'])
def register_user():
    if request.method == 'GET':
        return redirect('/Login')
    emailAddress = request.form['emailAddress']
    password = request.form['password']
    result = database.create_user(emailAddress, password)
    if(result):
        msg = "User was successfully created!"
        return render_template('/register', msg=msg)
    else:
        msg = "There was an error during registration"
        return render_template('/register', msg=msg)

if __name__ == "__main__":
    database.delete_tables()
    database.create_tags()
    database.create_tables()
    database.populate_tables()
    database.select_all()
    app.run(debug=True)
