# **Smoke Detector and Carbon Monoxide Monitor**
This Smoke Detector and CO Monitor uses a Raspberry Pi and various sensors to detect multiple harmful gases, smoke and carbon minoxide. **THIS PROJECT ASSUMES YOU ALREADY HAVE YOUR RASPBERRY PI UP AND RUNNING**

### **Equipment**
* Raspberry Pi
* MQ-2 Gas Smoke Sensor
* MQ-5 Combustible Gas Detector Sensor
* MQ-7 Carbon Monoxide Detector Sensor
* Flame Detection Sensor
* Buzzer Alarm Sensor
* Analog to Digital Converter
* Jumper wires
* Rainbow Ribbon Cable
* Breadboard
* GPIO Extension Board

Sensor kit that I used can be found [here](https://www.amazon.com/gp/product/B01J9GD3DG/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1)  
Breadboard kit that I used can be found [here](https://www.amazon.com/gp/product/B01MQSWUGY/ref=ppx_yo_dt_b_asin_title_o02_s01?ie=UTF8&psc=1)  

### **Breadboard & Raspberry Pi Setup**
In order to give us more space, we utilize a a GPIO Extension Board and a Breadboard to allow for more wiring.  
Take your GPIO Extension Board and connect it to your Breadboard like so:  
![alt text](https://i.ytimg.com/vi/Q6OiAWyJg5E/maxresdefault.jpg)  

Next, you're going to want to take the Rainbow Ribbon Cable and connect your Raspberry Pi to the GPIO Extension Board. Be mindful of the notch on the cable. There is a notch on the GPIO Extension Board to ensure the correct positioning and the notch connecting to the Raspberry Pi should be facing into the Pi. In the end, it should look like this:  
![alt text](https://lh3.googleusercontent.com/proxy/8ZOMycAOElsJwz1a6B-nZbWtE7h6IltGBIHBj_PT050HARhCe8_ifwxvbWryYb-hfd4nCqkRHF06rUJHJGRXvOHHhRtdpQ)  

Lastly, we're going to supply power to our side rails for easier access to power and ground. Take a pair of wires and connect one end to the 3.3v slot and the other end to the red side rail on either side. Take the other wire and connect one end to ground and the other end to the blue side rail. This allows for power and ground to be accessed on its respective rail. Should look something like this.  
![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/5/Pi_Wedge_B_Plus_Tutorial-10.jpg)  

Now, our Raspberry Pi is ready to start using the sensors.

### _alarm_test.py_
The Buzzer Alarm Sensor will be the first sensor to hook up on the pi and test.  
![alt text](https://i.ibb.co/CKmGsL4/Buzzer.png)  


The three prongs from top to bottom are: VCC(Power), I/O(Input/Output), and GND(Ground)  
As you can probably guess, we will be connecting the VCC to the power side rail with a wire and the GND to the ground side rail with a wire. The I/O pin will be connected to the GPIO22 port for the sake of testing with the python script. The end result should look something like this:  
![alt test](https://i.ibb.co/wBC15cL/IMG-20200514-173932.jpg)  
![alt test](https://i.ibb.co/6RLj98L/IMG-20200514-173901.jpg)  

In the second picture, if you locate GPIO22 on the board, you'll see three wires in that row. The white wire(I/O), red wire(Power), and the yellow wire(Ground), all connect to the sensor in the first picture in their respective positions.  
To test if your setup is correct or not, feel free to copy the alarm_test.py script and run it. The alarm should beep every second.

### _flame_test.py_
The next sensor to hook up is the Flame Detection Sensor.  
![alt test](https://i.ibb.co/bbtkq7s/IMG-20200514-114727.jpg)  
As we can see there are now four prongs. This sensor and the remaining ones will all have this four prong setup. Starting from the left, we have AO(Analog Output), GND(Ground), +(Power), and DO(Digital Output). GND and + are the same as before, they just require to be wired to their respective rail. For now, we will be using the Digital Output to interact with the sensor because of the lack of ADC(Analog to Digital Converter) chips that we have. The DO of a sensor will simply just tell us when a sensor detects the substance that is was made to detect. If there is smoke, the sensor will just tell us that there is smoke around. The Analog Output however will tell us the levels of the substance that has been detected. We will save this for the CO sensor when we get to it. For now, connect the DO pin to GPIO5 and the GND and power pins to their respective side rail. Hopefully your sensor will look like this:  
![alt test](https://i.ibb.co/MN927kW/IMG-20200514-180238.jpg)  
![alt test](https://i.ibb.co/fX6bs0w/IMG-20200514-180256.jpg)  

One thing to note about the wiring, I tend to align the wires in a single row that way they're easy to follow. It gives some organization to the entire project while you keep adding more sensors.  

To test the Flame Detection Sensor, proceed to copy the _flame_test.py_ and use a lighter to test if the sensor picks up the flame. **Important:** If your room is filled with sunlight, the sensor may give off false positives. Ensure you're in a not bright room.

### _mq2_test.py_  
The MQ2 Gas Smoke sensor is similar to the Flame Detection Sensor in terms of pins. We have the same AO, GND, VCC(+/Power), and DO pins. Again, we won't be using the AO pin for this sensor, so proceed to connect the DO pin to the GPIO17 position. The end result should look something like this:  
![alt test](https://i.ibb.co/0p0TzGr/IMG-20200511-194425.jpg)  

The testing for this is a little more tricky. In my case, I used an essence stick and blew it out to produce smoke to test the sensor. I was considering burning some bacon, but that is a literal crime and I prefer not to be sent to jail.

### _mq5_test.py_
Like the previous sensors, the MQ3 Combustible Gas Sensor has the same pin setup. The MQ3 is nearly identical to the MQ2 so you can go ahead and hook up the pins. The DO pin will be connected to the GPIO27 position. Unfortunately, I couldn't come up with a way to test this sensor but should work considering how similar it is to the MQ2.  
![alt test](https://i.ibb.co/Fb9DbD8/IMG-20200514-183113.jpg)  

As you can see, the MQ2 and MQ5 are nearly identical so it shouldn't cause too many issues.  

### _mq7_test.py_  
The MQ7 Carbon Monoxide Detection Sensor will be using the ADC mentioned earlier. Rather than type out everything from the source that I used to get this sensor to work, [here is a link to the resouce itself]!(http://kookye.com/2017/06/01/design-a-co-gas-detector-through-a-raspberry-pi-board-and-mq-7-co-sensor/). While everyone of these substances are dangerous, I choose the CO sensor because of its reputation as being the silent, odorless killer. Here is a photo of how the MQ7 sensor and ADC should be connected.  
![alt test](http://osoyoo.com/wp-content/uploads/2017/03/mq-7.png)  

Again, copy the _mq7_test.py_ script and run it. To test the sensor itself, I took a lighter and just pushed on the lever to let gas out of the lighter. This should pick up the gas when close enough to the sensor.  

### _smoke_co2.py_
This file is the culmination of all the test scripts written. You can either copy this script yourself and run it to get the whole thing working or you can try piecing together all the test scripts and try it for yourself. In the end, your circuit board should look like this but hopefully less messy!  
![alt test](https://i.ibb.co/sF03Qhf/IMG-20200514-191825.jpg)

The remaining python scripts are additional functionality such as texting alerts and website displaying of the CO levels. If you're interested in setting up a database and website. Proceed to look at these resources.  
[Flask Framework](http://mattrichardson.com/Raspberry-Pi-Flask/)  
[SQLite tutorial](https://iotbytes.wordpress.com/sqlite-db-on-raspberry-pi/)

