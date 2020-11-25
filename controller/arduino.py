import json
import time
import requests
import pyfirmata

class ArduinoClient:

    """
        @frequency : in seconds
    """
    def __init__(self, serial_port: str, server_url: str, frequency: int = 10) -> None:
        self.serial_port = serial_port
        self.server_url = server_url
        self.frequency = frequency
        
        self.arduino_device = None
        self.temp_sensor = None

        self.red_led = None
        self.green_led = None

        self.connect()


    def led_action(self, action: int):
        if action == 2:
            self.green_led.write(0)
            self.red_led.write(0)
        elif action == 1:
            self.green_led.write(1)
            self.red_led.write(0)
        elif action == 0:
            self.green_led.write(0)
            self.red_led.write(1)
        else: print('Unknown actions')


    def send_sensor_data(self):
        temperature = self.read_temp_value()
        if temperature is None: return False
        payload = {'temperature': temperature}
        print('sending:', payload)
        try:
            pass
            requests.post('{}/sensors/'.format(self.server_url), json=payload)
            resp = requests.get('{}/sensors/get/action'.format(self.server_url))
            action = resp.json()
            self.led_action(action['action'])
        except Exception as e:
            print('error sending data')
            pass
    
    def run(self):
        while True:
            time.sleep(self.frequency)
            self.send_sensor_data()


    def connect(self):
        arduino = pyfirmata.Arduino(self.serial_port)
        self.arduino_device = arduino
        acquisition = pyfirmata.util.Iterator(arduino)
        acquisition.start()
        self.temp_sensor = arduino.get_pin('a:0:i')
        self.red_led = arduino.get_pin('p:3:o')
        self.green_led = arduino.get_pin('p:10:o')

    def read_temp_value(self):
        sensor_data = self.temp_sensor.read()
        if sensor_data is None: return None
        sensor_data = float(sensor_data) * 1024
        voltage = sensor_data * 5.0;
        voltage /= 1024.0
        temperatureC = (voltage - 0.5) * 100
 
        # [(8-10:45), (14-19:30)]
        return int(temperatureC)




if __name__ == "__main__":
    serial_port = '/dev/cu.usbmodem14101'
    server_url ='http://localhost:8000'

    client = ArduinoClient(serial_port, server_url, 10)

    client.run()