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

@formRoute.route('/5')
def get_fifth_form():
    return render_template('form.html',state=5)

@formRoute.route('/6')
def get_sixth_form():
    return render_template('form.html',state=6)

@formRoute.route('/7')
def get_seventh_form():
    return render_template('form.html',state=7)