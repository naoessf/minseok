import serial
from time import sleep
import webbrowser
import sys

def GPS_info():
    global NMEA_buff
    global lat_in_degress
    global long_in_degress
    nmea_time = []
    nmea_latitude = []
    nmea_longitude = []
    nmea_time = NMEA_buff[0]
    nmea_latitude = NMEA_buff[1]
    nmea_longitude = NMEA_buff[3]

    print("NMEA Time: ", nmea_time, '\n')
    print ("NMEA Latitude:", nmea_latitude, "NMEA Longitude:", nmea_longitude, '\n')

    lat = float(nmea_latitude)
    longi = float(nmea_longitude)

    lat_in_degrees = convert_to_degress(lat)
    long_in_degrees = convert_to_degress(longi)

def convert_to_degrees(raw_value):
    decimal_value = raw_calue/100.00
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - int(decimal_value))/0.6
    position = degrees + mm_mmmm
    position = "%.4f" %(position)
    return position


gpgga_info = "$GPGA,"
ser = serial.Serial ("/dev/ttyS0")
GPGGA_buffer = 0
NMEA_buffer = 0
lat_in_degrees = 0
long_in_degrees = 0

try:
    while True:
        received_data = (str)(ser.readline())
        GPGGA_data_available = received_data.find(gpgga_info)
        if (GPGGA_data_available>0):
            GPGGA_buffer = received_data.split("$GPGGA,",1)[1]
            NMEA_buffer = (GPGGA_buffer.split(','))
            GPS_info()

            print("lat in degrees:", lat_in degrees, "long in degrees:", long_in_degrees, '\n')
            map_link = 'http://maps.google.com/?q=' + lat_in_degrees + ',' + long_in_degrees
            print('<<<<<<<<press ctrl+c to plot location on google maps>>>>>>>>\n')
            print('--------------------------------------------------------------\n')

except Keyboardinterrupt:
    webbrowser.open(map_link)
    sys.exit(0)