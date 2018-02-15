from HW1 import SturdyRobot
import ev3dev.ev3 as ev3
import time
import threading


robot = SturdyRobot("Obstacle")

def song():
    robot.playMusic("LB.wav")

def move():
    robot.turnRight(0.3, 1)
    robot.turnLeft(0.3, 1)
    robot.pointerRight(0.2, 2.6)

    robot.curve(0.2, 0.3, 4.7)
    robot.turnRight(0.5, 0.8)
    robot.curve(-0.3, -0.2, 4)

    robot.curve(0.3, 0.2, 4.7)
    robot.turnRight(0.5, 0.8)
    robot.curve(-0.2, -0.3, 4)

    robot.turnRight(0.3, 1)
    robot.turnLeft(0.3, 1)
    robot.pointerRight(0.2, 2.3)


threads = []    # Use threading to play music and dance at the same time
song = threading.Thread(target=song)
threads.append(song)
song.start()

time.sleep(1.2)

move = threading.Thread(target=move)
threads.append(move)
move.start()

