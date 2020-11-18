import pyfirmata
import asyncio
import websockets
import time

class ArduinoClient:

    def __init__(self, serial_port: str, wc_server_url: str) -> None:
        self.serial_port = serial_port
        self.wc_server_url = wc_server_url
        
        self.arduino_device = None
        self.temp_sensor = None

        self.red_led = None
        self.green_led = None

        self.connect()

    
    async def task(self):
        while True:
            try:
                async with websockets.connect(self.wc_server_url) as wc_client:
                    while True:
                        time.sleep(10)
                        # temperature = self.read_temp_value()
                        # if temperature is None: continue
                        # data = {'temperature': temperature}
                        data = {'temperature': 45}
                        print(data)
                        await wc_client.send(str(data))
            except Exception as e:
                pass

    def run(self):
        loop = asyncio.get_event_loop()
        loop.set_debug(True)
        loop.run_until_complete(self.task())
        loop.close()

    def connect(self):
        pass
        # arduino = pyfirmata.Arduino(self.serial_port)
        # self.arduino_device = arduino
        # acquisition = pyfirmata.util.Iterator(arduino)
        # acquisition.start()
        # self.temp_sensor = arduino.get_pin('a:0:i')
        # TODO: ajouter les leds

    def read_temp_value(self):
        max_temp = 125
        sensor_data = self.temp_sensor.read()
        if sensor_data is None: return None

        sensor_data = float(sensor_data) * max_temp
        return int(sensor_data)




if __name__ == "__main__":
    serial_port = '/dev/cu.usbmodem14101'
    wc_server_url ='ws://localhost:8000/sensors/exchange_data'

    client = ArduinoClient(serial_port, wc_server_url)

    client.run()