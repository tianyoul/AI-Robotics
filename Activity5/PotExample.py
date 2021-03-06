
from NewSturdyBot import SturdyBot
import PotentialFieldBrain
import time
import ev3dev.ev3 as ev3
import Behaviors
from random import *


# -----------------------------------------------------
# Run the demo using something like this:

def runDemo(runTime = 30):
    """This function is really a model to be modified.  It shows how to take a make
    a PotentialFieldBrain, add behaviors to the brain, and then run it for the given time."""
    # add behaviors, in order from lowest to hightest.

    config = {SturdyBot.LEFT_MOTOR: 'outC',
                   SturdyBot.RIGHT_MOTOR: 'outB',
                   SturdyBot.SERVO_MOTOR: 'outD',
                   SturdyBot.LEFT_TOUCH: 'in4',
                   SturdyBot.RIGHT_TOUCH: 'in1',
                   SturdyBot.ULTRA_SENSOR: 'in3',
                   SturdyBot.COLOR_SENSOR: 'in2',
                   # SturdyBot.GYRO_SENSOR: 'in3'
                   }
    robot = SturdyBot("beibei",config)
    brain = PotentialFieldBrain.PotentialFieldBrain(robot)
    keepMoving = Behaviors.keepMoving(robot)
    wander = Behaviors.wander(robot)
    obstacleForceLeft = Behaviors.obstacleForce(robot, -90)
    obstacleForceFront = Behaviors.obstacleForce(robot, 0)
    obstacleForceRight = Behaviors.obstacleForce(robot, 90)
    clearStallLeft = Behaviors.clearStall(robot, robot.left_motor, 'left')
    clearStallRight = Behaviors.clearStall(robot, robot.right_motor, 'right')
    senseTouch = Behaviors.senseTouch(robot)

    brain.add(keepMoving)
    brain.add(wander)
    brain.add(obstacleForceLeft)
    brain.add(obstacleForceFront)
    brain.add(obstacleForceRight)
    brain.add(clearStallLeft)
    brain.add(clearStallRight)
    brain.add(senseTouch)

    startTime = time.time()
    elapsedTime = time.time() - startTime

    buttons = ev3.Button()

    while elapsedTime < runTime and not buttons.any():
        print("======================================")
        brain.step()
        elapsedTime = time.time() - startTime
    brain.stopAll()
    robot.stop()


runDemo(10)