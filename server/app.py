# -*- coding: utf-8 -*- 
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
        asr=auth_token.split("'")[1]
        payload = jwt.decode(asr, 'secret')
        return usuarioDTO(payload['id'],payload['nombre'],payload['apellido'],payload['correo'],'',payload['tipo'])
    except jwt.ExpiredSignatureError as e:
        print(str(e))

        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError as te:
        print(str(te))
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
    user= content.get('user')
    passw= content.get('password')
    u = usuarioDAO()
    usi= u.find(user)
    if usi:
        if usi.correo == user and usi.contraseña == passw:
            token = encode_auth_token(usi)
            print(token)
            return json.dumps({'token':str(token)})


@app.route('/registro',methods=['GET', 'POST'])
def registro():
    print (request.is_json)
    content = request.get_json()

    nombre= content.get('nombre')
    apellido= content.get('apellido')
    correo=content.get('correo')
    contraseña=content.get('contraseña')
    tipo= content.get('tipo')
    usr = usuarioDTO('',nombre,apellido,correo,contraseña,tipo)

    u = usuarioDAO()

    if u.find(correo):
        return json.dumps({'status':'existe'})
    elif u.insert(usr): 
        return json.dumps({'status':'registered'})
    else:
        return json.dumps({'status':'fail'})

@app.route('/responder',methods=['GET', 'POST'])
def responder():
    print (request.is_json)
    content = request.get_json()
    token = request.headers['Authorization']
    user = decode_auth_token(token)
    respuestas=content.get('respuestas')
    puntaje= content.get('puntaje')
    print(str(content))
    val=[]
    for x in respuestas:
        bdid=x['bdkey']
        key=x['key']
        resp=-1
        correcta=0
        if 'resp' in x:
            resp= x['resp']
            if str(resp)==str(key) :
                correcta = 1
        val.append((int(puntaje),int(correcta),resp,int(bdid),int(user.idu)))
    p= respuestaDAO()
    if p.multyinsert(val):
        return json.dumps({'status':'guardado'})
    else:
        return json.dumps({'status':'fail'})


@app.route('/grupos',methods=['GET', 'POST'])
def lista_grupos():
    token = request.headers['Authorization']
    user = decode_auth_token(token)
    gd= grupoDAO()
    grupos=gd.selectBydocente(user.idu)
    listg=[]
    for g in grupos:
        listg.append({'id':g.idg , 'nombre':g.nombre ,'id_docente':g.id_docente})
    ret ={'grups':listg}
    return json.dumps(ret)

@app.route('/estudiantesgrupo',methods=['GET', 'POST'])
def lista_estudiantes_grupo():
    token = request.headers['Authorization']
    user = decode_auth_token(token)
    content = request.get_json()
    idg=content.get('idg')
    ud= usuarioDAO()
    estudiantes=ud.listStudentsByGrupo(idg)
    listg=[]
    for est in estudiantes:
        listg.append({
            'id':est.idu,
            'nombre':est.nombre,
            'apellido':est.apellido,
            'correo':est.correo
            })
    ret ={'estudents':listg}
    return json.dumps(ret)

@app.route('/creargrupo',methods=['GET', 'POST'])
def crear_grupo():
    token = request.headers['Authorization']
    user = decode_auth_token(token)
    content = request.get_json()
    nom=content.get('nombre')
    grupo = grupoDTO('',nom,user.idu)
    gd= grupoDAO()
    if gd.findByNombreAndDocente(grupo):
        return json.dumps({'status':'existe'})
    elif gd.insert(grupo): 
        return json.dumps({'status':'registered'})
    else:
        return json.dumps({'status':'fail'})

@app.route('/pruebamsj',methods=['GET', 'POST'])
def prmsj():
    return json.dumps({'status':'existe'})

@app.route('/respuestasestudiante',methods=['GET', 'POST'])
def respuestas_estudiante():
    token = request.headers['Authorization']
    user = decode_auth_token(token)
    content = request.get_json()
    nom=content.get('idest')
    tem=content.get('tema')
    pd=preguntaDAO()
    pregs = pd.listTodoEstudiante(nom,tem)
    retorno = []
    for preg in pregs:
        print(str(preg))
        pregunta = preg[1].split("%d%")
        print(str(pregunta))
        arreglo = []
        for x in range (1,len(pregunta)):
            arreglo.append(pregunta[x])
        contenido = {'enunciado':pregunta[0],'opciones':arreglo} 
        retorno.append({'id':preg[0],'pregunta':contenido,'respuesta':str(preg[2]) , 'escogido':preg[3] ,'correcto': preg[4] })
    ret ={'preguntas':retorno}
    return json.dumps(ret)
         

@app.route('/cargardocentes',methods=['GET', 'POST'])
def cargar_docentes():
    token = request.headers['Authorization']
    user = decode_auth_token(token)
    content = request.get_json()
    u = usuarioDAO()
    docs= u.listDocentes()
    arreglo = []
    for x in docs:
        arreglo.append({'id':x.idu,'nombre':x.nombre,'apellido':x.apellido,'correo':x.correo})
    ret ={'docs':arreglo}
    return json.dumps(ret)

@app.route('/gruposdocente',methods=['GET', 'POST'])
def cargar_grupos():
    token = request.headers['Authorization']
    user = decode_auth_token(token)
    content = request.get_json()
    iddoc=content.get('docente')
    gd= grupoDAO()
    grupos=gd.selectBydocente(iddoc)
    arreglo = []
    for x in grupos:
        arreglo.append({'id':x.idg,'nombre':x.nombre,'id_docente':x.id_docente})
    ret ={'grup':arreglo}
    return json.dumps(ret)


@app.route('/asignargrupo',methods=['GET', 'POST'])
def asignar_estudiante_grupo():
    token = request.headers['Authorization']
    user = decode_auth_token(token)
    content = request.get_json()
    grup=content.get('grupo')
    iddoc=content.get('docente')
    userdat=content.get('user')
    print('user')
    print(userdat)
    gd= grupoDAO()
    if gd.asignarestudaintegrupo(userdat,grup): 
        return json.dumps({'status':'registered'})
    else:
        return json.dumps({'status':'fail'})

if __name__ == "__main__":
	app.run(debug=True, port=5000)