from HW1 import SturdyRobot
import time

robot = SturdyRobot("Obstacle")

robot.forward(0.2, 7)

time.sleep(0.5)

robot.turnRight(0.2, 0.8)

time.sleep(0.5)

robot.forward(0.3, 2.6)

time.sleep(0.5)

robot.turnLeft(0.2, 0.75)

time.sleep(0.5)

robot.forward(0.3, 3)

time.sleep(0.5)

robot.turnLeft(0.2, 0.75)

time.sleep(0.5)

robot.forward(0.5, 3)

