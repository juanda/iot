import RPi.GPIO as GPIO
soosososo
sosososos
import time
import Adafruit_DHT

def get_humidity_and_temperature(pin):
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin)
    return humidity, temperature

def get_light_intensity(pin):
    GPIO.setmode(GPIO.BCM)

    count = 0

    #Output on the pin for
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin, GPIO.IN)

    #Count until the pin goes high
    while (GPIO.input(pin) == GPIO.LOW):
        count += 1

    return count

