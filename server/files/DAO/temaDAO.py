from files.DTO.DTO import *
from files.util.conexion import Conexion

class temaDAO(object):
	"""docstring for temaDAO"""
	def __init__(self):
		super(temaDAO, self).__init__()
		
	def insert(self ,tema):
		con = Conexion()
		sql = "INSERT INTO tema (id, nombre) VALUES (null,%s )"
		data=(tema.nombre,)
		return con.modify(sql,data)
	
	def select(self,idu ):
		con = Conexion()
		sql = "SELECT * FROM tema where id = %s"
		data = (idu,)
		val= con.find(sql,data)
		if val:
			return temaDTO(val[0][0],val[0][1],)
		else:
			return False
		
	def delete(self ,idu):
		con = Conexion()
		sql = "DELETE from tema where id= %s "
		data = (idu,)
		return con.modify(sql,data)

	def update(self ,user):
		con = Conexion()
		sql = "update tema set nombre= %s  where id=%s"
		data=(tema.nombre, tema.idt)
		return con.modify(sql,data)

	def listAll(self):
		con = Conexion()
		sql = "select * from tema"
		data= None
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(temaDTO(x[0],x[1]))
		return resul