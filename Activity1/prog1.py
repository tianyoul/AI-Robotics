import ev3dev.ev3 as ev3

bttn = ev3.Button()

LEDColors = [ev3.Leds.GREEN, ev3.Leds.YELLOW, ev3.Leds.ORANGE, ev3.Leds.AMBER, ev3.Leds.RED]

currColor = 0
currLED = ev3.Leds.LEFT

ev3.Sound.beep()
while True:
	if bttn.backspace:
		break
	elif bttn.left:
		ev3.Leds.all_off()
		currLED = ev3.Leds.LEFT
	elif bttn.right:
		ev3.Leds.all_off()
		currLED = ev3.Leds.RIGHT
	elif bttn.up:
		if currColor == 0:
			currColor = len(LEDColors) - 1
		else:
			currColor = currColor - 1
	elif bttn.down:
		currColor = (currColor + 1)% len(LEDColors)

	ev3.Leds.set_color(currLED, LEDColors[currColor])

ev3.Sound.beep()
ev3.Leds.all_off()
