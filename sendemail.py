import sys
from smtplib import SMTP as SMTP 
from email.mime.text import MIMEText

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
with open('textfile.txt') as fp:
    # Create a text/plain message
    msg = MIMEText(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % 'textfile.txt'
msg['From'] = 'Emma.Brady12@hotmail.co.uk'
msg['To'] = 'Emma.Brady12@hotmail.co.uk'

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
