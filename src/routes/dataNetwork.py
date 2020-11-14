from . import dataRoute
from flask import render_template,request
from src.utils import dataManagment
import dateutil
import datetime

@dataRoute.route('/head',methods=['POST'])
def create_head():
    number = request.form['number']
    df = dataManagment.data_frame_head(number)
    return render_template('data.html',tables=[df.to_html()])

@dataRoute.route('/sex/country',methods=['POST'])
def create_second_request():
    sexo = request.form.get('selection-sex')
    pais = request.form.get('selection-country')
    df = dataManagment.get_sex_country_deaths(pais,sexo)
    return render_template('data.html',tables=[df.to_html()])

@dataRoute.route('/country/dates',methods=['POST'])
def create_third_request():
    firstDate =  dateutil.parser.parse(request.form.get('firstDate'),dayfirst=False) #Datetime
    secondDate =  dateutil.parser.parse(request.form.get('secondDate'),dayfirst=False)
    firstDate = datetime.date(firstDate.year,firstDate.month,firstDate.day)
    secondDate = datetime.date(secondDate.year,secondDate.month,secondDate.day)
    pais = request.form.get('selection-country')
    df = dataManagment.get_country_dates(pais,firstDate,secondDate)
    return render_template('data.html',tables=[df.to_html()])

@dataRoute.route('/count/country',methods=['POST'])
def create_fourth_request():
    sexo = request.form.get('selection-sex')
    df = dataManagment.get_contagios_por_pais(sexo)
    return render_template('data.html',tables=[df.to_html()]) 