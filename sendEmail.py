import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_email = "bradye@cardiff.ac.uk"
from_pwd = "Summertime11"
to_email = "Emma.Brady12@hotmail.co.uk"

# Set up base of image
msg = MIMEMultipart('html')
msg['Subject'] = "Test SMTPlib Message"
msg['From'] = "bradye@cardiff.ac.uk"
msg['To'] = "Emma.Brady12@hotmail.co.uk"

# Create the body of the message (a plain-text and an HTML version).
html = """\
<html>
  <head></head>
  <body>
    <p>Hola!<br>
       <b>Wanna learn some things?</b><br>
       Here are my <a href="https://github.com/encima/cm6111_Comp_Thinking_In_Python">slides</a>.
    </p>
  </body>
</html>
"""

msg.attach(MIMEText(html, 'html'))
print(msg)

# May want to add some error checks here
# Change these based on the SMTP params of your mail provider
mail = smtplib.SMTP('outlook.office365.com', 587)
mail.ehlo()
mail.starttls()
mail.login("bradye@cardiff.ac.uk", "Summertime11")
mail.sendmail("bradye@cardiff.ac.uk", "Emma.Brady12@hotmail.co.uk", msg.as_string())
print("email sent")
mail.quit()
