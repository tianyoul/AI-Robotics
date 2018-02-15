from sturdyRobot import SturdyRobot
import reactiveCode as reactiveCode

robot = SturdyRobot("exit")
line_behavior = reactiveCode.LineFollowing(robot)
reactiveCode.runBehavior(line_behavior)