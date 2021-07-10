import serial
import time

name = "/dev/ttyUSB0"
spd = 19200
ser = serial.Serial(name, spd)
time.sleep(1)

def serialWrite(data):
    txs = ""
    for val in data:
        txs += str(val)
        txs += ','
    txs = txs[:-1]
    txs += ';'
    print(txs)
    ser.write(txs.encode())
    time.sleep(0.5)
