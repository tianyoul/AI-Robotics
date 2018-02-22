'''This file xxxxxxxxxx`'''
import ev3dev.ev3 as ev3
import time


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
            return None, self.rightTouch.is_pressed
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

    # -----------------------------------------------------------------------------------
    # Methods of previous SturdyBot code, instance names modified

    def forward(self, speed, time = 1.0):
        """makes the robot to move straight forward,
        either turning on the motors indefinitely or for the input time."""
        self.leftMotor.speed_sp = self.leftMotor.max_speed * speed
        self.rightMotor.speed_sp = self.rightMotor.max_speed * speed
        self.leftMotor.run_timed(time_sp=time * 1000)
        self.rightMotor.run_timed(time_sp=time * 1000)
        self.leftMotor.wait_until_not_moving()
        self.rightMotor.wait_until_not_moving()


    def backward(self, speed, time = 1.0):
        """makes the robot to move straight backward, either turning on the motors indefinitely or for the input time."""
        self.leftMotor.speed_sp = self.leftMotor.max_speed * -speed
        self.rightMotor.speed_sp = self.rightMotor.max_speed * -speed
        self.leftMotor.run_timed(time_sp=time * 1000)
        self.rightMotor.run_timed(time_sp=time * 1000)
        self.leftMotor.wait_until_not_moving()
        self.rightMotor.wait_until_not_moving()


    def turnLeft(self, speed, time = 1.0):
        """Causes the robot to rotate counter-clockwise at the given speed
        either indefinitely or until a given time.
        Negative speeds should cause it to rotate clockwise."""
        self.rightMotor.speed_sp = self.rightMotor.max_speed * speed
        self.leftMotor.speed_sp = self.leftMotor.max_speed * -speed
        self.rightMotor.run_timed(time_sp=time * 1000)
        self.leftMotor.run_timed(time_sp=time * 1000)
        self.rightMotor.wait_until_not_moving()
        self.leftMotor.wait_until_not_moving()


    def turnRight(self, speed, time = 1.0):
        self.leftMotor.speed_sp = self.leftMotor.max_speed * speed
        self.rightMotor.speed_sp = self.rightMotor.max_speed * -speed
        self.leftMotor.run_timed(time_sp=time * 1000)
        self.rightMotor.run_timed(time_sp=time * 1000)
        self.leftMotor.wait_until_not_moving()
        self.rightMotor.wait_until_not_moving()


    def stop(self):
        """turn off left and right motor, making robot stop"""
        self.leftMotor.stop()
        self.rightMotor.stop()


    def curve(self, leftSpeed, rightSpeed, time = 1):
        self.leftMotor.speed_sp = self.leftMotor.max_speed * leftSpeed
        self.rightMotor.speed_sp = self.rightMotor.max_speed * rightSpeed
        self.leftMotor.run_timed(time_sp=time * 1000)
        self.rightMotor.run_timed(time_sp=time * 1000)
        self.leftMotor.wait_until_not_moving()
        self.rightMotor.wait_until_not_moving()


    def zeroPointer(self):
        self.servoMotor.speed_sp = 180
        self.servoMotor.stop_action = 'hold'
        self.servoMotor.position_sp = -self.flagDir
        self.servoMotor.run_to_rel_pos()
        self.servoMotor.wait_until_not_moving()
        self.servoMotor.stop()
        self.flagDir = 0


    def pointerLeft(self, speed = 0.5, time = 1.0):
        '''Time is given in seconds. Speed is in [-1, 1]. Turn the flag left over a given time.'''
        speed = -speed
        self.servoMotor.speed_sp = speed * self.servoMotor.max_speed
        self.servoMotor.run_timed(time_sp = time * 1000)
        self.servoMotor.wait_until_not_moving()
        self.servoMotor.stop()
        angle = speed * self.servoMotor.max_speed * time
        self.flagDir += angle


    def pointerRight(self, speed = 0.5, time = 1.0):
        '''Time is given in seconds. Speed is in [-1, 1]. Turn the flag right over a given time.'''
        self.servoMotor.speed_sp = speed * self.servoMotor.max_speed
        self.servoMotor.run_timed(time_sp = time * 1000)
        self.servoMotor.wait_until_not_moving()
        self.servoMotor.stop()
        angle = speed * self.servoMotor.max_speed * time
        self.flagDir += angle


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


    def playMusic(self, name):
        self.Sound.set_volume(50)
        self.Sound.play(name).wait()


#Test the funtionalities

# def test():
#     ev3.Sound.beep()
#     robot = SturdyRobot("test")
#     robot.forward(0.5)
#     time.sleep(0.5)
#     robot.backward(0.5)
#     time.sleep(0.5)
#     robot.turnLeft(0.5)
#     time.sleep(0.5)
#     robot.turnRight(0.5)
#     time.sleep(0.5)
#     robot.curve(0.2, 0.7)
#     time.sleep(0.5)
#     robot.pointerLeft()
#     time.sleep(0.5)
#     robot.pointerRight()
#     time.sleep(0.5)
#     robot.zeroPointer()
#     time.sleep(0.5)
#     robot.pointerTo(90)
#     time.sleep(0.5)
#     robot.zeroPointer()
#     time.sleep(0.5)
#     robot.playMusic("LB.wav")
#     time.sleep(0.5)
#     robot.stop()
#     ev3.Sound.beep()


def test_sensors():
    ev3.Sound.beep()
    robot = SturdyRobot("test")
    while not button.any():
        result = robot.readTouch()
        print(result)
    ev3.Sound.beep()