import smtplib
import sys
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

DATABASE = 'Blocs.db'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

target_email = ""

def set_to_email(email):
    target_email = email

print("Getting blocs from server...")
conn = sqlite3.connect(DATABASE)
cur = conn.cursor()
cur.execute("SELECT weburl FROM Blocs")
weburl_data = cur.fetchall()
cur.execute("SELECT imgurl FROM Blocs")
imgurl_data = cur.fetchall()
cur.execute("SELECT title FROM Blocs")
title_data = cur.fetchall()
cur.execute("SELECT notes FROM Blocs")
notes_data = cur.fetchall()
conn.commit()
conn.close()

#Uncomment to check what data is coming through
# print(weburl_data)
# print("")
# print(imgurl_data)
# print("")
# print(title_data)
# print("")
# print(notes_data)
# print(weburl_data[0])
# print(type(weburl_data))

#Splitting up the data lists into variables that can be added to the email
weburl_1 = str(weburl_data[0])
weburl_2 = str(weburl_data[1])
weburl_3 = str(weburl_data[2])
weburl_4 = str(weburl_data[3])
weburl_5 = str(weburl_data[4])
weburl_6 = str(weburl_data[5])
weburl_7 = str(weburl_data[6])

imgurl_1 = str(imgurl_data[0])
imgurl_2 = str(imgurl_data[1])
imgurl_3 = str(imgurl_data[2])
imgurl_4 = str(imgurl_data[3])
imgurl_5 = str(imgurl_data[4])
imgurl_6 = str(imgurl_data[5])
imgurl_7 = str(imgurl_data[6])

title_1 = str(title_data[0])
title_1 = str(title_data[1])
title_1 = str(title_data[2])
title_1 = str(title_data[3])
title_1 = str(title_data[4])
title_1 = str(title_data[5])
title_1 = str(title_data[6])

notes_1 = str(notes_data[0])
notes_1 = str(notes_data[1])
notes_1 = str(notes_data[2])
notes_1 = str(notes_data[3])
notes_1 = str(notes_data[4])
notes_1 = str(notes_data[5])
notes_1 = str(notes_data[6])

# print(notes_1)
# print(type(notes_1))
from_email = "bradye@cardiff.ac.uk"
from_pwd = "Summertime11"
to_email = target_email

# Set up base of image
msg = MIMEMultipart('html')
msg['Subject'] = "Test SMTPlib Message"
msg['From'] = "BlocsTest@"
msg['To'] = target_email

open_HTML = '<html> <head></head> <body>'
title = '<h1 style="text-align:center;"> SMILEnotes </h1> <br>'
user_details = '<p> {{USER_FULLNAME}} has sent you some links. </p> <br>'

bloc_row_1_start = '<table style="width:100%;> <th style="font-style:strong;"> <br>'
bloc_1_title = '<a href=' + title_1 + '> </a>'
bloc_1_link =  "https://www.google.co.uk/?gws_rd=ssl"
test = '<br> <a href= ' + bloc_1_link + '> Google </a>'
close_HTML = '</th></table></body></html>'

new_html = open_HTML + title + user_details + bloc_row_1_start + bloc_1_title + test + close_HTML

msg.attach(MIMEText(new_html, 'html'))
print(msg)

# Change these based on the SMTP params of your mail provider
mail = smtplib.SMTP('outlook.office365.com', 587)
mail.ehlo()
mail.starttls()
mail.login("BlocsTest@outlook.com", "Blocs123")
mail.sendmail("bradye@cardiff.ac.uk", target_email, msg.as_string())
print("Email sent")
mail.quit()
