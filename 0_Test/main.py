from machine import Pin, ADC, PWM
from time import sleep

frequency = 5000
led = PWM(Pin(25), frequency)
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

duty_cycle = 0

while True:
    if button.value():
        duty_cycle = duty_cycle + 255
        while True:
            print("Hold Loop")
            if not button.value():
                break

    if duty_cycle > 1024:
        duty_cycle = 0

    sleep(0.001)
    led.duty(duty_cycle)
    print(duty_cycle)