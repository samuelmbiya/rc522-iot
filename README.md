=========
rc522-iot
=========


.. image:: https://img.shields.io/pypi/v/rc522_iot.svg
        :target: https://pypi.python.org/pypi/rc522_iot

.. image:: https://img.shields.io/travis/SKMbiya/rc522_iot.svg
        :target: https://travis-ci.com/SKMbiya/rc522_iot

.. image:: https://readthedocs.org/projects/rc522-iot/badge/?version=latest
        :target: https://rc522-iot.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




A python wrapper API that allows you to interface with the mfrc522 RFID card reader and a Raspberry Pi


* Free software: MIT license

Requirements
--------
The code requires you to have the mfrc522 and RPi.GPIO libraries installed. They can be installed using the following commands respectively ``sudo pip3 install mfrc522`` and ``pip install RPi.GPIO``

Features
--------

This API provides you with functions allowing you to:
* Enable/disable SPI communication between the Raspberry Pi and the RFID card reader
* Reset RFID cards and tags by clearing the text stored in them
* Read the text and id number associated to RFID cards and tags
* Write text to RFID cards and tags

Credits
-------

This API made use of [Mario Gómez'](https://github.com/mxgxw) class to interface with the NFC reader Module MFRC522 on the Raspberry Pi. It can be found [here](https://github.com/mxgxw/MFRC522-python)


Contributors
------------
* EEE3097S Group 19:

[@IviweMalotana](https://github.com/IviweMalotana)
[@SKMBiya](https://github.com/SKMbiya)