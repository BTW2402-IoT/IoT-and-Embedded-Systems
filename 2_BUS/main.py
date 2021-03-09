#################################################################
#
# Code by P. Marti BFH 20.05.2021
# Ecercise Ubidots Demo
#
#################################################################

from machine import Pin, I2C, reset
import BME280 


# Create library object using our bus I2C port
i2c1 = I2C(scl=Pin(22), sda=Pin(23), freq=10000)

try:
    bme = BME280.BME280(i2c=i2c1)
    temp = bme.temperature
    pres = bme.pressure
    hum = bme.humidity
    print("temperature: " ,temp,"  humidity: ",pres, " pressure: ",hum)
  
except OSError:
  print ('failed to read sensor')
  reset()

