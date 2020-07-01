from files.DTO.DTO import *
from files.util.conexion import Conexion

class usuarioDAO(object):
	"""docstring for usuarioDAO"""
	def __init__(self):
		super(usuarioDAO, self).__init__()

	def insert(self ,user):
		con = Conexion()
		sql = "INSERT INTO usuario (id, nombre,apellido,correo,contraseña,tipo) VALUES (null,%s ,%s,%s,%s,%s)"
		data =(user.nombre , user.apellido , user.correo , user.contraseña , user.tipo)
		return con.modify(sql,data)
	
	def select(self,idu ):
		con = Conexion()
		sql = "SELECT * FROM usuario where id = %s"
		data= (idu,)
		val= con.find(sql,data)
		if val:
			return usuarioDTO(val[0][0],val[0][1],val[0][2],val[0][3],val[0][4],val[0][5])
		else:
			return False

	def find(self,idu ):
		con = Conexion()
		sql = "SELECT * FROM usuario where correo = %s"
		data= (idu,)
		val= con.find(sql,data)
		if val:
			print(str(val))
			return usuarioDTO(val[0][0],val[0][1],val[0][2],val[0][3],val[0][4],val[0][5])
		else:
			return False
		
	def delete(self ,idu):
		con = Conexion()
		sql = "DELETE from usuario where id= %s"
		data= (idu,)
		return con.modify(sql,data)

	def update(self ,user):
		con = Conexion()
		sql = "update usuario set nombre= %s ,apellido= %s ,correo = %s ,contraseña= %s ,tipo= %s where id=%s"
		data=(user.nombre,user.apellido,user.correo,user.contraseña,user.tipo,user.idu)
		return con.modify(sql,data)

	def listAll(self):
		con = Conexion()
		sql = "select * from usuario"
		data = None
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(usuarioDTO(x[0],x[1],x[2],x[3],x[4],x[5]))
		return resul
		
	def listStudentsByGrupo(self,idg):
		con = Conexion()
		sql = "SELECT u.* FROM usuario u , grupoestudiante ge WHERE u.id=ge.id_estudiante AND ge.id_grupo = %s"
		data=(idg,)
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(usuarioDTO(x[0],x[1],x[2],x[3],x[4],x[5]))
		return resul

	def listStudentsByDocente(self,iddo):
		con = Conexion()
		sql = "SELECT u.* FROM usuario u , grupoestudiante ge , grupo g WHERE  u.id= ge.id_estudiante and ge.id_grupo = g.id and g.id_docente= %s"
		data=(iddo,)
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(usuarioDTO(x[0],x[1],x[2],x[3],x[4],x[5]))
		return resul

	def listStudentsByDocenteAndGrupo(self ,iddoc, idg):
		con = Conexion()
		sql = "SELECT u.* FROM usuario u , grupoestudiante ge , grupo g WHERE u.id=ge.id_estudiante  and ge.id_grupo = g.id  AND ge.id_grupo = %s and g.id_docente= %s"
		data=(idg,iddoc)
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(usuarioDTO(x[0],x[1],x[2],x[3],x[4],x[5]))
		return resul

	def listDocentes(self):
		con = Conexion()
		sql = "select * from usuario where tipo=2"
		data = None
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(usuarioDTO(x[0],x[1],x[2],x[3],x[4],x[5]))
		return resul