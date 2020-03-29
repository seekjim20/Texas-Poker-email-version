import smtplib
import getpass
import json
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Server:
    def __init__(self, host, port, user):
        self._host = host
        self._port = port
        self._user = user
        self._password = getpass.getpass('Password : ')
        self.connect()

    def connect(self):
        self._smtp = smtplib.SMTP(self._host, self._port)
        self._smtp.ehlo()
        self._smtp.starttls()
        self._smtp.ehlo()
        self._smtp.login(self._user, self._password)
        
    def send_message(self, addr_to, subject, cards):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self._user
        msg['To'] = addr_to
        msg.preamble = 'Your cards'

        msg.attach(MIMEText(
            '<br>' + 
            '<font size="+3">{}</font>'.format(subject) +
            '<br>' +
            ('<img src="cid:image{:d}" width="45%">'*2).format(0, 1) +
            '<br>'
        , 'html'))
        
        for i, card in enumerate(cards):
            with open(card.image_link, 'rb') as fp:
                msgImage = MIMEImage(fp.read())
                msgImage.add_header('Content-ID', '<image{:d}>'.format(i))
                msg.attach(msgImage)

        for trial in range(3):
            try:
                self._smtp.sendmail(self._user, addr_to, msg.as_string())
                break
            except SMTPRecipientsRefused:
                self.connect()
            
    def __del__(self):
        self._smtp.quit()
    