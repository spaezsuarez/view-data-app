from . import dataRoute
from flask import render_template
from src.controllers import dataManagment

@dataRoute.route('/',methods=['GET'])
def getData():
    df = dataManagment.init_data_frame()
    return render_template('data.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

@dataRoute.route('/head',methods=['GET'])
def getHead():
    df = dataManagment.data_frame_head()
    return render_template('data.html',tables=[df.to_html(classes='data')], titles=df.columns.values)