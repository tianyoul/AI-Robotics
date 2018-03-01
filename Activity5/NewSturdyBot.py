

import ev3dev.ev3 as ev3


class SturdyBot(object):
    """This provides a higher-level interface to the sturdy Lego robot we've been working
    with."""

    # ---------------------------------------------------------------------------
    # Constants for the configDict
    LEFT_MOTOR = 'left-motor'
    RIGHT_MOTOR = 'right-motor'
    SERVO_MOTOR = 'servo-motor'
    LEFT_TOUCH = 'left-touch'
    RIGHT_TOUCH = 'right-touch'
    ULTRA_SENSOR = 'ultra-sensor'
    COLOR_SENSOR = 'color-sensor'
    GYRO_SENSOR = 'gyro-sensor'

    # ---------------------------------------------------------------------------
    # Setup methods, including constructor

    def __init__(self, robotName, configDict=None):
        """Takes in a string, the name of the robot, and an optional dictionary
        giving motor and sensor ports for the robot."""
        self.name = robotName
        self.leftMotor = None
        self.rightMotor = None
        self.servoMotor = None
        self.leftTouch = None
        self.rightTouch = None
        self.ultraSensor = None
        self.colorSensor = None
        self.gyroSensor = None
        if configDict is not None:
            self.setupSensorsMotors(configDict)
        if self.leftMotor is None:
            self.leftMotor = ev3.LargeMotor('outC')
        if self.rightMotor is None:
            self.rightMotor = ev3.LargeMotor('outB')
        self.leftMotor.stop_action = 'brake'
        self.rightMotor.stop_action = 'brake'
        if self.servoMotor is not None:
            self.servoMotor.stop_action = 'hold'

    def setupSensorsMotors(self, configs):
        """Takes in a dictionary where the key is a string that identifies a motor or sensor
        and the value is the port for that motor or sensor. It sets up all the specified motors
        and sensors accordingly."""
        for item in configs:
            port = configs[item]
            if item == self.LEFT_MOTOR:
                self.leftMotor = ev3.LargeMotor(port)
            elif item == self.RIGHT_MOTOR:
                self.rightMotor = ev3.LargeMotor(port)
            elif item == self.SERVO_MOTOR:
                self.servoMotor = ev3.MediumMotor(port)
            elif item == self.LEFT_TOUCH:
                self.leftTouch = ev3.TouchSensor(port)
            elif item == self.RIGHT_TOUCH:
                self.rightTouch = ev3.TouchSensor(port)
            elif item == self.ULTRA_SENSOR:
                self.ultraSensor = ev3.UltrasonicSensor(port)
            elif item == self.COLOR_SENSOR:
                self.colorSensor = ev3.ColorSensor(port)
            elif item == self.GYRO_SENSOR:
                self.gyroSensor = ev3.GyroSensor(port)
            else:
                print("Unknown configuration item:", item)

    def setMotorPort(self, side, port):
        """Takes in which side and which port, and changes the correct variable
        to connect to that port."""
        if side == self.LEFT_MOTOR:
            self.leftMotor = ev3.LargeMotor(port)
        elif side == self.RIGHT_MOTOR:
            self.rightMotor = ev3.LargeMotor(port)
        elif side == self.SERVO_MOTOR:
            self.servoMotor = ev3.MediumMotor(port)
        else:  
            print("Incorrect motor description:", side)

    def setTouchSensor(self, side, port):
        """Takes in which side and which port, and changes the correct
        variable to connect to that port"""
        if side == self.LEFT_TOUCH:
            self.leftTouch = ev3.TouchSensor(port)
        elif side == self.RIGHT_TOUCH:
            self.rightTouch = ev3.TouchSensor(port)
        else:
            print("Incorrect touch sensor description:", side)

    def setColorSensor(self, port):
        """Takes in the port for the color sensor and updates object"""
        self.colorSensor = ev3.ColorSensor(port)

    def setUltrasonicSensor(self, port):
        """Takes in the port for the ultrasonic sensor and updates object"""
        self.ultraSensor = ev3.UltrasonicSensor(port)

    def setGyroSensor(self, port):
        """Takes in the port for the gyro sensor and updates object"""
        self.gyroSensor = ev3.GyroSensor(port)

    # ---------------------------------------------------------------------------
    # Methods to read sensor values

    def readTouch(self):
        """Reports the value of both touch sensors, OR just one if only one is connected, OR
        prints an alert and returns nothing if neither is connected."""
        if self.leftTouch is not None and self.rightTouch is not None:
            return self.leftTouch.is_pressed, self.rightTouch.is_pressed
        elif self.leftTouch is not None:
            return self.leftTouch.is_pressed, None
        elif self.rightTouch is not None:
            return None, self.rightTouch
        else:
            print("Warning, no touch sensor connected")
            return None, None

    def readReflect(self):
        """Reports the reflectance value for the color sensor"""
        if self.colorSensor is not None:
            return self.colorSensor.reflected_light_intensity
        else:
            print("Warning, no color sensor connected")
            return None

    def readLight(self):
        """Reports the amount of light in its surroundings,  (0-100, dark to light)"""
        if self.colorSensor is not None:
            return self.colorSensor.ambient_light_intensity
        else:
            print("Warning, no color sensor connected")
            return None

    def readColor(self):
        """Reports the color value (0 through 7)"""
        if self.colorSensor is not None:
            return self.colorSensor.color
        else:
            print("Warning, no color sensor connected")
            return None

    def readDistance(self):
        """Read and report the ultrasonic sensor's value, reporting in centimeters"""
        if self.ultraSensor is not None:
            return self.ultraSensor.distance_centimeters
        else:
            print("Warning, no ultra sensor connected")
            return None

    def readHeading(self):
        """Read and report the gyro sensor's value, adjusting it to be between 0 and 360"""
        if self.gyroSensor is not None:
            return self.gyroSensor.angle % 360
        else:
            print("Warning, no gyro sensor connected")
            return None


    # ---------------------------------------------------------------------------
    # Methods to move robot

    def forward(self, speed, runTime=None):
        """Takes in a speed between -1.0 and 1.0 inclusively, and an optional
        time to run (in seconds) and it sets the motors so the robot moves straight forward
        at that speed. This method blocks if a time is specified."""
        assert -1.0 <= speed <= 1.0
        assert self.leftMotor is not None
        assert self.rightMotor is not None
        motorSpeed = self.leftMotor.max_speed * speed
        self.leftMotor.speed_sp = motorSpeed
        self.rightMotor.speed_sp = motorSpeed
        self._moveRobot(runTime)


    def backward(self, speed, runTime=None):
        """Takes in a speed between -1.0 and 1.0 inclusively, and an optional
        time to run (in seconds) and it sets the motors so the robot moves straight forward
        at that speed. This method blocks if a time is specified."""
        assert -1.0 <= speed <= 1.0
        assert self.leftMotor is not None
        assert self.rightMotor is not None
        self.forward(-speed, runTime)


    def turnLeft(self, speed, runTime=None):
        """Takes in a speed between -1.0 and 1.0 inclusively, and an optional time
        to run (in seconds) and it sets the motors so the robot turns left in place at
        the given speed. This method blocks if a time is specified until the movement 
        is complete."""
        assert -1.0 <= speed <= 1.0
        assert self.leftMotor is not None
        assert self.rightMotor is not None
        motorSpeed = self.leftMotor.max_speed * speed
        self.leftMotor.speed_sp = -motorSpeed
        self.rightMotor.speed_sp = motorSpeed
        self._moveRobot(runTime)

            
    def turnRight(self, speed, runTime=None):
        """Takes in a speed between -1.0 and 1.0 inclusively, and an optional time
        to run (in seconds) and it sets the motors so the robot turns right in place at
        the given speed. This method blocks if a time is specified until the movement 
        is complete."""
        assert -1.0 <= speed <= 1.0
        assert self.leftMotor is not None
        assert self.rightMotor is not None
        motorSpeed = self.leftMotor.max_speed * speed
        self.leftMotor.speed_sp = motorSpeed
        self.rightMotor.speed_sp = -motorSpeed
        self._moveRobot(runTime)
        
    def stop(self):
        """Turns off the motors and blocks until they have stopped moving."""
        assert self.leftMotor is not None
        assert self.rightMotor is not None
        self.leftMotor.stop()
        self.rightMotor.stop()
        print(self.rightMotor.state)
        self.rightMotor.wait_until_not_moving()

    def curve(self, leftSpeed, rightSpeed, runTime=None):
        """Takes in two speeds, left motor and right motor speeds, both between
        -1.0 and 1.0 inclusively, and an optional time in seconds for the motors to run.
        It sets the speeds appropriately and runs just like the other movement methods,
        just with different speeds set on each motor. Blocks if a time is specified."""
        assert self.leftMotor is not None
        assert self.rightMotor is not None
        assert -1.0 <= leftSpeed <= 1.0
        assert -1.0 <= rightSpeed <= 1.0
        leftMotorSp = leftSpeed * self.leftMotor.max_speed
        rightMotorSp = rightSpeed * self.rightMotor.max_speed
        self.leftMotor.speed_sp = leftMotorSp
        self.rightMotor.speed_sp = rightMotorSp
        self._moveRobot(runTime)
            

    def move(self, translateSpeed, rotateSpeed, runTime=None):
        """Takes in two speeds, a translational speed in the direction the robot is facing,
        and a rotational speed both between -1.0 and 1.0 inclusively. Also takes in an 
        optional time in seconds for the motors to run.
        It converts the speeds to left and right wheel speeds, and thencalls curve."""
        wheelDist = 12 * 19.5
        assert self.leftMotor is not None
        assert self.rightMotor is not None
        assert -1.0 <= translateSpeed <= 1.0
        assert -1.0 <= rotateSpeed <= 1.0
        transMotorSp = translateSpeed * self.leftMotor.max_speed
        rotMotorSp = rotateSpeed * 2 # Note that technically rotational speed doesn't have the same units...
        
        # Here are formulas for converting from translate and rotate speeds to left and right
        # These formulas need to know the distance between the two wheels in order to work
        # which I measured to be 12 cm on my robot. But we have to watch out for units here
        # the speeds are in "ticks" (degrees) per second, so we need to map rotational ticks
        # to centimeters. I measured 360 ticks moving the robot 18.5 cm forward, so 1cm is
        # 19.5 tics. Thus the wheel distance is 12 * 19.5 = 234 ticks.
        leftSpeed = transMotorSp - (rotMotorSp * wheelDist) / 2.0
        rightSpeed = transMotorSp + (rotMotorSp * wheelDist) / 2.0
        print("SPEEDS:", leftSpeed, rightSpeed)
        self.leftMotor.speed_sp = leftSpeed
        self.rightMotor.speed_sp = rightSpeed
        self._moveRobot(runTime)
        

    def pointerTo(self, angle):
        """Turn the flag to the given direction."""
        angle = angle - self.flagDir
        self.flagDir = angle
        self.servoMotor.speed_sp = 180
        self.servoMotor.stop_action = 'hold'
        self.servoMotor.position_sp = angle
        self.servoMotor.run_to_rel_pos()
        self.servoMotor.wait_until_not_moving()
        self.servoMotor.stop()


    def _moveRobot(self, runTime):
        """Helper method, takes in a time in seconds, or time is None if no time limit, 
        and it runs the motors at the current speed either forever or for the given time.
        Blocks and waits if a time is given."""
        if runTime is None:
            self.leftMotor.run_forever()
            self.rightMotor.run_forever()
        else:
            milliSecTime = runTime * 1000.0
            self.leftMotor.run_timed(time_sp = milliSecTime)
            self.rightMotor.run_timed(time_sp = milliSecTime)
            self.rightMotor.wait_until_not_moving()


            
# Sample of how to use this
if __name__ == "__main__":
    firstConfig = {SturdyBot.LEFT_MOTOR: 'outC',
                   SturdyBot.RIGHT_MOTOR: 'outB',
                   SturdyBot.SERVO_MOTOR: 'outD',
                   SturdyBot.LEFT_TOUCH: 'in4',
                   SturdyBot.RIGHT_TOUCH: 'in1'}
    touchyRobot = SturdyBot('Touchy', firstConfig)
    for i in range(5):
        touchValues = touchyRobot.readTouch()
        print("Touch values: ", touchValues)
        touchyRobot.backward(0.5, 1.0)
        touchyRobot.move(0.5, 0.5, 1.5)
        # if touchValues == (0, 0):
        #     touchyRobot.forward(0.6, 0.75)
        # elif touchValues[1] == 1 and touchValues[0] == 0:
        #     touchyRobot.turnLeft(0.4, 0.75)
        # elif touchValues[0] == 1 and touchValues[1] == 0:
        #     touchyRobot.turnRight(0.4, 0.75)
        # else:
        #     touchyRobot.backward(0.6, 0.75)
        touchyRobot.stop()
