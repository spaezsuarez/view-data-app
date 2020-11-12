"""
- Sergio David Paez Suarez 20191020167
- Miguel Ángel Rico García 20191020107
- Estefany Murillo Torres 20191020123

"""

from flask import Flask,render_template
from routes import dataRoute

app = Flask(__name__)

#Configurar Rutas
app.register_blueprint(dataRoute)

@app.route('/')
def main():
    return render_template('index.html',name='Mundo')

if __name__ == "__main__":
    app.run(port=4000,debug=True)
