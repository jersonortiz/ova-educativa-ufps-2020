from files.DTO.DTO import *
from files.util.conexion import Conexion

class pendienteDAO(object):
	"""docstring for pendienteDAO"""
	def __init__(self):
		super(pendienteDAO, self).__init__()

	def insert(self ,pend):
		con = Conexion()
		sql = "INSERT INTO pendiente (id, id_grupo,correo) VALUES (null,%s ,%s)"
		#data=(pend) #pend=([idgr,corr],[idgr,corr])
		data=(pend.id_grupo,pend.correo)
		return con.modify(sql,data)

	def select(self,idu ):
		con = Conexion()
		sql = "SELECT * FROM pendiente where id =%s"
		data=(idu,)
		val= con.find(sql,data)
		if val:
			return pendienteDTO(val[0][0],val[0][1],val[0][2])
		else:
			return False
		
	def delete(self ,idu):
		con = Conexion()
		sql = "DELETE from pendiente where id=%s"
		data=(idu,)
		return con.modify(sql,data)

	def update(self ,user):
		con = Conexion()
		sql = "update pendiente set id_grupo= %s  ,correo= %s where id=%s"
		data=(pend.id_grupo,pend.correo , pend.idp)
		return con.modify(sql,data)

	def listAll(self):
		con = Conexion()
		sql = "select * from pendiente"
		data=None
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(pendienteDTO(x[0],x[1],x[2]))
		return resul

	def findByEmail(self, email):
		con = Conexion()
		sql = "select * from pendiente where email= %s"
		data = (email,)
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(pendienteDTO(x[0],x[1],x[2]))
		return resul

	def findByGrupo(self, idg):
		con = Conexion()
		sql = "select * from pendiente where id_grupo= %s"
		data = (idg,)
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(pendienteDTO(x[0],x[1],x[2]))
		return resul

	def findByEmailAndGrupo(self, idg, email):
		con = Conexion()
		sql = "select * from pendiente where id_grupo= %s and email = %s"
		data = (idg,email)
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(pendienteDTO(x[0],x[1],x[2]))
		return resul