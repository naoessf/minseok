import RPi.GPIO as GPIO
import operator
import math as m
import positionchange() from ex

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
    right = SVmotor.ChangeDutyCycle(6)
    return right

def left():
    left = SVmotor.ChangeDutyCycle(9)
    return left

def straight():
    straight = SVmotor.ChangeDutyCycle(7.5)
    return straight

def direction():
    ME = 0.0
    # The position of the ship in the 1st quadrant
    if position[3] > longitude(ps) and position[1] > latitude(ps) :
        difference = (270 - m.atan((position[1] - latitude(ps))/(position[3] - longitude(ps)))) - position[3]
        direction = difference*ME

    # The position of the ship in the 2nd quadrant
    elif (position[1]) > (latitude(ps)) and (position[2]) < (longitude(ps)) :
        difference = (90 + m.atan(position[1] - latitude(ps))/(longitude(ps) - position[3])) - position[3]
        direction = difference*ME

    # The position of the ship in the 3rd quadrant
    elif position[1] < latitude(ps) and position[2] < longitude(ps) :
        difference = (90 - m.atan((latitude(ps) - position[1])/(longitude(ps) - position[2]))) - position[3]
        direction = differenc*ME

    # The position of the ship in the 4th quadrant
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
