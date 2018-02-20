from sturdyRobot import SturdyRobot
import fsmCodeB as B

robot = SturdyRobot("wary")
wary_behavior = B.Wary(robot)
B.runBehavior(wary_behavior)