"""Contains a dictionary to represent the FSM: state is the key, value is ...
a function that checks sensors and takes actions, returning the new state. Other
models are possible."""

import time
import ev3dev.ev3 as ev3


class Wary(object):
    """If no object is close enough, the robot should move forward, 
    if an object is in the target range, then it should not move, 
    and if the object is too close, the robot should move backward."""
    def __init__(self, robot = None):
        """Set up motors/robot and sensors here, set state to 'seeking' and forward
        speed to nonzero"""
        self.flag = False
        self.ultrasonic_sensor = ev3.UltrasonicSensor('in2')
        self.robot = robot
        self.FSM = {'seeking': self.updateSeeking,
                    'found': self.updateFound}
        self.state = 'seeking'

    def updateSeeking(self):
        distance = self.ultrasonic_sensor.distance_centimeters
        if distance < 10 :#<object is close>:
            self.robot.stop()
            return 'found'
        if distance > 15:
            self.robot.runforever(0.1)
            return 'seeking'
        return None


    def updateFound(self):
        distance = self.ultrasonic_sensor.distance_centimeters
        if distance < 10 :#<object is not close>:
            self.robot.backwardforever(0.1)
            return 'seeking'
        return None


    def run(self):
        """Updates the FSM by reading sensor data, then choosing based on the state"""
        updateFunc = self.FSM[self.state]
        newState = updateFunc()
        if newState is not None:
            self.state = newState



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
    ev3.Sound.speak("Done")


if __name__ == '__main__':
    # set up robot object here if using it
    timBehav = Wary()  # pass robot object here if need be

    runBehavior(timBehav)

    # add code to stop robot motors

