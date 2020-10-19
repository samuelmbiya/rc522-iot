from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
reader = SimpleMFRC522()

def addPerson():
	try:
		print("Type the name of the person you want to add:")
		text = input()
		print("Tap tag")
		reader.write(text)
		print("Added the member",text)
	finally:
		GPIO.cleanup()

def getID():
	try:
		print("Tap tag to get ID number")
		print("Tag number is")
		id, text = reader.read()
		return id
	finally:
		GPIO.cleanup()

def getPerson():
	try:
		print("Tap tag to get name")
		print("Name is")
		id, text = reader.read()
		return text
	finally:
		GPIO.cleanup()
