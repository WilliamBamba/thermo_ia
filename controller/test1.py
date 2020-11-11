import pyfirmata
import requests
import time


serial_port = '/dev/cu.usbmodem14101'

arduino = pyfirmata.Arduino(serial_port)


red_led = arduino.get_pin('d:13:o')

count = 0
while True:
    count += 1
    print('iteration ', count)

    # juste un test
    response = requests.get('https://realpython.com/arduino-python/')
    print(response)

    red_led.write(1)
    time.sleep(1)
    red_led.write(0)
    time.sleep(1)
