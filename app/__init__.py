from flask import Flask
from config import Config
import os

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)

app.config['09053361954'] = os.environ.get("09053361954")


from app.routes import *