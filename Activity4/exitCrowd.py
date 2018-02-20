from sturdyRobot import SturdyRobot
import fsmCodeA as A

robot = SturdyRobot("exit")
exit_behavior = A.exitCrowd(robot)
A.runBehavior(exit_behavior)