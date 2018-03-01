#!/usr/bin/env python3

from SturdyBot import SturdyBot
import reactiveCode as reactiveCode


firstConfig = {SturdyBot.LEFT_MOTOR: 'outC',
               SturdyBot.RIGHT_MOTOR: 'outB',
               SturdyBot.SERVO_MOTOR: 'outD',
               SturdyBot.LEFT_TOUCH: 'in4',
               SturdyBot.RIGHT_TOUCH: 'in3',
               SturdyBot.ULTRA_SENSOR: 'in2',
               SturdyBot.COLOR_SENSOR: 'in1',
               #SturdyBot.GYRO_SENSOR: 'in3'
               }
robot = SturdyBot("escapeBox", firstConfig)
escape_behavior = reactiveCode.escapeBox(robot)
reactiveCode.runBehavior(escape_behavior)