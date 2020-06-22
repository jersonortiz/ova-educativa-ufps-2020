from flask import Flask, request ,make_response
from flask_cors import CORS
from files.DTO.DTO import *
from files.DAO.grupoDAO import grupoDAO
from files.DAO.pendienteDAO import pendienteDAO
from files.DAO.preguntaDAO import preguntaDAO
from files.DAO.respuestaDAO import respuestaDAO
from files.DAO.temaDAO import temaDAO
from files.DAO.usuarioDAO import usuarioDAO
from files.util.conexion import Conexion
import datetime
import json
import jwt

def encode_auth_token(user):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'id': user.idu,
            'nombre': user.nombre,
            'apellido': user.apellido,
            'correo': user.correo,
            'tipo': user.tipo
        }

        return jwt.encode(
            payload,
            'secret',
            algorithm='HS256'
            )
    except Exception as e:
        return e

def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, 'secret')
        return usuarioDTO(payload['id'],payload['nombre'],payload['apellido'],payload['correo'],'',payload['tipo'])
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

def validate_auth_token(auth_token):
    payload = jwt.decode(auth_token, 'secret')
    a = datetime.now()
    a = int(a.strftime('%Y%m%d'))
    if(a< int(payload['exp'])):
        return True
    return False


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
 	return 'Hello, World!'

@app.route('/login',methods=['GET', 'POST'])
def login():
    print (request.is_json)
    content = request.get_json()
    #content = json.loads(request.get_json())
    user= content.get('user')
    passw= content.get('password')
    #return passw
    u = usuarioDAO()
    us1= u.find(user)
    if us1:
        if us1.correo == user and us1.contraseña == passw:
            token = encode_auth_token(us1)
            print(token)
            #return token
            return json.dumps({'token':str(token)})


@app.route('/registro',methods=['GET', 'POST'])
def registro():
    print (request.is_json)
    content = json.loads(request.get_json())
    usr=content['name']
    print(usr)
    u = usuarioDAO()

    if u.select(usr):
        return json.dumps({'status':'existe'})
    elif u.insert(usr): 
        return json.dumps({'status':'registered'})
    else:
        return json.dumps({'status':'fail'})


if __name__ == "__main__":
	app.run(debug=True, port=5000)