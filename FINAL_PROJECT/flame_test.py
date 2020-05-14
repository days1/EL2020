import time, sys
import RPi.GPIO as GPIO

# Pin that the digital out is going to
flamePin = 5

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(flamePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def action(pin):
	print("Flame Detected!")
	return

# If flame has been detected, the voltage will rise which will cause the callback
# to perform its function of calling the 'action' function
GPIO.add_event_detect(flamePin, GPIO.RISING)
GPIO.add_event_callback(flamePin, action)

# Sets up a loop to check for flames every second and breaks on keyboard interrupt
try:
	while True:
		print("Scanning for flames...")
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
	sys.exit()

