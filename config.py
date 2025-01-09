import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)


class Config:
    DEBUG = True
    SECRET_KEY = config.get("SECRET_KEY")