class Persona(object):
	def __init__(self,nom, nota1, nota2, nota3):
		self.nombre = nom
		self.nota1 = not1
		self.nota2 = not2
		self.nota3 = not3 
	
	def agregarnombre(self,nom):
		self.nombre = nom
	def obtenernombre(self):
		return self.nombre
	def agregarnota1(self,not1):
		self.nota1 = not1
	def obtenernota1(self):
		return self.nota1
	def agregarnota2(self,not2):
		self.nota2 = not2
	def obtenernota2(self):
		return self.nota2
	def agregarnota3(self,not3):
		self.nota3 = not3
	def obtenernota3(self):
		return self.nota3

	def prom(self):
		prom = (self.nota1 + self.nota2 + self.nota3)/3
		return prom

	def __str__(self):
		return "Nombre: %s | Promedio: %.2f" % (self.nombre(),self.prom())