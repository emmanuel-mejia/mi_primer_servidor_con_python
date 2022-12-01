from jinja2 import Environment
from jinja2 import FileSystemLoader

from wsgiref.simple_server import make_server

env = Environment(loader=FileSystemLoader('templates'))

def aplication(environ, start_response): # Interfaz - WSGI 
    status = '200 OK'

    context = {
        'username': 'Cody',
        'courses': ['Python', 'Django', 'Flask', 'Base de datos']
    }
    
    path = environ.get('PATH_INFO')
    
    if path == '/':
        template = env.get_template('index.html')
    
    elif path == '/users':
        template = env.get_template('users.html')
    
    response = template.render(**context)
    start_response(status, []) # MetaData
    return [ bytes(response, 'UTF-8') ] # Respuesta al cliente


PORT = 4000

with make_server('localhost', PORT, aplication) as server:
    print(f">>> El servidor se encuentra a la escucha en el puerto {PORT}")
    server.serve_forever()

