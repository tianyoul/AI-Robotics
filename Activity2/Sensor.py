import ev3dev.ev3 as ev3

button = ev3.Button()

leftTouch = ev3.TouchSensor("in4")
rightTouch = ev3.TouchSensor("in1")

ev3.Sound.beep()


while not button.any():
    #print(leftTouch.value(), rightTouch.value())
    if leftTouch.value() and rightTouch.value():
        ev3.Sound.play_song([('E4', 'e')])
    elif leftTouch.value():
        ev3.Sound.play_song([('C4', 'e')])
    elif rightTouch.value():
        ev3.Sound.play_song([('G4', 'e')])

ev3.Sound.speak("Program done.")