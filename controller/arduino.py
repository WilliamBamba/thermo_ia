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

    
    async def task(self):
        pass
        # loop = asyncio.get_event_loop()
        # loop.set_debug(True)
        # loop.run_until_complete(self.task())
        # loop.close()
        # while True:
        #     try:
        #         async with websockets.connect(self.wc_server_url) as wc_client:
        #             while True:
        #                 time.sleep(10)
        #                 # temperature = self.read_temp_value()
        #                 # if temperature is None: continue
        #                 # data = {'temperature': temperature}
        #                 data = {'temperature': 45}
        #                 print(data)
        #                 await wc_client.send(str(data))
        #     except Exception as e:
        #         pass
    
    def send_sensor_data(self):
        temperature = self.read_temp_value()
        if temperature is None: return False
        payload = {'temperature': temperature}
        print('sending:', payload)
        try:
            requests.post('{}/sensors/'.format(self.server_url), json=payload)
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
        # TODO: ajouter les leds

    def read_temp_value(self):
        max_temp = 125
        sensor_data = self.temp_sensor.read()
        if sensor_data is None: return None

        sensor_data = float(sensor_data) * max_temp
        return int(sensor_data)




if __name__ == "__main__":
    serial_port = '/dev/cu.usbmodem14201'
    server_url ='http://localhost:8000'

    client = ArduinoClient(serial_port, server_url)

    client.run()