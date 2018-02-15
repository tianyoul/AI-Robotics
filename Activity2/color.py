import ev3dev.ev3 as ev3
'''Detect yellow, green as blue.'''

button = ev3.Button()
cs = ev3.ColorSensor('in3')
leftM = ev3.LargeMotor('outC')
rightM = ev3.LargeMotor('outB')

ev3.Sound.beep()

dict = {0:"no", 1:"black", 2:"blue", 3:"green", 4:"yellow", 5:"red", 6:"white", 7:"brown"}

leftM.speed_sp = 100
rightM.speed_sp = 100

leftM.run_forever()
rightM.run_forever()

prev = 0

while not button.any():

    if prev == 5:
        break

    col = cs.color

    if not col == prev:
        prev = col
        ev3.Sound.speak(dict[col]).wait()





leftM.stop()
rightM.stop()

ev3.Sound.speak("Program done.")