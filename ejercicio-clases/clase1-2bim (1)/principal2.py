#UTILIZACION DE EXCEPCIONES

#edad = input("ingrese la edad porfavor:\n ")
#edad = int (edad)
#edad2= input("Ingrese la edad2 porfavor: \n")


try:
	numero1 = input ("Ingrese numero 1:\n")
	numero1 = int(numero1)
	numero2 = input ("Ingrese numero 2:\n")
	numero2= int(numero2)
	operacion = numero1 / numero2
	print("El valor de la operacion es:%d"% (operacion))

#except NameError as e:
#	print("Existe un error:%s" % e)
#except ValueError as e:
#	print("Existe un error:(%s):%s" % (e. __class__, e))

except ZeroDivisionError as e:
	print("Existe un error:(%s):%s" % (e. __class__, e))
except Exception as e:
	print("Existe un error:(%s):%s" % (e. __class__, e))
