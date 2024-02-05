from config import config
from src import init_app

configuracion = config['development']
app = init_app(configuracion)

if __name__ == '__main__':
    app.run()
    