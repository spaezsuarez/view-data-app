from flask import Blueprint

dataRoute = Blueprint('data',__name__,url_prefix = '/data')

from . import dataNetwork