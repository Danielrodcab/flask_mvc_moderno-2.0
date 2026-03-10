import os

class Configuracion:
    CLAVE_SECRETA = os.environ.get('SECRET_KEY') or 'secreto'
    
    uri = os.environ.get('DATABASE_URL')
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
        
    SQLALCHEMY_DATABASE_URI = uri or 'sqlite:///basededatos.db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
