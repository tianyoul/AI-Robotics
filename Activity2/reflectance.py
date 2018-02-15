import ev3dev.ev3 as ev3

button = ev3.Button()
cs = ev3.ColorSensor('in3')
leftM = ev3.LargeMotor('outC')
rightM = ev3.LargeMotor('outB')

ev3.Sound.beep()


while not button.any():
    leftM.speed_sp = 100
    rightM.speed_sp = 100

    leftM.run_forever()
    rightM.run_forever()

    print(cs.reflected_light_intensity)

    if cs.reflected_light_intensity < 20:
        break

leftM.stop()
rightM.stop()

ev3.Sound.speak("Program done.")