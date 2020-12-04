import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(08, GPIO.OUT)
pwm=GPIO.PWM(08, 50)
pwm.start(0)
def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(08, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(08, False)
	pwm.ChangeDutyCycle(0)
SetAngle(90) 
pwm.stop()
