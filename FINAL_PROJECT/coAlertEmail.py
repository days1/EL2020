import os
import time
import smtplib
import socket
import sys

args = sys.argv[1:]
temp = args[0]

Text = "CO2 levels are at dangerous levels!!! {}".format(temp)

#SMTP Variables
eFROM = "sanchoday@gmail.com"
eTO = "8452496138@tmomail.net"
Subject = "DANGEROUS CO2 LEVELS!!!"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)


print "Alert Sent"

eMessage = 'Subject: {}\n\n{}'.format(Subject, Text)
server.login("sanchoday@gmail.com", "ftcdhvcaazevdzhv")
server.sendmail(eFROM, eTO, eMessage)
server.quit
time.sleep(5)
