import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
pwm=GPIO.PWM(8, 50)

def SetAngle(angle):
	pwm.start(0)
	duty = angle / 18 + 2
	GPIO.output(8, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(8, False)
	pwm.ChangeDutyCycle(0)
	pwm.stop()


