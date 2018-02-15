import ev3dev.ev3 as ev3

flatMot = ev3.MediumMotor('outD')

flatMot.speed_sp = 180
flatMot.stop_action = 'hold'
flatMot.position_sp = -90
ev3.Sound.beep()
ev3.Sound.set_volume(10)
for i in range(12):
    flatMot.run_to_rel_pos()
    flatMot.wait_until_not_moving()
    ev3.Sound.beep()

flatMot.stop()