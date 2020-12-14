from gpiozero import Servo
from time import sleep
servo = Servo(14)

def SetAngle(angle):
        servo.value = angle
