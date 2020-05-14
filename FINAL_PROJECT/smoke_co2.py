import RPi.GPIO as GPIO
import os, time, smtplib, socket, sys
import sqlite3 as db

# Initialize pin setup
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8
mq7_dpin = 26
mq7_apin = 0
mq2_pin = 17
mq3_pin = 27
flame_pin = 5
alarm_pin = 22


# Initialize GPIO setup
def init():
        # Clears the GPIO and then sets the I/O of all the pins
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SPIMOSI, GPIO.OUT)
        GPIO.setup(SPIMISO, GPIO.IN)
        GPIO.setup(SPICLK, GPIO.OUT)
        GPIO.setup(SPICS, GPIO.OUT)
        GPIO.setup(mq7_dpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(mq2_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(mq3_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(flame_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(alarm_pin, GPIO.OUT)
        GPIO.output(alarm_pin, GPIO.HIGH)

        # Adds trigger event handlers to the digital output sensors
        GPIO.add_event_detect(mq2_pin, GPIO.RISING)
        GPIO.add_event_callback(mq2_pin, action)
        GPIO.add_event_detect(mq3_pin, GPIO.RISING)
        GPIO.add_event_callback(mq3_pin, action)
        GPIO.add_event_detect(flame_pin, GPIO.RISING)
        GPIO.add_event_callback(flame_pin, action)

# Reads SPI data from ADC channels 0-7
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)	

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout

# Stores reading record of CO level to the database
def writeToDb(time, density):
	conn = None
	record = (time, density)
	
	try:
		conn = db.connect('COdb.db')

		sql = ''' INSERT INTO coRecords(Date, Density)
			VALUES(?,?);'''
		cur = conn.cursor()
		cur.execute(sql, record)
		conn.commit()
		return cur.lastrowid
	
	except db.Error, e:
		print ("Error %s:" %e.args[0])
		sys.exit(1)

	finally:
		if conn:
			conn.close()

# Sends an alert if CO levels are abnormal
def emailAlert(colevel):
	msg = "Warning!!! CO levels are becoming dangerous! Current CO density is:" +str("%.2f"%((colevel/1024.)*100))+" %"

	#SMTP Variables
	eFROM = "sanchoday@gmail.com"
	eTO = "8452496138@tmomail.net"
	subject = "CO Level Alert"
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

	eMsg = 'Subject: {}\n\n{}'.format(subject, msg)
	server.login("sanchoday@gmail.com", "ftcdhvcaazevdzhv")
	server.sendmail(eFROM, eTO, eMsg)
	server.quit

	print("Alert Sent")
	time.sleep(1)

def alarm():
        GPIO.output(alarm_pin, GPIO.LOW)
	time.sleep(1)
	GPIO.output(alarm_pin, GPIO.HIGH)
	time.sleep(1)

def action(pin):
	if(pin == flame_pin):
                print("Flame Detected!")
        elif(pin == mq2_pin):
                print("Smoke Detected!")
        else:
                print("Gas Detected!")
        
        alarm()

# Main loop 
def main():
         init()
         print"Calibrating CO levels..."
         time.sleep(20)
         while True:
		COlevel=readadc(mq7_apin, SPICLK, SPIMOSI, SPIMISO, SPICS)
		density=((COlevel/1024.)*100)

		dateTime = time.strftime("%a %d %b %Y %H:%M:%S", time.localtime())

		writeToDb(dateTime, density)

                if GPIO.input(mq7_dpin):
			print("CO Levels Normal")
			time.sleep(5)
                else:
                        print("Abnormal amount of CO detected!")
			print(density)
                        print"Current CO density is:" +str("%.2f"%density+" %") #%((COlevel/1024.)*100))
			emailAlert(COlevel)
                        time.sleep(5)

if __name__ =='__main__':
         try:
                  main()
                  pass
         except KeyboardInterrupt:
                  pass

GPIO.cleanup()
         
         
