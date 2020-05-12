# Library imports
import time
import sys
import RPi.GPIO as GPIO

# Sets the GPIO numbering system. BCM = Actual GPIO labels; BOARD = Actual Pin numbers
GPIO.setmode(GPIO.BCM)

# Assign the GPIO label being used to the mq2Pin variable
mq2Pin = 17

# Sets up how the Pi will interpret the signal from the sensor
GPIO.setup(mq2Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Function that lets the user know if smoke is detected
def action(pin):
	print("Smoke Detected!")
	return

# When the sensor is triggered, a rise in voltage occurs
# which will be picked up by the following line
GPIO.add_event_detect(mq2Pin, GPIO.RISING)

# After detected, the following line will call the action function
GPIO.add_event_callback(mq2Pin, action)

# A loop that checks the sensor every .5 seconds until the program
# is interrupted by the keyboard
try:
	while True:
		print("active")
		time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
	sys.exit()
