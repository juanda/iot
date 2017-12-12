import RPi.GPIO as GPIO
sosoos
saodoas
ksksksks
kakajajaja
import logging

from time import  sleep
from carriots import send
from sensors import get_light_intensity, get_humidity_and_temperature

api_key = 'b779f9758a184f024a7f698682f7a84ab443ea5f4bb3e6f4d8b5d3ff4a2d974a'
device = 'resistencia@juandalibaba.juandalibaba'
pin_dht11 = 24
pin_light = 23
time_beetwen_mesure = 10

logging.basicConfig(filename='iot.log', level=logging.DEBUG)

try:
    while True:
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
        
        sleep(time_beetwen_mesure)
except KeyboardInterrupt:
    logging.info('exited (keyboard interrupt')
    print('exited')
except Exception as e:
    logging.error('Excepcion: {}'.format(e))
finally:
    GPIO.cleanup()
