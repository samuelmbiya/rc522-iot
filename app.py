import api
import RPi.GPIO as GPIO
import BlynkLib

BLYNK_AUTH = '9rvmtZDBOuQr0KrJ-FFwB2dZblwt3yDp'

blynk = BlynkLib.Blynk(BLYNK_AUTH)

for i in range(2):
	api.addPerson()

while True:
	blynk.run()

	name = api.getPerson()
	print(name)
	blynk.virtual_write(2,name)

	id = api.getID()
	blynk.virtual_write(4,id)
	print(id)
