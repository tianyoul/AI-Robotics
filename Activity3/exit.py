from sturdyRobot import SturdyRobot
import reactiveCode as reactiveCode

robot = SturdyRobot("exit")
exit_behavior = reactiveCode.ExitCrowd(robot)
reactiveCode.runBehavior(exit_behavior)