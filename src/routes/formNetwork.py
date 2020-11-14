from . import formRoute
from flask import render_template,request,redirect

@formRoute.route('/1')
def get_first_form():
    return render_template('form.html',state=1)

@formRoute.route('/2')
def get_second_form():
    return render_template('form.html',state=2)

@formRoute.route('/3')
def get_third_form():
    return render_template('form.html',state=3)

@formRoute.route('/4')
def get_fourth_form():
    return render_template('form.html',state=4)