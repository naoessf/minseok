import math as m
import serial
import operator 
import RPi.GPIO as GPIO
from time import sleep

ser = serial.Serial(port = "/dev/ttyACM0", baudrate = 387400, timeout = 0.1)

GPIO.setmode(GPIO.BOARD)
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
departure_lat = input("위도를 입력하시오 : ")
departure_lon = input("경도를 입력하시오 : ")
#배의 현재 위치
latitude = latitude(n)
longitude = longitude(n)


#도착지 기준 배의 위치가 1사분면에 있을 경우
if float(latitude) > float(departure_lat) and float(longitude) < float(departure_lon) :
    difference = (90 + m.atan((float(latitude) - float(departure_lat))/(float(departure_lon) - float(longitude)))) - float(direction)
    svmotor.ChangeDutyCycle(7.5 + (float(difference)))
#도착지 기준 배의 위치가 2사분면에 있을 경우
elif float(longitude) > float(departure_lon) and float(latitude) > float(departure_lat) :
    difference = (270 - m.atan((float(latitude) - float(departure_lat))/(float(longitude) - float(departure_lon)))) - float(direction)
    svmotor.ChangeDutyCycle(7.5 + (float(difference)))
#도착지 기준 배의 위치가 3사분면에 있을 경우
elif float(longitude) > float(departure_lon) and float(latitude) < float(departure_lat) :
    difference = (270 + m.atan((float(departure_lat) - float(latitude))/(float(longitude) - float(departure_lon)))) - float(direction)
    svmotor.CHangeDutyCycle(7.5 + (float(difference)))
#도착지 기준 배의 위치가 4사분면에 있을 경우
else :
    difference = (90 - m.atan((float(departure_lat) - float(latitude)/(float(departure_lon) - float(longitude)))) - float(direction)
    svmotor.ChangeDutyCycle(7.5 + (float(difference)))
