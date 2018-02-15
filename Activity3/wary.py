from sturdyRobot import SturdyRobot
import reactiveCode as reactiveCode

robot = SturdyRobot("wary")
wary_behavior = reactiveCode.Wary(robot)
reactiveCode.runBehavior(wary_behavior)