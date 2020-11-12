from . import dataRoute

@dataRoute.route('/',methods=['GET'])
def getData():
    return 'Hola Data'
