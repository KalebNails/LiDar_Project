import serial
import time
import json

ser = serial.Serial("/dev/serial0", 115200,timeout=0) # mini UART serial device

def read_tfluna_data(ser):
    counter = ser.in_waiting
    if counter > 8:
        bytes_serial = ser.read(9)
        ser.reset_input_buffer()

        if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59:
            distance = bytes_serial[2] + bytes_serial[3]*256
            strength = bytes_serial[4] + bytes_serial[5]*256
            temperature = bytes_serial[6] + bytes_serial[7]*256
            temperature = (temperature/8.0) - 256.0
            return distance/100.0, strength, temperature
    # If no valid data is found, return None for all values
    return None, None, None




export_data = {"distance": [], "angle": []}
writer_counter = 0

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
        raw_data = ser1.readline()
        if raw_data.strip():  # Check if raw_data is not empty or contains only whitespace
            try:
                line = float(raw_data.decode('utf-8').rstrip())
            except ValueError:
                print("Error converting string to float, setting line to default value")
                line = 0  # Set line to a default value if conversion fails
        else:
            print("Empty or whitespace-only data received, setting line to default value")
            line = 0  # Set line to a default value if raw_data is empty
        
        print(line)

        distance, strength, temperature = read_tfluna_data(ser)
        print(distance)
        if distance is not None and strength is not None and temperature is not None:
            print('Distance: {0:2.2f} m, Strength: {1:2.0f} / 65535 (16-bit), Chip Temperature: {2:2.1f} C'.format(distance, strength, temperature))
        else:
            print("Error reading TFLuna data, setting default values")
            distance, strength, temperature = 0, 0, 0  # Set default values

        export_data["distance"].append(distance)
        export_data["angle"].append(line)

        distance, strength, temperature = read_tfluna_data(ser1)
        if distance is not None and strength is not None and temperature is not None:
            print('Distance: {0:2.2f} m, Strength: {1:2.0f} / 65535 (16-bit), Chip Temperature: {2:2.1f} C'.format(distance, strength, temperature))
                
        filename ='combinedoutput.json'
        writer_counter += 1
        if writer_counter > 100:
            writer_counter = 0
            print("Attempting to write!!!!")
            with open(filename, mode='w', newline='') as file:
                json_object = json.dumps(export_data, indent=4)
                file.write(json_object)
