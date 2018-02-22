from sturdyRobot import SturdyRobot
import fsmCodeA as A

robot = SturdyRobot("lf")
lf_behavior = A.lineFollowing(robot)
A.runBehavior(lf_behavior)