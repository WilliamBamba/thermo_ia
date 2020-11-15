import pyfirmata
import time

if __name__ == "__main__":
    
    serial_port = '/dev/cu.usbmodem14101'

    arduino = pyfirmata.Arduino(serial_port)
    acquisition = pyfirmata.util.Iterator(arduino)
    acquisition.start()

    sensor_temp = arduino.get_pin('a:0:i')

    while True:
        min_temp = -40
        max_temp = 120
        sensor_interval = abs(min_temp) + abs(max_temp)
        sensor_data = sensor_temp.read()
        if sensor_data is not None:
            sensor_data = float(sensor_data)
            val = sensor_data * sensor_interval
            print(sensor_data, val, '°C')
            time.sleep(2)
        else:
            time.sleep(0.5)

