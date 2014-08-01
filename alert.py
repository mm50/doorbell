from heylook import pushingbox
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
num = 0

while True:
    inputValue = GPIO.input(24)
    if (inputValue == True):
     key = "v9E72FF43C1BC3C6"
     pushingbox(key)
     num = 1
    if (num == 1): 
     inputValue = False
     print("ya")
     time.sleep(.3) 
time.sleep(.01)
time.sleep(.9)
