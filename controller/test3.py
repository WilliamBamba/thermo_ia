import pyfirmata
import requests
from threading import Thread, RLock
import time


class LedBlinker(Thread):
    def __init__(self, led, on: bool, lock: RLock):
        Thread.__init__(self)
        self.lock = lock
        with self.lock:
            self.led = led
        self.on = on

    def run(self):
        while True:
            with self.lock:
                if self.on:
                    self.led.write(1)
                else: self.led.write(0)
            time.sleep(1)


if __name__ == "__main__":
    
    serial_port = '/dev/cu.usbmodem14101'

    arduino = pyfirmata.Arduino(serial_port)

    lock = RLock()
    led = arduino.get_pin('d:13:o')

    led_on = LedBlinker(led, True, lock)
    led_off = LedBlinker(led, False, lock)

    led_on.start()
    time.sleep(0.5)
    led_off.start()

    led_on.join()
    led_off.join()
