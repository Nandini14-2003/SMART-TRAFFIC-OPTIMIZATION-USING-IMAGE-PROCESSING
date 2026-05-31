import serial

ser = serial.Serial(
   'COM8',  
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)

def send_data(a):
    print('sent')
    ser.write(str.encode(a))

def read_data():
    d = ser.read()
    d = d.decode('UTF-8', 'ignore')
    return d
