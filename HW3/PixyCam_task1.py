import ev3dev.ev3 as ev3
import random
from SturdyBot import SturdyBot
import time

lcd = ev3.Screen()

# Connect Pixy camera
pixy = ev3.Sensor(address = 'in3')
assert pixy.connected, "Connecting PixyCam"
print('good1\n')

# Set mode
pixy.mode = 'SIG1'
print('good2\n')

# Part 1
firstConfig = {SturdyBot.LEFT_MOTOR: 'outC',
               SturdyBot.RIGHT_MOTOR: 'outB',
               SturdyBot.SERVO_MOTOR: 'outD',
               SturdyBot.LEFT_TOUCH: 'in4',
               SturdyBot.RIGHT_TOUCH: 'in1'
               }
robot = SturdyBot("honeybee", firstConfig)
buttons = ev3.Button()

while not buttons.any():
  lcd.clear()
  if pixy.value(0) != 0:  # Object with SIG1 detected
    starSong = [('C4', 'q')]
    ev3.Sound.play_song(starSong).wait()
    robot.stop()
  else:
    touch = robot.readTouch()
    robot.turnRight(0.1, 0.3)
    if touch[0] and touch[1]:
      robot.backward(0.1, 1)
    elif touch[0]:
      robot.backward(0.1, 1)
      robot.turnRight(0.1, 0.3)
    elif touch[1]:
      robot.backward(0.1, 1)
      robot.turnLeft(0.1, 0.3)