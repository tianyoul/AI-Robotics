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
robot = SturdyBot("honeybee", firstConfig)
honey_behavior = reactiveCode.Honeybee(robot)
reactiveCode.runBehavior(honey_behavior)
