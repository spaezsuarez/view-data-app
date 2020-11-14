from . import dataRoute
from flask import render_template,request
from src.utils import dataManagment
import pprint as p

@dataRoute.route('/',methods=['GET'])
def getData():
    df = dataManagment.init_data_frame()
    return render_template('data.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

@dataRoute.route('/head',methods=['POST'])
def create_head():
    number = request.form['number']
    df = dataManagment.data_frame_head(number)
    return render_template('data.html',tables=[df.to_html(classes='data')], titles=df.columns.values)

@dataRoute.route('/sex/country',methods=['POST'])
def create_second_request():
    sexo = request.form.get('selection-sex')
    pais = request.form.get('selection-country')
    df = dataManagment.get_sex_country_deaths(pais,sexo)
    return render_template('data.html',tables=[df.to_html(classes='data')], titles=df.columns.values)