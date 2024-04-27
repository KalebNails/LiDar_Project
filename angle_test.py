import serial
import time

# Open the serial port
while True:
    try:
        ser1 = serial.Serial(port='/dev/ttyACM0', baudrate=9600, bytesize=8)
        ser1.flush()
        ser1.flushInput()
        ser1.reset_input_buffer()
    except serial.SerialException as e:
        print('An exception occurred:', e)
    else:
        print('Serial port opened')
        break

while True:
    ser1.flush()
    line = 0
    if ser1.in_waiting > 8:
        try:
            raw_data = ser1.readline()
            line = float(raw_data.decode('utf-8').rstrip())
        except UnicodeDecodeError:
            print("Error decoding UTF-8, printing raw data:")
            print(raw_data)
            # Set line to a default value or handle the error as needed
            line = 0  # Example: Set line to 0 if decoding fails
        print(line)
