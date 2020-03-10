import Adafruit_DHT
import RPi.GPIO as GPIO
import signal
import time
import os

redPin = 27
greenPin = 25 
tempPin = 17
touchPin = 26

tempSensor = Adafruit_DHT.DHT11

blinkDur = .1
blinkTime = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(touchPin, GPIO.IN)

def greenLed(pin):
	GPIO.output(redPin,False)
	GPIO.output(pin,True)

def redLed(pin):
	GPIO.output(greenPin,False)
	GPIO.output(pin,True)

def oneBlink(pin):
	GPIO.output(pin,True)
	time.sleep(blinkDur)
	GPIO.output(pin,False)
	time.sleep(blinkDur)

def readF(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	temperature = temperature * 9/5.0 +32
	if temperature is not None:
		tempFahr = '{0:0.1f}*F'.format(temperature)
	else:
		print('Error Reading Sensor')

	if (temperature >= 70) and (temperature <= 80):
		greenLed(greenPin)
	else:
		redLed(redPin)
		os.system('python mail_temp.py {}'.format(tempFahr))

	return tempFahr

def readH(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	if humidity is not None:
		tempHumid = '{0:.0f}%H'.format(humidity)
	else:
		print('Error Reading Sensor')

	return tempHumid

try:
	with open("/home/sancho/CSP342/EL2020/TEMP_PROJECT/log/templog.csv", "a") as log:
		while True:
			time.sleep(60)
			dataF = readF(tempPin)
			dataH = readH(tempPin)
			print(dataF)
			print(dataH)
			log.write("{0},{1},{2}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"), str(dataF), str(dataH)))

except KeyboardInterrupt:
	os.system('clear')
	print('Thanks for Blinking and Thinking')
	GPIO.cleanup()
