from sturdyRobot import SturdyRobot
import reactiveCode as reactiveCode

robot = SturdyRobot("vehicle2")
vehicle2 = reactiveCode.Vehicle2(robot)
reactiveCode.runBehavior(vehicle2)