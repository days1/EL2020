import RPi.GPIO as GPIO

redPin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin, GPIO.OUT)

GPIO.output(redPin,True)
time.sleep(.3)
GPIO.output(redPin,False)

except KeyboardInterrupt:
	GPIO.cleanup()
