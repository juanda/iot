# Installation

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
    
For humidity and temperature messure a DHT11 sensor is used. In order
to use this sensor with the raspberry pi we have used this library:

https://github.com/adafruit/Adafruit_Python_DHT.git

Developed by adafruit team.


