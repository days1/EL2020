import RPi.GPIO as GPIO
import time

greenPin = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(greenPin, GPIO.OUT)

GPIO.output(greenPin,True)
time.sleep(.3)
GPIO.output(greenPin,False)

GPIO.cleanup()
