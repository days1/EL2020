import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)

buzzer = 22

GPIO.setup(buzzer, GPIO.OUT)

try:
	while True:
		GPIO.output(buzzer, GPIO.HIGH)
		print("Beep")
		time.sleep(0.5)
		GPIO.output(buzzer, GPIO.LOW)
		print("No Beep")
		time.sleep(0.5)
except KeyboardInterrupt:
	os.system("clear")
	print("Beeps have stopped :(")
	GPIO.cleanup()
