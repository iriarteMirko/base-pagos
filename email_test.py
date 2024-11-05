from gmail_sender import GmailSender
from dotenv import load_dotenv
import os

class EmailTest:
    def __init__(self, file_path: str,):
        load_dotenv()
        self.file_path = file_path
        self.sender_email = os.getenv('GMAIL')
        self.password = os.getenv('PASSWORD')
        self.recipients_emails = os.getenv('RECIPIENTS_TEST').split(', ')
        self.cc_emails = os.getenv('CC_TEST').split(', ')
        self.gmail_sender = GmailSender(self.sender_email, self.password)
    
    def enviar_correo(self):
        subject = f'Test email subject'
        body = {
            'body_msg': 'Test message',
            'firma': 'Mirko',
        }
        files = [self.file_path]
        
        self.gmail_sender.send_email(recipient_emails=self.recipients_emails, subject=subject, body=body, cc_emails=self.cc_emails, files=files)


def main():
    file_path = 'C://Users//p042833//Documents//GitHub//base-pagos//src//test//test_file.txt'
    email_test = EmailTest(file_path)
    email_test.enviar_correo()

if __name__ == '__main__':
    main()