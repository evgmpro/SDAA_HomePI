
  
from time import sleep
import RPi.GPIO as GPIO
#Configuraciones:
GPIO.setmode(GPIO.BOARD)




def AnguloServoX(angulo):
	assert angulo >=10 and angulo <= 170
	XServo = GPIO.PWM(12, 50)
	XServo.start(7.5)
	dutyCycle = (angulo + 18*2.5)/18.
	XServo.ChangeDutyCycle(dutyCycle)
	sleep(0.3)
	XServo.stop()
	

if __name__ == '__main__':
	import sys
	GPIO.setup(12, GPIO.OUT)
	AnguloServoX(int(sys.argv[1]))
	GPIO.cleanup()

