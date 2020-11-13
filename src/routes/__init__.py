from flask import Blueprint

dataRoute = Blueprint('data',__name__,url_prefix = '/data')
formRoute = Blueprint('forms',__name__,url_prefix='/form')

from . import dataNetwork
from . import formNetwork