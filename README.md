rc522-iot
=========

A python wrapper API that allows you to interface with the mfrc522 RFID card reader and a Raspberry Pi Zero W

Requirements
--------
This code requires you to have the mfrc522 and RPi.GPIO libraries installed. They can be installed using the following commands respectively ``sudo pip3 install mfrc522`` and ``pip install RPi.GPIO``. It is also recommended that you make use of a python virtual environment before installing the libraries, by making use of tools such as venv or virtualenv.

Features
--------

This API provides you with functions allowing you to:
* Enable/disable SPI communication between the Raspberry Pi and the RFID card reader
* Reset RFID cards and tags by clearing the text stored in them
* Read the text and id number associated to RFID cards and tags
* Write text to RFID cards and tags

Usage
-----
Copy the class into your project directory and import it at the top of your script, for your personal use.
Refer to Table 1 below, for how to connect the Raspberry Pi and RFID card reader

Alternatively, you can also have  a look at the demonstration application that was made for the API. It can be found [here](https://github.com/SKMbiya/rc522-iot-demo)

Credits
-------

This API made use of [Mario Gómez'](https://github.com/mxgxw) class to interface with the NFC reader Module MFRC522 on the Raspberry Pi. It can be found [here](https://github.com/mxgxw/MFRC522-python)


Contributors
------------
* EEE3097S Group 19:

Iviwe Malotana:[@IviweMalotana](https://github.com/IviweMalotana)\
Samuel Mbiya: [@SKMbiya](https://github.com/SKMbiya)

License
-------

This project is under the MIT License
