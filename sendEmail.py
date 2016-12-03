import smtplib
import sys
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

DATABASE = 'Blocs.db'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

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

print(weburl_data)
print("")
print(imgurl_data)
print("")
print(title_data)
print("")
print(notes_data)

from_email = "bradye@cardiff.ac.uk"
from_pwd = "Summertime11"
to_email = "BlocsTest@outlook.com"

# Set up base of image
msg = MIMEMultipart('html')
msg['Subject'] = "Test SMTPlib Message"
msg['From'] = "bradye@cardiff.ac.uk"
msg['To'] = "BlocsTest@outlook.com"

firstHTML = '<html> <head></head> <body><table style="border: 1px solid black; font-color:red;"> <tr>'
bloc_one = "weburl_data"
secondHTML = '</tr></table></body></html>'

new_html = firstHTML + bloc_one + secondHTML

msg.attach(MIMEText(new_html, 'html'))
print(msg)

# May want to add some error checks here
# Change these based on the SMTP params of your mail provider
mail = smtplib.SMTP('outlook.office365.com', 587)
mail.ehlo()
mail.starttls()
mail.login("bradye@cardiff.ac.uk", "Summertime11")
mail.sendmail("bradye@cardiff.ac.uk", "BlocsTest@outlook.com", msg.as_string())
print("email sent")
mail.quit()
