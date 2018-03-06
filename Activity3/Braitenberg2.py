from sturdyRobot import SturdyRobot
import reactiveCode as reactiveCode

robot = SturdyRobot("braitenberg2")
berg2_behavior = reactiveCode.Timid(robot)
reactiveCode.runBehavior(berg2_behavior)