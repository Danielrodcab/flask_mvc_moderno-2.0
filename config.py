import os

class Configuracion:
    CLAVE_SECRETA = os.environ.get('SECRET_KEY') or 'secreto'
    
    # Prioridad 1: Variable de Railway (DATABASE_URL)
    # Prioridad 2: SQLite local (si no hay variable configurada)
    uri = os.environ.get('DATABASE_URL')
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
        
    SQLALCHEMY_DATABASE_URI = uri or 'sqlite:///basededatos.db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
