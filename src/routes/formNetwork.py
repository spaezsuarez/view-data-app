from . import formRoute
from flask import render_template,request,redirect

@formRoute.route('/1',methods=['GET'])
def get_first_form():
    return render_template('form.html',state=1)

@formRoute.route('/2',methods=['GET'])
def get_second_form():
    return render_template('form.html',state=2)
