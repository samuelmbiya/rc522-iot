"""Main module."""
import mfrc522
import RPi.GPIO as GPIO

class rc522_iot:

	GPIO.setwarnings(False)

	#Create object of MFRC522 class
	MIFAREReader = mfrc522.MFRC522()



	def _init_(self):
		"""Creates an object of the MFRC522 class"""
		self.MIFAREReader = mfrc522.MFRC522()

	#Controls communication via SPI between pi and card reader
	def SPICommunication(self,value):
		"""Controls the communication via SPI between the RaspberryPi and the RFID card reader

		Keyword arguments:
		value -- This value determines whether the SPI communication is enabled or disabled
		If value = 0: the communication is terminated, else if value = 1: communication is maintained 

		"""
		if value==0: #If SPI Enable button is switched off
			self.MIFAREReader.Close_MFRC522() #Terminates SPI commuunication
			exit() #Exits program

	#Resets the text associated with a tag
	def Reset(self,value):
		"""Resets the test associated with an RFID card or tag

		Keyword arguments:
		value -- This value determines whether the card is reset or not
		If value = 1: the card is reset, by writing '' to the card

		"""
		if value==1: #If the reset button is pressed
			return self.WriteToCard('') #Write "nothing" to the card

	#Returns the ID number associated with a tag
	def getTagID(self):
		"""Returns the ID number associated with the RFID card or tag
		
		Keyword arguments and methods:

		MFRC522_Request() -- Requests the card reader to listen for a tag nearby
		MFRC522_Anticoll() -- Gets the status of the reader and the UID (Unique Identifier) of the tag
		
		status -- Status value of the RFID card reader
		uid -- unique identifier of the RFID tag
		reading -- boolean variable used to start and end the search for RFID cards nearby. When set to true, it indicates that the RFID card reader is listening for RFID tags nearby
		n  -- the RFID tag id number

		"""
		reading=True
		while reading==True:
			(status,TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL) #Request for card reader to listen for a tag nearby
			if status == self.MIFAREReader.MI_OK: #if tag is detected
				(status,uid) = self.MIFAREReader.MFRC522_Anticoll() #get the status of the reader and the iud of the tag
				reading=False #Do not search for any more tags

			#Converts uid number to tag ID
			n = 0
			for i in range(0, 5): #iterates through 4 element array of uid
				n = n * 256 + uid[i]
			return n #returns the tag id number

	#Writes text to the card and returns the text written
	def WriteToCard(self,input):
		"""Writes text to the RFID card or tag and returns the text that has been written to it

		Keywords and methods:

		MFRC522_SelectTag(uid) -- Selects the tag assoicated with the of the RFID tag
		MFRC522_Auth() -- Authenticates the tag
		MFRC522_StopCrypto1() -- Terminates reading from the RFID tag

		input -- The input string to be written to the RFID tag
		text -- The input string in the form of a list object
		name -- An array which stores the characters of the input string, once they have been converted to ASCII
		namestring -- The string which is returned. 

		"""
		reading=True
		while reading==True:
			(status,TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL) #Reqest for card reader to listen for a nearby tag
			if status == self.MIFAREReader.MI_OK: # If tag is detected
				(status,uid) = self.MIFAREReader.MFRC522_Anticoll() #Get status of the reader and uid of tag
			if status == self.MIFAREReader.MI_OK: #If the uid is found
				key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
				self.MIFAREReader.MFRC522_SelectTag(uid) #Select the tag associated with the uid in registers
				status = self.MIFAREReader.MFRC522_Auth(self.MIFAREReader.PICC_AUTHENT1A, 8, key, uid) #This authenticates the tag
				if status == self.MIFAREReader.MI_OK: #If authentication is passed 
					text = list(input) #Convert input string into list
					name = [] #Initialize empty array to populate with data and send to card

					#Add each element of the input list to the first elements in empty array
					for k in range(0,len(text)):
						name.append(ord(text[k])) #Comvert each character to an ASCII value

					#Populate the rest of the 16 elements of the empty array with spaces
					for j in range(len(text),16):
						name.append(ord(chr(32))) #Convert each character to an ASCII value

					self.MIFAREReader.MFRC522_Write(8,name) #Write to card

					i = 0
					arr=[] #Initialize empty array to populate with data to print

					#Convert each element in array from ASCII to string character
					while name[i]!=32: #While element is not a space
						letter = chr(name[i])
						i+=1
						arr.append(letter)

					namestring = ''.join(arr) #Convert array to string
					self.MIFAREReader.MFRC522_StopCrypto1() #Stop reading
					reading=False
		return namestring #return string to be printed

	#Return text from tag
	def getTextFromTag(self):
		"""Returns the text stored on the RFID card reader

		Keywords and methods:

		MFRC522_Read() -- Reads from the RFID tag

		"""
		reading=True
		while reading==True:
			(status,TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL) #Request for card reader to listen for a neearby tag
			if status == self.MIFAREReader.MI_OK: #If tag is detected
				(status,uid) = self.MIFAREReader.MFRC522_Anticoll() #Get status of the card reader and uid of the tag
			if status == self.MIFAREReader.MI_OK: #If the uid is found
				key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
				self.MIFAREReader.MFRC522_SelectTag(uid) #Select the tag associated with the uid in registers
				status = self.MIFAREReader.MFRC522_Auth(self.MIFAREReader.PICC_AUTHENT1A, 8, key, uid) #This authenticates the tag
				if status == self.MIFAREReader.MI_OK: #If authentication is passed 
					name = self.MIFAREReader.MFRC522_Read(8) #Read from the tag and store text
					i = 0
					arr=[]
					#Convert each element in the array read from ASCII to characters
					while name[i]!=32:
						letter = chr(name[i])
						i+=1
						arr.append(letter)

					self.MIFAREReader.MFRC522_StopCrypto1() #Stop reading
					namestring = ''.join(arr) #Convert array to string
		return namestring #return string to be printed

	#Return ID and text 
	def getTextAndID(self):
		"""Returns both the id number and text associated with an RFID tag, in user friendly message.

		Keywords and methods:

		name -- An array containing the text that has been read from the RFID card in the ASCII format
		namestring -- The text stored on the card, once converted to a string

		"""
		reading=True
		while reading==True:
			(status,TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL) #Request card reader to detect a card
			if status == self.MIFAREReader.MI_OK: #If a card is found
				(status,uid) = self.MIFAREReader.MFRC522_Anticoll() #Get the status of the card reader and uid of the tag
			if status == self.MIFAREReader.MI_OK: # If the uid is found
				key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF] #Set the default authentication key
				self.MIFAREReader.MFRC522_SelectTag(uid) #Searches for uid associated with the tag in registers
				status = self.MIFAREReader.MFRC522_Auth(self.MIFAREReader.PICC_AUTHENT1A, 8, key, uid) # Authenticates the card
				if status == self.MIFAREReader.MI_OK: #If card is authenticated

					#Converts uid to tag id number
					n = 0 
					for i in range(0, 5): #iterates through 4 element array of uid
						n = n * 256 + uid[i]
						id = str(n) #returns the tag id number
					
					name = self.MIFAREReader.MFRC522_Read(8) #Reads the text associated with the tag
					i = 0
					arr=[]

					#Converts text from array and ASCII values to string  
					while name[i]!=32:
						letter = chr(name[i])
						i+=1
						arr.append(letter)
					self.MIFAREReader.MFRC522_StopCrypto1()
					namestring = ''.join(arr)
					if namestring=='':
						return "The id "+id+" has no owner" 
					else:
						return "The id "+id+" belongs to "+namestring