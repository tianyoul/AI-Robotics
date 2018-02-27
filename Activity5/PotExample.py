
from NewSturdyBot import SturdyBot
import PotentialFieldBrain
import time
import ev3dev.ev3 as ev3
from random import *




def keepMoving():
    """This is a very simple behavior that reports a fixed magnitude and a
    heading that matches the robot's current heading"""

    return (30.0, 0.0)


def wander():
    """Generate random directions"""

    angle = randint(-90, 90)

    i = randint(0,5)

    if i == 4:
        return (30.0, angle)

    return (30.0, 0)

def obstacle():
    """obstacle behavior"""

    angle = randint(-90, 90)

    i = randint(0,5)

    if i == 4:
        return (30.0, angle)

    return (30.0, 0)


# -----------------------------------------------------
# Run the demo using something like this:

def runDemo(runTime = 30):
    """This function is really a model to be modified.  It shows how to take a make
    a PotentialFieldBrain, add behaviors to the brain, and then run it for the given time."""
    # add behaviors, in order from lowest to hightest

    config = {SturdyBot.LEFT_MOTOR: 'outC',
                   SturdyBot.RIGHT_MOTOR: 'outB',
                   SturdyBot.SERVO_MOTOR: 'outD',
                   SturdyBot.LEFT_TOUCH: 'in4',
                   SturdyBot.RIGHT_TOUCH: 'in3',
                   SturdyBot.ULTRA_SENSOR: 'in2',
                   SturdyBot.COLOR_SENSOR: 'in1',
                   # SturdyBot.GYRO_SENSOR: 'in3'
                   }
    robot = SturdyBot("beibei",config)
    brain = PotentialFieldBrain.PotentialFieldBrain(robot)
    brain.add(keepMoving,wander)

    startTime = time.time()
    elapsedTime = time.time() - startTime

    buttons = ev3.Button()

    while elapsedTime < runTime and not buttons.any():
        print("======================================")
        brain.step()
        elapsedTime = time.time() - startTime
    brain.stopAll()


runDemo(10)