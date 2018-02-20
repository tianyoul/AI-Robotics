from sturdyRobot import SturdyRobot
import reactiveCode as reactiveCode

robot = SturdyRobot("vehicle1")
vehicle1 = reactiveCode.Vehicle1(robot)
reactiveCode.runBehavior(vehicle1)