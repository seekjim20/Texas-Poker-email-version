import smtplib
import getpass
import json
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Server:
    def __init__(self, server_addr, port_num, email_addr):
        self._smtp = smtplib.SMTP(server_addr, port_num)
        self._smtp.starttls()
        self._smtp.ehlo()
        self._email_addr = email_addr
        self._password = getpass.getpass('Password : ')
        self._smtp.login(self._email_addr, self._password)
        
    def send_message(self, addr_to, subject, cards):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self._email_addr
        msg['To'] = addr_to
        msg.preamble = 'Your cards'

        msgText = MIMEText('<br>' + ('<img src="cid:image{:d}" width="45%">'*2).format(0, 1)
                           + '<br>', 'html')
        msg.attach(msgText)
        
        for i, card in enumerate(cards):
            with open(card.image_link, 'rb') as fp:
                msgImage = MIMEImage(fp.read())
                msgImage.add_header('Content-ID', '<image{:d}>'.format(i))
                msg.attach(msgImage)

        self._smtp.sendmail(self._email_addr, addr_to, msg.as_string())
        
    def __del__(self):
        self._smtp.quit()
    