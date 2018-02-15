import ev3dev.ev3 as ev3
import time
import random


bttn = ev3.Button()

ev3.Sound.beep()

success = [('C4','q'),('E4','q'),('G4', 'q'), ('C5','h')]

lowerBound = 1
upperBound = 5

flag = False

while True:
    i = random.randint(lowerBound, upperBound)

    ev3.Sound.speak("I guess it is " + str(i)).wait()

    while True:
        if bttn.up:
            lowerBound = i + 1
            break
        elif bttn.down:
            upperBound = i - 1
            break
        elif bttn.enter:
            ev3.Sound.play_song(success).wait()
            flag = True
            break


    if flag:
        break


ev3.Sound.beep()


