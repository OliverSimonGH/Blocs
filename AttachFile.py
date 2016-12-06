
import sys
import ast
from datetime import datetime

import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText



filePath = "flower.jpg"#your file name

From = 'blocstest@gmail.com'
To = 'blocstest@gmail.com'

msg = MIMEMultipart()
msg['From'] = From
msg['To'] = To
msg['Subject'] = 'Message From Ahmed'

msg.attach(MIMEText('Sample message'))

try:
    smtp = smtplib.SMTP('smtp.gmail.com:587')
    smtp.starttls()
    smtp.login('blocstest@gmail.com', 'Blocs123')
except:
    i = 1
else:
    i = 0

if i == 0:
    ctype, encoding = mimetypes.guess_type(filePath)
    if ctype is None or encoding is not None:
        # No guess could be made, or the file is encoded (compressed), so
        # use a generic bag-of-bits type.
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    if maintype == 'text':
        fp = open(filePath)
        # Note: we should handle calculating the charset
        part = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == 'image':
        fp = open(filePath, 'rb')
        part = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == 'audio':
        fp = open(filePath, 'rb')
        part = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(filePath, 'rb')
        part = MIMEBase(maintype, subtype)
        part.set_payload(fp.read())
        fp.close()
        # Encode the payload using Base64
        Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % filePath)
    msg.attach(part)
    try:
        smtp.sendmail(From, To, msg.as_string())
    except:
        print ("Mail not sent")
    else:
        print ("Mail sent")
    smtp.close()
else:
    print ("Connection failed")
