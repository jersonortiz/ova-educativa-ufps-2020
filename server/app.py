from flask import Flask, request
from files.DTO.DTO import *
from files.DAO.grupoDAO import grupoDAO
from files.DAO.pendienteDAO import pendienteDAO
from files.DAO.preguntaDAO import preguntaDAO
from files.DAO.respuestaDAO import respuestaDAO
from files.DAO.temaDAO import temaDAO
from files.DAO.usuarioDAO import usuarioDAO
from files.util.conexion import Conexion
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
 	return 'Hello, World!'

@app.route('/login',methods=['GET', 'POST'])
def login():
    print (request.is_json)
    content = json.loads(request.get_json())
    print (content)
    print(content['name'])
    u = usuarioDAO()
    us1= u.select(content['name'])
    if us1:
        print(str(us1))
        print(json.dumps({'status':'unknow'}))

        if len(us1.nombre) is 0:
            return json.dumps({'status':'unknow'})
        return json.dumps({'status':'logged'})

    return 'ola'


    


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

@app.route('/list',methods=['GET', 'POST'])
def listas():
    #print (request.is_json)
    content = json.loads(request.get_json())
    #print (content)

    u = usuarioDAO()
    us1= u.select(content['name'])
    #print(str(us1))

    l = listaDAO()
    ls1 = l.select(us1.idu)
    #print(str(ls1))

    c = cancionDAO()
    cs1 = c.select(ls1.lid)
    #print(str(cs1[0]))

    date= []

    for x in cs1:
        se = { 
            'name': x.nombre,
            'file':x.archivo
            }
        date.append(se)

    return json.dumps(date)




if __name__ == "__main__":
	app.run(debug=True, port=5000)