from flask import Flask, render_template, redirect
from routes import dataRoute, formRoute

app = Flask(__name__)

# Configurar Rutas
app.register_blueprint(dataRoute)
app.register_blueprint(formRoute)


@app.route('/first-form', methods=['GET'])
def load_first_form():
    return redirect('/form/1')


@app.route('/second-form', methods=['GET'])
def load_second_form():
    return redirect('/form/2')


@app.route('/third-form', methods=['GET'])
def load_third_form():
    return redirect('/form/3')


@app.route('/fourth-form', methods=['GET'])
def load_fourth_form():
    return redirect('/form/4')

@app.route('/fifth-form', methods=['GET'])
def load_fifth_form():
    return redirect('/form/5')


@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port = 3000, debug = True)
