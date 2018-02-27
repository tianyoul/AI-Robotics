import time
import ev3dev.ev3 as ev3


class Timid(object):
    """This behavior should move forward at a fixed, not-too-fast speed if no object
    is close enough in front of it. When an object is detected, it should stop moving."""
    def __init__(self, robot = None):
        """Set up motors/robot and sensors here"""
        self.flag = False
        self.ultrasonic_sensor = ev3.UltrasonicSensor('in2')
        self.robot = robot

    def run(self):
        """One cycle of feedback loop: read sensors, choose movement, set movement."""
        distance = self.ultrasonic_sensor.distance_centimeters
        if(distance > 10):
            flag = True
            self.robot.runforever(0.1)

        if(distance < 10):
            self.robot.stop()
            flag = False


class Wary(object):
    def __init__(self, robot = None):
        """Set up motors/robot and sensors here"""
        self.flag = False
        self.ultrasonic_sensor = ev3.UltrasonicSensor('in2')
        self.robot = robot

    def run(self):
        """One cycle of feedback loop: read sensors, choose movement, set movement."""
        distance = self.ultrasonic_sensor.distance_centimeters
        if (distance > 15):
            self.robot.runforever(0.1)
        elif (distance > 10):
            self.robot.stop()
        else:
            self.robot.backwardforever(0.1)

class ExitCrowd(object):
    def __init__(self, robot = None):
        """Set up motors/robot and sensors here"""
        self.flag = False
        self.ultrasonic_sensor = ev3.UltrasonicSensor('in2')
        self.robot = robot

    def run(self):
        """One cycle of feedback loop: read sensors, choose movement, set movement."""
        distance = self.ultrasonic_sensor.distance_centimeters
        if(distance > 15):
            flag = True
            self.robot.runforever(0.1)
        else:
            flag = False
            self.robot.turnLeftforever(0.3)

class LineFollowing(object):
    def __init__(self, robot = None):
        """Set up motors/robot and sensors here"""
        self.flag = False
        self.reflectance_sensor = ev3.ColorSensor('in3')
        self.robot = robot

    def run(self):
        """One cycle of feedback loop: read sensors, choose movement, set movement."""
        intensity = self.reflectance_sensor.reflected_light_intensity

        self.robot.runforever(0.1)

        if intensity > 30:
            self.robot.turnLeft(0.1, 0.1)
        elif intensity < 20:
            time.sleep(0.2)
            self.robot.turnRight(0.2, 0.1)


class Vehicle1(object):
    def __init__(self, robot = None):
        """Set up motors/robot and sensors here"""
        self.flag = False
        self.ultrasonic_sensor = ev3.UltrasonicSensor('in2')
        self.robot = robot

    def run(self):
        """One cycle of feedback loop: read sensors, choose movement, set movement."""
        dist = self.ultrasonic_sensor.distance_centimeters
        if dist > 20:
            self.robot.stop()
        else:
            self.robot.backwardforever(3/dist)

class Vehicle2(object):
    def __init__(self, robot = None):
        """Set up motors/robot and sensors here"""
        self.flag = False
        self.ultrasonic_sensor = ev3.UltrasonicSensor('in2')
        self.robot = robot

    def run(self): # This is incomplete. The left speed is not always greater than right speed.
        """One cycle of feedback loop: read sensors, choose movement, set movement."""
        dist = self.ultrasonic_sensor.distance_centimeters
        if dist > 50:
            self.robot.stop()
        elif dist > 30:
            self.robot.forward(3/dist)
        else:
            self.robot.curve(5/dist, dist/51, 0.3)


def runBehavior(behavObj, runTime = None):
    """Takes in a behavior object and an optional time to run. It runs
    a loop that calls the run method of the behavObj over and over until
    either the time runs out or a button is pressed."""
    buttons = ev3.Button()
    startTime = time.time()
    elapsedTime = time.time() - startTime
    ev3.Sound.speak("Starting")
    while (not buttons.any()) and ((runTime is None) or (elapsedTime < runTime)):
        behavObj.run()
        # Could add time.sleep here if need to slow loop down
        elapsedTime = time.time() - startTime
    behavObj.robot.stop()
    ev3.Sound.speak("Done")


# if __name__ == '__main__':
    # set up robot object here if using it
    # timBehav = Timid()
    # runBehavior(timBehav)

