from sturdyRobot import SturdyRobot
import reactiveCode as reactiveCode

robot = SturdyRobot("timid")
timid_behavior = reactiveCode.Timid(robot)
reactiveCode.runBehavior(timid_behavior)