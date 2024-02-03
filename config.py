import secrets

clave_secreta = secrets.token_hex(24)

class DevelopmentConfig:
    DEBUG = True
    SECRET_KEY = 'clave_secreta'

# Diccionario de configuración
config = {
    'development': DevelopmentConfig
}
