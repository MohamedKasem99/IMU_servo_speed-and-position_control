import time
import RPi.GPIO as GPIO
from AngleMeterAlpha import AngleMeterAlpha


angleMeter = AngleMeterAlpha()
angleMeter.measure()

	
GPIO.setmode(GPIO.BOARD) #to set the pin numbers according to the board
servo = 11
GPIO.setup(servo,GPIO.OUT)

pwm = GPIO.PWM(servo, 50)   #create a PWM object with that's initialized with 50hz signal frequency
pwm.start(7)      #start a duty cycle of 7%

midPoint = 7.07


while True:
    #print(angleMeter.get_kalman_roll(),",", angleMeter.get_complementary_roll(), ",",angleMeter.get_kalman_pitch(),",", angleMeter.get_complementary_pitch(),".")
    roll = abs(angleMeter.get_int_roll())
    pitch = (angleMeter.get_int_pitch())
    print(roll, pitch)
    if roll <= 45:
        pwm.ChangeDutyCycle(midPoint* (1+pitch/180.0))
        print(midPoint* (1+pitch/180.0))
        time.sleep(0.02)
    else:
    	pwm.ChangeDutyCycle(0)
    	
