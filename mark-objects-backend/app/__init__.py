from flask import Flask
from flask_cors import CORS

from app.routes.api import api

app = Flask(__name__, static_folder='../build', static_url_path='/')

CORS(app, expose_headers=["Content-Disposition"])

app.register_blueprint(api, url_prefix="/api")


@app.route('/')
@app.route('/report')
def index():
    return app.send_static_file('index.html')
