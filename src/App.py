from flask import Flask, render_template
from routes import dataRoute, formRoute

app = Flask(__name__)

# Configurar Rutas
app.register_blueprint(dataRoute)
app.register_blueprint(formRoute)

#Ruta por defecto
@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port = 3000, debug = True)
