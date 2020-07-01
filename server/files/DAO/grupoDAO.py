from files.DTO.DTO import *
from files.util.conexion import Conexion

class grupoDAO(object):
	"""docstring for grupoDAO"""
	def __init__(self):
		super(grupoDAO, self).__init__()
		
	def insert(self ,grupo):
		con = Conexion()
		sql = "INSERT INTO `grupo` (`id`, `nombre`, `id_docente`) VALUES (NULL, %s, %s)"
		data=(grupo.nombre,grupo.id_docente)
		return con.modify(sql,data)

	def select(self,idu ):
		con = Conexion()
		sql = "SELECT * FROM `grupo` WHERE id = %s"
		data=(idu,)
		val= con.find(sql,data)
		if val:
			return grupoDTO(val[0][0],val[0][1],val[0][2])
		else:
			return False
			
	def findByNombreAndDocente(self,grupo):
		con = Conexion()
		sql = "SELECT * FROM `grupo` WHERE nombre = %s and id_docente = %s"
		data=(grupo.nombre,grupo.id_docente)
		val= con.find(sql,data)
		if val:
			return grupoDTO(val[0][0],val[0][1],val[0][2])
		else:
			return False

	def selectBydocente(self,idd):
		con = Conexion()
		sql = "SELECT * FROM `grupo` WHERE id_docente = %s"
		data=(idd,)
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(grupoDTO(x[0],x[1],x[2]))
		return resul
		
	def delete(self ,idu):
		con = Conexion()
		sql = "DELETE from grupo where id=%s"
		data=(idu,)
		return con.modify(sql,data)

	def update(self ,grupo):
		con = Conexion()
		sql = "update grupo set  `nombre`= %s , `id_docente`= %s  where id=%s"
		data=(grupo.nombre,grupo.id_docente ,grupo.id)
		return con.modify(sql,data)

	def listAll(self):
		con = Conexion()
		sql = "select * from grupo"
		data=None
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(grupoDTO(x[0],x[1],x[2]))
		return resul

	def asignarestudaintegrupo(self , idest,idg):
		con = Conexion()
		sql = "INSERT INTO `grupoestudiante` (`id`, `id_grupo`, `id_estudiante`) VALUES (NULL, %s, %s)"
		data=(idg,idest)
		return con.modify(sql,data)