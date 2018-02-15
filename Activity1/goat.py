import ev3dev.ev3 as ev3
import time

ev3.Sound.play("GoatBah.wav").wait()
time.sleep(1.0)
ev3.Sound.speak("I love goats!").wait()
time.sleep(1.0)
ev3.Sound.set_volume(50)
starSong = [('C4','q'),('C4','q'),('G4', 'q'), ('G4','q'),('A4','q'),('A4','q'),('G4','h'),('F4','q'),('F4','q'),('E4','q'),('E4','q'),('D4','q'),('D4', 'q'),('C4', 'h')]
ev3.Sound.play_song(starSong).wait()
time.sleep(1.0)
ev3.Sound.beep("-l 500 -f 440 -n -f 880 -n -f 440")
