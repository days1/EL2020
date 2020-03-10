import os
import time
import smtplib
import socket
import sys

args = sys.argv[1:]
temp = args[0]

Text = "The temperature is not my favorite way! It is currently {}".format(temp)

#SMTP Variables
eFROM = "sanchoday@gmail.com"
eTO = "8452496138@tmomail.net"
Subject = "The temperature is shit yo"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)


print "Notifying you of how inconvenienced I am"

eMessage = 'Subject: {}\n\n{}'.format(Subject, Text)
server.login("sanchoday@gmail.com", "ftcdhvcaazevdzhv")
server.sendmail(eFROM, eTO, eMessage)
server.quit
time.sleep(5)
