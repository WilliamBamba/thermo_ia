import serial
import time

# this is on mac os. need to verify for other sys
serial_port = '/dev/cu.usbmodem14101'


if __name__ == "__main__":
    with serial.Serial(port=serial_port) as port:
        while True:
            data_wrote = port.write(b'hello\n')
            # print('data wrote: ', data_wrote)
            data = port.readline()
            print(data.decode("utf-8").replace('\r\n', ''))
            time.sleep(2)

