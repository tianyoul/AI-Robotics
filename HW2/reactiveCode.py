import time
import ev3dev.ev3 as ev3
import random

class escapeBox(object):

    def __init__(self, robot = None):
        self.robot = robot
        self.prev_light = 0 # assume the darkest surrounding


    def run(self):
        # Getting the reflectance from the color sensor
        self.robot.forward(0.2, 0.3)
        while self.robot.readLight() == 0:
            self.robot.turnLeft(0.1, 0.2)
        light = self.robot.readLight()
        if light >= 5:
            starSong = [('C4', 'q')]
            ev3.Sound.play_song(starSong).wait()
            self.robot.stop()
            return False
        elif self.robot.readDistance() < 15:
            self.robot.backward(0.3, 0.5)
            i = random.randint(0, 1)
            time = random.randint(0, 100)
            if i == 1:
                self.robot.turnLeft(0.3, time / 200)
            else:
                self.robot.turnRight(0.3, time / 200)
            return True
        else:
            touch = self.robot.readTouch()
            # the robot should both avoid obstacles and seek out light
            if touch[0] and touch[1]:
                # first, we should consider when the bumpers are hit
                self.robot.backward(0.3,0.5)
            elif touch[0]:
                self.robot.backward(0.3, 0.5)
                self.robot.turnRight(0.2, 0.3)
            elif touch[1]:
                self.robot.backward(0.3, 0.5)
                self.robot.turnLeft(0.2, 0.3)
            # when the bumpers are alright, we need to make sure it's not too close to any obstacles

            return True




class Honeybee(object):
    def __init__(self, robot = None):
        """Set up motors/robot and sensors here"""
        self.robot = robot

    def run(self):
        color = self.robot.readColor()

        if color == 5:
            starSong = [('C4', 'q')]
            ev3.Sound.play_song(starSong).wait()
            self.robot.stop()
            return False
        else:
            distance = self.robot.readDistance()
            touch = self.robot.readTouch()

            if touch[0] and touch[1]:
                self.robot.backward(0.1, 1)
            elif touch[0]:
                self.robot.backward(0.1, 1)
                self.robot.turnRight(0.1, 0.3)
            elif touch[1]:
                self.robot.backward(0.1, 1)
                self.robot.turnLeft(0.1, 0.3)
            else:
                if distance < 10:
                    self.robot.backward(0.1, 1)
                    i = random.randint(0, 1)
                    time = random.randint(0,100)
                    if i == 1:
                        self.robot.turnLeft(0.3, time / 200)
                    else:
                        self.robot.turnRight(0.3, time / 200)
                else:
                    self.robot.forward(0.2, 0.5)

            return True



def runBehavior(behavObj, runTime = None):
    """Takes in a behavior object and an optional time to run. It runs
    a loop that calls the run method of the behavObj over and over until
    either the time runs out or a button is pressed."""
    buttons = ev3.Button()
    startTime = time.time()
    elapsedTime = time.time() - startTime
    ev3.Sound.speak("Starting")
    while (not buttons.any()) and ((runTime is None) or (elapsedTime < runTime)):
        boo = behavObj.run()

        if(not boo):
            break
        # Could add time.sleep here if need to slow loop down
        elapsedTime = time.time() - startTime
    behavObj.robot.stop()
    ev3.Sound.speak("Done")


#if __name__ == '__main__':
    # set up robot object here if using it

    # add code to stop robot motors
