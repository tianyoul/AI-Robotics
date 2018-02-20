from sturdyRobot import SturdyRobot
import fsmCodeA as A

robot = SturdyRobot("timid")
timid_behavior = A.Timid(robot)
A.runBehavior(timid_behavior)