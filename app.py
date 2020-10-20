import api
import BlynkLib
import RPi.GPIO as GPIO

# Initialize Blynk
blynk = BlynkLib.Blynk('9rvmtZDBOuQr0KrJ-FFwB2dZblwt3yDp')

# Add Member
@blynk.VIRTUAL_WRITE(1)
def AddMember(value):
	if value==[u'1']:
		message = api.addPerson()
		blynk.virtual_write(10,message)
		blynk.virtual_write(1,0)
# Get Member
@blynk.VIRTUAL_WRITE(2)
def GetName(value):
        if value==[u'1']:
                name = api.getPerson()
		blynk.virtual_write(11,name)
		blynk.virtual_write(2,0)

# Get ID
@blynk.VIRTUAL_WRITE(3)
def GetID(value):
        if value==[u'1']:
                id = api.getID()
		blynk.virtual_write(12,id)
		blynk.virtual_write(3,0)

while True:
    blynk.run()
