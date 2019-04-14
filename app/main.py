import os

import waitress
from flask import Flask

def start():
    app = Flask(__name__)


    @app.route('/')
    def hello_world():
        return 'Hello World!'

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9866, debug=True)


if __name__ == '__main__':
    start()
