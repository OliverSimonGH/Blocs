import smtplib
import sys
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

DATABASE = 'Blocs.db'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

conn = sqlite3.connect(DATABASE)
cur = conn.cursor()
test = cur.execute("SELECT weburl FROM Blocs")
print(test)
#blocs = cur.fetchall()

#print("Getting blocs from server...")
# print(blocs)
# web_url_list = []
# img_url_list = []
# for record in blocs:
#     name = record[1::6]
#     print("------------------------")
#     print("Name:")
#     print(name)
#     print("------------------------")
#
#     img_URL = record[2::6]
#     print("........................")
#     print("img_URL")
#     print(img_URL)
#     print("........................")
#
#     title = record[3::6]
#     print("________________________")
#     print("title")
#     print(title)
#     print("________________________")
#
#     notes = record[4::6]
#     print("========================")
#     print("notes")
#     print(notes)
#     print("========================")

conn.commit()
conn.close()

# print("Web URL:", name)
# print(" ")
# print("Image URL:", img_URL)
# print("Title:", title)
# print("Notes:", notes)

from_email = "bradye@cardiff.ac.uk"
from_pwd = "Summertime11"
to_email = "BlocsTest@outlook.com"

# Set up base of image
msg = MIMEMultipart('html')
msg['Subject'] = "Test SMTPlib Message"
msg['From'] = "bradye@cardiff.ac.uk"
msg['To'] = "BlocsTest@outlook.com"

firstHTML = "<html> <head></head> <body><table></table>"
bloc_one = "<div>This is the bloc title</div>"
secondHTML = "</body></html>"
print(firstHTML)

# bloc_one = "<div>This is the bloc title</div>"
# secondHTML = "</body></html>"
#
# new_html = firstHTML + bloc_one + secondHTML
#
# # firstHTML.append(bloc_one)
# # firstHTML.append(secondHTML)
#
# msg.attach(MIMEText(new_html, 'html'))
# print(msg)
#
# # May want to add some error checks here
# # Change these based on the SMTP params of your mail provider
# mail = smtplib.SMTP('outlook.office365.com', 587)
# mail.ehlo()
# mail.starttls()
# mail.login("bradye@cardiff.ac.uk", "Summertime11")
# mail.sendmail("bradye@cardiff.ac.uk", "BlocsTest@outlook.com", msg.as_string())
# print("email sent")
# mail.quit()
