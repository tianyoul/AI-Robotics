'''This file xxxxxxxxxx`'''
import ev3dev.ev3 as ev3
import time


class SturdyRobot(object):
    def __init__(self, name, left_motor=ev3.LargeMotor('outC'), right_motor=ev3.LargeMotor('outB'),
                 medium_motor=ev3.MediumMotor('outD')):
        self.name = name
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.medium_motor = medium_motor
        self.flagDir = 0
        self.Sound = ev3.Sound

    def forward(self, speed, time = 1.0):
        """makes the robot to move straight forward,
        either turning on the motors indefinitely or for the input time."""
        self.left_motor.speed_sp = self.left_motor.max_speed * speed
        self.right_motor.speed_sp = self.right_motor.max_speed * speed
        self.left_motor.run_timed(time_sp=time * 1000)
        self.right_motor.run_timed(time_sp=time * 1000)
        self.left_motor.wait_until_not_moving()
        self.right_motor.wait_until_not_moving()


    def backward(self, speed, time = 1.0):
        """makes the robot to move straight backward, either turning on the motors indefinitely or for the input time."""
        self.left_motor.speed_sp = self.left_motor.max_speed * -speed
        self.right_motor.speed_sp = self.right_motor.max_speed * -speed
        self.left_motor.run_timed(time_sp=time * 1000)
        self.right_motor.run_timed(time_sp=time * 1000)
        self.left_motor.wait_until_not_moving()
        self.right_motor.wait_until_not_moving()


    def turnLeft(self, speed, time = 1.0):
        """Causes the robot to rotate counter-clockwise at the given speed
        either indefinitely or until a given time.
        Negative speeds should cause it to rotate clockwise."""
        self.right_motor.speed_sp = self.right_motor.max_speed * speed
        self.left_motor.speed_sp = self.left_motor.max_speed * -speed
        self.right_motor.run_timed(time_sp=time * 1000)
        self.left_motor.run_timed(time_sp=time * 1000)
        self.right_motor.wait_until_not_moving()
        self.left_motor.wait_until_not_moving()


    def turnRight(self, speed, time = 1.0):
        self.left_motor.speed_sp = self.left_motor.max_speed * speed
        self.right_motor.speed_sp = self.right_motor.max_speed * -speed
        self.left_motor.run_timed(time_sp=time * 1000)
        self.right_motor.run_timed(time_sp=time * 1000)
        self.left_motor.wait_until_not_moving()
        self.right_motor.wait_until_not_moving()


    def stop(self):
        """turn off left and right motor, making robot stop"""
        self.left_motor.stop()
        self.right_motor.stop()


    def curve(self, leftSpeed, rightSpeed, time = 1):
        self.left_motor.speed_sp = self.left_motor.max_speed * leftSpeed
        self.right_motor.speed_sp = self.right_motor.max_speed * rightSpeed
        self.left_motor.run_timed(time_sp=time * 1000)
        self.right_motor.run_timed(time_sp=time * 1000)
        self.left_motor.wait_until_not_moving()
        self.right_motor.wait_until_not_moving()


    def zeroPointer(self):
        self.medium_motor.speed_sp = 180
        self.medium_motor.stop_action = 'hold'
        self.medium_motor.position_sp = -self.flagDir
        self.medium_motor.run_to_rel_pos()
        self.medium_motor.wait_until_not_moving()
        self.medium_motor.stop()
        self.flagDir = 0


    def pointerLeft(self, speed = 0.5, time = 1.0):
        '''Time is given in seconds. Speed is in [-1, 1]. Turn the flag left over a given time.'''
        speed = -speed
        self.medium_motor.speed_sp = speed * self.medium_motor.max_speed
        self.medium_motor.run_timed(time_sp = time * 1000)
        self.medium_motor.wait_until_not_moving()
        self.medium_motor.stop()
        angle = speed * self.medium_motor.max_speed * time
        self.flagDir += angle


    def pointerRight(self, speed = 0.5, time = 1.0):
        '''Time is given in seconds. Speed is in [-1, 1]. Turn the flag right over a given time.'''
        self.medium_motor.speed_sp = speed * self.medium_motor.max_speed
        self.medium_motor.run_timed(time_sp = time * 1000)
        self.medium_motor.wait_until_not_moving()
        self.medium_motor.stop()
        angle = speed * self.medium_motor.max_speed * time
        self.flagDir += angle


    def pointerTo(self, angle):
        """Turn the flag to the given direction."""
        angle = angle - self.flagDir
        self.flagDir = angle
        self.medium_motor.speed_sp = 180
        self.medium_motor.stop_action = 'hold'
        self.medium_motor.position_sp = angle
        self.medium_motor.run_to_rel_pos()
        self.medium_motor.wait_until_not_moving()
        self.medium_motor.stop()


    def playMusic(self, name):
        self.Sound.set_volume(50)
        self.Sound.play(name).wait()

    def runforever(self, speed = 0.5):
        self.left_motor.speed_sp = self.left_motor.max_speed * speed
        self.right_motor.speed_sp = self.right_motor.max_speed * speed
        self.left_motor.run_forever()
        self.right_motor.run_forever()

    def backwardforever(self, speed = 0.5):
        self.left_motor.speed_sp = -1 * self.left_motor.max_speed * speed
        self.right_motor.speed_sp = -1* self.right_motor.max_speed * speed
        self.left_motor.run_forever()
        self.right_motor.run_forever()

    def turnLeftforever(self, speed = 0.5):
        self.right_motor.speed_sp = self.right_motor.max_speed * speed
        self.left_motor.speed_sp = self.left_motor.max_speed * -speed
        self.left_motor.run_forever()
        self.right_motor.run_forever()





