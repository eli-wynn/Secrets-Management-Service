from cryptography.fernet import Fernet
from app.core.config import settings

fernet = Fernet(settings.SECRET_KEY.encode())

def encrypt(value: str) -> str:
    return fernet.encrypt(value.encode()).decode()

def decrypt(token: str) -> str:
    return fernet.decrypt(token.encode()).decode()
