import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
pwm=GPIO.PWM(8, 50)
pwm.start(0)
def SetAngle(angle):

	duty = angle / 18 + 2
	GPIO.output(8, True)
	pwm.ChangeDutyCycle(angle)




