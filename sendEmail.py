import smtplib
import sys
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

DATABASE = 'Blocs.db'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

conn = sqlite3.connect(DATABASE)
cur = conn.cursor()
cur.execute("SELECT * FROM Blocs")
blocs = cur.fetchall()
print("Getting blocs from server...")
print(blocs)

for record in blocs:
    name = record[1]
    occupation = record[2]
    location = record[3]
conn.commit()
conn.close()

print("Current record:", id)
print("Name: ", name)
print("Occupation: ", occupation)
print("Location: ", location)

# from_email = "bradye@cardiff.ac.uk"
# from_pwd = "Summertime11"
# to_email = "BlocsTest@outlook.com"
#
# # Set up base of image
# msg = MIMEMultipart('html')
# msg['Subject'] = "Test SMTPlib Message"
# msg['From'] = "bradye@cardiff.ac.uk"
# msg['To'] = "BlocsTest@outlook.com"
#
# firstHTML = "<html> <head></head> <body><table></table>"
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
