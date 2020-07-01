from files.DTO.DTO import *
from files.util.conexion import Conexion

class preguntaDAO(object):
	"""docstring for preguntaDAO"""
	def __init__(self):
		super(preguntaDAO, self).__init__()

	def insert(self ,pregunta):
		con = Conexion()
		sql = "INSERT INTO pregunta (id, id_tema, contenido ,respuesta) VALUES (null,%s,%s,%s)"
		data=(pregunta.id_tema,pregunta.contenido,pregunta.respuesta )
		return con.modify(sql,data)

	def select(self,idu ):
		con = Conexion()
		sql = "SELECT * FROM pregunta where id = %s"
		data=(idu,)
		val= con.find(sql,data)
		if val:
			return preguntaDTO(val[0][0],val[0][1],val[0][2],val[0][3])
		else:
			return False
		
	def delete(self ,idu):
		con = Conexion()
		sql = "DELETE from pregunta where id=%s"
		data=(idu,)
		return con.modify(sql,data)

	def update(self ,user):
		con = Conexion()
		sql = "update pregunta set id_tema= %s  where id=%s"
		data=(pregunta.id_tema, pregunta.idp)
		return con.modify(sql,data)

	def listAll(self):
		con = Conexion()
		sql = "select * from pregunta"
		data=None
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(preguntaDTO(x[0],x[1],x[2],x[3]))
		return resul

	def listByTema(self, numtema):
		con = Conexion()
		sql = "select * from pregunta where id_tema= %s"
		data = (numtema,)
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(preguntaDTO(x[0],x[1],x[2],x[3]))
		return resul

	def listTodoEstudiante(self , ide , idt ): 
		con = Conexion()
		sql = "SELECT p.id, p.contenido , p.respuesta , r.opcion_escogida, r.correcta FROM pregunta p , respuesta r, tema t WHERE r.id_pregunta = p.id and p.id_tema = t.id and r.id_estudiante = %s AND t.id = %s ORDER BY p.id"
		data = (ide,idt)
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append([x[0] ,x[1], x[2],x[3],x[4]])	
		return resul