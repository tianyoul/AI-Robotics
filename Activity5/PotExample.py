
import SturdyBot
import PotentialFieldBrain
import time


def keepMoving():
    """This is a very simple behavior that reports a fixed magnitude and a
    heading that matches the robot's current heading"""

    return (30.0, 0.0)



# -----------------------------------------------------
# Run the demo using something like this:

def runDemo(runTime = 120):
    """This function is really a model to be modified.  It shows how to take a make
    a PotentialFieldBrain, add behaviors to the brain, and then run it for the given time."""
    # add behaviors, in order from lowest to hightest

    config = {}  # fill this in
    robot = SturdyBot.SturdyBot("MYNAME")
    brain = PotentialFieldBrain.PotentialFieldBrain(robot)
    brain.add( keepMoving )

    startTime = time.time()
    elapsedTime = 0.0
    while elapsedTime < runTime:
        print("======================================")
        brain.step()
    brain.stopAll()


runDemo(10)