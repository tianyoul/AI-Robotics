import ev3dev.ev3 as ev3



button = ev3.Button()

leftTouch = ev3.TouchSensor("in4")
rightTouch = ev3.TouchSensor("in1")


leftM = ev3.LargeMotor('outC')
rightM = ev3.LargeMotor('outB')

maxSpeed = leftM.max_speed

ev3.Sound.beep()

def backward():
    leftM.speed_sp = -200
    rightM.speed_sp = -200
    rightM.run_timed(time_sp=500)
    leftM.run_timed(time_sp=500)
    rightM.wait_until_not_moving()
    leftM.wait_until_not_moving()

while not button.any():

    #print(leftTouch.value(), rightTouch.value())
    leftM.speed_sp = 200
    rightM.speed_sp = 200
    rightM.run_forever()
    leftM.run_forever()

    if leftTouch.value() and rightTouch.value():

        backward()

        leftM.speed_sp = 0.2 * maxSpeed
        rightM.speed_sp = - 0.2 * maxSpeed
        rightM.run_timed(time_sp = 1800)
        leftM.run_timed(time_sp = 1800)
        rightM.wait_until_not_moving()
        leftM.wait_until_not_moving()

    elif leftTouch.value():

        backward()

        leftM.speed_sp = 0.2 * maxSpeed
        rightM.speed_sp = - 0.2 * maxSpeed
        rightM.run_timed(time_sp = 800)
        leftM.run_timed(time_sp = 800)
        rightM.wait_until_not_moving()
        leftM.wait_until_not_moving()

    elif rightTouch.value():

        backward()

        leftM.speed_sp = - 0.2 * maxSpeed
        rightM.speed_sp = 0.2 * maxSpeed
        rightM.run_timed(time_sp = 800)
        leftM.run_timed(time_sp = 800)
        rightM.wait_until_not_moving()
        leftM.wait_until_not_moving()


leftM.stop()
rightM.stop()


ev3.Sound.speak("Program done.")