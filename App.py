"""
- Sergio David Paez Suarez 20191020167
- Miguel Ángel Rico García 20191020107
- Estefany Murillo Torres 20191020123

"""
from src import init_app

app = init_app()

if __name__ == "__main__":
    app.run(port=3000,debug=True)
