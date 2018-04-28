from SturdyBot import *

config = {SturdyBot.LEFT_MOTOR: 'outC',
          SturdyBot.RIGHT_MOTOR: 'outB',
          SturdyBot.ULTRA_SENSOR: 'in3'}

bei = SturdyBot('Bei', config)

velocity = 0.2
bei.forward(velocity, 3.65)


# Max speed = 43.835 cm /s