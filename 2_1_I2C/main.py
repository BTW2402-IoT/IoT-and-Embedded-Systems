###############################################################
#
# Code by P. Marti BFH 20.05.2020
# Ecercise Ubidots Demo
#
###############################################################
from time import sleep
from machine import Pin, I2C, reset, freq, deepsleep
import BME280 


# Create library object using our bus I2C port
i2c1 = I2C(scl=Pin(22), sda=Pin(23), freq=10000)
#1 Create led object using pin class
led=Pin(13,Pin.OUT)


def read_ds_sensor():
  try:
    bme = BME280.BME280(i2c=i2c1)
    t = float(bme.read_temperature()) / 100
    p = float(bme.read_pressure()) / 100
    h = float(bme.read_humidity()) / 1024
    if isinstance(t, float) and isinstance(p, float) and isinstance(t, float):
      msg = b'{"temperature": %s, "humidity": %s, "pressure": %s}' % (t,h,p)
      print(msg)
      return msg
    else:
      print('invalid sensor value')
  except OSError:
    print ('failed to read sensor')
    reset()

def do():
  i = 0
  while True:
    read_ds_sensor()
    sleep(0.1)
    i += 1
    if(i>100):
      break

def count():
  i = 0
  while True:
    i += 1
    if i > 1000000:
      break




