from . import dataRoute
from flask import render_template
from src.controllers import test

@dataRoute.route('/',methods=['GET'])
def getData():
    df = test.init_data_frame()
    return render_template('test.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)
