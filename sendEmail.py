import smtplib
import sys
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

DATABASE = 'Blocs.db'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

target_email = "blocstest@outlook.com"

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

#print(weburl_data)
formatted_web = []
formatted_img = []
formatted_title = []
formatted_notes = []

for data in range(0,7):
    #Format weburl data
    new_url_data = str(weburl_data[data])
    new_url_data = new_url_data[2:-3]
    web_url_data = '"{}"'.format(new_url_data)
    data = web_url_data
    formatted_web.append(data)

for data in range(0,7):
    #Format imgurl data
    new_img_data = str(imgurl_data[data])
    new_img_data = new_img_data[2:-3]
    img_url_data = '"{}"'.format(new_img_data)
    data = img_url_data
    formatted_img.append(data)

for data in range(0,7):
    #Format title data
    new_title_data = str(title_data[data])
    new_title_data = new_title_data[2:-3]
    title_url_data = '"{}"'.format(new_title_data)
    data = title_url_data
    formatted_title.append(data)

for data in range(0,7):
    #Format notes data
    new_notes_data = str(notes_data[data])
    new_notes_data = new_notes_data[2:-3]
    notes_url_data = '"{}"'.format(new_notes_data)
    data = notes_url_data
    formatted_notes.append(data)

#Check formatting
# print(formatted_web)
# print(formatted_web[0])
# print(" ")
# print(formatted_img)
# print(formatted_img[0])
# print(" ")
# print(formatted_title)
# print(formatted_title[0])
# print(" ")
# print(formatted_notes)
# print(formatted_notes[0])
# print(" ")

weburl_1 = str(formatted_web[0])
weburl_2 = str(formatted_web[1])
weburl_3 = str(formatted_web[2])
weburl_4 = str(formatted_web[3])
weburl_5 = str(formatted_web[4])
weburl_6 = str(formatted_web[5])
weburl_7 = str(formatted_web[6])

imgurl_1 = str(formatted_img[0])
imgurl_2 = str(formatted_img[1])
imgurl_3 = str(formatted_img[2])
imgurl_4 = str(formatted_img[3])
imgurl_5 = str(formatted_img[4])
imgurl_6 = str(formatted_img[5])
imgurl_7 = str(formatted_img[6])

title_1 = str(formatted_title[0])
title_2 = str(formatted_title[1])
title_3 = str(formatted_title[2])
title_4 = str(formatted_title[3])
title_5 = str(formatted_title[4])
title_6 = str(formatted_title[5])
title_7 = str(formatted_title[6])

notes_1 = str(formatted_notes[0])
notes_2 = str(formatted_notes[1])
notes_3 = str(formatted_notes[2])
notes_4 = str(formatted_notes[3])
notes_5 = str(formatted_notes[4])
notes_6 = str(formatted_notes[5])
notes_7 = str(formatted_notes[6])

from_email = "blocstest@outlook.com"
from_pwd = "Blocs123"
to_email = target_email

# Set up base of image
msg = MIMEMultipart('html')
msg['Subject'] = "Test SMTPlib Message"
msg['From'] = "blocstest@outlook.com"
msg['To'] = target_email

open_HTML = '<html> <head></head> <body>'
title = '<h1 style="text-align:center;"> SMILEnotes </h1> <br>'
user_details = '<p> {{USER_FULLNAME}} has sent you some links. </p> <br>'
bloc_row_1_start = '<table style="width:100%;> <th style="font-style:strong;"> <br>'
bloc_1_title = '<h3>' + title_1 + '</h3>'
bloc_1_link = '<a href=' + weburl_1 + '>' + weburl_1 + '</a>'
close_HTML = '</th></table></body></html>'

new_html = open_HTML + title + user_details + bloc_row_1_start + bloc_1_title + bloc_1_link + close_HTML

msg.attach(MIMEText(new_html, 'html'))
print(msg)

# Change these based on the SMTP params of your mail provider
mail = smtplib.SMTP('smtp-mail.outlook.com', 587)
mail.ehlo()
mail.starttls()
mail.login("blocstest@outlook.com", "Blocs123")
mail.sendmail("blocstest@outlook.com", target_email, msg.as_string())
print("Email sent")
mail.quit()
