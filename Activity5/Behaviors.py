from random import *
from abc import ABC, abstractmethod

class behaviorBase():
    def __init__(self, robot):
        self.robot = robot
        self.magnitude = 0.0
        self.angle = 0.0

    @abstractmethod
    def update(self):
        pass

    def getVec(self):
        return self.magnitude, self.angle

class keepMoving(behaviorBase):
    def update(self):
        self.magnitude = 30.0
        self.angle = 0.0


class wander(behaviorBase):
    def update(self):
        self.magnitude = 15.0
        i = randint(0, 5)
        if i == 4:
            self.angle = randint(-60, 60)

class obstacleForce(behaviorBase):
    def __init__(self, robot, angel):
        super().__init__(robot)
        self.flagAngel = angel

    def update(self):
        self.robot.pointTo(self.flagAngel) # Pointing the ultrasonic sensor to its intended direction
        distance = self.robot.readDistance()
        if distance > 100: # if the distance is too big / there are no obstacles, then we don't need to change its direction or magnitude
            self.angel = 0.0
            self.magnitude = 0.0
        else: # the closer we are to the obstacle, the greater the magnitude should be, with the angle pointing to another direction
            self.magnitude = 100/distance/distance
            self.angel = -self.flagAngel

class clearStall(behaviorBase):
    def __init__(self, robot, motor, whichMotor):
        super().__init__(robot)
        self.motor = motor
        self.whichMotor = whichMotor

    #TODO: this update function may not do exactly what we want for different motors
    def update(self):
        if self.motor.is_stalled:
            # according to the documentation, is_stalled means the motor is not turning when it should be
            self.magnitude = 10.0
            if self.whichMotor == 'left':
                self.angle = 135.0 # when  the left motor is stalled, the direction of this vector should be pointing to the right
            elif self.whichMotor == 'right':
                self.angle = -1355.0
            # With this setup, if both motors are stalled, the combination of the two vectors is going to give us a stronger backward force
        else:
            self.magnitude = 0.0
            self.angle = 0.0

class