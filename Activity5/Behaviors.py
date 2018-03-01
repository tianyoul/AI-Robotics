from random import *

class keepMoving():
    def __init__(self):
        self.magnitude = 30.0
        self.angle = 0.0

    def update(self):
        self.magnitude = 30.0
        self.angle = 0.0

    def getVec(self):
        return self.magnitude, self.angle


class wander():
    def __init__(self):
        self.angle = 0
        self.magnitude = 15

    def update(self):
        i = randint(0, 5)
        if i == 4:
            self.angle = randint(-60, 60)


    def getVec(self):
        return self.magnitude, self.angle
