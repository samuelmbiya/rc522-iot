from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import BlynkLib

GPIO.setwarnings(False)
reader = SimpleMFRC522()

def start(code):
	blynk = BlynkLib.Blynk(code)

	# Add Member
	@blynk.VIRTUAL_WRITE(1)
	def AddMember(value):
        	if value==[u'1']:
			try:
				blynk.virtual_write(10,"Type name of person to add:")

				@blynk.VIRTUAL_WRITE(9)
				def ReadInput(str):
					text = ' '.join(str)
					blynk.virtual_write(10,"Tap tag")
					reader.write(text)
					blynk.virtual_write(10,"Added the member "+text)

					blynk.virtual_write(1,0)
			finally:
				GPIO.cleanup()
	# GetID
	@blynk.VIRTUAL_WRITE(2)
	def getID(value):
		if value==[u'1']:
			try:
				blynk.virtual_write(10,"Tap tag to get ID number")
				id, text = reader.read()
				blynk.virtual_write(10,id)
				blynk.virtual_write(2,0)
			finally:
				GPIO.cleanup()

	# GetName
	@blynk.VIRTUAL_WRITE(3)
	def getPerson(value):
		if value==[u'1']:
			try:
				blynk.virtual_write(10,"Tap tag to get name")
				id, text = reader.read()
				blynk.virtual_write(10,text)
				blynk.virtual_write(3,0)
			finally:
				GPIO.cleanup()

	while True:
		blynk.run()
