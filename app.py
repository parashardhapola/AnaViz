from flask import Flask

appObj = Flask(__name__)
appObj.config.from_object(__name__)

appObj.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default',
    ALLOWED_EXTENSIONS=set(['mtx', 'tsv', 'csv'])
))
