import ev3dev.ev3 as ev3
'''Works when >= 4cm'''

button = ev3.Button()
us = ev3.UltrasonicSensor('in2')
leftM = ev3.LargeMotor('outC')
rightM = ev3.LargeMotor('outB')

ev3.Sound.beep()

leftM.speed_sp = 100
rightM.speed_sp = 100

leftM.run_forever()
rightM.run_forever()


while not button.any():
    distance = us.distance_centimeters
    if(distance < 10):
        break


leftM.stop()
rightM.stop()

ev3.Sound.speak("Program done.")