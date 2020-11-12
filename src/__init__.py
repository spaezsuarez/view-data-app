from flask import Flask,render_template,redirect
from .routes import dataRoute


def init_app():

    app = Flask(__name__)

    #Configurar Rutas
    app.register_blueprint(dataRoute)

    @app.route('/form',methods=['POST'])
    def load_form():
        return redirect('/data')

    @app.route('/test',methods=['POST'])
    def load():
        return redirect('/data/head')


    @app.route('/')
    def main():
        return render_template('index.html')

   
    return app


