# temp_log.py  
Uses the DHT11 sensor to read the temperature and humidity every 60 seconds.  
If the temperature is not between 70 to 80 degrees fahrenheit, the _**mail_temp.py**_ script is called to alert the user and a red LED turns on to indicate such. If the temperature is in the correct range, a green LED will be turned on instead. 
Lastly, the _**writetodb.py**_ script is called to write the data into a Sqlite database.  

# mail_temp.py 
Sends an email and text message to the user informing them that the temperature is not between 70 and 80 degrees fahrenheit.  

# writetodb.py 
Inserts the data from the DHT11 sensor to the Sqlite database.
