import RPi.GPIO as GPIO
import operator
import math as m

def gpiosetup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)

def dcmotor():
    DCmotor = GPIO.PWM(12, 50)
    DCmotor.start(0)
    DCmotor.ChangeDutyCycle(7.5)

def svmotor():
    SVmotor = GPIO.PWM(11,50)
    SVmotor.start(0)
    SVmotor.ChangeDutyCycle(7.5)

# SVmotor

def right():
    right = SVmotor.ChangeDutyCycle(7.5 + direction)
    return right

def left():
    left = SVmotor.ChangeDutyCycle(7.5 + direction)
    return left

def straight():
    straight = SVmotor.ChangeDutyCycle(7.5)
    return straight

departure_lon1 = input("첫 번째 도착지의 경도 : ")
departure_lat1 = input("첫 번째 도착지의 위도 : ")

departure_lon2 = input("두 번째 도착지의 경도 : ")
departure_lat2 = input("두 번째 도착지의 위도 : ")

departure_lon3 = input("세 번째 도착지의 경도 : ")
departure_lat3 = input("세 번째 도착지의 위도 : ")


departure_lon = departure_lon1
deparutre_lat = departure_lat1


def direction():
    #도착지 기준 배의 위치가 1사분면에 있을 경우
    elif position[3] > longitude(ps) and position[1] > latitude(ps) :
        difference = (270 - m.atan((position[1] - latitude(ps))/(position[3] - longitude(ps)))) - position[3]
        direction = difference*ME
        #도착지 기준 배의 위치가 2사분면에 있을 경우
    if (position[1]) > (latitude(ps)) and (position[2]) < (longitude(ps)) :
        difference = (90 + m.atan(position[1] - latitude(ps))/(longitude(ps) - position[3])) - position[3]
        direction = difference*ME
    #도착지 기준 배의 위치가 3사분면에 있을 경우
    elif: position[1] < latitude(ps) and position[2] < longitude(ps) :
        difference = (90 - m.atan((latitude(ps) - position[1])/(longitude(ps) - position[2]))) - position[3]
        direction = differenc*ME
    #도착지 기준 배의 위치가 4사분면에 있을 경우
    else  :
        difference = (270 + m.atan((latitude(ps) - position[1])/(position[1] - longitude(ps)))) - position[3]
        direction = difference*ME
   
# DCmotor

def forward():

    
    forward = DCmotor.ChangeDutyCycle(8)
    return forward

def shipstop():
    shipstop = DCmotor.ChangeDutyCycle(7.5)
    return shipstop
    
def shipback():
    shipback = DCmotor.ChangeDutyCycle(7)
    return shipback

def cleanup():
    SVmotor.stop()
    DCmotor.stop()
    GPIO.cleanup

departure_lon2 = float(input("두 번째 도착지의 위도 : "))
departure_lat2 = float(input("두 번째 도착지의 위도 : "))

if (departure_lon - 0.08064516) < longitude < (departure_lon + 0.08064516) and (deaparture_lat - 0.08064516) < latitude < (departure_lat - 0.08064516) :
    
    departure_lon = departure_lon2

    departure_lat = departure_lat2