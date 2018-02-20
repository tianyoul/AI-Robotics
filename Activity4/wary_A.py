from sturdyRobot import SturdyRobot
import fsmCodeA as A

robot = SturdyRobot("wary")
wary_behavior = A.Wary(robot)
A.runBehavior(wary_behavior)