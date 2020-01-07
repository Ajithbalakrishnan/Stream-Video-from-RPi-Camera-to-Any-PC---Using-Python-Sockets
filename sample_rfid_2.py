#! /user/bin/env python
import RPi.GPIO as GPIO
import sys
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)
GPIO.cleanup()
reader=SimpleMFRC522()
while True:
    try: 
        a,b = reader.read()
        #print(type(a))
        #print(type(b))
        print(sys.getsizeof(b))
        print("a = ",a)
        print("b = ",b)
    finally:
        GPIO.cleanup()

