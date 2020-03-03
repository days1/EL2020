### Installation

The Adafruit DHT library will allow us to properly use the DH11 temperature sensor.
For Python 3, simply enter in   
**_sudo python3 -m pip install --upgrade pip setuptools wheel_**

This installs and upgrades 'pip', 'setuptools', and 'wheel' that is needed to install the library.

Next, enter in   
**_sudo pip3 install Adafruit_DHT_**

This command installs the Adafruit DHT Library.

### temp_sense.py

This script uses the DHT11 Temperature & Humidity Sensor Module and Adafruit DHT library in python
to measure the temperature of the area.

The code itself has two functions: oneBlink and readF   
oneBlink makes the led blink to indicate that the touch sensor is being touched and that temp readings are taking place   
readF reads in the temperature and has logic to convert it from celsius to fahrenheit.  
The main portion of the code loops until the input of the touch sensor is triggered. The code then proceeds to use the two functions
mentioned to read the temperature and output it to the terminal.

