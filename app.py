"""
This software makes use of Adafruit_Python_DHT library to read humidity and temperature from
a DHT11 sensor (https://github.com/adafruit/Adafruit_Python_DHT). So in order to work it must be
previously installed in the raspberry pi (see README.md).

It also uses the "requests" library in order to access the carriots API (http://docs.python-requests.org)

"""

import RPi.GPIO as GPIO
import logging

from time import  sleep
from carriots import send
from sensors import get_light_intensity, get_humidity_and_temperature

api_key = 'b779f9758a184f024a7f698682f7a84ab443ea5f4bb3e6f4d8b5d3ff4a2d974a'
device = 'resistencia@juandalibaba.juandalibaba'
pin_dht11 = 4
pin_light = 7
time_beetwen_mesure = 300

logging.basicConfig(filename='iot.log', level=logging.DEBUG)

try:
    sleep(time_beetwen_mesure)
    light_intensity = get_light_intensity(pin_light)
    humidity, temperature = get_humidity_and_temperature(pin_dht11)

    data = {
        'light_intensity': light_intensity,
        'humidity': humidity,
        'temperature': temperature
    }

    r = send(device, data, api_key)

    if r.status_code != 200:
        logging.error('Error: {}'.format(r.text))
    else:
        logging.info(r.text)
except KeyboardInterrupt:
    logging.info('exited (keyboard interrupt')
    print('exited')
except Exception as e:
    logging.error('Excepcion: {}'.format(e))
finally:
    GPIO.cleanup()
