from random import *
from abc import ABC, abstractmethod

class behaviorBase():
    def __init__(self, robot):
        self.robot = robot
        self.magnitude = 15.0
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
            self.magnitude = -100/distance/distance
            self.angel = -self.flagAngel

# class clearStall(behaviorBase):
#     def update(self):
#         if self.robot.leftMotor.is_stalled and self.robot.rightMotor.is_stalled:
#             # according to the documentation, is_stalled means the motor is not turning when it should be
#             self.magnitude = -30.0
#             self.angle = 0.0 # run backwards when both motors are stalled
#
