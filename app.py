from src import init_app, db
from config import config

configuracion = config['development']

app, db = init_app(configuracion)

if __name__ == '__main__':
    app.run()
    