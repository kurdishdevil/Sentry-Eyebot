from gpiozero import Servo
from time import sleep
servo = Servo(8)

def SetAngle(angle):
	servo.value = angle




