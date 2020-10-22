import mfrc522
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
reader = SimpleMFRC522()
mfr = mfrc522.MFRC522()

def AntennaOn():
	mfr.AntennaOn()

def AntennaOff():
	mfr.AntennaOff()

def addMember(text):
        try:
		id,name = reader.write(text)
		return name
	finally:
		GPIO.cleanup()

def getID():
	try:
		id, text = reader.read()
		return id
	finally:
		GPIO.cleanup()

def getName():
	try:
		id, text = reader.read()
		return text
	finally:
		GPIO.cleanup()
