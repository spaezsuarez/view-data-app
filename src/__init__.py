from flask import Flask,render_template,redirect
from .routes import dataRoute,formRoute


def init_app():

    app = Flask(__name__)

    #Configurar Rutas
    app.register_blueprint(dataRoute)
    app.register_blueprint(formRoute)

    @app.route('/first-form',methods=['POST'])
    def load_first_form():
        return redirect('/form/1')

    @app.route('/second-form',methods=['POST'])
    def load_second_form():
        return redirect('/form/2')

    @app.route('/test',methods=['POST'])
    def load():
        return redirect('/data/head')


    @app.route('/')
    def main():
        return render_template('index.html')

   
    return app


