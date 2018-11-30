#UTILIZACION DE EXCEPCIONES

#edad = input("ingrese la edad porfavor:\n ")
#edad = int (edad)
#edad2= input("Ingrese la edad2 porfavor: \n")


try:
	edad = input ("Ingrese su edad:\n")
	edad = int(edad)
	print("Su edad es%d: % "(edad))
except NameError as e:
	print("Existe un error:%s" % e)
except ValueError as e:
	print("Existe un error:(%s):%s" % (e. __class__, e))
#except Exception as e:
#	print("Existe un error:(%s):%s" % (e. __class__, e))

