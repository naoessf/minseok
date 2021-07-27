import math as m
import serial
import operator
import RPi.GPIO as GPIO
from time import sleep

ser = serial.Serial(port = "/dev/ttyACM0", baudrate = 38400, timeout = 0.1)

GPIO,setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
LED = 36
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
svmotor = GPIO.PWM(11, 50)
dcmotor = GPIO.PWM(12, 50)
svmotor.start(0)
dcmotor.start(0)
svmotor.ChangeDutyCycle(7.5)
dcmotor.ChangeDutyCycle(7.5)
sleep(2)

#도착지 위도 경도 입력
latitude = input("위도를 입력하시오 : ")
longitude = input("경도를 입력하시오 : ")
#배의 현재 위치
"배의 위도" = spliteddata[3]
"배의 경도" = spliteddata[5]
def GPSparser(data):
	gps_data = list()
	idx_rmc = data.find('GNRMC')
	if data[idx_rmc:idx_rmc+5] == "GNRMC":
		data = data[idx_rmc:]	
		print data
		if checksum(data):
			spliteddata = data.split(",")
			if spliteddata[2] == 'V':
				print "data invalid"
	
			elif spliteddata[2] == 'A':
				gps_data.append(float(spliteddata[1]))
				if spliteddata[4] == 'N' :
					gps_data.append(float(spliteddata[3]))
                    dcmotor.ChangeDutyCycle(8)
                    # 도착지 기준 배의 위치가 1사분면에 있을 경우
                    if spliteddata[3] > latitude and spliteddata[5] < longitude :
                        difference = 90 + m.atan((spliteddata[3] - latitude)/(longitude - spliteddata[5]))
                        svmotor.ChangeDutyCycle(7.5 + difference)
                    # 도착지 기준 배의 위치가 2사분면에 있을 경우
                    if spliteddata[5] > longitude and spliteddata[3] > latitude : 
                        difference = 270 - m.atan((spliteddata[3] - latitude)/(spliteddata[5] - longitude))    
                        svmotor.ChangeDutyCycle(7.5 + difference)
                    # 도착지 기준 배의 위치가 3사분면에 있을 경우
                    if spliteddata[5] > longitude and spliteddata[3] < latitude :
                        difference = 270 + m.atan((latitude - spliteddata[3]/spliteddata[5] - longitude))
                        svmotor.ChangeDutyCycle(7.5 - difference)
                    # 도착지 기준 배의 위치가 4사분면에 있을 경우
                    if latitude > spliteddata[3] and longitude > spliteddata[5] :
                        difference = 90 - m.atan((latitude - spliteddata[3])/(longitude - spliteddata[5]))
                        svmotor.ChangeDutyCycle(7.5 - difference)