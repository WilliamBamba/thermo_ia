import pyfirmata
import time


class ArduinoClient:

    def __init__(self, serial_port: str, wc_server: str) -> None:
        self.wc_server = wc_server
        self.serial_port = serial_port
        self.arduino_device = None
        self.temp_sensor = None

    def connect(self):
        arduino = pyfirmata.Arduino(self.serial_port)
        self.arduino_device = arduino
        acquisition = pyfirmata.util.Iterator(arduino)
        acquisition.start()
        self.temp_sensor = arduino.get_pin('a:0:i')

    def read_temp_value(self):
        sensor_data = self.temp_sensor.read()
        min_temp = -10
        max_temp = 150

        sensor_interval = abs(min_temp) + abs(max_temp)
        sensor_data = float(sensor_data)
        sensor_data *= 1024

        val = sensor_data * sensor_interval
        val += min_temp/2
        return val


if __name__ == "__main__":
    
    serial_port = '/dev/cu.usbmodem14101'

    arduino = pyfirmata.Arduino(serial_port)
    acquisition = pyfirmata.util.Iterator(arduino)
    acquisition.start()

    sensor_temp = arduino.get_pin('a:0:i')

    while True:
        min_temp = -10
        max_temp = 150
        sensor_interval = abs(min_temp) + abs(max_temp)
        sensor_data = sensor_temp.read()
        if sensor_data is not None:
            sensor_data = float(sensor_data) * 1024
            # val = sensor_data * sensor_interval
            # val += min_temp/2
            print(sensor_data, '°C')
            time.sleep(2)
        else:
            time.sleep(0.5)

