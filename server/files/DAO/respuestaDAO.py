from files.DTO.DTO import *
from files.util.conexion import Conexion

class  respuestaDAO(object):
	"""docstring for respuestaDAO"""
	def __init__(self):
		super(respuestaDAO, self).__init__()

	def insert(self ,respuesta):
		con = Conexion()
		sql = "INSERT INTO `respuesta` (`id`, `puntaje`, `correcta`, `opcion_escogida`, `id_pregunta`, `id_estudiante`) VALUES (NULL, '%s', '%s', '%s', '%s', '%s')"
		val=(respuesta.puntaje,respuesta.correcta,respuesta.opcion_escogida,respuesta.id_pregunta,respuesta.id_estudiante)
		return con.modify(sql,val)
	
	def multyinsert(self,resp):
		con = Conexion()
		sql = "INSERT INTO `respuesta` (`id`, `puntaje`, `correcta`, `opcion_escogida`, `id_pregunta`, `id_estudiante`) VALUES (NULL, %s, %s,%s, %s, %s)"
		print(str(resp))
		return con.many(sql,resp)

	def select(self,idu ):
		con = Conexion()
		sql = "SELECT * FROM `respuesta` WHERE id =%s"
		data=(idu,)
		val= con.find(sql,data)
		if val:
			return respuestaDTO(val[0][0],val[0][1],val[0][2],val[0][3],val[0][4],val[0][5])
		else:
			return False
		
	def delete(self ,idu):
		con = Conexion()
		sql = "DELETE from respuesta where id=%s"
		data=(idu,)
		return con.modify(sql,data)

	def update(self ,respuesta):
		con = Conexion()
		sql = "update respuesta set  `puntaje`= %s , `correcta`= %s , `opcion_escogida`= %s , where id=%s"
		data=(respuesta.puntaje,respuesta.correcta,respuesta.opcion_escogida ,respuesta.idr)
		return con.modify(sql,data)

	def listAll(self):
		con = Conexion()
		sql = "select * from respuesta"
		data=None
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(respuestaDTO(x[0],x[1],x[2],x[3],x[4],x[5]))
		return resul

	def listByPregunta(selfidp):
		con = Conexion()
		sql = "select * from respuesta WHERE id_pregunta = %s"
		data=(selfidp,)
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(respuestaDTO(x[0],x[1],x[2],x[3],x[4],x[5]))
		return resul

	def listByEstudiante(self, ide):
		con = Conexion()
		sql = "select * from respuesta WHERE  id_estudiante = %s"
		data=(ide,)
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(respuestaDTO(x[0],x[1],x[2],x[3],x[4],x[5]))
		return resul

	def listByEstudianteAndTema(self, ide, numtema):
		con = Conexion()
		sql = "SELECT r.* FROM respuesta r, tema t,pregunta p WHERE p.id_tema= t.id and r.id_pregunta=p.id and t.id= %s and r.id_estudiante=%s"
		data= (numtema,ide)
		val= con.find(sql,data)
		resul=[]
		for x in val:
			resul.append(respuestaDTO(x[0],x[1],x[2],x[3],x[4],x[5]))
		return resul