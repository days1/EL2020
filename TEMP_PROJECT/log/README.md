#temp_log.py  
Uses the DHT11 sensor to read the temperature and humidity every 60 seconds.  
If the temperature is not between 70 to 80 degrees fahrenheit, the mail_temp.py script is called to alert the user.  
Lastly, the writetodb.py script is called to write the data into a Sqlite database.  

#mail_temp.py 
Sends an email and text message to the user informing them that the temperature is not between 70 and 80 degrees fahrenheit.  

#writetodb.py 
Inserts the data from the DHT11 sensor to the Sqlite database.
