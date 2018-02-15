import ev3dev.ev3 as ev3
import random
import time

bttn = ev3.Button()

LEDLocation = [ev3.Leds.LEFT, ev3.Leds.RIGHT]
seqList = [0, 0, 0, 0]

ev3.Sound.beep()


for i in range(4):
    j = random.randint(0, 1)
    currLED = LEDLocation[j]
    seqList[i] = j
    ev3.Leds.all_off()
    ev3.Leds.set_color(currLED, ev3.Leds.RED)
    ev3.Leds.all_off()
    time.sleep(1.0)

ev3.Sound.beep()

# works up to this point

index = 0

while True:
    if index == 4:
        break
    elif bttn.left and seqList[index] == 0:
        index = index + 1
        continue
    elif bttn.right and seqList[index] == 1:
        index = index + 1
        continue
    elif bttn.left or bttn.right:
        break


ev3.Sound.beep()