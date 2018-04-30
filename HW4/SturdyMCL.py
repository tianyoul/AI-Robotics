from MCLStarter import *
from SturdyBot import *

doorsWorld = [(0.0, 32.0, "wall"), (32.0, 48.0, "no wall"),
              (48.0, 93.0, "wall"), (93.0, 109.0, "no wall"), (109.0, 121.0, "wall"),
              (121.0, 137.0, "no wall"), (137.0, 182.0, "wall"), (182.0, 185.0, "no wall")]
opposites = {"wall": "no wall", "no wall": "wall"}

monte = MonteCarloLocalizer(1000, 0, 185, doorsWorld)

config = {SturdyBot.LEFT_MOTOR: 'outC',
          SturdyBot.RIGHT_MOTOR: 'outB',
          SturdyBot.ULTRA_SENSOR: 'in3'}

bei = SturdyBot('Bei', config)

# quick simulation to test the code
buttons = ev3.Button()
max_v = 43.835
velocity = -0.2  # Negative for backward
actualLoc = 179.0
expectedLoc = 179.0
twoNumsStr = "{0:7.3f}  {1:7.3f}"
print("------------ Initial location, expected and actual:", twoNumsStr.format(expectedLoc, actualLoc))
while not buttons.any() and expectedLoc < 180:
    distMoved = random.gauss(velocity * max_v, 0.25)
    print("------------ Movement, expected and actual:", twoNumsStr.format(max_v * velocity, distMoved))
    if distMoved > 0:
        bei.forward(velocity, distMoved/(velocity * max_v))
    else:
        bei.backward(-velocity, distMoved/(velocity * max_v))

    expectedLoc += velocity * max_v
    actualLoc = actualLoc + distMoved
    print("------------ New location, expected and actual:", twoNumsStr.format(expectedLoc, actualLoc))

    distance = bei.readDistance()  # Instead of getting the value from map, use the ultrasonic sensor.
    print('distance: ' + str(distance))
    if distance < 15:
        actualSensor = "wall"
    else:
        actualSensor = "no wall"
    oppSensor = opposites[actualSensor]
    #sensorData = random.choices([actualSensor, oppSensor, "unknown"], [96, 1, 4])
    r = random.randint(1, 100)
    if r == 1:
        reportedData = oppSensor
    elif r <= 5:
        reportedData = "unknown"
    else:
        reportedData = actualSensor

    print("------------ Sensor value, actual and reported:", actualSensor, reportedData)

    result = monte.mclCycle(distMoved, reportedData)
    monte.printPoint(expectedLoc, 'E')
    monte.printPoint(actualLoc, 'A')
    if result is not None:
        monte.printPoint(result, 'C')
        print("MCL Result:", result)

robot.stop()