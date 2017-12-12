# Installation
instalacion
listo el error
resuleto
ooooo

- Install "requests" library:
    
    pip install requests

- Install "Adafruit_Python_DHT" Library:
 
    git clone https://github.com/adafruit/Adafruit_Python_DHT.git
    cd Adafruit_Python_DHT
    sudo apt-get update
    sudo apt-get install build-essential python-dev python-openssl
    sudo python setup.py install
    
        
- Edit the file app.py and set the variables:
    - api_key, the key to API carriots
    - device, the device registered in carriots
    - pin_dht11, the BCM GPIO pin where dht11 data pin is connected 
    - pin_light, the BCM GPIO pin where ldr sensor pin is connected
    - time_beetwen_mesure, the number of seconds beetween messures


Then run the application:

    python app.py
    

# Description

This application reads pereiodically the following data from sensors:

    - light intensity
    - humidity
    - temperature
    
and sends to carriot servers through API.

Sensor for light intensity is a RC (R is a LDR) circuit which is being
charged and discharged continously. The time needed to charge the
capacitor is counted and the inverse is used as an intensity light
messure, since greater time means greater value of R, and for LDR R
decrease when light intensity rise.

(https://www.raspberrypi.org/learning/physical-computing-with-python/ldr/)
(https://pimylifeup.com/raspberry-pi-light-sensor/)
    
For humidity and temperature messure a DHT11 sensor is used. The pinout 
of this sensor has only 3 pins: VCC, GND and DATA, so it is very easy to
plug to the GPIO. However the communication process to read the messure
is a bit elaborated. This process is explained here:
 
http://www.micro4you.com/files/sensor/DHT11.pdf

Affortunately Adafruit team has developed a library which implements all
the nitty-gritty of such communication process:

https://github.com/adafruit/Adafruit_Python_DHT.git

We have made use of this library and taken information from:

https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/wiring?view=all

# The circuit

See ``iot.pdf`` to see the circuit schematic.


kskskkssd



