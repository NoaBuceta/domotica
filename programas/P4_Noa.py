"""Noa Buceta Blanco"""
from microbit import *

def mover_servo(angulo):
pwm = int((angulo / 180) * 102 + 26)
pin2.write_analog(pwm)


angulo = 0
mover_servo(angulo)
sleep(1000)

while True:
if button_b.is_pressed():
if angulo == 0:
angulo = 90
else:
angulo = 0
mover_servo(angulo)
sleep(500)
