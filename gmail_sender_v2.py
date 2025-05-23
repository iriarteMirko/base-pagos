import smtplib
from jinja2 import Environment, FileSystemLoader
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import os

class GmailSender:
    def __init__(self, sender_email: str, password: str):
        self.sender_email = sender_email
        self.password = password
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587
        self.env = Environment(loader=FileSystemLoader('templates'))
    
    def send_email(self, recipient_emails: list, subject: str, body: dict, cc_emails: list = None, files: list = None):
        """ Envía un correo electrónico a los destinatarios especificados. """
        
        # Verificar el número total de destinatarios
        all_recipients = recipient_emails + (cc_emails if cc_emails else [])
        if len(all_recipients) > 500:
            print('El número total de destinatarios excede el límite de 500. Dividiendo en lotes...')
            self._send_in_batches(recipient_emails, subject, body, cc_emails, files)
        else:
            self._send_single_email(recipient_emails, subject, body, cc_emails, files)
    
    def _send_single_email(self, recipient_emails: list, subject: str, body: dict, cc_emails: list = None, files: list = None):
        msg = MIMEMultipart() # Mensaje
        
        msg['From'] = self.sender_email # Remitente
        msg['To'] = ', '.join(recipient_emails) # Destinatarios
        msg['Subject'] = subject # Asunto
        
        # Destinararios en copia
        if cc_emails:
            msg['CC'] = ', '.join(cc_emails)
        
        # Cuerpo del correo
        template = self.env.get_template('email_body.html')
        body_html = template.render(body)
        
        msg_alternative = MIMEMultipart('alternative')
        msg.attach(msg_alternative)
        
        msg_text = MIMEText(body_html, 'html')
        msg_alternative.attach(msg_text)
        
        # Firma
        try:
            with open('static/images/firma_bbva.gif', 'rb') as img:
                msg_image = MIMEImage(img.read())
                msg_image.add_header('Content-ID', '<signature_image>')
                msg.attach(msg_image)
        except Exception as e:
            print(f'Error adjuntando la imagen de firma: {str(e)}')
        
        # Archivos adjuntos
        if files:
            for file in files:
                try:
                    with open(file, 'rb') as attachment:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file)}')
                    msg.attach(part)
                except Exception as e:
                    print(f'Error adjuntando el archivo {file}: {str(e)}')
        
        # Enviar correo
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.password)
            all_recipients = recipient_emails + (cc_emails if cc_emails else [])
            server.sendmail(self.sender_email, all_recipients, msg.as_string())
            print('Correo enviado exitosamente.')
        except Exception as e:
            print(f'Error al enviar el correo: {str(e)}')
        finally:
            server.quit()
    
    def _send_in_batches(self, recipient_emails: list, subject: str, body: dict, cc_emails: list = None, files: list = None):
        all_recipients = recipient_emails + (cc_emails if cc_emails else [])
        batch_size = 500
        for i in range(0, len(all_recipients), batch_size):
            batch_recipients = all_recipients[i:i + batch_size]
            self._send_single_email(batch_recipients, subject, body, cc_emails=None, files=files)