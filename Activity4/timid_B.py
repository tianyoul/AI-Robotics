from sturdyRobot import SturdyRobot
import fsmCodeB as B

robot = SturdyRobot("timid")
timid_behavior = B.Timid(robot)
B.runBehavior(timid_behavior)