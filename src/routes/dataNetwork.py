from . import dataRoute
from flask import render_template,request
from src.utils import dataManagment

@dataRoute.route('/',methods=['GET'])
def getData():
    df = dataManagment.init_data_frame()
    return render_template('data.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

@dataRoute.route('/head',methods=['POST'])
def getHead():
    number = request.form['number']
    df = dataManagment.data_frame_head(number)
    return render_template('data.html',tables=[df.to_html(classes='data')], titles=df.columns.values)