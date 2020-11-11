import pyfirmata

if __name__ == "__main__":
    
    serial_port = '/dev/cu.usbmodem14101'

    arduino = pyfirmata.Arduino(serial_port)

    led = arduino.get_pin('d:13:o')
    while True:
        inp = input('type on or off: ')
        if inp == 'on':
            led.write(1)
        elif inp == 'off':
            led.write(0)
        
