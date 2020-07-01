class usuarioDTO:

	def __init__(self,idu,nom,apel ,corr,passw,tip):
		self.idu=str(idu)
		self.nombre=str(nom)
		self.apellido=str(apel)
		self.correo=str(corr)
		self.contraseña=str(passw)
		self.tipo=str(tip)

class temaDTO:

	def __init__(selg,idt,nom):
		self.idt=str(idt)
		self.nombre=str(nom)

class respuestaDTO:

	def __init__(self,idr ,nom,opes,idpre,ides):
		self.idr=str(idr)
		self.puntaje=str(nom)
		self.correcta=str(idpre)
		self.opcion_escogida=str(opes)
		self.id_pregunta=str(idpre)
		self.id_estudiante=str(ides)

class preguntaDTO:

	def __init__(sef,idpre,idtem,conten,resp):
		self.idp=str(idpre)
		self.id_tema=str(idtem)
		self.contenido=str(conten)
		self.respuesta=str(resp)


class pendienteDTO:

	def __init__(self,idpen,idgrup,corr):
		self.idp=str(idpen)
		self.id_grupo=str(idpen)
		self.correo=str(corr)


class grupoDTO:

	def __init__(self,idgru,nom,iddoc):
		self.idg=str(idgru)
		self.nombre=str(nom)
		self.id_docente=str(iddoc)