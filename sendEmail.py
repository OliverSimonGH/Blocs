import smtplib
import sys
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

DATABASE = 'blocs.db'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

from_email = ""
target_email = ""

def set_emails(to_email_local, from_email_local):
	global target_email
	global from_email
	from_email = from_email_local
	target_email = to_email_local


def send_email():
    global target_email
    global from_email

    print("Getting blocs from server...")
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = lambda cursor, row: row[0]
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM `Logs`")
    count = cur.fetchall()
    print(count)
    cur.execute("SELECT `blocList` FROM `Logs` WHERE `logId` = ?", (count[0],))
    Array_blocs = cur.fetchall()
    print(Array_blocs)

    new_list = []
    for i in Array_blocs:
        for val in i:
            if val.isdigit():
                new_list.append(val)
    print(new_list)

    # cur.execute("SELECT b.title FROM `Logs` AS L JOIN `Blocs` AS B ON b.blocid = ? WHERE l.logId = ?", (bloclist, count));
    weburl_store = []
    imgurl_store = []
    title_store = []
    notes_store = []

    for val in new_list:
        cur.execute("SELECT weburl FROM Blocs WHERE blocId = ?", (val,))
        weburl = cur.fetchall()
        weburl_store.append(weburl)

    for val in new_list:
        cur.execute("SELECT imgurl FROM Blocs WHERE blocId = ?", (val,))
        imgurl = cur.fetchall()
        imgurl_store.append(imgurl)

    for val in new_list:
        cur.execute("SELECT title FROM Blocs WHERE blocId = ?", (val,))
        title = cur.fetchall()
        title_store.append(title)

    for val in new_list:
        cur.execute("SELECT notes FROM Blocs WHERE blocId = ?", (val,))
        notes = cur.fetchall()
        notes_store.append(notes)
    conn.commit()
    conn.close()

    weburl_data = []
    imgurl_data = []
    title_data = []
    notes_data = []

    for val in weburl_store:
        for new in val:
            weburl_data.append(new)

    for val in imgurl_store:
        for new in val:
            imgurl_data.append(new)

    for val in title_store:
        for new in val:
            title_data.append(new)

    for val in notes_store:
        for new in val:
            notes_data.append(new)

    # Uncomment to check what data is coming through
    # print(weburl_data)
    # print("")
    # print(imgurl_data)
    # print("")
    # print(title_data)
    # print("")
    # print(notes_data)
    # print(weburl_data[0])
    # print(type(weburl_data))

    weburl_show = []
    imgurl_show = []
    title_show = []
    notes_show = []

    for i in range(len(new_list)):
        weburl = str(weburl_data[i])
        weburl_show.append(weburl)

        imgurl = str(imgurl_data[i])
        imgurl_show.append(imgurl)

        title = str(title_data[i])
        title_show.append(title)

        notes = str(notes_data[i])
        notes_show.append(notes)

    from_email = "blocstest@outlook.com"
    from_pwd = "Blocs123"
    to_email = target_email

    # Set up base of image
    msg = MIMEMultipart('html')
    msg['Subject'] = "Test SMTPlib Message"
    msg['From'] = from_email
    msg['To'] = target_email

    open_HTML = '<html> <head></head> <body>'

    title = '<h1 style="text-align:center;"> SMILEnotes </h1> <br>'
    user_details = '<p> {{USER_FULLNAME}} has sent you some links. </p> <br>'

    bloc_title = []
    bloc_link = []
    bloc_notes = []
    title_count = 1
    weburl_count = 1
    notes_count = 1

    # print(title_show)
    # print(weburl_show)
    # print(notes_show)


    for i, f in enumerate(title_show):
        bloc_title_title = '<h3>' + title_show[i] + '</h3>'
        bloc_title.append(bloc_title_title)


    for s, e in enumerate(weburl_show):
        bloc_link_link = '<a href=' + weburl_show[s] + '>' + weburl_show[s] + '</a>'
        bloc_link.append(bloc_link_link)


    for t, r in enumerate(notes_show):
        bloc_notes_notes = '<h4>' + notes_show[t] + '</h4>'
        bloc_notes.append(bloc_notes_notes)

        # print(bloc_title)
        # print(bloc_link)
        # print(bloc_notes)

    if len(new_list) == 1:
        bloc_row_start_1 = '<table style="width:100%";>'
        bloc_title_1 = bloc_title[0]
        bloc_link_1 = bloc_link[0]
        bloc_notes_1 = bloc_notes[0]
        bloc_row_end_1 = '</table> <br>'

    elif len(new_list) == 2:
        bloc_row_start_1 = '<table style="width:100%";>'
        bloc_title_1 = bloc_title[0]
        bloc_link_1 = bloc_link[0]
        bloc_notes_1 = bloc_notes[0]
        bloc_row_end_1 = '</table> <br>'

        bloc_row_start_2 = '<table style="width:100%";>'
        bloc_title_2 = bloc_title[1]
        bloc_link_2 = bloc_link[1]
        bloc_notes_2 = bloc_notes[1]
        bloc_row_end_2 = '</table> <br>'

    elif len(new_list) == 3:

        bloc_row_start_1 = '<table style="width:100%";>'
        bloc_title_1 = bloc_title[0]
        bloc_link_1 = bloc_link[0]
        bloc_notes_1 = bloc_notes[0]
        bloc_row_end_1 = '</table> <br>'

        bloc_row_start_2 = '<table style="width:100%";>'
        bloc_title_2 = bloc_title[1]
        bloc_link_2 = bloc_link[1]
        bloc_notes_2 = bloc_notes[1]
        bloc_row_end_2 = '</table> <br>'

        bloc_row_start_3 = '<table style="width:100%";>'
        bloc_title_3 = bloc_title[2]
        bloc_link_3 = bloc_link[2]
        bloc_notes_3 = bloc_notes[2]
        bloc_row_end_3 = '</table> <br>'

    elif len(new_list) == 4:
        bloc_row_start_1 = '<table style="width:100%";>'
        bloc_title_1 = bloc_title[0]
        bloc_link_1 = bloc_link[0]
        bloc_notes_1 = bloc_notes[0]
        bloc_row_end_1 = '</table> <br>'

        bloc_row_start_2 = '<table style="width:100%";>'
        bloc_title_2 = bloc_title[1]
        bloc_link_2 = bloc_link[1]
        bloc_notes_2 = bloc_notes[1]
        bloc_row_end_2 = '</table> <br>'

        bloc_row_start_3 = '<table style="width:100%";>'
        bloc_title_3 = bloc_title[2]
        bloc_link_3 = bloc_link[2]
        bloc_notes_3 = bloc_notes[2]
        bloc_row_end_3 = '</table> <br>'

        bloc_row_start_4 = '<table style="width:100%";>'
        bloc_title_4 = bloc_title[3]
        bloc_link_4 = bloc_link[3]
        bloc_notes_4 = bloc_notes[3]
        bloc_row_end_4 = '</table> <br>'

    elif len(new_list) == 5:
        bloc_row_start_1 = '<table style="width:100%";>'
        bloc_title_1 = bloc_title[0]
        bloc_link_1 = bloc_link[0]
        bloc_notes_1 = bloc_notes[0]
        bloc_row_end_1 = '</table> <br>'

        bloc_row_start_2 = '<table style="width:100%";>'
        bloc_title_2 = bloc_title[1]
        bloc_link_2 = bloc_link[1]
        bloc_notes_2 = bloc_notes[1]
        bloc_row_end_2 = '</table> <br>'

        bloc_row_start_3 = '<table style="width:100%";>'
        bloc_title_3 = bloc_title[2]
        bloc_link_3 = bloc_link[2]
        bloc_notes_3 = bloc_notes[2]
        bloc_row_end_3 = '</table> <br>'

        bloc_row_start_4 = '<table style="width:100%";>'
        bloc_title_4 = bloc_title[3]
        bloc_link_4 = bloc_link[3]
        bloc_notes_4 = bloc_notes[3]
        bloc_row_end_4 = '</table> <br>'

        bloc_row_start_5 = '<table style="width:100%";>'
        bloc_title_5 = bloc_title[4]
        bloc_link_5 = bloc_link[4]
        bloc_notes_5 = bloc_notes[4]
        bloc_row_end_5 = '</table> <br>'

    elif len(new_list) == 6:
        bloc_row_start_1 = '<table style="width:100%";>'
        bloc_title_1 = bloc_title[0]
        bloc_link_1 = bloc_link[0]
        bloc_notes_1 = bloc_notes[0]
        bloc_row_end_1 = '</table> <br>'

        bloc_row_start_2 = '<table style="width:100%";>'
        bloc_title_2 = bloc_title[1]
        bloc_link_2 = bloc_link[1]
        bloc_notes_2 = bloc_notes[1]
        bloc_row_end_2 = '</table> <br>'

        bloc_row_start_3 = '<table style="width:100%";>'
        bloc_title_3 = bloc_title[2]
        bloc_link_3 = bloc_link[2]
        bloc_notes_3 = bloc_notes[2]
        bloc_row_end_3 = '</table> <br>'

        bloc_row_start_4 = '<table style="width:100%";>'
        bloc_title_4 = bloc_title[3]
        bloc_link_4 = bloc_link[3]
        bloc_notes_4 = bloc_notes[3]
        bloc_row_end_4 = '</table> <br>'

        bloc_row_start_5 = '<table style="width:100%";>'
        bloc_title_5 = bloc_title[4]
        bloc_link_5 = bloc_link[4]
        bloc_notes_5 = bloc_notes[4]
        bloc_row_end_5 = '</table> <br>'

        bloc_row_start_6 = '<table style="width:100%";>'
        bloc_title_6 = bloc_title[5]
        bloc_link_6 = bloc_link[5]
        bloc_notes_6 = bloc_notes[5]
        bloc_row_end_6 = '</table> <br>'

    elif len(new_list) == 7:
        bloc_row_start_1 = '<table style="width:100%";>'
        bloc_title_1 = bloc_title[0]
        bloc_link_1 = bloc_link[0]
        bloc_notes_1 = bloc_notes[0]
        bloc_row_end_1 = '</table> <br>'

        bloc_row_start_2 = '<table style="width:100%";>'
        bloc_title_2 = bloc_title[1]
        bloc_link_2 = bloc_link[1]
        bloc_notes_2 = bloc_notes[1]
        bloc_row_end_2 = '</table> <br>'

        bloc_row_start_3 = '<table style="width:100%";>'
        bloc_title_3 = bloc_title[2]
        bloc_link_3 = bloc_link[2]
        bloc_notes_3 = bloc_notes[2]
        bloc_row_end_3 = '</table> <br>'

        bloc_row_start_4 = '<table style="width:100%";>'
        bloc_title_4 = bloc_title[3]
        bloc_link_4 = bloc_link[3]
        bloc_notes_4 = bloc_notes[3]
        bloc_row_end_4 = '</table> <br>'

        bloc_row_start_5 = '<table style="width:100%";>'
        bloc_title_5 = bloc_title[4]
        bloc_link_5 = bloc_link[4]
        bloc_notes_5 = bloc_notes[4]
        bloc_row_end_5 = '</table> <br>'

        bloc_row_start_6 = '<table style="width:100%";>'
        bloc_title_6 = bloc_title[5]
        bloc_link_6 = bloc_link[5]
        bloc_notes_6 = bloc_notes[5]
        bloc_row_end_6 = '</table> <br>'

        bloc_row_start_7 = '<table style="width:100%";>'
        bloc_title_7 = bloc_title[6]
        bloc_link_7 = bloc_link[6]
        bloc_notes_7 = bloc_notes[6]
        bloc_row_end_7 = '</table> <br>'

    elif len(new_list) == 8:
        bloc_row_start_1 = '<table style="width:100%";>'
        bloc_title_1 = bloc_title[0]
        bloc_link_1 = bloc_link[0]
        bloc_notes_1 = bloc_notes[0]
        bloc_row_end_1 = '</table> <br>'

        bloc_row_start_2 = '<table style="width:100%";>'
        bloc_title_2 = bloc_title[1]
        bloc_link_2 = bloc_link[1]
        bloc_notes_2 = bloc_notes[1]
        bloc_row_end_2 = '</table> <br>'

        bloc_row_start_3 = '<table style="width:100%";>'
        bloc_title_3 = bloc_title[2]
        bloc_link_3 = bloc_link[2]
        bloc_notes_3 = bloc_notes[2]
        bloc_row_end_3 = '</table> <br>'

        bloc_row_start_4 = '<table style="width:100%";>'
        bloc_title_4 = bloc_title[3]
        bloc_link_4 = bloc_link[3]
        bloc_notes_4 = bloc_notes[3]
        bloc_row_end_4 = '</table> <br>'

        bloc_row_start_5 = '<table style="width:100%";>'
        bloc_title_5 = bloc_title[4]
        bloc_link_5 = bloc_link[4]
        bloc_notes_5 = bloc_notes[4]
        bloc_row_end_5 = '</table> <br>'

        bloc_row_start_6 = '<table style="width:100%";>'
        bloc_title_6 = bloc_title[5]
        bloc_link_6 = bloc_link[5]
        bloc_notes_6 = bloc_notes[5]
        bloc_row_end_6 = '</table> <br>'

        bloc_row_start_7 = '<table style="width:100%";>'
        bloc_title_7 = bloc_title[6]
        bloc_link_7 = bloc_link[6]
        bloc_notes_7 = bloc_notes[6]
        bloc_row_end_7 = '</table> <br>'

        bloc_row_start_8 = '<table style="width:100%";>'
        bloc_title_8 = bloc_title[7]
        bloc_link_8 = bloc_link[7]
        bloc_notes_8 = bloc_notes[7]
        bloc_row_end_8 = '</table> <br>'

    elif len(new_list) == 9:
        bloc_row_start_1 = '<table style="width:100%";>'
        bloc_title_1 = bloc_title[0]
        bloc_link_1 = bloc_link[0]
        bloc_notes_1 = bloc_notes[0]
        bloc_row_end_1 = '</table> <br>'

        bloc_row_start_1 = '<table style="width:100%";>'
        bloc_title_1 = bloc_title[0]
        bloc_link_1 = bloc_link[0]
        bloc_notes_1 = bloc_notes[0]
        bloc_row_end_1 = '</table> <br>'

        bloc_row_start_2 = '<table style="width:100%";>'
        bloc_title_2 = bloc_title[1]
        bloc_link_2 = bloc_link[1]
        bloc_notes_2 = bloc_notes[1]
        bloc_row_end_2 = '</table> <br>'

        bloc_row_start_3 = '<table style="width:100%";>'
        bloc_title_3 = bloc_title[2]
        bloc_link_3 = bloc_link[2]
        bloc_notes_3 = bloc_notes[2]
        bloc_row_end_3 = '</table> <br>'

        bloc_row_start_4 = '<table style="width:100%";>'
        bloc_title_4 = bloc_title[3]
        bloc_link_4 = bloc_link[3]
        bloc_notes_4 = bloc_notes[3]
        bloc_row_end_4 = '</table> <br>'

        bloc_row_start_5 = '<table style="width:100%";>'
        bloc_title_5 = bloc_title[4]
        bloc_link_5 = bloc_link[4]
        bloc_notes_5 = bloc_notes[4]
        bloc_row_end_5 = '</table> <br>'

        bloc_row_start_6 = '<table style="width:100%";>'
        bloc_title_6 = bloc_title[5]
        bloc_link_6 = bloc_link[5]
        bloc_notes_6 = bloc_notes[5]
        bloc_row_end_6 = '</table> <br>'

        bloc_row_start_7 = '<table style="width:100%";>'
        bloc_title_7 = bloc_title[6]
        bloc_link_7 = bloc_link[6]
        bloc_notes_7 = bloc_notes[6]
        bloc_row_end_7 = '</table> <br>'

        bloc_row_start_8 = '<table style="width:100%";>'
        bloc_title_8 = bloc_title[7]
        bloc_link_8 = bloc_link[7]
        bloc_notes_8 = bloc_notes[7]
        bloc_row_end_8 = '</table> <br>'

        bloc_row_start_9 = '<table style="width:100%";>'
        bloc_title_9 = bloc_title[8]
        bloc_link_9 = bloc_link[8]
        bloc_notes_9 = bloc_notes[8]
        bloc_row_end_9 = '</table> <br>'

    elif len(new_list) == 10:
        bloc_row_start_1 = '<table style="width:100%";>'
        bloc_title_1 = bloc_title[0]
        bloc_link_1 = bloc_link[0]
        bloc_notes_1 = bloc_notes[0]
        bloc_row_end_1 = '</table> <br>'

        bloc_row_start_2 = '<table style="width:100%";>'
        bloc_title_2 = bloc_title[1]
        bloc_link_2 = bloc_link[1]
        bloc_notes_2 = bloc_notes[1]
        bloc_row_end_2 = '</table> <br>'

        bloc_row_start_3 = '<table style="width:100%";>'
        bloc_title_3 = bloc_title[2]
        bloc_link_3 = bloc_link[2]
        bloc_notes_3 = bloc_notes[2]
        bloc_row_end_3 = '</table> <br>'

        bloc_row_start_4 = '<table style="width:100%";>'
        bloc_title_4 = bloc_title[3]
        bloc_link_4 = bloc_link[3]
        bloc_notes_4 = bloc_notes[3]
        bloc_row_end_4 = '</table> <br>'

        bloc_row_start_5 = '<table style="width:100%";>'
        bloc_title_5 = bloc_title[4]
        bloc_link_5 = bloc_link[4]
        bloc_notes_5 = bloc_notes[4]
        bloc_row_end_5 = '</table> <br>'

        bloc_row_start_6 = '<table style="width:100%";>'
        bloc_title_6 = bloc_title[5]
        bloc_link_6 = bloc_link[5]
        bloc_notes_6 = bloc_notes[5]
        bloc_row_end_6 = '</table> <br>'

        bloc_row_start_7 = '<table style="width:100%";>'
        bloc_title_7 = bloc_title[6]
        bloc_link_7 = bloc_link[6]
        bloc_notes_7 = bloc_notes[6]
        bloc_row_end_7 = '</table> <br>'

        bloc_row_start_8 = '<table style="width:100%";>'
        bloc_title_8 = bloc_title[7]
        bloc_link_8 = bloc_link[7]
        bloc_notes_8 = bloc_notes[7]
        bloc_row_end_8 = '</table> <br>'

        bloc_row_start_9 = '<table style="width:100%";>'
        bloc_title_9 = bloc_title[8]
        bloc_link_9 = bloc_link[8]
        bloc_notes_9 = bloc_notes[8]
        bloc_row_end_9 = '</table> <br>'

        bloc_row_start_10 = '<table style="width:100%";>'
        bloc_title_10 = bloc_title[9]
        bloc_link_10 = bloc_link[9]
        bloc_notes_10 = bloc_notes[9]
        bloc_row_end_10 = '</table> <br>'

    signature_1 = '<br> <table style="width:100%";> <h4 style="text-align:center;"> Kind regards, </h4> </table>'

    close_HTML = '</body></html>'

    if len(new_list) == 1:
        new_html = open_HTML + title + user_details + bloc_row_start_1 + bloc_title_1 + bloc_link_1 + bloc_notes_1 + bloc_row_end_1 + signature_1 + close_HTML
    if len(new_list) == 2:
        new_html = open_HTML + title + user_details + bloc_row_start_1 + bloc_title_1 + bloc_link_1 + bloc_notes_1 + bloc_row_end_1 + bloc_row_start_2 + bloc_title_2 + bloc_link_2 + bloc_notes_2 + bloc_row_end_2 + signature_1 + close_HTML
    if len(new_list) == 3:
        new_html = open_HTML + title + user_details + bloc_row_start_1 + bloc_title_1 + bloc_link_1 + bloc_notes_1 + bloc_row_end_1 + bloc_row_start_2 + bloc_title_2 + bloc_link_2 + bloc_notes_2 + bloc_row_end_2 + bloc_row_start_3 + bloc_title_3 + bloc_link_3 + bloc_notes_3 + bloc_row_end_3 + signature_1 + close_HTML
    if len(new_list) == 4:
        new_html = open_HTML + title + user_details + bloc_row_start_1 + bloc_title_1 + bloc_link_1 + bloc_notes_1 + bloc_row_end_1 + bloc_row_start_2 + bloc_title_2 + bloc_link_2 + bloc_notes_2 + bloc_row_end_2 + bloc_row_start_3 + bloc_title_3 + bloc_link_3 + bloc_notes_3 + bloc_row_end_3 + bloc_row_start_4 + bloc_title_4 + bloc_link_4 + bloc_notes_4 + bloc_row_end_4 + signature_1 + close_HTML
    if len(new_list) == 5:
        new_html = open_HTML + title + user_details + bloc_row_start_1 + bloc_title_1 + bloc_link_1 + bloc_notes_1 + bloc_row_end_1 + bloc_row_start_2 + bloc_title_2 + bloc_link_2 + bloc_notes_2 + bloc_row_end_2 + bloc_row_start_3 + bloc_title_3 + bloc_link_3 + bloc_notes_3 + bloc_row_end_3 + bloc_row_start_4 + bloc_title_4 + bloc_link_4 + bloc_notes_4 + bloc_row_end_4 + bloc_row_start_5 + bloc_title_5 + bloc_link_5 + bloc_notes_5 + bloc_row_end_5 + signature_1 + close_HTML
    if len(new_list) == 6:
        new_html = open_HTML + title + user_details + bloc_row_start_1 + bloc_title_1 + bloc_link_1 + bloc_notes_1 + bloc_row_end_1 + bloc_row_start_2 + bloc_title_2 + bloc_link_2 + bloc_notes_2 + bloc_row_end_2 + bloc_row_start_3 + bloc_title_3 + bloc_link_3 + bloc_notes_3 + bloc_row_end_3 + bloc_row_start_4 + bloc_title_4 + bloc_link_4 + bloc_notes_4 + bloc_row_end_4 + bloc_row_start_5 + bloc_title_5 + bloc_link_5 + bloc_notes_5 + bloc_row_end_5 + bloc_row_start_6 + bloc_title_6 + bloc_link_6 + bloc_notes_6 + bloc_row_end_6 + bloc_+ signature_1 + close_HTML
    if len(new_list) == 7:
        new_html = open_HTML + title + user_details + bloc_row_start_1 + bloc_title_1 + bloc_link_1 + bloc_notes_1 + bloc_row_end_1 + bloc_row_start_2 + bloc_title_2 + bloc_link_2 + bloc_notes_2 + bloc_row_end_2 + bloc_row_start_3 + bloc_title_3 + bloc_link_3 + bloc_notes_3 + bloc_row_end_3 + bloc_row_start_4 + bloc_title_4 + bloc_link_4 + bloc_notes_4 + bloc_row_end_4 + bloc_row_start_5 + bloc_title_5 + bloc_link_5 + bloc_notes_5 + bloc_row_end_5 + bloc_row_start_6 + bloc_title_6 + bloc_link_6 + bloc_notes_6 + bloc_row_end_6 + bloc_row_start_7 + bloc_title_7 + bloc_link_7 + bloc_notes_7 + bloc_row_end_7 + signature_1 + close_HTML
    if len(new_list) == 8:
        new_html = open_HTML + title + user_details + bloc_row_start_1 + bloc_title_1 + bloc_link_1 + bloc_notes_1 + bloc_row_end_1 + bloc_row_start_2 + bloc_title_2 + bloc_link_2 + bloc_notes_2 + bloc_row_end_2 + bloc_row_start_3 + bloc_title_3 + bloc_link_3 + bloc_notes_3 + bloc_row_end_3 + bloc_row_start_4 + bloc_title_4 + bloc_link_4 + bloc_notes_4 + bloc_row_end_4 + bloc_row_start_5 + bloc_title_5 + bloc_link_5 + bloc_notes_5 + bloc_row_end_5 + bloc_row_start_6 + bloc_title_6 + bloc_link_6 + bloc_notes_6 + bloc_row_end_6 + bloc_row_start_7 + bloc_title_7 + bloc_link_7 + bloc_notes_7 + bloc_row_end_7 + bloc_row_start_8 + bloc_title_8 + bloc_link_8 + bloc_notes_8 + bloc_row_end_8 + signature_1 + close_HTML
    if len(new_list) == 9:
        new_html = open_HTML + title + user_details + bloc_row_start_1 + bloc_title_1 + bloc_link_1 + bloc_notes_1 + bloc_row_end_1 + bloc_row_start_2 + bloc_title_2 + bloc_link_2 + bloc_notes_2 + bloc_row_end_2 + bloc_row_start_3 + bloc_title_3 + bloc_link_3 + bloc_notes_3 + bloc_row_end_3 + bloc_row_start_4 + bloc_title_4 + bloc_link_4 + bloc_notes_4 + bloc_row_end_4 + bloc_row_start_5 + bloc_title_5 + bloc_link_5 + bloc_notes_5 + bloc_row_end_5 + bloc_row_start_6 + bloc_title_6 + bloc_link_6 + bloc_notes_6 + bloc_row_end_6 + bloc_row_start_7 + bloc_title_7 + bloc_link_7 + bloc_notes_7 + bloc_row_end_7 + bloc_row_start_8 + bloc_title_8 + bloc_link_8 + bloc_notes_8 + bloc_row_end_8 + bloc_row_start_9 + bloc_title_9 + bloc_link_9 + bloc_notes_9 + bloc_row_end_9 + signature_1 + close_HTML
    if len(new_list) == 10:
        new_html = open_HTML + title + user_details + bloc_row_start_1 + bloc_title_1 + bloc_link_1 + bloc_notes_1 + bloc_row_end_1 + bloc_row_start_2 + bloc_title_2 + bloc_link_2 + bloc_notes_2 + bloc_row_end_2 + bloc_row_start_3 + bloc_title_3 + bloc_link_3 + bloc_notes_3 + bloc_row_end_3 + bloc_row_start_4 + bloc_title_4 + bloc_link_4 + bloc_notes_4 + bloc_row_end_4 + bloc_row_start_5 + bloc_title_5 + bloc_link_5 + bloc_notes_5 + bloc_row_end_5 + bloc_row_start_6 + bloc_title_6 + bloc_link_6 + bloc_notes_6 + bloc_row_end_6 + bloc_row_start_7 + bloc_title_7 + bloc_link_7 + bloc_notes_7 + bloc_row_end_7 + bloc_row_start_8 + bloc_title_8 + bloc_link_8 + bloc_notes_8 + bloc_row_end_8 + bloc_row_start_9 + bloc_title_9 + bloc_link_9 + bloc_notes_9 + bloc_row_end_9 + bloc_row_start_10 + bloc_title_10 + bloc_link_10 + bloc_notes_10 + bloc_row_end_10 + signature_1 + close_HTML
    msg.attach(MIMEText(new_html, 'html'))
    print(msg)
    print(target_email)
    # Change these based on the SMTP params of your mail provider
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.ehlo()
    mail.login("blocstest@gmail.com", "Blocs123")
    mail.ehlo()
    print(target_email)
    mail.sendmail("blocstest@outlook.com", target_email, msg.as_string())
    print("Email sent")
    mail.quit()
