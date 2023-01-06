import serial

while True:
	serialPort = serial.Serial(port = "COM3", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

	data1 = serialPort.readline()
	data2 = data1.decode()
	print(data2)
