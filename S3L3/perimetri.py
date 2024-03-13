import math

def quadrato ():
	lato = int (input ("Lato: "))
	print ("Il perimetro e': ",lato*4)


def cerchio ():
	raggio = int (input ("Raggio: "))
	print ("La circonferenza e': ",round(2*math.pi*raggio,2)) 


def rettangolo():
	base = int (input ("Base: "))
	altezza = int (input ("Altezza: "))
	print ("Il perimetro e': ",(base*2)+(altezza*2))	


def menu():
	print ("1) Quadrato")
	print ("2) Rettangolo")
	print ("3) Cerchio")
	return int (input ("Che perimetro vuoi calcolare? "))


#Ho aggiunto un blocco try/except per gestire l'inserimento di un non numero in fase di input dell'utente
try:
	scelta = menu()
	if(scelta==1):
		quadrato()
	elif(scelta==2):
		rettangolo()
	elif(scelta==3):
		cerchio()
	else:
		print("Scelta non valida")

except ValueError:
	print("Perfavore inserire un numero intero")

