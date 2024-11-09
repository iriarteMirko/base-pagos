import pandas as pd
from cryptography.fernet import Fernet

class EncryptionService:
    def __init__(self, key_path='secret.key'):
        self.key = self.load_or_generate_key(key_path)
        self.cipher_suite = Fernet(self.key)
    
    def load_or_generate_key(self, key_path: str) -> bytes:
        try:
            with open(key_path, 'rb') as key_file:
                return key_file.read()
        except FileNotFoundError:
            key = Fernet.generate_key()
            with open(key_path, 'wb') as key_file:
                key_file.write(key)
            return key
    
    def encrypt(self, data: str) -> str:
        try:
            return self.cipher_suite.encrypt(data.encode()).decode()
        except Exception:
            raise ValueError('Error al encriptar los datos')
    
    def decrypt(self, encrypted_data: str) -> str:
        try:
            return self.cipher_suite.decrypt(encrypted_data.encode()).decode()
        except Exception:
            raise ValueError('Error al desencriptar los datos')

class ExcelService:
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def read_sheet(self, sheet_name: str|None = None) -> pd.DataFrame:
        return pd.read_excel(self.file_path, sheet_name=sheet_name)
    
    def write_sheet(self, df: pd.DataFrame, sheet_name: str):
        with pd.ExcelWriter(self.file_path, mode='a', if_sheet_exists='replace') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)

class Correos:
    def __init__(self):
        self.excel_service = ExcelService('email/correos.xlsx')
        self.encryption_service = EncryptionService()
        self.df_credenciales = self.excel_service.read_sheet('Credenciales')
        self.df_destinatarios = self.excel_service.read_sheet('Destinatarios')
    
    @property
    def credenciales(self) -> dict[str, list[str]]:
        encrypted_password = self.df_credenciales['PASSWORD'][0]
        return {
            'EMAIL': self.df_credenciales['EMAIL'][0],
            'PASSWORD': self.encryption_service.decrypt(encrypted_password),
        }
    
    def get_recipients(self, tipo: str|None = None) -> tuple[list[str], list[str]]:
        destinatarios = None
        con_copia = None
        
        for _, row in self.df_destinatarios.iterrows():
            if row['CORREO'] == tipo:
                destinatarios = list(map(str.strip, str(row['DESTINATARIOS']).split(',')))
                con_copia = list(map(str.strip, str(row['CON_COPIA']).split(',')))
        
        if destinatarios == None and con_copia == None:
            raise ValueError(f'No se encontraron destinatarios para el tipo de correo: {tipo}')
        
        return destinatarios, con_copia