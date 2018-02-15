import ev3dev.ev3 as ev3
import threading

flatMot = ev3.MediumMotor('outD')

flatMot.speed_sp = 180
flatMot.stop_action = 'hold'
flatMot.position_sp = 180
ev3.Sound.beep()


newSong = [('C4','q'),('C4','q'),('G4', 'q'), ('G4','q'),('A4','q'),('A4','q'),('G4','h'),('F4','q'),('F4','q'),('E4','q'),('E4','q'),('D4','q'),('D4', 'q'),('C4', 'h')]

def song():
    ev3.Sound.set_volume(5)
    ev3.Sound.play_song(newSong).wait()


def waveFlag():
    for i in range(12):
        flatMot.position_sp = flatMot.position_sp * -1
        flatMot.run_to_rel_pos()
        flatMot.wait_until_not_moving()

threads = []
song = threading.Thread(target=song)
threads.append(song)
song.start()
wave = threading.Thread(target=waveFlag)
threads.append(wave)
wave.start()

flatMot.stop()

