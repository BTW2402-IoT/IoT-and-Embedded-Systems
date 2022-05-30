from machine import Pin
from time import sleep
import _thread

Green = Pin(5, Pin.OUT)
Yellow = Pin(18, Pin.OUT)
Red = Pin(19, Pin.OUT)

number = 10
threads_list = set()
lock = _thread.allocate_lock()

def blink(name, led, pause):
    for i in range(number):
        led.on()
        sleep(pause)
        led.off()
        sleep(pause)
    
    lock.acquire()
    threads_list.discard(name)
    lock.release()

_thread.start_new_thread(blink, ("ROT", Red, 1))
_thread.start_new_thread(blink, ("GELB", Yellow, 0.5))
_thread.start_new_thread(blink, ("GRUEN", Green, 0.5))

while not threads_list: pass
while threads_list:
    print(threads_list)
    sleep(0.25)

print("fertig")