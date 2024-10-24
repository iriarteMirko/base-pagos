from gmail_sender import GmailSender
from dotenv import load_dotenv
import os

class CorreoMultiproducto:
    def __init__(self, fecha: str, file_path: str, hora_formateada: str):
        load_dotenv()
        self.fecha = fecha
        self.file_path = file_path
        self.hora_formateada = hora_formateada
        self.sender_email = os.getenv('GMAIL')
        self.password = os.getenv('PASSWORD')
        self.recipients_emails = os.getenv('MULTIPRODUCTO_test').split(', ')
        self.cc_emails = os.getenv('CC_MULTIPRODUCTO_test').split(', ')
        self.gmail_sender = GmailSender(self.sender_email, self.password)
    
    def enviar_correo(self):
        subject = f'MULTIPRODUCTO {self.fecha}'
        body = {
            'body_msg': 'Multiproducto',
            'hora': self.hora_formateada,
            'firma': 'Mirko',
        }
        files = [f'{self.file_path}/MULTIPRODUCTO {self.fecha}.xlsx', f'{self.file_path}/REACTIVA {self.fecha}.xlsx']
        
        self.gmail_sender.send_email(recipient_emails=self.recipients_emails, subject=subject, body=body, cc_emails=self.cc_emails, files=files)