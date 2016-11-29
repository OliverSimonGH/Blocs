import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_email = "bradye@cardiff.ac.uk"
from_pwd = "Summertime11"
to_email = "BlocsTest@outlook.com"

# Set up base of image
msg = MIMEMultipart('html')
msg['Subject'] = "Test SMTPlib Message"
msg['From'] = "bradye@cardiff.ac.uk"
msg['To'] = "BlocsTest@outlook.com"

# Create the body of the message (a plain-text and an HTML version).

#
# html = """\
# <html>
#   <head></head>
#   <body>
#     <table>
#
#     </table>
#   </body>
# </html>
# """

firstHTML = "<html> <head></head> <body><table></table>"
bloc_one = "<div>This is the bloc title</div>"
secondHTML = "</body></html>"

new_html = firstHTML + bloc_one + secondHTML

#
# firstHTML.append(bloc_one)
# firstHTML.append(secondHTML)

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
