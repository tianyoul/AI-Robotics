import ev3dev.ev3 as ev3

'''Clockwise is negative for gs.angle'''

button = ev3.Button()
gs = ev3.GyroSensor('in1')
leftM = ev3.LargeMotor('outC')
rightM = ev3.LargeMotor('outB')


def turn(heading):
    leftM.speed_sp = 100
    rightM.speed_sp = -100

    leftM.run_forever()
    rightM.run_forever()

    while not button.any():
        print(gs.angle)
        if gs.angle <= heading:
            break

ev3.Sound.beep()

turn(-90)

leftM.stop()
rightM.stop()

ev3.Sound.speak("Program done.")