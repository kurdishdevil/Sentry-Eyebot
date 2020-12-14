from gpiozero import Servo
from time import sleep
servo = Servo(8)

def SetAngle(angle):
        servo.value = angle
        servo.min()
        sleep(2)
        servo.mid()
        sleep(2)
        servo.max()
        sleep(2)




