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

class obstacleForceLeft(behaviorBase):
    def update(self):
        self.robot.pointTo(-90) # Pointing the ultrasonic sensor to the left and read distance input
        distance = self.robot.readDistance()
        if distance < 10:
            self.magnitude = 0.0
            self.angle = 0.0
        else:
            self.magnitude = 30.0 #TODO: modify the calculation of the corresponding magnitude
            self.angle = 0.0
        self.robot.pointTo(0)  # Return to the front

class obstacleForceFront(behaviorBase):
    def update(self):
        distance = self.robot.readDistance()
        if distance < 10:
            self.magnitude = 0.0
            self.angle = 0.0
        else:
            self.magnitude = 30.0 #TODO: modify the calculation of the corresponding magnitude
            self.angle = 0.0

class obstacleForceRight(behaviorBase):
    def update(self):
        self.robot.pointTo(90) # Pointing the ultrasonic sensor to the right and read distance input
        distance = self.robot.readDistance()
        if distance < 10:
            self.magnitude = 0.0
            self.angle = 0.0
        else:
            self.magnitude = 30.0 #TODO: modify the calculation of the corresponding magnitude
            self.angle = 0.0
        self.robot.pointTo(0)  # Return to the front