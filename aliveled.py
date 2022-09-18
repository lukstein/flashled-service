import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
 
p = GPIO.PWM(23, 200)  # frequency=200Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 51, 5):
            p.ChangeDutyCycle(0)
            time.sleep(0.5)
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(50, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
    p.stop()
    GPIO.cleanup()
