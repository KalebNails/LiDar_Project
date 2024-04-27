import serial #This is from pyserial
import time

from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

import serial,time
import csv
import json
#
##########################
# TFLuna Lidar
##########################
#
ser = serial.Serial("/dev/serial0", 115200,timeout=0) # mini UART serial device lidar




#This checks if the port is open, and describes the issue if it isnt.
while True:
    try:
        ser1 = serial.Serial(port = '/dev/ttyACM0',baudrate=9600,bytesize=8) #absolute encoder
        ser1.flush()
        ser1.flushInput()
        ser1.reset_input_buffer()

    except serial.SerialException as var:
        print('an exception occurred',var)


    else:
        print('serial port opened')
        break
        
        
def read_tfluna_data():
        counter = ser.in_waiting # count the number of bytes of the serial port
        if counter > 8:
            bytes_serial = ser.read(9) # read 9 bytes
            ser.reset_input_buffer() # reset buffer

            if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59: # check first two bytes
                distance = bytes_serial[2] + bytes_serial[3]*256 # distance in next two bytes
                strength = bytes_serial[4] + bytes_serial[5]*256 # signal strength in next two bytes
                temperature = bytes_serial[6] + bytes_serial[7]*256 # temp in next two bytes
                temperature = (temperature/8.0) - 256.0 # temp scaling and offset
                #print(f"the distance is {distance}")
                return distance/100.0,strength,temperature
distance_list = []
counter = 0
if ser.isOpen() == False:
    ser.open() # open serial port if not open
    
    


data_list = []
times_list = []

#data = {'x_values': data_list,'y_values': times_list}
start=time.time()
data = {'x_values': times_list,'y_values': data_list}

source = ColumnDataSource(data=data)

# create a plot using the ColumnDataSource's two columns
p = figure()
p.scatter(x='x_values', y='y_values',source=source,size=5, color='red', alpha=0.5 )

global export_data
export_data = {"distance":[],"angle":[]}
global writer_counter 
writer_counter = 0

def callback_update_data():
#while True:
    ser1.flush()
    ser.flush()
    window_size = 50
    line = 0
    line = float(ser1.readline().decode('utf-8').rstrip())
    print(f"first angle is {line}")
    if ser1.in_waiting > 0:
        line = float(ser1.readline().decode('utf-8').rstrip())

        print(f"angle is {line}")
        
        



        if len(data_list) >= window_size:
            data_list.pop(0);
            data_list.append(line)
                #print(type(data_list[0]))
            times_list.pop(0);
            times_list.append(time.time()-start)
            #print('at max' )
            #print(data_list)

        else:
            data_list.append(line)
            times_list.append(time.time()-start)
            #print('growing: ' + str(len(data_list)))

        #print(data_list)
        #print(times_list)
        #print('!')
        source.data = {'x_values': times_list,'y_values': data_list}
        #print('hi')
    else:

        if len(data_list) >= window_size:
            data_list.pop(0);
            data_list.append(line)
            #print(type(data_list[0]))

            times_list.pop(0);
            times_list.append(time.time()-start)

            #print(data_list)

        else:
            data_list.append(line)
            times_list.append(time.time()-start)
            #print('growing: ' + str(len(data_list)))

        #print(data_list)
        #print(times_list)
        #print('tesing')
        source.data = {'x_values': times_list,'y_values': data_list}
        
        
        
    distance,strength,temperature = read_tfluna_data() # read values
    distance_list.append(distance)
    export_data["distance"].append(distance)
    export_data["angle"].append(line)
    
    print('Distance: {0:2.2f} m, Strength: {1:2.0f} / 65535 (16-bit), Chip Temperature: {2:2.1f} C'.\
                format(distance,strength,temperature)) # print sample data
                
    
    filename ='combinedoutput.json'
    global writer_counter
    writer_counter = writer_counter + 1
    print(writer_counter)
    if writer_counter > 100:
        writer_counter = 0
        print("attempting to write!!!!")
        with open(filename,mode='w',newline='') as file:
            json_object = json.dumps(export_data,indent=4)
            file.write(json_object)
            #fieldnames = ["distance","angle"]
            #writer = csv.DictWriter(file,fieldnames=fieldnames)
            #writer.writeheader()
            #writer.writerow({"distance":export_data["distance"],"angle":export_data["angle"]})
            
            #writer = csv.writer(file)
            #writer.writerow(export_data)
        
        



layout = layout([p],sizing_mode='stretch_width')

curdoc().add_root(layout)


curdoc().add_periodic_callback(callback_update_data, 500)
