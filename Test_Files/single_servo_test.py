from servo import Servo, servo2040
from time import sleep

servo = Servo(servo2040.SERVO_1)

servo.enable()

servo.value(-1.0)
sleep(1)

servo.value(0.0)
sleep(1)

servo.value(1.0)
sleep(1)

servo.disable()