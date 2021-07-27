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
위도 = input("위도를 입력하시오 : ")
경도 = input("경도를 입력하시오 : ")
#배의 현재 위치
배의 위도
배의 경도
# 도착지 기준 배의 위치가 1사분면에 있을 경우
if 배의 위도 > 위도 and 배의 경도 < 경도 :
    차이 =  90 + m.atan((배의 위도 - 위도)/(경도 - 배의 경도))
    svmotor.ChangeDutyCycle(7.5 + 차이*비율)
# 도착지 기준 배의 위치가 2사분면에 있을 경우
if 배의 경도 > 경도 and 배의 위도 > 위도 :
    차이 = 270 - m.atan((배의 위도 - 위도)/(배의 경도 - 경도))
    svmotor.ChangeDutyCycle(7.5 + 차이*비율)
# 도착지 기준 배의 위치가 3사분면에 있을 경우
if 배의 경도 > 경도 and 배의 위도 < 위도 :
    차이 = 270 + m.atan((위도 - 배의 위도)/(배의 경도 - 경도))
    svmotor.ChangeDutyCycle(7.5 - 차이*비율)
# 도착지 기준 배의 위치가 4사분면에 있을 경우
if 위도 > 배의 위도 and 경도 > 배의 경도 :
    차이 = 90 - m.atan((위도 - 배의 위도)/(경도 - 배의 경도))
    svmotor.ChangeDutyCycle(7.5 - 차이*비율)