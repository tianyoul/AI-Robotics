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
               SturdyBot.RIGHT_TOUCH: 'in1',
               SturdyBot.COLOR_SENSOR: 'in2',
               }
robot = SturdyBot("honeybee", firstConfig)
buttons = ev3.Button()

while not buttons.any():
  lcd.clear()
  if pixy.value(0) != 0:  # Object with SIG1 detected
    print("went pass through ")
    x = pixy.value(1)
    y = pixy.value(2)
    w = pixy.value(3)
    h = pixy.value(4)
    dx = int(w/2)       # Half of the width of the rectangle
    dy = int(h/2)       # Half of the height of the rectangle
    xb = x + int(w/2)   # X-coordinate of bottom-right corner
    yb = y - int(h/2)   # Y-coordinate of the bottom-right corner
    lcd.draw.rectangle((0, 0, 177, 40), fill='black')
    # lcd.draw.rectangle((dx,dy,xb,yb), fill='black')
    lcd.update()
    time.sleep(0)

    # if pixy.value(0) != 0:
  #   starSong = [('C4', 'q')]
  #   ev3.Sound.play_song(starSong).wait()
  #   robot.stop()
  # else:
  #   # distance = robot.readDistance()
  #   touch = robot.readTouch()
  #
  #   if touch[0] and touch[1]:
  #     robot.backward(0.1, 1)
  #   elif touch[0]:
  #     robot.backward(0.1, 1)
  #     robot.turnRight(0.1, 0.3)
  #   elif touch[1]:
  #     robot.backward(0.1, 1)
  #     robot.turnLeft(0.1, 0.3)
  #   # else:
  #   #   if distance < 10:
  #   #     robot.backward(0.1, 1)
  #   #     i = random.randint(0, 1)
  #   #     time = random.randint(0, 100)
  #   #     if i == 1:
  #   #       robot.turnLeft(0.3, time / 200)
  #   #     else:
  #   #       robot.turnRight(0.3, time / 200)
  #   #   else:
  #   #     robot.forward(0.2, 0.5)