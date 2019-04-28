import RPi.GPIO as GPIO
import time

try :
    GPIO.setmode(GPIO.BCM)

    gp_out = 21
    GPIO.setup(gp_out, GPIO.OUT)
    motor = GPIO.PWM(gp_out, 50)
    motor.start(0.0)
    time.sleep(0.5)

    bot = 2.5
    mid = 7.2
    top = 12.0

    motor.ChangeDutyCycle(bot)
    time.sleep(0.5)

    motor.ChangeDutyCycle(top)
    time.sleep(0.5)
    
    motor.ChangeDutyCycle(mid)
    time.sleep(0.5)

    for i in range(10):
        motor.ChangeDutyCycle(2.5)
        time.sleep(0.5)
        motor.ChangeDutyCycle(6.0)
        time.sleep(0.5)
        motor.ChangeDutyCycle(9.0)
        time.sleep(0.5)
        motor.ChangeDutyCycle(12.0)
        time.sleep(0.5)

    GPIO.cleanup()
except:
    GPIO.cleanup()
    print("error!")
