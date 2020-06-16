from files.DTO.DTO import *
from files.util.conexion import Conexion

class preguntaDAO(object):
	"""docstring for preguntaDAO"""
	def __init__(self, arg):
		super(preguntaDAO, self).__init__()

	def insert(self ,pregunta):
		con = Conexion()
		sql = "INSERT INTO pregunta (id, id_tema) VALUES (null,%s)"
		data=(pregunta.id_tema, )
		return con.modify(sql,data)

	def select(self,idu ):
		con = Conexion()
		sql = "SELECT * FROM pregunta where id = %s"
		data=(idu,)
		val= con.find(sql,data)
		if val:
			return preguntaDTO(val[0][0],val[0][1])
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
			resul.append(usuarioDTO(x[0],x[1]))
		return resul

	def listByTema(self, numtema):
		con = Conexion()
		sql = "select * from pregunta where id_tema= %s"
		data = (numtema,)
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(usuarioDTO(x[0],x[1]))
		return resul