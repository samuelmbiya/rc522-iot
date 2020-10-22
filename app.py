import api
import BlynkLib

# Initialize Blynk
blynk = BlynkLib.Blynk('9rvmtZDBOuQr0KrJ-FFwB2dZblwt3yDp')

# Turn on and off
@blynk.VIRTUAL_WRITE(0)
def Antenna(value):
	if value==[u'0']:
		api.AntennaOff()
	elif value==[u'1']:
		api.AntennaOn()
# Add Member
@blynk.VIRTUAL_WRITE(1)
def AddMember(value):
	if value==[u'1']:
		blynk.virtual_write(10,"Type name of person to add:")
		@blynk.VIRTUAL_WRITE(9)
		def ReadInput(str):
			text = ' '.join(str)
			blynk.virtual_write(10,"Tap tag")
			name = api.addMember(text)
			blynk.virtual_write(10,"Added the member "+name)
			blynk.virtual_write(1,0)
# GetID
@blynk.VIRTUAL_WRITE(2)
def GetID(value):
	if value==[u'1']:
		blynk.virtual_write(10,"Tap tag to get ID number")
		id = api.getID()
		blynk.virtual_write(10,id)
		blynk.virtual_write(2,0)
# GetName
@blynk.VIRTUAL_WRITE(3)
def getPerson(value):
	if value==[u'1']:
		blynk.virtual_write(10,"Tap tag to get name")
		text = api.getName()
		blynk.virtual_write(10,text)
		blynk.virtual_write(3,0)
while True:
                blynk.run()
